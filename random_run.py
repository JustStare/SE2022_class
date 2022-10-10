import random
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
def run_bad_student():
        global  bad_student,random_student
        for i in range(0,5):
            class_in = class_num[i]
            random_student['class_in'] = class_in
            random_student['random_student_num'] = str(random.randint(5, 8))
            bad_num_str = []
            bad_num = random.sample(list(range(90)), int(random_student['random_student_num']))
            for z in range(0,len(bad_num)):
                bad_num_str.append(class_in+str(bad_num[z]))
            random_student['all_random_student'] = bad_num_str
            bad_student.append(str(random_student))
        with open('bad_student.data','w') as f:
            for line in bad_student:
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


