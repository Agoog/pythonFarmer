import tools_page
#生成一个迷宫
def make_maze():
	tools_page.moveTo(0,0)
	clear()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)


#破解迷宫
def solve_maze():
	#创建一个关键节点列表，用于存储分叉点信息
	keyPointList = []
	#用一个变量记录当前行进方向
	currentDirection = None
	#记录前进方向的反方向
	reDirection = None
	#记录是否到末
	isEnd = False
	directionList = [East,North,West,South]
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			return
		if isEnd:
			#如果到达终点,而当前位置没有宝藏
			#则返回上一个分叉点继续选择下一个方向走
			while len(keyPointList) > 0:
				#如果当前位置没有宝藏，则返回上一个分叉点
				keyPoint = keyPointList.pop()
				#如果上一个分叉点有多个方向，则选择下一个方向走
				if len(keyPoint.mbDirection) > 0:
					currentDirection = keyPoint.mbDirection[len(keyPoint.mbDirection)]
					reDirection = tools_page.get_re_direction(currentDirection)
					move(currentDirection)
					keyPointDic.mbDirection.pop()
					keyPointList.append(keyPointDic)
					isEnd = False
					break
				else:
					#移动到上一个点位
					tools_page.moveTo(keyPoint.x,keyPoint.y)
			continue	
					

		#创建一个字典记录当前点位信息，键为坐标，值为已选择的方向列表
		keyPointDic = {x:get_pos_x(),y:get_pos_y(),mbDirection:[]}	
		
		for dir_member in directionList:
			if can_move(dir_member) and reDirection != dir_member:
				keyPointDic.mbDirection.append(dir_member) 	
		#判定当前位置是否有多个方向
		if len(keyPointDic.mbDirection) >1:
			#如果有多个方向则记录当前位置为分叉点，记录当前点位信息
			currentDirection = keyPointDic.mbDirection[len(keyPointDic.mbDirection)]
			reDirection = tools_page.get_re_direction(currentDirection)
			move(currentDirection)
			keyPointDic.mbDirection.pop()
			keyPointList.append(keyPointDic)
		elif len(keyPointDic.mbDirection) == 1:
			#选择最后一个方向走
			currentDirection = keyPointDic.mbDirection[len(keyPointDic.mbDirection)]
			reDirection = tools_page.get_re_direction(currentDirection)
			move(currentDirection)
			keyPointDic.mbDirection.pop()
			keyPointList.append(keyPointDic)			
		else:
			# 无路可走，标记为末端，触发回溯
			isEnd = True
		#判定是否到达终点
		#如果到达终点则结束
		#如果没有到达终点则继续走	
		#如果遇到死路则返回上一个分叉点继续选择下一个方向走
	

make_maze()
solve_maze()