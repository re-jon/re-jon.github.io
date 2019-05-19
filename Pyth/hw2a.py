
#Homework Digital Humanities, Lesson 8, Code and Comments by Regina Jonach

#This#This Python file uses the following encoding: utf-8
import re
import os, sys                                       
                                        

pathToFolder=("./Perseus/")                          

listOfFiles = os.listdir(pathToFolder)   	

for f in listOfFiles:
	newList = (pathToFolder+f)
	with open(newList, "rt") as af:
		data = af.read()
		#newData = re.search(r"[\D<div3\s\w+\D\D\article]([^<]+)[\D</div3>]", data).group()


		newData = re.search(r"[\D<div3\s\w+\D\D\article]", data).group()


	


	newFileName = newList + "_modified_article.xml"         
	with open(newFileName, "wt") as afe:
		afe.write(newData)


#newData = re.sub("<div3 type="article"*>([^<]</div3>", "", data)      