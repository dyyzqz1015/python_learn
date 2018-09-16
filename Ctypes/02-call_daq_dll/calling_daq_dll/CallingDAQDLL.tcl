#!/bin/sh
# -*- tcl -*-
# The next line is executed by /bin/sh, but not tcl \
exec tclsh "$0" ${1+"$@"}

source dll_tcl.tcl

if {[catch {::dll::load nicaiu.dll -> daqDLL}]} {
    error "SimpleDLL library not found!"
}

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
set taskName "AITask"               ;#DAQmx TaskHandle
set taskHandle 0                    ;#Task Name

puts "Creating a Task"

#Function Prototype: int32 DAQmxCreateTask (const char taskName[], TaskHandle *taskHandle);
::daqDLL::cmd "int DAQmxCreateTask(char *, int *)"					;# &library

#First create the task and get a handle to the task that will be used for all subsequenct operations
set returnValue [::daqDLL::DAQmxCreateTask $taskName taskHandle]
if {$returnValue != 0} {
    puts stderr "Could not Create Task. Error: $returnValue \n"
    return returnValue
}

puts "TaskName: $taskName"
puts "TaskHandle: $taskHandle"
puts "ReturnValue: $returnValue \n"

###############################
##Add an AI Channel to the Task
###############################
set physicalChannel "dev1/ai0"      ;#Physical Channel: AI0 on Dev1 
set channelName "ai0" 
set terminalConfig -1               ;#DAQmx_Val_Cfg_Default constant from NIDAQmx.h
set minVal -10.0
set maxVal 10.0
set units 10348                     ;#DAQmx_Val_Volts constant from NIDAQmx.h
set customScaleName [::dll::buffer 0]

puts "Adding an AI Channel to the Task"

#Function Prototype: int32 DAQmxCreateAIVoltageChan (TaskHandle taskHandle, const char physicalChannel[],
    #const char nameToAssignToChannel[], int32 terminalConfig, float64 minVal, float64 maxVal,
    #int32 units, const char customScaleName[])
::daqDLL::cmd "int DAQmxCreateAIVoltageChan (int, char *, char *, int, double, double, int, char *)"

#Add an analog input channel to the task and specify/configure the channel to read on:
#Specify dev1/ai0 as the channel, use the default terminal configuration and specify that the units is Volts
set returnValue [::daqDLL::DAQmxCreateAIVoltageChan $taskHandle $physicalChannel $channelName $terminalConfig $minVal $maxVal $units $customScaleName]
if {$returnValue != 0} {
    puts stderr "Could not add Channel. Error: $returnValue \n"
    return returnValue
}

puts "ReturnValue: $returnValue \n";

###############################
##Read a scalar value
###############################
set timeout 10.0
set value 0.0
set reserved 0

puts "Reading a scalar value from the channel"

#Function Prototype: int32 DAQmxReadAnalogScalarF64 (TaskHandle taskHandle, float64 timeout, float64 *value, bool32 *reserved);
::daqDLL::cmd "int DAQmxReadAnalogScalarF64 (int, double, double *, int *)"

#Next, use the taskHandle to read a single scalar value on the channel specified earlier
set returnValue [::daqDLL::DAQmxReadAnalogScalarF64 $taskHandle $timeout value 0]
if {$returnValue != 0} {
    puts stderr "Could not read Value. Error: $returnValue \n"
    return returnValue
}

puts "Value: $value";
puts "ReturnValue: $returnValue \n";

##############################
##Clear the Task
##############################
puts "Clearing the task"

#Function Prototype: int32 DAQmxClearTask (TaskHandle taskHandle);
::daqDLL::cmd "int DAQmxClearTask (int)"

#Finally, clear the task to release its resources
set returnValue [::daqDLL::DAQmxClearTask $taskHandle]
if {$returnValue != 0} {
    puts stderr "Could not clear Task. Error: $returnValue \n"
    return returnValue
}

puts "ReturnValue: $returnValue \n";