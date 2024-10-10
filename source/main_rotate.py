from _screens import *

screens = [
	['Hay', screen_hay, 5, {
		'until': {
			Items.Hay: 8000,
		},
	}],
	['Wood', screen_wood, 2, {}],
	['Carrot', screen_carrot, 5, {}],
	['Pumpkin', screen_pumpkinDumb, 4, {}],
	['Maze', screen_mazeDumb, 6, {}],
]
s = 0

while True:
	name = screens[s][0]
	screen = screens[s][1]
	iterations = screens[s][2]
	config = screens[s][3]
	s = num_cycle(s, len(screens))
	
	i = 0
	
	while i < iterations:
		quick_print(name, i)
		
		# first (-1), middle (0), last (1)
		fml = 0
		if (i == 0):
			fml = -1
		elif (i == iterations - 1):
			fml = 1
		
		if fml == 1 and 'until' in config:
			quick_print('until found')
			for item in config['until']:
				min = config['until'][item]
				if num_items(item) < min:
					iterations += 1
					fml = 0
					break
			
		screen(fml)
		i += 1