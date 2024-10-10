from _utils import *

def screen_carrot(fml):
	move_start()
	moved = False
	totalPlots = get_world_size() * get_world_size()
	carrotSeedCount = num_items(Items.Carrot_Seed)
	
	if carrotSeedCount < totalPlots:
		trade(Items.Carrot_Seed, totalPlots - carrotSeedCount)

	while (not moved) or (not is_start_pos()):
		moved = True
		
		if get_ground_type() != Grounds.Soil:
			till()
			
		if get_entity_type() == Entities.Carrots:
			while not can_harvest():
				continue
			harvest()
		
		if fml < 1:
			if num_items(Items.Carrot_Seed) < 1:
				trade(Items.Carrot_Seed)
			plant(Entities.Carrots)

		move_next()
	