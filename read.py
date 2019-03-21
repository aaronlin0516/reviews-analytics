data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1  # count = count +1
		if count % 1000 == 0:
			print (len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

#每一筆留言的平均長度怎麼計算?

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度是', sum_len / len(data))

#篩選

new = []  # 建立一個new的清單
for d in data:	#data一百萬筆的留言中 把清單中一個一個拿出來，d是每一個留言
	if len(d) < 100:	#每一個留言長度是否小於100
		new.append(d)	#如果是，就把d留言裝進去new清單內
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])