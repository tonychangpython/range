# range 範圍
# python內建功能: 清單產生器
import random
for i in range(5):
	r = random.randint(1, 1000)
	print('這是第幾', i + 1, '次隨機數', r)