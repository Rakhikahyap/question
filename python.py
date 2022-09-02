# dict = {"devloper" : {"count" : '2',"user" : ["anurag"]},"tester" : {"count":"2","user":["jyoti","rohit"]}}
# for i in dict:
# 	length = len(dict[i]["user"])
# 	print(i,length)
# 	print(dict[i]["user"])

dict = {"devloper" : {"count" : '2',"user" : ["anurag"]},"tester" : {"count":"2","user":["jyoti","rohit"]}}
for i in dict:
	length = len(dict[i]["user"])
	print(i,length)
	for j in range(len(dict[i]["user"])):
		print(dict[i]["user"][j])
	print()