
import re
import os, sys                                       
                                        

pathToFolder=("./Perseus/")                          

listOfFiles = os.listdir(pathToFolder)   	

for f in listOfFiles:
	newList = (pathToFolder+f)
	
	with open(newList, "rt", encoding="utf-8") as af:
		data = af.read()


		newData = re.sub(r"\D<div3\s\w+\D\D\article\D\s\w\D\D\d\d\D\s\w+\D\D\w+\D\s\w+\D\D\w+\D\D(\D>\s.+\s\D<) \D</div3>", "", data)

		newfile = [newData]

		#print (newfile)

	
	f = open("All-in-All", "wt", encoding="utf-8")
	f.write(str(newData))
	f.close()

	#with open("allperseus1.txt", "w") as output:
		#output.write(str(newcomp))
