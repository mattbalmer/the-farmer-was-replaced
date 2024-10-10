def screen_hay(fml):
	move_start()
	moved = False
	
	if fml < 0:
		clear()

	while (not moved) or (not is_start_pos()):
		moved = True

		while not can_harvest():
			continue
		harvest()
		move_next()
	