import cv2
import dlib
from scipy.spatial import distance
import winsound

def calculate_EAR(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	aspect_ratio = (A+B)/(2.0*C)
	return aspect_ratio

cap = cv2.VideoCapture(0)
hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

sleep = 0
here = 0
while True:
	_, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = hog_face_detector(gray)

	if not faces:
		here += 5
		if here >= 100:
			winsound.Beep(2000,750)
			print("None")
			here = 0

	for face in faces:
		face_landmarks = dlib_facelandmark(gray, face)
		leftEye = []
		rightEye = []
		for n in range(36,42):
			x = face_landmarks.part(n).x
			y = face_landmarks.part(n).y
			leftEye.append((x,y))
			next_point = n+1
			if n == 41:
				next_point = 36
			x2 = face_landmarks.part(next_point).x
			y2 = face_landmarks.part(next_point).y
			cv2.line(frame,(x,y),(x2,y2),(255,255,255),1)
		
		for n in range(42,48):
			x = face_landmarks.part(n).x
			y = face_landmarks.part(n).y
			rightEye.append((x,y))
			next_point = n+1
			if n == 47:
				next_point = 42
			x2 = face_landmarks.part(next_point).x
			y2 = face_landmarks.part(next_point).y
			cv2.line(frame,(x,y),(x2,y2),(255,255,255),1)
		
		left_ear = calculate_EAR(leftEye)
		right_ear = calculate_EAR(rightEye)
		
		EAR = (left_ear+right_ear)/2
		EAR = round(EAR,2)
		if EAR<0.26:
			sleep += 5
			if sleep >= 80:
				for i in range(3):
					winsound.Beep(2000,750)
					print("Wake UP!!")
				sleep = 0

	cv2.imshow("Wake Up!!", frame)

	key = cv2.waitKey(1)
	if key == 27:
		break
cap.release()
cv2.destroyAllWindows()