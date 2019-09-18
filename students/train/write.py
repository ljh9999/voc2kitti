import os
path = os.path.join('/home/nano/Documents/students/val/labels/')
txtname = os.path.join('/home/nano/Documents/students/val/xmllist.txt')
listname = os.listdir(path)

with open(txtname,'w+') as f:

	for i in range(len(listname)):
		item_name = listname[i]
		print(item_name)
		f.write(item_name)
		f.write('\r\n')
	
	
