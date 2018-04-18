import nltk

import openpyxl 
wb = openpyxl.load_workbook('dataset.xlsx')
sheet = wb['Sheet1']
arr = []

for i in range(1 , sheet.max_row):
			key = sheet.cell(row=i, column=1).value
			if(key!= None):
				arr.append(key)
value=nltk.pos_tag(arr,tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in value)
print(tag_fd.most_common())