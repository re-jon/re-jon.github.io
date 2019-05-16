
import os

path = "/home/rjuniwien/re-jon.github.io/Pyth/pers1355"
lof = os.listdir(path)


for fileName in lof:
with open path*fileName, "r", encoding="utf8" as f1:
    data = f1.read()
  
    newFileName = fileName + "_modified.xml"
    with open(newFileName, "w", encoding="utf8") as f9:
        f9.write(dataNew)
