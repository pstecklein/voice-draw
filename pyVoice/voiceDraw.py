from tkinter import *
from tkinter import ttk, Canvas, Frame, BOTH
import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS
root = Tk()
canvas = Canvas(root, height=600, width=600)
canvas.pack()
r = sr.Recognizer()

counter = 0
elements = []
points = []
color = ''
audio = ''
voice_data = ''


def updateConsole():
	L['text'] = "Current element \nPoints: %s \nColor: %s" % (elements[-1]["points"], elements[-1]["color"])

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,50000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"kiri: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

def square(color, points):
	return canvas.create_polygon(points, outline=color, fill=color, width=5)
def triangle(color, points):
	return canvas.create_polygon(points, outline=color, fill=color, width=5)
def circle(color, points):
	return canvas.create_oval(points, outline=color, fill=color, width=5)
def line():
	return canvas.create_line(15, 25, 200, 25)
def dotted():
	return canvas.create_line(300, 35, 300, 200, dash=(4, 2))

def crud():
	global counter
	global elements
	global color
	global points
	if len(elements) == 0:
		createElement()
	else:
		alexis_speak("Do you want to create a new element?, remove the current element?, or edit the current element?")
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data = r.recognize_google(audio)
		if "create" in voice_data:
			createElement()
		elif "remove" in voice_data:
			remove()
		elif "edit" in voice_data:
			edit()
		else:
			alexis_speak("Sorry, couldn't understand")
			crud()


def createElement():
	global counter
	global elements
	global color
	global points
	alexis_speak("What element do you want to create?, and where do you want it located?")
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data = r.recognize_google(audio)
		if "red" in voice_data:
			color = '#f00'
		if "green" in voice_data:
			color = '#0f0'
		if "blue" in voice_data:
			color = '#00f'
		if "square" and ("center" or "middle") in voice_data:
			newObj = "a" + str(counter)
			newObj = {
				"points": [250, 250, 350, 250, 350, 350, 250, 350, 250, 250],
				"color": color
			}
			newObj["type"] = square(color = newObj["color"], points = newObj["points"])
			elements.append(newObj)
			counter += 1
		if "square" and "top left" in voice_data:
			newObj = "a" + str(counter)
			newObj = {
				"points": [10, 10, 110, 10, 110, 110, 10, 110, 10, 10],
				"color": color
			}
			newObj["type"] = square(color = newObj["color"], points = newObj["points"])
			elements.append(newObj)
			square(color = newObj["color"], points = newObj["points"])
			counter += 1
		if "square" and "top right" in voice_data:
			newObj = "a" + str(counter)
			newObj = {
				"points": [495, 10, 595, 10, 595, 110, 495, 110, 495, 10],
				"color": color
			}
			newObj["type"] = square(color = newObj["color"], points = newObj["points"])
			elements.append(newObj)
			square(color = newObj["color"], points = newObj["points"])
			counter += 1
		if "square" and "bottom right" in voice_data:
			newObj = "a" + str(counter)
			newObj = {
				"points": [495, 495, 595, 495, 595, 595, 495, 595, 495, 495],
				"color": color
			}
			newObj["type"] = square(color = newObj["color"], points = newObj["points"])
			elements.append(newObj)
			square(color = newObj["color"], points = newObj["points"])
			counter += 1
		if "square" and "bottom left" in voice_data:
			newObj = "a" + str(counter)
			newObj = {
				"points": [10, 495, 110, 495, 110, 595, 10, 595, 10, 495],
				"color": color
			}
			newObj["type"] = square(color = newObj["color"], points = newObj["points"])
			elements.append(newObj)
			square(color = newObj["color"], points = newObj["points"])
			counter += 1
		if "triangle" in voice_data:
			triangle(color = color, points = [10, 10, 70, 20, 40, 120, 10, 10 ])
		if "circle" in voice_data:
			circle(color = color, points = [10, 10, 80, 80])
		if "line" in voice_data:
			line()
		if "dotted" in voice_data:
			dotted()
	updateConsole()

def edit():
	global counter
	global elements
	alexis_speak("Do you want to move the current element?, make it bigger or smaller?, or change the color")
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data = r.recognize_google(audio)
		if "move" or "translate" in voice_data:
			translate()
		else:
			alexis_speak("Sorry, couldn't understand, do you still want to edit?")
			with sr.Microphone() as source:
				aud = r.listen(source)
				v_data = r.recognize_google(aud)
				if "yes" or "yeah" or "yep" or "sure" or "I do" in v_data:
					edit()
				elif "no" or "nah" or "nope" or "I do not" or "not" in v_data:
					return 
				else:
					alexis_speak("couldn't understand, say yes or no next time")
					return

def remove():
	global counter
	global elements
	global points
	global color
	canvas.delete(current)
	current = None
	points = []
	color = ''
	updateConsole()

def translate():
	alexis_speak("What direction do you want to move the element?")
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data = r.recognize_google(audio)
		global counter
		global elements
		global points
		if "right" in voice_data:
			moveRight()
		elif "left" in voice_data:
			moveLeft()
		elif "up" in voice_data:
			moveUp()
		elif "down" in voice_data:
			moveDown()
		else:
			alexis_speak("Sorry, couldn't understand")
			translate()

def moveRight():
	alexis_speak("How far right? in pixels")
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data = r.recognize_google(audio)
		global counter
		global elements
		global points
		canvas.move(elements[-1]["type"], int(voice_data), 0)
		for i in range(len(points)):
			points[i] += int(voice_data)
		updateConsole()

def moveLeft():
	alexis_speak("How far left? in pixels")
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data = r.recognize_google(audio)
		global counter
		global elements
		global points
		canvas.move(current, (int(voice_data) * -1), 0)
		for i in range(len(points)):
			points[i] += int(voice_data)
		updateConsole()

def moveUp():
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data = r.recognize_google(audio)
		global counter
		global elements
		global points
		canvas.move(current, 0, int(voice_data))
		for i in range(len(points)):
			points[i] += int(voice_data)
		updateConsole()

def moveDown():
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data = r.recognize_google(audio)
		global counter
		global elements
		global points
		canvas.move(current, 0, (int(voice_data) * -1))
		for i in range(len(points)):
			points[i] += int(voice_data)
		updateConsole()



B = Button(root, text = "speak", command = crud)
B.pack()
L = Label(root)
L.pack()
root.mainloop()























