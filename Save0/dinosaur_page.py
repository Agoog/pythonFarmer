import tools_page



#恐龙骨头-贪食蛇-路径算法
def get_dinosaur_bone():
	clear()
	tools_page.till_all()
	tools_page.moveTo(0,1)
	change_hat(Hats.Dinosaur_Hat)
	#假定大小是偶数的矩阵，这里存在一个路径可以够遍历所有点位
	#while True:
	#	next_x, next_y = measure()
	#	if not tools_page.moveTo(next_x,next_y):
	#		change_hat(Hats.Brown_Hat)
	while True:
		for i in range(get_world_size()/2):
			for j in range(get_world_size()-1):
				move(North)
			move(East)
			for j in range(get_world_size()-1):	
				move(South)
			move(East)
		move(South)
		tools_page.moveTo(0,1)


#恐龙骨头-贪食蛇-DFS路径算法
def get_dinosaur_bone_dfs():
	clear()
	tools_page.till_all()
	change_hat(Hats.Dinosaur_Hat)
	venue_List = []
	snake_Path = []
	for i in range(get_world_size()):
		line_list = []
		for j in range(get_world_size()):
			line_list.append(0)
		venue_List.append(line_list)
	venue_List[get_pos_x()][get_pos_y()] = 1
	snake_Path.append((get_pos_x(),get_pos_y()))	
	bfs_path_list = {}
	while True:
		#获取到下一个点位
		next_x, next_y = measure()
		bfs_list = [(get_pos_x(),get_pos_y())]

		while len(bfs_list) > 0:
			curr_x,curr_y = bfs_list.pop()
			if curr_x == next_x and curr_y == next_y:
				break

			#找出来时的路径
			for path_item in bfs_path_list:
				if list(path_item.keys())[0] == (curr_x,curr_y):
					path = list(path_item.values())[0]
			#记录当前点位路径
			if curr_x>0:
				if venue_List[curr_x-1][curr_y] == 0:
					bfs_list.append((curr_x-1,curr_y))

					bfs_path_list.append({(curr_x-1,curr_y),path.append((curr_x,curr_y))}) 
			if curr_x<get_world_size()-1:
				if venue_List[curr_x+1][curr_y] == 0:
					bfs_list.append((curr_x+1,curr_y))
					bfs_path_list.append({(curr_x+1,curr_y),path.append((curr_x,curr_y))}) 
			if curr_y>0:
				if venue_List[curr_x][curr_y-1] == 0:
					bfs_list.append((curr_x,curr_y-1))
					bfs_path_list.append({(curr_x,curr_y-1),path.append((curr_x,curr_y))}) 
			if curr_y<get_world_size()-1:
				if venue_List[curr_x][curr_y+1] == 0:
					bfs_list.append((curr_x,curr_y+1))
					bfs_path_list.append({(curr_x,curr_y+1),path.append((curr_x,curr_y))}) 
		#移动到下一个点位
		#获取路径
		for path_item in bfs_path_list:
			if list(path_item.keys())[0] == (next_x,next_y):
				path = list(path_item.values())[0]
		for path_point in path:
			tools_page.moveTo(path_point[0],path_point[1])
			venue_List[get_pos_x()][get_pos_y()] = 1
			#记录蛇的位置
			snake_Path.insert(0,(get_pos_x(),get_pos_y()))
			(tail_x,tail_y) = snake_path.pop()
			#释放尾部位置
			venue_List[tail_x][tail_y] = 0

get_dinosaur_bone()