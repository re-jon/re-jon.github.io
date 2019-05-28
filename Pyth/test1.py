
import re
import os
#import json



source = ("./Perseus/") 
 

lof = os.listdir(source)
  

for f in lof:
    if f.startswith("dltext"):        
        with open(source + f, "r", encoding="utf-8") as af:
            text = af.read()

            
            date = re.search(r'<date value="([\d-]+)"', text).group(1)

            
            split = re.split("<div3 ", text)

         

            for s in split[1:]:
                
                s = "<div3 " + s 

                try:
                    unitType = re.search(r'type="([^\"]+)"', s).group(1)
                except:
                    unitType = "noType"
                    print(s)
    

                try:
                    header = re.search(r'<head>(.*)</head>', s).group(1)
                    header = re.sub("<[^<]+>", "", header)
                except:
                    header = "NO HEADER"
                    print("\nNo header found!\n")

        

                text = re.sub("<[^<]+>", "", s)
                text = re.sub(" +\n|\n +", "\n", text)
                text = re.sub("\n+", ";;; ", text)

                
                

                itemID = "#ID: " + date+"_"+unitType+"_"
                dateVar   = "#DATE: " + date
                unitType = "#TYPE: " + unitType
                header = "#HEADER: " + header
                text = "#TEXT: " + text


                #newfile = []

                
                uti = "\n".join([itemID,unitType,header,text])

                


                #print (var)

    
                #f = open("All-in-All.xml", "wb")
                #f.write(var)
                #f.close()

                fName = "_"+"_new"

                with open(source+fName+".txt", "wt", encoding="utf-8") as afe:
                    afe.writelines(uti)
                    #json.dump(uti, afe)
                    #afe.writelines("%s\n" % i for i in var)
                    

