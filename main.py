from treeGenerater import generateTree
import word  

words=[]
words.append(word.Word(0,"I","DET"))
words.append(word.Word(-10,"don't","VER"))
words.append(word.Word(8,"like","VER"))
words.append(word.Word(0,"you","ADV"))

generateTree(words)

