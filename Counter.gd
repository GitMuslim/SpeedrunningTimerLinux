extends Label

var time = 0
var timer_on = false

func _ready():
	$AnimationPlayer.play("gray")
	pass

func _process(delta):
	if int(get_node("stop_play").text) == 0 and time != 0:
		timer_on = false
		$AnimationPlayer.play("blue")
	elif int(get_node("stop_play").text) == 1:
		timer_on = true
		$AnimationPlayer.play("green")
	elif int(get_node("stop_play").text) == 2:
		timer_on = false
		time = 0
		$AnimationPlayer.play("gray")
	if(timer_on):
		time += delta
		
	var mils = fmod(time,1)*1000
	var secs = fmod(time,60)
	var mins = fmod(time, 60*60) / 60
	var hr = fmod(fmod(time,3600 * 60) / 3600,24)
	var dy = fmod(time,12960000) / 86400
	
	var time_passed = "%02d : %02d : %02d : %02d : %03d" % [dy,hr,mins,secs,mils]
	text = time_passed# + " : " + var2str(time)
	
	pass
