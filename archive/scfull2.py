import os
import time
fich=[]
dirct=input("repertoire complet du dossier a copier : ")
try:
	fds=os.listdir(str(dirct))
except NameError:
	print(" repertoire invalide")

count=0
for nex in  fds:
	if "." in nex:
		count+=1
		fich.append(nex)
count2=len(fds)-count
print(fich)
print("le dossier contien {} fichiers et {} sous_dossiers ".format(count,count2))
dirct2=input("repertoire de destination : ")
numb=0

for ned in fich:
	fd=open(dirct+ned,'rb')
	fs=open(dirct2+ned,'wb')
	fs.write(fd.read())
	fd.close()
	fs.close() 
	numb+=1
	trem=(numb/len(fds))*100
	print("copie terminer a {} %".format(trem),end ='\r')
print("copie terminer")
