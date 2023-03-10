import speech_recognition
import pyttsx3
from datetime import date, datetime


robot_ear = speech_recognition.Recognizer() #robot ear and reply
robot_mouth = pyttsx3.init()
robot_brain= ""

while True:
	with speech_recognition.Microphone() as mic: #robot speech
	   print("Robot: I'm listening")
	   audio = robot_ear.listen(mic)
	 
	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio)   # robot listening
	except: 
		you=""
	print("you : " + you)


	if you=="":
		robot_brain= "I can't hear you, try again"
	elif "hello" in you:
	    robot_brain="Hello Hoang"
	elif "good morning" in you:
	    robot_brain="Good morning Hoàng"	    
	elif "how is the weather today" in you:
	    robot_brain="Today's weather is very beautiful, very suitable for traveling or camping with friends and family. Moreover, I can participate in many outdoor activities such as jogging, sunbathing."	    
	elif " introduce" in you:
	    robot_brain="Hello.My name is Hoang. I'm 21 years old. I living and styding at Da Nang City.My favorite subjects are Maths and English. They are very interesting and I always learn them whenever I have free time. My hobbies are reading book and listening to music. My strengths are creative thinking and good independent work. In the future I want to become programmer."		
	elif " future" in you:
	    robot_brain="I will be a  artificial intelligence engineer AI"	    
	elif "day" in you:
	    today = date.today()
	    robot_brain = today.strftime("%d/%m/%Y")
	elif "time" in you :
	    now = datetime.now()
	    robot_brain = now.strftime("%H:%M:%S") 
	elif "bye" in you:
		robot_brain="Bye Hoang"

		print("Robot:"+ robot_brain)

		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain="I'm fine thank you and you"

	print("Robot:"+ robot_brain)

	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()