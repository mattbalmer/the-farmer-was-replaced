from game.builtins import *

def is_start_pos():
	return get_pos_x() == 0 and get_pos_y() == 0

def is_end_pos():
	x = get_pos_x()
	y = get_pos_y()
	mx = get_world_size() - 1
	my = get_world_size() - 1
	worldIsEven = get_world_size() % 2 == 0
	if worldIsEven:
		my = 0
	
	return x == mx and y == my

def next_col():
	x = get_pos_x()
	y = get_pos_y()
	m = get_world_size() - 1
	
	if x == m:
		move_start()
	else:
		move(East)
		
def move_start():
	half_x = get_world_size() / 2
	half_y = get_world_size() / 2
	while get_pos_x() > 0:
		if get_pos_x() > half_x:
			move(East)
		else:
			move(West)
	while get_pos_y() > 0:
		if get_pos_y() > half_y:
			move(North)
		else:
			move(South)
	
def move_next():
	x = get_pos_x()
	y = get_pos_y()
	m = get_world_size() - 1

	if x % 2 == 0:
		if y == m:
			next_col()
		else:
			move(North)
	else:
		if y == 0:
			next_col()
		else:
			move(South)
			
def is_xy_in_phase():
	yOdd = get_pos_y() % 2 == 1
	xOdd = get_pos_x() % 2 == 1
	return (xOdd and yOdd) or (not xOdd and not yOdd)
