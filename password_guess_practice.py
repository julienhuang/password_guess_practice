#猜密碼程式
password_answer = 'a123456'
n = 0
while n < 3:
	m = 2 - n
	password_entered = input('請輸入密碼')
	if m == 0:
		print('密碼錯誤! 遊戲結束!')
		break
	if password_entered != password_answer:
		print('密碼錯誤! 還有', m, '次機會!')
	elif password_entered == password_answer:
		print('猜對了!!!!')
		break
	n = n + 1