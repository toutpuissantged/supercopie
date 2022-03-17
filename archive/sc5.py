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
	t1=time.time()
	lec3=lec.read()
	t2=time.time()
	lon=len(lec3)
	if lon<=1000:
		unit=taille[0]
		lon2=lon
	elif 1000<lon<1000000:
		unit=taille[1]
		lon2=(lon)//1000
	elif 1000000<lon<1000000000:
		unit=taille[2]
		lon2=(lon)//1000000
	elif 1000000000<lon:
		unit=taille[3]
		lon2=(lon)//1000000000
	print("la taille du fichier est de {} {}".format(str(lon2),str(unit)))
	ecr=input('specifier le nom (+/ou) le chemin de destination : ')
	while ecr=="":
		ecr=input('specifier le nom (+/ou) le chemin de destination : ')
	try:
		ecr2=open(ecr,'wb')
	except:
		print("chemin specifier invalide")
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

	print("copie terminer ... ")
	print("vitesse de {} {}/s , temps pris : {} secondes ".format(lon3,unit,t5))
	print("fermeture des fichiers et vidage memoire...")
	lec.close()
	ecr2.close()
	

monocopy()
