strx = input().split(" ")
a = int(strx[0])
b = int(strx[1])
c = int(strx[2])

if(a==b or b==c or a==c or a+b == c or a+c == b or b + c == a):
	print('S')
else:
	print('N')