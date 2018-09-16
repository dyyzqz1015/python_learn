#!/usr/bin/perl -w
use strict;
use Win32::API;

#Steps:
#    1. Create a task.
#    2. Create an analog input voltage channel.
#    3. Read a scalar value from the channel.
#    4. Call the Clear Task function to clear the task.
#    5. Display an error if any.

#Note: All DAQmx function return 0 on success.
#This example checks for 0 at each step and reports an error for non-zero return values

##############################
#Create a Task
##############################
my $inTaskHandle = pack('i', 0);    #DAQmx TaskHandle
my $taskName = "AITask";            #Task Name

print "Creating a Task\n";

#Function Prototype: int32 DAQmxCreateTask (const char taskName[], TaskHandle *taskHandle);
my $functionDAQmxCreateTask = Win32::API->new('nicaiu','DAQmxCreateTask','PP','I');

#First create the task and get a handle to the task that will be used for all subsequenct operations
my $return = $functionDAQmxCreateTask->Call($taskName, $inTaskHandle);
die ("Could not Create Task. Error: ", $return, "\n" ) unless ($return == 0);

my $outTaskHandle = unpack('i', $inTaskHandle);

print "TaskName: ", $taskName, "\n";
print "TaskHandle: ", $outTaskHandle, "\n";
print "ReturnValue: ", $return, "\n\n";

##############################
#Add an AI Channel to the Task
##############################
my $physicalChannel = "dev1/ai0";   #Physical Channel: AI0 on Dev1
my $channelName = "ai0";            
my $terminalConfig = -1;            #DAQmx_Val_Cfg_Default constant from NIDAQmx.h
my $minVal = -10.0;
my $maxVal = 10.0;  
my $units = 10348;                  #DAQmx_Val_Volts constant from NIDAQmx.h
my $customScaleName = "";

print "Adding an AI Channel to the Task\n";

#Function Prototype: int32 DAQmxCreateAIVoltageChan (TaskHandle taskHandle, const char physicalChannel[],
    #const char nameToAssignToChannel[], int32 terminalConfig, float64 minVal, float64 maxVal,
    #int32 units, const char customScaleName[])
my $functionDAQmxCreateAIVoltageChan = Win32::API->new('nicaiu', 'DAQmxCreateAIVoltageChan', 'IPPIDDIP', 'I');

#Add an analog input channel to the task and specify/configure the channel to read on:
#Specify dev1/ai0 as the channel, use the default terminal configuration and specify that the units is Volts
$return = $functionDAQmxCreateAIVoltageChan->Call($outTaskHandle, $physicalChannel, $channelName, $terminalConfig, $minVal, $maxVal, $units, $customScaleName);
die ("Could not add Channel. Error: ", $return, "\n" ) unless ($return == 0);

print "ReturnValue: ", $return, "\n\n";

##############################
#Read a scalar value
##############################
my $timeout = 10.0;
my $inValue = pack('d', 0.0);
my $reserved = 0;

print "Reading a scalar value from the channel\n";

#Function Prototype: int32 DAQmxReadAnalogScalarF64 (TaskHandle taskHandle, float64 timeout, float64 *value, bool32 *reserved);
my $functionDAQmxReadAnalogScalarF64 = Win32::API->new('nicaiu', 'DAQmxReadAnalogScalarF64', 'IDPP', 'I');

#Next, use the taskHandle to read a single scalar value on the channel specified earlier
$return = $functionDAQmxReadAnalogScalarF64->Call($outTaskHandle, $timeout, $inValue, $reserved);
die ("Could not read Value. Error: ", $return, "\n" ) unless ($return == 0);

my $outValue = unpack('d', $inValue);
print "Value: ", $outValue, "\n";
print "ReturnValue: ", $return, "\n\n";

##############################
#Clear the Task
##############################
print "Clearing the task\n";

#Function Prototype: int32 DAQmxClearTask (TaskHandle taskHandle);
my $functionDAQmxClearTask = Win32::API->new ('nicaiu', "DAQmxClearTask", 'I', 'I');
#Finally, clear the task to release its resources
$return = $functionDAQmxClearTask->Call($outTaskHandle);
die ("Could not clear Task. Error: ", $return, "\n" ) unless ($return == 0);

print "ReturnValue: ", $return, "\n";