import random
import numpy as np
class_day = {'calss_name' : '',
             'miss_student': []
           }
class_num = ['A','B','C','D','E']
random_student = {
    'class_in':'',
    'random_student_num':int,
    'all_random_student':[]

}

bad_student = []
all_bad_student = []
def run_bad_student(X):
        global  bad_student,random_student
        bad_student = run_bad_student_gpa(X)
        for i in range(0,5):
            class_in = class_num[i]
            random_student['class_in'] = class_in
            random_student['all_random_student']=(bad_student[i])
            random_student['random_student_num'] = str(len(random_student['all_random_student']))
            all_bad_student.append(str(random_student))
        with open('bad_student.data','w') as f:
            for line in all_bad_student:
                f.write(str(line)+'\n')

def day_class_run():
    global  class_num
    all_day_class = []
    bad_student_list = []
    with open('bad_student.data','r') as f:
        bad_student = f.readlines()
        for item in bad_student:  # 遍历列表
            strt = item.replace('\n', '')  # 将每个列表中的字符串都使用空字符代替\n
            d = eval(strt)
            bad_student_list.append(d)
    newa = []
    for t in range(0,5):

        class_day['calss_name'] = class_num[t]
        class_day['miss_student'] = []
        bad_student_someone = bad_student_list[t]['all_random_student']
        for one in bad_student_someone:
            random_roll = random.randint(1,100)
            if random_roll>20:
                class_day['miss_student'].append(one)
        other_student_num  =  random.randint(0,3)
        add_num =0
        while add_num < other_student_num:
            roll_num  = random.randint(1,100)
            other_student = class_num[t] + str(roll_num)
            if (other_student not in class_day['miss_student']):
                class_day['miss_student'].append(other_student)
                add_num += 1
        all_day_class.append(class_day.copy())

    return all_day_class

def make_GPA():
    student_name = []
    for i in range(0,5):
        for t in range(0,90):
            student_name.append(class_num[i]+str(t))

    # 生成正态分布
    s = np.random.normal(200, 60, 1000)
    s = s/100.0
    student_gpa_list = s.tolist()
    student_gpa = dict(zip(student_name,student_gpa_list))
    print(student_gpa)
    with open("student_gpa.data",'w') as f:
        f.write(str(student_gpa))



def run_bad_student_gpa(X):
    with open("student_gpa.data",'r') as f:
        t = f.read()
    student_gpa_dict = eval(t)
    all_bad_student_gpa = []
    for i in range(0,5):
        class_bad_student_gpa = []
        think_bad_student_gpa = []
        while(1):
            think_bad_student_gpa=check_bad_student_gpa(i,X,student_gpa_dict)
            if len(think_bad_student_gpa)>=8:
                break
        class_bad_student_gpa = random.sample(think_bad_student_gpa,random.randint(5,8))
        all_bad_student_gpa.append(class_bad_student_gpa)
    return all_bad_student_gpa

def check_bad_student_gpa(i,X,student_gpa_dict):
    think_bad_student_gpa = []
    for t in range(0, 90):

        student_name = class_num[i] + str(t)
        if (100 * (4 - student_gpa_dict[student_name]) + random.randint(300, 400)) > 350 + 3 * X:
            think_bad_student_gpa.append(student_name)
    return think_bad_student_gpa
make_GPA()