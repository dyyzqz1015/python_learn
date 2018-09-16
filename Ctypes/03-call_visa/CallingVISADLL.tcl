#!/bin/sh
# -*- tcl -*-
# The next line is executed by /bin/sh, but not tcl \
exec tclsh "$0" ${1+"$@"}

source dll_tcl.tcl

if {[catch {::dll::load visa32.dll -> visaDLL}]} {
    error "SimpleDLL library not found!"
}

#Steps:
#    1. Open Resource Manager                                       
#    2. Open VISA Session to an Instrument
#    3. Set Timeout Attribute
#    4. Write the Identification Query Using viWrite                
#    5. Try to Read a Response With viRead                          
#    6. Close the VISA Session & Resource Manager
#    7. Display an error if any.

#Note: All VISA function return 0 on success.
#This example checks for 0 at each step and reports an error for non-zero return values

##############################
#Open Resource Manager
##############################
set resourceManagerHandle 0         ;#Resource Manager Handle

puts "Opening Resource Manager"

#Function Prototype: ViStatus viOpenDefaultRM(ViPSession sesn)
::visaDLL::cmd "int viOpenDefaultRM(int *)"
#First get the resource manager handle. This will be used next to get a handle to the instrument
set returnValue [::visaDLL::viOpenDefaultRM resourceManagerHandle]
    
if {$returnValue != 0} {
    puts stderr "Could not open Resource Manager. Error: $returnValue \n"
    return returnValue
}

puts "ResourceManagerHandle: $resourceManagerHandle"
puts "ReturnValue: $returnValue \n"

##############################
#Open Resource Session
##############################
set sessionHandle 0                 ;#Instrument Handle
set VI_NULL 0                       ;#VI_NULL constant from visa.h
set resourceName "GPIB0::2::INSTR"  ;#Resource: GPIB Device 0, Primary Adress 2

puts "Opening Resource Session"

#Function Prototype: ViStatus viOpen(ViSession sesn, ViRsrc rsrcName, ViAccessMode accessMode, ViUInt32 openTimeout, ViPSession vi)
::visaDLL::cmd "int viOpen(int, char *, int, int, int *)"
#Open a VISA session to a device on GPIB Device 0 at Primary Address 2 and retreive a handle to this session
#This session handle will be used for subsequent operations
set returnValue [::visaDLL::viOpen $resourceManagerHandle $resourceName $VI_NULL $VI_NULL sessionHandle]

if {$returnValue != 0} {
    puts stderr "Could not open Resource Session. Error: $returnValue \n"
    return returnValue
}

puts "SessionHandle: $sessionHandle"
puts "ReturnValue: $returnValue \n"

##############################
#Set Timeout Attribute
##############################
set VI_ATTR_TMO_VALUE 1073676314    ;#Timeout Attribute Constant from visa.h
set timeout 5000                    ;#Timeout: 5000ms

puts "Setting Timeout Attribute"

#Function Prototype: ViStatus viSetAttribute(ViObject vi, ViAttr attribute, ViAttrState attrState)
::visaDLL::cmd "int viSetAttribute(int, int, int)"
#Set timeout value to 5000 milliseconds (5 seconds)
set returnValue [::visaDLL::viSetAttribute $sessionHandle $VI_ATTR_TMO_VALUE $timeout]

if {$returnValue != 0} {
    puts stderr "Could not set Timeout Attribute. Error: $returnValue \n"
    return returnValue
}

puts "ReturnValue: $returnValue \n"

##############################
#Write "*IDN?" to Device
##############################
set bufferToWrite "*IDN?"           ;#*IDN? typically tells devices to return identification
set bytesToWrite [expr {1 + [string length $bufferToWrite]}]
set bytesWritten 0

puts "Writing *IDN? to Device $bytesToWrite"

#Function Prototype: ViStatus viWrite(ViSession vi, ViBuf buf, ViUInt32 count, ViPUInt32 retCount)
::visaDLL::cmd "int viWrite(int, char *, int, int *)"
#Use this session handle to write *IDN? command to the instrument asking for the its identification.
set returnValue [::visaDLL::viWrite $sessionHandle $bufferToWrite $bytesToWrite bytesWritten]

if {$returnValue != 0} {
    puts stderr "Could not write *IDN? to Device. Error: $returnValue \n"
    return returnValue
}

puts "Bytes Written: $bytesWritten"
puts "ReturnValue: $returnValue \n"

##############################
#Read Response from Device
##############################
set response [::dll::buffer 128]
set bytesToRead 128
set bytesRead 0

puts "Reading Response from Device";

#Function Prototype: ViStatus viRead(ViSession vi, ViPBuf buf, ViUInt32 count, ViPUInt32 retCount)
::visaDLL::cmd "int viRead(int, char *, int, int *)"
#Attempt to read back a response from the device to the identification query that was sent.
set returnValue [::visaDLL::viRead $sessionHandle $response $bytesToRead bytesRead]

if {$returnValue != 0} {
    puts stderr "Could not Read Response from Device. Error: $returnValue \n"
    return returnValue
}

puts "Bytes Read $bytesWritten"
puts "Response: $response"
puts "ReturnValue: $returnValue \n"

##############################
#Close Sessions
##############################
puts "Closing Resource Session"

#Finally, close the instrument session and the resource manager to free resources

#Function Prototype: ViStatus viClose(ViObject vi)
::visaDLL::cmd "int viClose(int)"
set returnValue [::visaDLL::viClose $sessionHandle]
if {$returnValue != 0} {
    puts stderr "Could not close Resource Session. Error: $returnValue \n"
    return returnValue
}

puts "ReturnValue: $returnValue \n"

puts "Closing Resource Manager"

set returnValue [::visaDLL::viClose $resourceManagerHandle]
if {$returnValue != 0} {
    puts stderr "Could not close Resource Manager. Error: $returnValue \n"
    return returnValue
}

puts "ReturnValue: $returnValue \n";
