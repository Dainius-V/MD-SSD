import jetson.inference
import jetson.utils
import argparse
import sys

net = jetson.inference.detectNet(argv=["--model=models/ssd-mobilenet.onnx","--labels=models/labels.txt","--input-blob=input_0","--output-cvg=scores","--output-bbox=boxes"],threshold=0.5)

camera = jetson.utils.videoSource("csi://0")

display = jetson.utils.videoOutput()
font = jetson.utils.cudaFont()
smdCounter = 0
smdLeft = 1
while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img)
	if not detections:
		pass
	else:
		for detection in detections:
			pass
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
		else:
			smdLeft = 1			
	# overlay the result on the image	
	font.OverlayText(img, img.width, img.height, "SMD count: {:d}".format(smdCounter), 5, 5, font.White, font.Gray40)
	font.OverlayText(img, img.width, img.height, ' X '.format('X'), 293, 267, font.Green, font.Green)
	#print(detection.Center[1])
	# display picture
	display.Render(img)
	# display SSD Network FPS
	display.SetStatus("SMD Detection and Count | Network {:.0f} FPS".format(net.GetNetworkFPS()))

