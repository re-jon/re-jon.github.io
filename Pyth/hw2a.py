
#Homework Digital Humanities, Lesson 8, Code and Comments by Regina Jonach

#This#This Python file uses the following encoding: utf-8
import re
import os, sys                                       
                                        

pathToFolder=("./Perseus/")                          

listOfFiles = os.listdir(pathToFolder)   	

for f in listOfFiles:
	newList = (pathToFolder+f)
	with open(newList, "rt", encoding="utf-8") as af:
		data = af.read()
		#newData = re.search(r"[\D<div3\s\w+\D\D\article]([^<]+)[\D</div3>]", data).group()


		newData = re.sub(r"\D<div3\s\w+\D\D\article\D\s\w\D\D\d\d\D\s\w+\D\D\w+\D\s\w+\D\D\w+\D\D(\D>\s.+\s\D<) \D</div3>", "", data)
	
		
	


	


	newFileName = newList + "_modified_article.xml"         
	with open(newFileName, "wt", encoding="utf-8") as afe:
		afe.write(str(newData))


#newData = re.sub("<div3 type="article"*>([^<]</div3>", "", data)      