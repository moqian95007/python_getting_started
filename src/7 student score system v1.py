'''
def get_list(type):
    names = []
    num = int(input(f'请输入{type}数量：'))
    for i in range(num):
        name=input(f'请输入第{i+1}的名称：')
        names.append(name)
    print(f'所有{type}：',names)
    print()
    return names


course_names=get_list('课程')
student_names=get_list('学生')
print(course_names)
print(student_names)
'''

student_num=2
course_num=2
course_names=['语文','数学']
student_names=['小明','小红']

scores=[]
for i in range(student_num):
	student_score={}
	student_name=student_names[i]
	student_score.update({'名字':student_name})
	#总分
	total_score=0
	for j in range(course_num):
		course_name=course_names[j]
		score=float(input(f'请输入{student_name}的{course_name}成绩：'))
		student_score.update({course_name:score})
		total_score+=score
	#平均分average
	avg_score=total_score/course_num
	student_score.update({'总分':total_score,'平均分':avg_score})
	scores.append(student_score)
print(scores)
sorted_scores=sorted(scores,key=lambda i:i['总分'],reverse=True)
print(sorted_scores)

if student_num>0 and course_num>0:
	#拼表头
	print('名称',end='\t')
	for i in range(course_num):
		print(course_names[i],end='\t')
	print('总分',end='\t')
	print('平均分',end='\t')
	print('排名')
	rank=1
	for i in sorted_scores:
		for j in i.values():
			print(j,end='\t')
		print(f'第{rank}名')
		rank+=1