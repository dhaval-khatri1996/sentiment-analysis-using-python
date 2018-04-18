import word         

def sign(p):
    if p>=0:
        return 1
    else:
        return -1

#Function to evaluate Adverb or a determinet followed by a Noun/Adjective
def evalADV(polarity, oldP):
    if polarity==0:
        return oldP
    elif polarity<0:
        return polarity + abs(oldP)
    else:
        if polarity<5:
            if oldP<0:
                return polarity + oldP
            else:
                return polarity - oldP

#Function to evaluate Verb
def evalVERB(polarity, oldP):
    return polarity + sign(polarity) * oldP



                                    #Evaluation of Whole Tree
def evalTree(nodes, data, node):
    if node in data:
        return data[node].polarity
    
    else:
        temp=nodes[node]
        polarity,countP=0,0
        
        if temp[-1] in data:
            for i in temp:
                polarity+=data[i].polarity
                if data[i].polarity !=0:
                    countP+=1
            if countP!=0:
                polarity/=countP
        
        #Evaluation for Dual Case
        elif temp[0] in data:
            n = len(temp)
            for i in temp[0:n-1]:
                polarity+=data[i].polarity
                if data[i].polarity !=0:
                    countP+=1
            if countP!=0:
                polarity/=countP
                
            x,y=temp[0],temp[-1]
            oldP = evalTree(nodes, data, y)
            if data[x].tag=='ADV':
                return evalADV(polarity , oldP)

            elif data[x].tag=='VER':
                return evalVERB(polarity, oldP)

            else:
                return (polarity+oldP)/2
    
        else:
            for i in temp:
                x=evalTree(nodes, data, i)
                polarity+=x
                if x!=0:
                    countP+=1
            if countP!=0:
                polarity/=countP
    return polarity

#Tree Generation
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

        elif node.tag=='CON':
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
        
    print(evalTree(nodes, data, 1))
