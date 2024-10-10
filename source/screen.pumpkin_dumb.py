def screen_pumpkinDumb(fml):
	move_start()
	moved = False
	totalPlots = get_world_size() * get_world_size()
	seedCount = num_items(Items.Pumpkin_Seed)
	
	if seedCount < totalPlots:
		trade(Items.Pumpkin_Seed, totalPlots - seedCount)

	while (not moved) or (not is_start_pos()):
		moved = True
		
		if get_ground_type() != Grounds.Soil:
			till()
			
		if get_entity_type() == Entities.Pumpkin:
			while not can_harvest():
				continue
			harvest()
		
		if fml < 1:
			if num_items(Items.Pumpkin_Seed) < 1:
				trade(Items.Pumpkin_Seed)
			plant(Entities.Pumpkin)

		move_next()
	