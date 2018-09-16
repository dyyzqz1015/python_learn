#!/usr/bin/perl -w
use strict;
use Win32::API;

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
my $inResourceManagerHandle = pack('i', 0);     #Resource Manager Handle

print "Opening Resource Manager\n";

#Function Prototype: ViStatus viOpenDefaultRM(ViPSession sesn)
my $functionViOpenDefaultRM = Win32::API->new('visa32','viOpenDefaultRM','P','I');

#First get the resource manager handle. This will be used next to get a handle to the instrument
my $return = $functionViOpenDefaultRM->Call($inResourceManagerHandle);
die ("Could not open Resource Manager. Error: ", $return, "\n" ) unless ($return == 0);

my $outResourceManagerHandle = unpack('i', $inResourceManagerHandle);

print "ResourceManagerHandle: ", $outResourceManagerHandle, "\n";
print "ReturnValue: ", $return, "\n\n";

##############################
#Open Resource Session
##############################
my $inSessionHandle = pack('i', 0);     #Instrument Handle
my $VI_NULL = 0;                        #VI_NULL constant from visa.h
my $resourceName = "GPIB0::2::INSTR";   #Resource: GPIB Device 0, Primary Adress 2

print "Opening Resource Session\n";

#Function Prototype: ViStatus viOpen(ViSession sesn, ViRsrc rsrcName, ViAccessMode accessMode, ViUInt32 openTimeout, ViPSession vi)
my $functionViOpen = Win32::API->new('visa32','viOpen','IPIIP','I');

#Open a VISA session to a device on GPIB Device 0 at Primary Address 2 and retreive a handle to this session
#This session handle will be used for subsequent operations
$return = $functionViOpen->Call($outResourceManagerHandle,$resourceName,$VI_NULL,$VI_NULL,$inSessionHandle);
die ("Could not open Resource Session. Error: ", $return, "\n" ) unless ($return == 0);

my $outSessionHandle = unpack('i', $inSessionHandle);

print "SessionHandle: ", $outSessionHandle, "\n";
print "ReturnValue: ", $return, "\n\n";

##############################
#Set Timeout Attribute
##############################
my $VI_ATTR_TMO_VALUE = 1073676314;     #Timeout Attribute Constant from visa.h
my $timeout = 5000;                     #Timeout: 5000ms

print "Setting Timeout Attribute\n";

#Function Prototype: ViStatus viSetAttribute(ViObject vi, ViAttr attribute, ViAttrState attrState)
my $functionViSetAttribute = Win32::API->new('visa32','viSetAttribute','III','I');

#Set timeout value to 5000 milliseconds (5 seconds)
$return = $functionViSetAttribute->Call($outSessionHandle, $VI_ATTR_TMO_VALUE, $timeout);
die ("Could not set Timeout Attribute. Error: ", $return, "\n" ) unless ($return == 0);

print "ReturnValue: ", $return, "\n\n";

##############################
#Write "*IDN?" to Device
##############################
my $bufferToWrite = "*IDN?";            #*IDN? typically tells devices to return identification
my $bytesToWrite = length($bufferToWrite) + 1;
my $inBytesWritten = pack('i', 0);

print "Writing *IDN? to Device\n";

#Function Prototype: ViStatus viWrite(ViSession vi, ViBuf buf, ViUInt32 count, ViPUInt32 retCount)
my $functionViWrite = Win32::API->new('visa32','viWrite','IPIP','I');

#Use this session handle to write *IDN? command to the instrument asking for the its identification.
$return = $functionViWrite->Call($outSessionHandle, $bufferToWrite, $bytesToWrite, $inBytesWritten);
die ("Could not write *IDN? to Device. Error: ", $return, "\n" ) unless ($return == 0);

my $outBytesWritten = unpack('i', $inBytesWritten);

print "Bytes Written: ", $outBytesWritten, "\n";
print "ReturnValue: ", $return, "\n\n";

##############################
#Read Response from Device
##############################
my $response = " " x 128;
my $bytesToRead = 128;
my $inBytesRead = pack('i', 0);

print "Reading Response from Device\n";

#Function Prototype: ViStatus viRead(ViSession vi, ViPBuf buf, ViUInt32 count, ViPUInt32 retCount)
my $functionViRead = Win32::API->new('visa32','viRead','IPIP','I');

#Attempt to read back a response from the device to the identification query that was sent.
$return = $functionViRead->Call($outSessionHandle, $response, $bytesToRead, $inBytesRead);
die ("Could not Read Response from Device. Error: ", $return, "\n" ) unless ($return == 0);

my $outBytesRead = unpack('i', $inBytesRead);

print "Bytes Read: ", $outBytesWritten, "\n";
print "Response: ", $response, "\n";
print "ReturnValue: ", $return, "\n\n";

##############################
#Close Sessions
##############################
print "Closing Resource Session\n";

#Finally, close the instrument session and the resource manager to free resources

#Function Prototype: ViStatus viClose(ViObject vi)
my $functionViClose = Win32::API->new('visa32','viClose','I','I');

$return = $functionViClose->Call($outSessionHandle);
die ("Could not close Resource Session. Error: ", $return, "\n" ) unless ($return == 0);

print "ReturnValue: ", $return, "\n\n";

print "Closing Resource Manager\n";

$return = $functionViClose->Call($outResourceManagerHandle);
die ("Could not close Resource Manager. Error: ", $return, "\n" ) unless ($return == 0);

print "ReturnValue: ", $return, "\n\n";
