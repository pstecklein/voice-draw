from tkinter import *
from tkinter import ttk, Canvas, Frame, BOTH
import speech_recognition as sr
root = Tk()
canvas = Canvas(root, height=600, width=600)
canvas.pack()
r = sr.Recognizer()


current = None
points = []
color = ''
audio = ''
voice_data = ''

def updateConsole():
	L['text'] = "Points: %s \nColor: %s \nCurrent: %s" % (points, color, current)

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
def poly(color, points):
	return canvas.create_polygon(points, outline=color, fill=color, width=5)


def createElement():
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data = r.recognize_google(audio)
		global color
		global points
		global current
		if "red" in voice_data:
			color = '#f00'
		if "green" in voice_data:
			color = '#0f0'
		if "blue" in voice_data:
			color = '#00f'
		if "square" and ("center" or "middle") in voice_data:
			points = [250, 250, 350, 250, 350, 350, 250, 350, 250, 250]
			current = square(color = color, points = points)
		if "square" and "top left" in voice_data:
			points = [10, 10, 110, 10, 110, 110, 10, 110, 10, 10]
			current = square(color = color, points = points)
		if "square" and "top right" in voice_data:
			points = [495, 10, 595, 10, 595, 110, 495, 110, 495, 10]
			current = square(color = color, points = points)
		if "square" and "bottom right" in voice_data:
			points = [495, 495, 595, 495, 595, 595, 495, 595, 495, 495]
			current = square(color = color, points = points)
		if "square" and "bottom left" in voice_data:
			points = [10, 495, 110, 495, 110, 595, 10, 595, 10, 495]
			current = square(color = color, points = points)
		if "triangle" in voice_data:
			triangle(color = color, points = [10, 10, 70, 20, 40, 120, 10, 10 ])
		if "circle" in voice_data:
			circle(color = color, points = [10, 10, 80, 80])
		if "line" in voice_data:
			line()
		if "polygon" in voice_data:
			poly(color = color, points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200])
		if "dotted" in voice_data:
			dotted()
		if "remove" in voice_data:
			remove()
		if "move" in voice_data:
			translate()
	updateConsole()


def remove():
	global current
	global points
	global color
	canvas.delete(current)
	current = None
	points = []
	color = ''
	updateConsole()

def translate():
	with sr.Microphone() as source:
		audio = r.listen(source)
		voice_data = r.recognize_google(audio)
		global current
		global points
		canvas.move(current, int(voice_data), int(voice_data))
		for i in range(len(points)):
			points[i] += int(voice_data)
		updateConsole()


B = Button(root, text = "speak", command = createElement)
B.pack()

M = Button(root, text = "Move shape", command = translate)
M.pack()

L = Label(root)
L.pack()

root.mainloop()








