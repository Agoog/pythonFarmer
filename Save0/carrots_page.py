def plant_carrots(targetNums = 10*1000):
	change_hat(Hats.Gray_Hat)
	clear()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			till()
			plant(Entities.Carrot)			
			move(North)
		move(East)
	
	while num_items(Items.Carrot)<targetNums:
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
			else:	
				if get_water()<0.5 and num_items(Items.Water)>0:
					use_item(Items.Water)
			move(North)
		move(East)
		if num_items(Items.Wood)<100 or num_items(Items.Hay)<100:
			break
