from game.builtins import *
from utils_movement import *

def snake(fn):
	move_start()
	while not is_end_pos():
		fn()
	fn()

def harvest_all():
	move_start()
	while not is_end_pos():
		if get_entity_type() == None:
			move_next()
			continue
		while not can_harvest():
			continue
		harvest()
		move_next()
	if get_entity_type() != None:
		while not can_harvest():
			continue
		harvest()

def xy_id(x, y):
	return x * 10 + y
	
def getXYID():
	c = xy_id(get_pos_x(), get_pos_y())

def getDirs():
	return [North, South, East, West]	
