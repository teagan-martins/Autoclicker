import pyautogui
import time
import keyboard

count = 0

def autoclick():
	if keyboard.is_pressed('q'):
		while count == 0:
			pyautogui.click(clicks=16)
			if keyboard.is_pressed('e'):
				break

tracker = 0

while tracker == 0:
	autoclick()


