import word

def sign(p):
    if p>=0:
        return 1
    return -1
    
def calculate(data, lst):
    polarity,count=0,0
    for i in lst:
        if i!=0:
            polarity+=data[i].polarity
            count+=1
    if polarity==0:
        return 0
    return polarity/count

#Function to evaluate Adverb or a determinet followed by a Noun/Adjective
def evalAdv(polarity, oldP):
    if polarity==0 or oldP==0:
        return oldP
    elif polarity<0:
        return sign(oldP) *(polarity + abs(oldP))
    else:
        if polarity<5:
            if oldP<0:
                return (5-polarity) + oldP
            else:
                return oldP - (5-polarity)
        return oldP + sign(oldP)*(polarity-4)

#Function to evaluate Verb
def evalVerb(polarity, oldP):
    return sign(polarity) * oldP


#Function to evaluate  the tree
def evalTree(nodes, data, node):
    if node in data:
        return data[node].polarity
    
    else:
        temp=nodes[node]
        polarity,x,n=0,temp[0],len(temp)
        if n==1:
            return evalTree(nodes, data, temp[0])
        else:
            if temp[-1] in data:
                return calculate(data, temp)
            else:
                polarity = calculate(data, temp[0:n-1])
                oldP = evalTree(nodes, data, temp[-1])
                if data[x].tag=='ADV':
                    return evalAdv(polarity, oldP)
                elif data[x].tag=='VERB':
                    print(polarity)
                    return evalVerb(polarity, oldP)
                else:
                    if polarity==0:
                        return oldP
                    elif oldP == 0:
                        return polarity
                return (polarity+oldP)/2


#Fucntion to generate tree
def generateTree(words):
    n=len(words)
    nodes={1:[2]}
    data={}
    nodes[2]=[3]
    data[3],prev,crNode,countN=words[0],words[0],2,3
    for node in words[1:n]:
        if prev.tag==node.tag:
            countN+=1
            nodes[crNode].append(countN)
            data[countN]=node

        elif node.tag=='CONJ':
            nodes[1].append(countN+1)
            nodes[countN+1]=[countN+2]
            data[countN+2]=node
            crNode=countN+1
            countN+=2
            
        else:
            countN+=1
            nodes[crNode].append(countN)
            crNode=countN
            nodes[crNode]=[]
            countN+=1
            nodes[crNode].append(countN)
            data[countN]=node
            
    return(evalTree(nodes, data, 1))
