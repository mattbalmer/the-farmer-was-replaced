from _screens import *

MAX_WATER_TANKS = 50
PUMPKIN_SIZE = 3
CARROT_COL = PUMPKIN_SIZE

PUMPKIN_WATER_LEVEL = 0.2
CARROT_WATER_LEVEL = 0.2
TREE_WATER_LEVEL = 0.2

def pos_for_pumpkin():
	return get_pos_x() < PUMPKIN_SIZE and get_pos_y() < PUMPKIN_SIZE

def pos_for_carrot():
	return get_pos_x() == PUMPKIN_SIZE
	
def pos_for_wood():
	yOdd = get_pos_y() % 2 == 1
	xOdd = get_pos_x() % 2 == 1
	return (xOdd and yOdd) or (not xOdd and not yOdd)
	
lap = 0
lastLap = -1
focusPumpkins = True

go_to_start()

while True: 
	while num_items(Items.Empty_Tank) + num_items(Items.Water_Tank) < MAX_WATER_TANKS:
		trade(Items.Empty_Tank)
		
	harvestable = 0
	while focusPumpkins:
		if can_harvest():
			harvestable += 1
			if harvestable == 8:
				if get_pos_x() == 0:
					move(East)
				if get_pos_x() == 2:
					move(West)
				if get_pos_y() == 0:
					move(North)
				if get_pos_y() == 2:
					move(South)
		else:
			harvestable = 0
			
		if get_ground_type() != Grounds.Soil:
			till()
		if get_entity_type() != Entities.Pumpkin:
			trade(Items.Pumpkin_Seed)
			plant(Entities.Pumpkin)

		if get_water() < PUMPKIN_WATER_LEVEL and num_items(Items.Water_Tank) > 0:
			use_item(Items.Water_Tank)
			
		if harvestable < 8:
			if get_pos_x() == 0 and get_pos_y() < PUMPKIN_SIZE - 1:
				move(North)
			elif get_pos_y() == PUMPKIN_SIZE - 1 and get_pos_x() < PUMPKIN_SIZE - 1:
				move(East)
			elif get_pos_x() == PUMPKIN_SIZE - 1 and get_pos_y() > 0:
				move(South)
			elif get_pos_y() == 0 and get_pos_x() > 0:
				move(West)
		else:
			while not can_harvest():
				if get_entity_type() != Entities.Pumpkin:
					trade(Items.Pumpkin_Seed)
					plant(Entities.Pumpkin)
			harvest()
			focusPumpkins = False
			move(North)
			move(North)
			move(West)

	if is_end_pos():
		lap += 1
		focusPumpkins = True

	if can_harvest():
		harvest()
		
	if pos_for_pumpkin():
		quick_print('skip')
	elif pos_for_carrot():
		if get_ground_type() != Grounds.Soil:
			till()
		if get_entity_type() != Entities.Carrots:
			trade(Items.Carrot_Seed)
			plant(Entities.Carrots)
			
		if get_water() < CARROT_WATER_LEVEL and num_items(Items.Water_Tank) > 0:
			use_item(Items.Water_Tank)	
	elif pos_for_wood():
		if get_ground_type() != Grounds.Turf:
			till()
		plant(Entities.Tree)
	else:
		if get_ground_type() != Grounds.Turf:
			till() 
		
	if get_pos_y() == get_world_size() - 1:
		move(East)
		move(North)
	else:
		move(North)
	
		
		
	