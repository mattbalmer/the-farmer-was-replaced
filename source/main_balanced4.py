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

while True: 
	while num_items(Items.Empty_Tank) + num_items(Items.Water_Tank) < MAX_WATER_TANKS:
		trade(Items.Empty_Tank)

	if can_harvest():
		harvest()
		
	if pos_for_pumpkin():
		if get_ground_type() != Grounds.Soil:
			till()
		if get_entity_type() != Entities.Pumpkin:
			trade(Items.Pumpkin_Seed)
			plant(Entities.Pumpkin)

		if get_water() < PUMPKIN_WATER_LEVEL and num_items(Items.Water_Tank) > 0:
			use_item(Items.Water_Tank)
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
	
		
		
