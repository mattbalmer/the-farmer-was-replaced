def solveMaze():
	solved = False

	dirs = [North, East, South, West]
	dirIndex = 0

	while not solved:
		if get_entity_type() == Entities.Treasure:
			harvest()
			solved = True
			break

		dirIndex = cycleNum(dirIndex, 2, 4)
		
		for i in range(4):
			dirIndex = cycleNum(dirIndex, -1, 4)
			if move(dirs[dirIndex]):
				break

def screen_mazeDumb(fml):
	move_start()
	moved = False

	if fml < 0:
		clear()

	while (not moved) or (not is_start_pos()):
		moved = True
		
		if get_entity_type() == Entities.Bush:
			while not can_harvest():
				continue
			if num_items(Items.Fertilizer) < 1:
				trade(Items.Fertilizer)
				use_item(Items.Fertilizer)
				if get_entity_type() == Entities.Bush or get_entity_type() == Entities.Treasure:
					harvest()
				elif get_entity_type() == Entities.Hedge:
					solveMaze()
		
		if fml < 1:
			plant(Entities.Bush)
		move_next()