import tools_page



#恐龙骨头-贪食蛇-路径算法
def get_dinosaur_bone():
	clear()
	set_world_size(14)
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
			#print("i=",i)
			for j in range(get_world_size()-2):
				if not move(North):
					change_hat(Hats.Brown_Hat)
					change_hat(Hats.Dinosaur_Hat)
			if not move(East):
				change_hat(Hats.Brown_Hat)
				change_hat(Hats.Dinosaur_Hat)
			for j in range(get_world_size()-2):	
				if not move(South):
					change_hat(Hats.Brown_Hat)
					change_hat(Hats.Dinosaur_Hat)
			if i!=get_world_size()/2-1: 
				if not move(East):
					change_hat(Hats.Brown_Hat)
					change_hat(Hats.Dinosaur_Hat)
		if not move(South):
			change_hat(Hats.Brown_Hat)
			change_hat(Hats.Dinosaur_Hat)
		if not  tools_page.moveTo(0,1):
			change_hat(Hats.Brown_Hat)
			change_hat(Hats.Dinosaur_Hat)


#恐龙骨头-贪食蛇-DFS路径算法
def get_dinosaur_bone_dfs():
	clear()
	set_world_size(6)
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
	#bfs_path_list []
	bfs_path_list = []
	path = []
	
	mPoint = "mPoint"
	mRecordPath="recordPath"
	
	while True:
		#获取到下一个点位
		next_x, next_y = measure()
		bfs_list = [(get_pos_x(),get_pos_y())]

		while len(bfs_list) > 0:
			curr_x,curr_y = bfs_list.pop(0)
			if curr_x == next_x and curr_y == next_y:
				break

			#创建一个字典记录当前点位信息，键为坐标，值为已选择的方向列表
			keyPointDic = {mPoint:(get_pos_x(),get_pos_y()),mRecordPath:[(get_pos_x(),get_pos_y())]}
			#找出来时的路径
			for path_item in bfs_path_list:
				if path_item[mPoint]==(curr_x,curr_y):
					keyPointDic[mRecordPath] = path_item[mRecordPath]
					break
			#记录当前点位路径
			#向四个方向扩展
			for direction in [North,South,West,East]:
				target_x = curr_x
				target_y = curr_y
				if direction == West:
					if curr_x>0:
						target_x = curr_x-1
				elif direction == East:
					if curr_x<get_world_size()-1:
						target_x = curr_x+1
				elif direction == North:
					if curr_y<get_world_size()-1:
						target_y = curr_y+1
				elif direction == South:
					if curr_y>0:
						target_y = curr_y-1
				if (target_x != curr_x or target_y != curr_y) and venue_List[target_x][target_y] == 0:
					keyPointDicTemp = {mPoint:(get_pos_x(),get_pos_y()),mRecordPath:[]}
					keyPointDicTemp[mPoint]=(target_x,target_y)
					rePoint = False
					for recordItem in keyPointDic[mRecordPath]:
						keyPointDicTemp[mRecordPath].append(recordItem)
					for bfs_item in bfs_list:
						if bfs_item == keyPointDicTemp[mPoint]:
							rePoint = True
							break
					keyPointDicTemp[mRecordPath].append(keyPointDicTemp[mPoint])
					if not rePoint :
						bfs_path_list.append(keyPointDicTemp) 
						bfs_list.append((target_x,target_y))
			# if curr_x>0:
			# 	if venue_List[curr_x-1][curr_y] == 0:
			# 		keyPointDicTemp = {mPoint:(get_pos_x(),get_pos_y()),mRecordPath:[]}
			# 		keyPointDicTemp[mPoint]=(curr_x-1,curr_y)
			# 		rePoint = False
			# 		for recordItem in keyPointDic[mRecordPath]:
			# 			keyPointDicTemp[mRecordPath].append(recordItem)
			# 		for bfs_item in bfs_list:
			# 			if bfs_item == keyPointDicTemp[mPoint]:
			# 				rePoint = True
			# 				break
			# 		keyPointDicTemp[mRecordPath].append(keyPointDicTemp[mPoint])
			# 		if not rePoint :
			# 			bfs_path_list.append(keyPointDicTemp) 
			# 			bfs_list.append((curr_x-1,curr_y))
			# if curr_x<get_world_size()-1:
			# 	if venue_List[curr_x+1][curr_y] == 0:
			# 		keyPointDicTemp = {mPoint:(get_pos_x(),get_pos_y()),mRecordPath:[]}
			# 		keyPointDicTemp[mPoint]=(curr_x+1,curr_y)
			# 		rePoint = False
			# 		for recordItem in keyPointDic[mRecordPath]:
			# 			keyPointDicTemp[mRecordPath].append(recordItem)
			# 		for bfs_item in bfs_list:
			# 			if bfs_item == keyPointDicTemp[mPoint]:
			# 				rePoint = True
			# 				break
			# 		keyPointDicTemp[mRecordPath].append(keyPointDicTemp[mPoint])
			# 		if not rePoint :
			# 			bfs_path_list.append(keyPointDicTemp) 
			# 			bfs_list.append((curr_x+1,curr_y))
			# if curr_y>0:
			# 	if venue_List[curr_x][curr_y-1] == 0:
			# 		keyPointDicTemp = {mPoint:(get_pos_x(),get_pos_y()),mRecordPath:[]}
			# 		keyPointDicTemp[mPoint]=(curr_x,curr_y-1)
			# 		rePoint = False
			# 		for recordItem in keyPointDic[mRecordPath]:
			# 			keyPointDicTemp[mRecordPath].append(recordItem)
			# 		for bfs_item in bfs_list:
			# 			if bfs_item == keyPointDicTemp[mPoint]:
			# 				rePoint = True
			# 				break
			# 		keyPointDicTemp[mRecordPath].append(keyPointDicTemp[mPoint])
			# 		if not rePoint :
			# 			bfs_path_list.append(keyPointDicTemp) 
			# 			bfs_list.append((curr_x,curr_y-1))					
			# if curr_y<get_world_size()-1:
			# 	if venue_List[curr_x][curr_y+1] == 0:
			# 		keyPointDicTemp = {mPoint:(get_pos_x(),get_pos_y()),mRecordPath:[]}
			# 		keyPointDicTemp[mPoint]=(curr_x,curr_y+1)
			# 		rePoint = False
			# 		for recordItem in keyPointDic[mRecordPath]:
			# 			keyPointDicTemp[mRecordPath].append(recordItem)
			# 		for bfs_item in bfs_list:
			# 			if bfs_item == keyPointDicTemp[mPoint]:
			# 				rePoint = True
			# 				break
			# 		keyPointDicTemp[mRecordPath].append(keyPointDicTemp[mPoint])
			# 		if not rePoint :
			# 			bfs_path_list.append(keyPointDicTemp) 
			# 			bfs_list.append((curr_x,curr_y+1))
		#移动到下一个点位
		#获取路径
		for path_item in bfs_path_list:
			if path_item[mPoint] == (next_x,next_y):
				path = path_item[mRecordPath]
		for path_point in path:
			tools_page.moveTo(path_point[0],path_point[1])
			venue_List[get_pos_x()][get_pos_y()] = 1
			#记录蛇的位置
			snake_Path.insert(0,(get_pos_x(),get_pos_y()))
			(tail_x,tail_y) = snake_path.pop()
			#释放尾部位置
			venue_List[tail_x][tail_y] = 0
		


#get_dinosaur_bone()
get_dinosaur_bone_dfs()