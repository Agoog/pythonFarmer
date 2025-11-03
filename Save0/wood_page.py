def plant_wood(targetNums = 10*1000):
	change_hat(Hats.Gray_Hat)
	clear()
	while num_items(Items.Wood)<targetNums:
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				if get_water()<0.5 and num_items(Items.Water)>0:
					use_item(Items.Water)
				if get_pos_x()==get_pos_y() or get_pos_x()+get_pos_y() == 5:
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
		
			move(North)
		move(East)

def plant_wood(targetNums = 10*1000):
	change_hat(Hats.Gray_Hat)
	clear()
	while num_items(Items.Wood)<targetNums:
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				if get_water()<0.5 and num_items(Items.Water)>0:
					use_item(Items.Water)
				if get_pos_x()==get_pos_y() or get_pos_x()+get_pos_y() == get_world_size()-1:
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
				if num_items(Items.Fertilizer)>0:
					use_item(Items.Fertilizer)
		
			move(North)
		move(East)	
