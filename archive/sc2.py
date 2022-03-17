import time
lec2=input("entrer le chemin complet du fichier a copier : ")
lec=open(lec2,'rb')
t1=time.time()
lec3=lec.read()
t2=time.time()
lon=len(lec3)
lon2=(lon)//1000000
print("la taille du fichier est de {} Mo".format(str(lon2)))
ecr=input('quelle non donnez au fichier ? : ')
ecr2=open(ecr,'wb')
t3=time.time()
ecr2.write(lec3)
t4=time.time()
try:
	t5=int((t2-t1)+(t4-t3))
except:
	t5=1
lon3=lon2//t5
print("copie terminer ... ")
print("vitesse de {} Mo/s , temps pris : {} secondes ".format(lon3,t5))

