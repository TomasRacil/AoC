log=[prikaz.strip().split()+[0] for prikaz in open("log.txt", "r")]

def do(radek, logcopy):
	if radek>len(logcopy): return {"acc":0,"radek":radek,"uspech":False}
	if radek==len(logcopy): return {"acc":0,"radek":radek,"uspech":True}
	if logcopy[radek][2]>0: return {"acc":0,"radek":radek,"uspech":False}
	logcopy[radek][2]+=1
	if logcopy[radek][0] =="jmp": return do(radek+int(logcopy[radek][1]),logcopy)
	elif logcopy[radek][0]=="acc":
		val=do(radek+1,logcopy)
		return {"acc":val["acc"]+int(logcopy[radek][1]),"radek":val["radek"],"uspech":val["uspech"]}
	else: return do(radek+1,logcopy)

def repair(radek,acc):
	if log[radek][0] =="jmp" or log[radek][0] =="nop":
		cesta=do(radek+1 if log[radek][0] =="jmp" else radek+int(log[radek][1]),[prvek.copy() for prvek in log])
		if cesta["uspech"]==False:
			return repair(radek+int(log[radek][1]) if log[radek][0] =="jmp" else radek+1,acc)
		else:
			return {"acc":acc+cesta["acc"],"radek":cesta["radek"],"uspech":cesta["uspech"]}
	else:
		return repair(radek+1,acc+int(log[radek][1]))

print(do(0,[prvek.copy() for prvek in log]))
print(repair(0,0))