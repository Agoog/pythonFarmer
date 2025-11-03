#工具类

def moveTo(x,y):
	while get_pos_x() != x:
		if get_pos_x() > x:
			move(West)
		else:
			move(East)
	while get_pos_y() != y:
		if get_pos_y()>y:
			move(South)
		else:
			move(North)

def wait_pumpkin():
	for i in range(4):
		do_a_flip()

def wait_num(num):
	for i in range(num):
		do_a_flip()