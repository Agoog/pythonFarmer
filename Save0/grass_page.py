def plant_grass(targetNums = 10*1000):
	change_hat(Hats.Gray_Hat)
	clear()
	while num_items(Items.Hay)<targetNums:
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				#if get_water()<0.5:
					#use_item(Items.Water)
				move(North)
		move(East)

