
import re
import os


source = ("./Perseus/") 
 

lof = os.listdir(source)
counter = 0 # 

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

                
                fName = date+"_"+unitType+"_"+str(c)

                itemID = "#ID: " + date+"_"+unitType+"_"+str(c)
                dateVar   = "#DATE: " + date
                unitType = "#TYPE: " + unitType
                header = "#HEADER: " + header
                text = "#TEXT: " + text

                
                var = "\n".join([itemID,unitType,header,text])
                

                with open(source+fName+".txt", "w", encoding="utf8") as afe:
                    afe.write(var)

                #var1 = "\n".join([itemID,unitType,header,text])[1:]

                #with open("test.txt", "w", encoding="utf8") as afe:
                    #afe.write(var1)



                
counter += 1
if counter % 100 == 0:
    print(counter)

