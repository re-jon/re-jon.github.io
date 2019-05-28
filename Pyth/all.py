import re
import os
import json


source = ("./Perseus/") 
 

lof = os.listdir(source)

for f in lof:
	filenames=(source+f)
	if f.startswith("1860"):
		with open("allIn.txt", "w") as outfile:
			for fname in filenames:
				with open(fname)as infile:
					for line in infile:
						outfile.write(line)




		#with open(source+f, "r") as afi, open("allIn.txt", "wt", encoding="utf-8") as afo:
			#for line in afi:
				#line.add(line)

				#afo.write(str(line)+"\n")

			



			#text = af.read()

			#newt = "".join(['i' for i in textrange(526)])

			#newt="\n".join(text)+f

			#new = re.sub(r"([.+])", "", text)

			#newt = ()

			#for f in new:
				#newt+=f
				

		

		
				

			#print(newt)

			#list=[]

			#for x in new:
				#if x.startswith("#"):
					#list.append(x)

			
			

			#with open("allIn.txt", "wt", encoding="utf-8") as afe:
				#afe. write(str(newt))



      
        	
        		