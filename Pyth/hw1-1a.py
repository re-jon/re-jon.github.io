



#Homework Digital Humanities, Lesson 8, Code and Comments by Regina Jonach

#This#This Python file uses the following encoding: utf-8

import os, sys                                      
import re                                           

pathToFolder=("./Perseus/")                         


listOfFiles = os.listdir(pathToFolder)   			
        
for f in listOfFiles:
	newList = (pathToFolder+f)
	with open(newList, "rt") as af:
		data = af.read()
		newData = re.sub("<[^<]+>", "", data)      
	newFileName = newList + "_modified.xml"         
	with open(newFileName, "wt") as afe:
		afe.write(newData)


	

