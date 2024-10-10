def screen_wood(fml):
	move_start()
	moved = False

	if fml < 0:
		clear()

	while (not moved) or (not is_start_pos()):
		moved = True
		
		if get_ground_type() != Grounds.Turf:
			till()
			
		if get_entity_type() == Entities.Tree:
			while not can_harvest():
				continue
			harvest()
		elif get_entity_type() == Entities.Bush:
			harvest()
		
		if fml < 1:
			if is_xy_in_phase():
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
		move_next()
	