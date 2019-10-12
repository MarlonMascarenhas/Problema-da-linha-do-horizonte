def insere():
	sky = []
	for x in range(5000):
		entrada = eval(input(''))
		if len(sky) == 0:
			sky.append(entrada[0])
			sky.append(entrada[1])
			sky.append(entrada[2])
			salvaMaior = entrada[2]
			numMaior = entrada[1]
		else:
			index = 0
			salvo = 0
			for index in range (0, len(sky) , 2):
				xe,e,d = sky[index], entrada[0], entrada[2]
				if (index + 2 <= len(sky) - 1):
					xd = sky[index + 2]
					if(xe < e and xd > e):
						if(sky[index + 1] < entrada[1]):
							sky[index + 2] =  entrada[0]
							sky.append(entrada[1])
							sky.append(entrada[2])
							salvo = 1
					elif(index + 2 == len(sky) - 1 and xe < entrada[0]):
						if(salvaMaior > xd ):
							sky.append(numMaior)
						else:
							sky.append(0)
						sky.append(entrada[0])
						sky.append(entrada[1])
						sky.append(entrada[2])
						salvo = 1
			if salvo == 0:
				
				if salvaMaior < entrada[2]:
					salvaMaior = entrada[2]
					salvaPrimeiro = entrada[0]
					numMaior = entrada[1]
		if entrada == (0,0,0):
			break
	print ('(', end= "")
	for index in range (len(sky)):
		print(str(sky[index]) + ',', end = "")
	print("0)")	
insere()