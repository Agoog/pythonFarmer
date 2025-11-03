import wood_page
import grass_page
import carrots_page
import pumpkin_page

targetNum = 20*1000

#用于调试
#grass_page.plant_grass(targetNum)
wood_page.plant_wood(targetNum)
#carrots_page.plant_carrots(targetNum)
#pumpkin_page.plant_pumpkin(targetNum)

while True:
	if num_items(Items.Hay)<targetNum: 
		grass_page.plant_grass(targetNum)
	if num_items(Items.Wood)<targetNum: 
		wood_page.plant_wood(targetNum)
	if num_items(Items.Carrot)<targetNum: 
		carrots_page.plant_carrots(targetNum)
	if num_items(Items.Pumpkin)<targetNum: 
		pumpkin_page.plant_pumpkin(targetNum)