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
	
	
	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')
		
	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
	
	def _process(self, _delta):
		print(sus)
		if sus == 0:
			self.get_node("Counter/stop_play").text = "0";
		elif sus == 1:
			self.get_node("Counter/stop_play").text = "1";
		elif sus == 2:
			self.get_node("Counter/stop_play").text = "2";
		pass
