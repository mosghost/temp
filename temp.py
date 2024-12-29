temp = input('請問你要攝氏溫度還是華氏溫度(輸入"攝氏"或是"華氏"): ')
if temp == '攝氏':
	c = input('輸入攝氏溫度: ')
	f = float(c) * 9 / 5 + 32
	print('華氏溫度為: ', f)
if temp == '華氏':
	f = input('輸入華氏溫度: ')
	c = (float(f) - 32) * 5 / 9
	print('攝氏溫度: ', c) 