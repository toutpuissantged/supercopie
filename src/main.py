
def monocopy():	

	print("supercopie version 1.0 ...")
	import time
	taille=["o","Ko","Mo","Go"]
	lec2=input("entrer le chemin complet du fichier a copier : ")
	try:
		lec=open(lec2,'rb')
	except FileNotFoundError:
		print("fichiers specifier introuvable")
		exit()
	print("initialisation en cours ...")
	t1=time.time()
	lec3=lec.read()
	t2=time.time()
	lon=len(lec3)
	if lon<=1000:
		number=0
		lon2=lon
	elif 1000<lon<1000000:
		number=1
	elif 1000000<lon<1000000000:
		number=2
	elif 1000000000<lon:
		number=3
	unit=taille[number]
	lon2=lon//(10**(3*number))
	print("initialisation terminer")
	print("la taille du fichier est de {} {}".format(str(lon2),str(unit)))
	ecr=input('specifier le nom (+/ou) le chemin de destination : ')
	while ecr=="":
		ecr=input('specifier le nom (+/ou) le chemin de destination : ')
	try:
		ecr2=open(ecr,'wb')
	except:
		print("chemin specifier invalide")
		exit()
	print("copie de fichier en cours ...")
	t3=time.time()
	ecr2.write(lec3)
	t4=time.time()
	try:
		t5=int((t2-t1)+(t4-t3))
	except:
		pass
	if t5==0:
		t5=1
	lon3=lon2//t5
	if lon3==0:
		number-=1
		unit=taille[number]
		lon2=lon//(10**(3*number))
		lon3=lon2//t5
	if t5<=60:
		temps="secondes"
	elif 60<t5<60**2:
		t5=t5//60
		temps="minutes"
	
	print("copie terminer ... ")
	print("vitesse de {} {}/s , temps pris : {} {} ".format(lon3,unit,t5,temps))
	print("fermeture des fichiers et vidage memoire...")
	lec.close()
	ecr2.close()
	print("bye")
	

monocopy()
