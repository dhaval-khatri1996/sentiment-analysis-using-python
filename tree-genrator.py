lst=[1,2,2,3,2,1,0,0,1,1,2,-3,2,1]
prev=99999
nodes={1:[2]}
data={1:[]}
current,nodc=1,1

for nmbr in lst:
    if nmbr==3:
        nodc+=1
        nodes[1].append(nodc)
        current=nodc
        data[nodc]=[3]
        prev=3

    elif nmbr==prev:
        data[current].append(nmbr)

    else:
        prev=nmbr
        nodc+=1
        nodes[current]=[nodc]
        current=nodc
        nodes[nodc]=[]
        data[current]=[prev]
print('Nodes and Childs')
for i in nodes:
      print(i,' : ',nodes[i])
print('Nodes and Data')
for i in data:
      print(i,' : ',data[i])
