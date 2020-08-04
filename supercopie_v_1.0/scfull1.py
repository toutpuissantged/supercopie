import os
import time
dirct=input("repertoire complet du dossier a copier")
try:
	fds=os.listdir(str(dirct))
except NameError:
	print(" repertoire invalide")

count=0
for nex in  fds:
	if ".py" in nex:
		count+=1
print("le nombre de fichier python est de {}".format(count))

