#Part1
f=open("./Data/Day6input.txt",'r+')
h=f.read().split(",")
g=h
for i in range(80):
			for j in range(len(g)):
				if g[j] == 0:
					g[j] = 6
					g.append(8)
				else:
					g[j] = int(g[j])-1
					
					
print("the number of lanternfishes after 80 days is",len(g))
