from godot import exposed, export
from godot import *
from pynput import keyboard

sus = 0

def on_press(key):
	global sus
	try:
		print('alphanumeric key {0} pressed'.format(key.char))
	except AttributeError:
		print('special key {0} pressed'.format(key))
		if str(key) == "Key.ctrl_r":
			sus = 0
		elif str(key) == "Key.f9":
			sus = 1
		elif str(key) == "Key.insert":
			sus = 2
		
listener = keyboard.Listener(on_press=on_press)
listener.start()

@exposed
class scene1(Node2D):
	def _process(self, _delta):
		self.get_node("Counter/stop_play").text = str(sus)
