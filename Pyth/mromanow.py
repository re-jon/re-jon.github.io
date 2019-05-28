import re, os

source = ("./Perseus/") 

lof = os.listdir(source)
counter = 0 # general counter to keep track of the progress

ourCSV = []

for f in lof:
    if f.startswith("dltext"): # fileName test        
        with open(source + f, "r", encoding="utf8") as f1:
            text = f1.read()

            # try to find the date
            date = re.search(r'<date value="([\d-]+)"', text).group(1)

            # splitting the issue into articles/items
            split = re.split("<div3 ", text)

            c = 0 # item counter
            for s in split[1:]:
                c += 1
                s = "<div3 " + s # a step to restore the integrity of items
                #input(s)

                # try to find a unitType
                try:
                    unitType = re.search(r'type="([^\"]+)"', s).group(1)
                except:
                    unitType = "noType"
                    print(s)

                # try to find a header
                try:
                    header = re.search(r'<head>(.*)</head>', s).group(1)
                    header = re.sub("<[^<]+>", "", header)
                except:
                    header = "NO HEADER"
                    #print("No header found!")

                text = re.sub("<[^<]+>", "", s)
                text = re.sub(" +\n|\n +", "\n", text)
                text = re.sub("\n+", ";;; ", text)

                # generating necessary bits 
                fName = date+"_"+unitType+"_"+str(c)

                itemID = date+"_"+unitType+"_"+str(c)
                dateVar   = date
                #unitType = unitType
                #header = header
                text = text.replace("\t", " ")

                # creating a text variable
                var = "\t".join([itemID,dateVar,unitType,header,text])
                #input(var)

                ourCSV.append(var)


        # count processed issues and print progress counter at every 100        
        counter += 1
        if counter % 100 == 0:
            print(counter)

# saving
with open("dispatch_as_TSV.csv", "w", encoding="utf8") as f9:
    f9.write("\n".join(ourCSV))
print(counter)

