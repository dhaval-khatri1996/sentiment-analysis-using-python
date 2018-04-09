class Node(object):
    def __init__(self, polarity=None, word=None, tag=None):
        self.polarity=polarity
        self.word=word
        self.tag=tag

words=[]
words.append(Node(2,"Apple","Noun"))
words.append(Node(2,"Cashew","Pronoun"))
words.append(Node(2,"Apple","Conjunction"))
words.append(Node(2,"Apple","Others"))
words.append(Node(2,"Apple","Conjunction"))

    
                #######################
               #  * * * * * * * * * *  #
              #  *  TREE EVALUATION  *  #
               #  * * * * * * * * * *  #
                #######################


def evalTree(nodes, data, x, polaritty):
    if x in data:
        polaritty+=data[x].polarity
    else:
        sm=0
        for i in nodes[x]:
            sm+=evalTree(nodes, data, i, 0)
        polaritty+=(sm/len(nodes[x]))
    return  polaritty


                #######################
               #  * * * * * * * * * *  #
              #  *  TREE GENERATION  *  #
               #  * * * * * * * * * *  #
                #######################

                
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

    elif node.tag=='Conjunction':
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

print(evalTree(nodes, data, 1, 0))
