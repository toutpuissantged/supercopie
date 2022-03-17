import os
import time
import sys
fich=[]
try:
	dirct=sys.argv[1]
	dirct2=sys.argv[2]
except:
	print("dossiers parrent ou destinataire non fourni")
	print("utilisation : >>> python3 scfull.py /dossier_a_copier/ /dossier_vers_ou_copier/")
	print("plus d'information sur www.github.org/toutpuissantgeed")
	sys.exit()
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
print("le dossier contien {} fichiers et {} sous_dossiers ".format(count,count2))
numb=0
lock=0
for ned in fich:
	try:
		ft=open(dirct2+ned,'rb')
		lock=1
	except:
		lock=0
	if lock==0:
		try:
			fd=open(dirct+ned,'rb')
			fs=open(dirct2+ned,'wb')
			fs.write(fd.read())
			fd.close()
			fs.close()
		except :
			pass
		 
	elif lock==1:
		print("le fichiers existe deja")
		lock=0
	numb+=1
	trem=(numb//len(fds))*100
	print("copie terminer a {} %".format(trem),end ='\r')
print("copie terminer",end ='\r')
