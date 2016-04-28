XML 2 JSON
This Module is used for conjunction with NiFi's ExecuteProcess Processor.
The Module is configured to look at a directory and pull in any new files
that are present if they are appended with an ".xml" file type.
It acts almost as a spooling directory and will delete the .xml file after run
The main.py file can be modified by commenting out the last line and changing it
to simply moving the file to a different directory if needed.

This module expects three arguments:
1. Path to main.py file ("/home/user/xml2json/src/runner/main.py")
2. The spooling directory to look for files ("/testDir")
3. The value of xmlns in the XML file ("{http://www.ws3.com/dbdl}")

The command in the Execute Processor will be:
python

The arguments would be
/home/user/xml2json/src/runner/main.py "/testDir" "{http://www.ws3.com/dbdl}"

The argument delimiter in this instance would be a single space

Be sure to apply the proper permissions to allow NiFi to access the file as well
as the different directories