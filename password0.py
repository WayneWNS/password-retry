# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出 "登入成功!"
# 如果不正確 界印出 "密碼錯誤! 還有__次機會!"

password = 'a123456'
count = 3
while True:
	test_password = input('請輸入密碼:')
	count = count - 1
	if test_password == password:
		print('登入成功!')
		break
	elif count == 0:
		print('沒機會了，掰掰!')
		break
	else:
		print('密碼錯誤! 還有', count, '次機會!')
