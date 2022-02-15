extends Control

var following = false
var dragging_start_position = Vector2()

func _on_Move_gui_input(event):
	if event is InputEventMouseButton:
		if event.get_button_index() == 1:
			following = !following
			dragging_start_position = get_local_mouse_position()
	pass

func _process(_delta):
	if following:
		OS.set_window_position(OS.get_window_position() + get_global_mouse_position() - dragging_start_position)
	pass
