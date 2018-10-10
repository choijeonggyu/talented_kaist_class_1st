txt1 = '자바'
txt2 = '파이썬'
num1 = 5.0
num2 = 10
print('나는 %s보다 %s에 익숙합니다..' % (txt1, txt2))
print('%s은 %s 보다 %d배 더 쉽습니다..' % (txt2, txt1, num1))
print('%d + %d = %d' % (num1, num2, num1 + num2))
print('작년 세계 경제 성장률은 전년에 비해 %d%% 포인트 증가 했다.' % num1)

from time import sleep
for i in range(100):
    msg = '\r진행률 %d%%' %(i+1)
    print(''*len(msg), end='')
    print(msg, end='')
    sleep(0.5)