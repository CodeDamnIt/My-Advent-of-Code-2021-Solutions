#Part1
f=open("./Data/Day1input.txt")
depth=f.readlines()
count=0
for i in range(len(depth)):
	if int(depth[i])>int(depth[i-1]):
		count+=1
	
	
print(count)
#Part2
newcnt=0
for i in range(len(depth)-3):
	if int(depth[i])+int(depth[i+1])+int(depth[i+2])<int(depth[i+1])+int(depth[i+2])+int(depth[i+3]):
		newcnt+=1
	
print(newcnt)
f.close()
