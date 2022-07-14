def get_name_list(type):
	"""
	获取用户输入的列表
	
	Args:
		type(str)
	Return
		名称列表(list)
	"""
	num = int(input(f'请输入{type}数量：'))
	names = []
	for i in range(num):
		name=input(f'请输入第{i+1}个{type}的名称：')
		names.append(name)
	print(f'所有{type}：',names)
	print()
	return names

def get_scores(student_names,course_names):
	"""
	获取学生成绩
	
	Args:
		student_names(list)：学生名字列表
		course_names(list)：课程名字列表
	Return
		名称列表(list)
	"""
	scores=[]
	for i in student_names:
		student_score={}
		student_score.update({'名字':i})
		#总分
		total_score=0
		for j in course_names:
			score=float(input(f'请输入{i}的{j}成绩：'))
			student_score.update({j:score})
			total_score+=score
		student_score.update({'总分':total_score})
		#平均分average
		avg_score=total_score/len(course_names)
		student_score.update({'平均分':avg_score})
		scores.append(student_score)
	return scores

def print_tables(course_names,scores):
	"""
	打印成绩表格
	
	Args:
		course_names(list)：课程名字列表
		scores(list)：成绩列表
	Return
		None
	"""
	table_head='姓名\t'
	for i in course_names:
		table_head+=i+'\t'
	table_head+='总分\t'
	table_head+='平均分\t'
	table_head+='排名'
	print(table_head)

	sorted_scores=sorted(scores,key=lambda i:i['平均分'],reverse=True)

	rank=1
	for i in sorted_scores:
		for j in i.values():
			print(j,end='\t')
		print(f'第{rank}名')
		rank+=1

course_names=['语文','数学']
student_names=['小明','小红']
'''
course_names=get_name_list('课程')
student_names=get_name_list('学生')
'''
scores=get_scores(student_names,course_names)
print_tables(course_names,scores)