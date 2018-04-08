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

#ABOVE IS JUST FOR TESTING PURPOSE. LATER THE LIST WILL BE IMPORTED FROM THE NLTK.

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


                #######################
               #  * * * * * * * * * *  #
              #  *  TREE EVALUATION  *  #
               #  * * * * * * * * * *  #
                #######################




