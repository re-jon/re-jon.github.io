
import re
import os




with open("./perseus", "r", encoding=None) as f1:
    data = f1.read()

    liftOfFiles = os.listdir(pathToFolder)

	for f in lof:
    print(pathToFolder+f) 

    <milestone n="18" unit="sentence"/>


	newlist = []

		for names in items:
    		if names.startswith("dltext"):
        	newlist.append(names)

 
    new_pers = "perseus" + "_modified.xml"
    with open(new_pers, "w". encoding=None) as f9:
        f9.write(dataNew)

os.fsdecode() 




	cltext = re.sub("<[^<]+>", "", str(af))

		print cltext