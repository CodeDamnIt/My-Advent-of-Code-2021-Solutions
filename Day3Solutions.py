#Part1
f=open("./Data/Day3input.txt")
a=f.readlines()
Bit0=[]
Bit1=[]
Bit2=[]
Bit3=[]
Bit4=[]
Bit5=[]
Bit6=[]
Bit7=[]
Bit8=[]
Bit9=[]
Bit10=[]
Bit11=[]

for i in a:
	Bit0.append(i[0])
	Bit1.append(i[1])
	Bit2.append(i[2])
	Bit3.append(i[3])
	Bit4.append(i[4])
	Bit5.append(i[5])
	Bit6.append(i[6])
	Bit7.append(i[7])
	Bit8.append(i[8])
	Bit9.append(i[9])
	Bit10.append(i[10])
	Bit11.append(i[11])
	
gam=''
epi=''
if Bit0.count('0')>Bit0.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
if Bit1.count('0')>Bit1.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
if Bit2.count('0')>Bit2.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
if Bit3.count('0')>Bit3.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
if Bit4.count('0')>Bit4.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
if Bit5.count('0')>Bit5.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
if Bit6.count('0')>Bit6.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
if Bit7.count('0')>Bit7.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
if Bit8.count('0')>Bit8.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
if Bit9.count('0')>Bit9.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
if Bit10.count('0')>Bit10.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
if Bit11.count('0')>Bit11.count('1'):
	gam=gam+'0'
	epi=epi+'1'
else:
	gam=gam+'1'
	epi=epi+'0'
	
print(int(gam,2)*(int(epi,2)))
