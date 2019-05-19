



#Homework Digital Humanities, Lesson 8, Code and Comments by Regina Jonach

#This#This Python file uses the following encoding: utf-8

import os, sys                                       #import of necessary libraries: os, sys. "The functions that the OS module provides allows you to interface with the 
													 #underlying operating system that Python is running on – be that Windows, Mac or
													 #Linux. " see: https://www.pythonforbeginners.com/os/pythons-os-module
import re                                            #import of library for Regular Expression, in order to be able to use Regular Expression Commands within Python

pathToFolder=("./Perseus/")                          #Since it is more comfortable to use in the further code 
													 #a shortcut for the path is created in this way


listOfFiles = os.listdir(pathToFolder)   			# These two commands access the Folder through the given path, loop through it, and 
													# create as result a direct path to each file (foldernamefilename)
        
for f in listOfFiles:
	newList = (pathToFolder+f)

	

	with open(newList, "rt") as af:                 # With this command each file is open, read 
		data = af.read()
		newData = re.sub("<[^<]+>", "", data)       # A new variable is created that performs a Regular Expression Command on the data in each file
	
	
		
	newFileName = newList + "_modified.xml"         # For the new data new files are created (as well each file with directory path attached)

	with open(newFileName, "w") as afe:             # The new Files are written bis the new data gained from the Regular Expression Command above
		afe.write(newData)


	

