key = 1234
error = 3
while error > 0:
	password = input('請輸入密碼: ')
	password = int(password)
	if password != key:
		print('密碼錯誤、還可以輸入:' , error)
		error = error - 1
	else:
		print('登入成功')
		break





