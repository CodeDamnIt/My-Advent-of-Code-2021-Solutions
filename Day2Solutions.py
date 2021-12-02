#Part1
f=open("./Data/Day2input.txt","r")
a=f.readlines()
horizon=0
depth=0
for i in a:
	i,x=i.split()
	x=int(x)
	if i == 'forward':
		horizon+=x
	if i == 'down':
		depth+=x
	if i == 'up':
		depth-=x
	
print(horizon*depth)
#Part2
horizon=0
depth=0
aim=0
for i in a:
	i,x=i.split()
	x=int(x)
	if i == 'up':
		aim-=x
	if i == 'down':
		aim+=x
	if i == 'forward':
		horizon+=x
		depth=depth+aim*x

print(horizon*depth)
f.close()
