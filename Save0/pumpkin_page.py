import tools_page

#重置无人机的位置
def reset_location():
	for i in range(get_pos_x()):
		move(West)
	for i in range(get_pos_y()):
		move(South)

#计算最近的位置
def calculate_recent(x_list,y_list,ignore_list):
	min_distance = 10000
	min_index = -1
	curr_x = get_pos_x()
	curr_y = get_pos_y()
	for i in range(len(x_list)):
		if i in ignore_list:
			continue
		distance = abs(curr_x - x_list[i]) + abs(curr_y - y_list[i])
		if distance < min_distance:
			min_distance = distance
			min_index = i
	return min_index
	
#种植南瓜	
def sowing_pumpkin():
	reset_location()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			plant(Entities.Pumpkin)			
			move(North)
		move(East)	
#收获南瓜
def get_pumpkin():
	reset_location()
	x_list =[] 
	y_list =[]
	listSize = 0
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			#判定坏南瓜
			if not can_harvest():
				listSize +=1
				x_list.append(get_pos_x())
				y_list.append(get_pos_y())
				plant(Entities.Pumpkin)				
			move(North)
		move(East)	
	while True:		
		#遍历一遍
		if listSize == 0:
			harvest()
			return	
		else:
			tools_page.wait_pumpkin()
			currSize =  listSize
			ignore_list = []
			for locationI in range(currSize):
				#倒序，节省路径
				#currIndex = currSize - locationI - 1 
				currIndex = calculate_recent(x_list,y_list,ignore_list)
				ignore_list.append(currIndex)
				tools_page.moveTo(x_list[currIndex],y_list[currIndex])
				if not can_harvest():
					plant(Entities.Pumpkin)
				else:
					listSize -=1
					x_list.pop(currIndex)
					y_list.pop(currIndex)
					

							
				
				
				
#种植和收获南瓜
def plant_pumpkin(targetNums = 10*1000):
	change_hat(Hats.Gray_Hat)
	clear()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			till()
			plant(Entities.Pumpkin)			
			move(North)
		move(East)
	
	while num_items(Items.Pumpkin)<targetNums:
		get_pumpkin()
		sowing_pumpkin()
		if num_items(Items.Carrot)<100:
			break
			

			
