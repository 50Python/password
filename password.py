
key = input('請設定密碼: ') #使用者設定密碼
error = 3 #設定密碼輸入錯誤次數
while error > 0: #設定 while loop 次數如果大於0、則繼續執行
	password = input('請輸入密碼: ')
	#password = int(password) #取消轉化字串為 int
	if password != key: #假如輸入的 password 不等於一開始設定的密碼
		print('密碼錯誤、還可以輸入:' , error , '次') #印出剩餘次數
		error = error - 1 # error 變數值減 1
	else:
		print('登入成功')
		break





