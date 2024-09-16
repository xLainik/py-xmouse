import mouse
import keyboard
import time

import win32api, win32con

GIRO = (205, 749)
BALL = [(100, 105)]

def click(delay):
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(delay)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def giro():
	pos = win32api.GetCursorPos()

	win32api.SetCursorPos(GIRO)
	click(0)
	win32api.SetCursorPos(pos)

def ball_click():
	pos = win32api.GetCursorPos()

	win32api.SetCursorPos(BALL[-1])
	click(0)
	win32api.SetCursorPos(pos)
	click(0)
	click(0)

def set_ball():
	pos = win32api.GetCursorPos()
	print('setting ball: ', pos)
	BALL.append(pos)

# HOTKEYS
keyboard.add_hotkey('f3', giro)
keyboard.add_hotkey('f2', ball_click)
keyboard.add_hotkey('f4', set_ball)

while True:
    keyboard.wait('space')