
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

            c = 0

            for s in split[1:]:
                c += 1
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

                
                

                itemID = "#ID: " + date+"_"+unitType+"_"+str(c)
                dateVar   = "#DATE: " + date
                unitType = "#TYPE: " + unitType
                header = "#HEADER: " + header
                text = "#TEXT: " + text


         

                
                var = "\n".join([itemID,unitType,header,text])

               

            fName = "_"+"_InOne"

            with open(source+fName+".txt", "w", encoding="utf-8") as afe:
                afe.write(var)
                    

                          #new = re.sub(r"([.+])", "", text)


           


            #newText=[]
            #for x in text:
                #if x == new:
    #newText.append(x)
                   

                   for x in text:
                if x.startswith("#"):
                    with open(text + x, "rt", encoding="utf-8") as afe:
                        ntext = afe.read()

