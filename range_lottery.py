# 威力彩產生器
# 第一區 1~38 任選六個號碼
# 第二區 1~8 任選一個號碼
import random
a = []
t = 0
for i in range(6):
	x = random.randint(1, 38)
	a.append(x)
for i in range(len(a) - 1):
	for k in range(len(a)- i - 1):
		if a[k] > a[k + 1]:
			a[k], a[k + 1] = a[k + 1], a[k]  #交換位置

b = []
for i in range(1):
	y = random.randint(1, 8)
	b.append(y)

print('第一區號碼: ', a[0], a[1], a[2], a[3], a[4], a[5])
print('第二區號碼: ', b[0])	