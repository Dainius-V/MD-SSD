#SMD komponentu atpazinimas+skaiciavimas
#Ikeliame bibliotekas
import jetson.inference #neuroniniam tinklui
import jetson.utils # jetson irenginiui
import argparse		# Parametru perdavimui
import sys			# Sistemai

# Sukuriame apmokyto SSD-Mobilenet tinklo objekta
net = jetson.inference.detectNet(argv=["--model=models/ssd-mobilenet.onnx","--labels=models/labels.txt","--input-blob=input_0","--output-cvg=scores","--output-bbox=boxes"],threshold=0.3)
# Vaizdo gavimui priskiriame CSI kameros isejima
camera = jetson.utils.videoSource("csi://0")

display = jetson.utils.videoOutput() # Sukuriame objekta vaizdo atvaizdavimui
font = jetson.utils.cudaFont()		 # Objektas teksto atvaizdavimui ekrane
smdCounter = 0	# Sukuriame kintamaji skaiciavimui
smdLeft = 1		# Skaiciavimo veliavele True
# Ciklas suksis kol bus atidarytas vaizdo ekranas
while display.IsStreaming():
	img = camera.Capture()			# Issaugome vaizda
	detections = net.Detect(img)	# Perduodame issaugota vaizda musu tinklui
	if not detections:	# Jei nieko neaptinko praleidziame
		pass
	else:	# Jei aptiko objekta
		for detection in detections: # Inicializuojame visus aptikimus parametru gavimui
			pass
		# Jei aptikto objekto koordinates yra norimoje pozicijoje prisumuojame ir flag True
		if detection.Center[0] >= 293 and detection.Center[1] >= 267 and smdLeft == 1:
			if detection.Center[0] <= 293+100 and detection.Center[1] <= 267+100 and smdLeft == 1:
				smdCounter = smdCounter+1
				smdLeft = 0
			else:
				pass			
		elif detection.Center[0] <= 293 and detection.Center[1] <= 267 and smdLeft == 1:
			if detection.Center[0] >= 293+100 and detection.Center[1] >= 267+100 and smdLeft == 1:
				smdCounter = smdCounter+1
				smdLeft = 0
			else:
				pass
		# Jei objektas yra norimoje pozicijoje ir Flag False, neskaiciuojame
		elif detection.Center[0] >= 293 and detection.Center[1] >= 267 and smdLeft == 0:
			if detection.Center[0] <= 293+100 and detection.Center[1] <= 267+100 and smdLeft == 0:
				pass
			else:
				pass			
		elif detection.Center[0] <= 293 and detection.Center[1] <= 267 and smdLeft == 0:
			if detection.Center[0] >= 293+100 and detection.Center[1] >= 267+100 and smdLeft == 0:
				pass
			else:
				pass
		# Kitu atveju reiskia objektas nera musu norimoje pozicijoje, nustatome flag True
		else:
			smdLeft = 1			
	# Atvaizduojame gautus rezultatus
	font.OverlayText(img, img.width, img.height, "SMD count: {:d}".format(smdCounter), 5, 5, font.White, font.Gray40)
	font.OverlayText(img, img.width, img.height, ' X '.format('X'), 293, 267, font.Green, font.Green)
	# Atvaizduojame apdorota vaizda
	display.Render(img)
	# Atvaizduojame tinklo FPS
	display.SetStatus("SMD Detection and Count | Network {:.0f} FPS".format(net.GetNetworkFPS()))

