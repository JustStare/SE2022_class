import random
import random_run
probability = 85
student_dic = {}
class_num = ['A','B','C','D','E']
check_num = 0
E_num = 0
def creat_dic(probability):
    # 一个初始概率值
    global  class_num,student_dic

    student_name = []
    for t in range(0,5):
        for i in range(0,90):
            student_ID = class_num[t] + str(i)
            student_name.append(student_ID)
    student_dic = dict.fromkeys(student_name,probability)
    print(student_dic)


def check_run(add_p,sub_p,think_bad,this_day):
    one_check_num = 0.0
    one_E_num = 0.0
    global student_dic,check_num,E_num
    print(student_dic)
    for t in range(0,5):
        for i in range(0,90):
            random_int = random.randint(1,100)
            student_name = str(class_num[t])+str(i)
            student_dic[student_name] += add_p
            if random_int > 100 - student_dic[student_name]:
                check_num += 1
                one_check_num += 1.0

                if student_name in this_day[t]['miss_student']:
                    E_num += 1
                    one_E_num += 1.0
                    print(student_name)
                    student_dic[str(student_name)] += think_bad
                else:
                    student_dic[str(student_name)] -= sub_p
    print("~~~~",one_E_num/one_check_num,one_E_num,one_check_num)

if __name__ == '__main__':
    random_run.run_bad_student()
    creat_dic(probability)

    for i in range(0,20):
        this_day = random_run.day_class_run()
        print(this_day)
        check_run(0,100,80,this_day)
    print(check_num,E_num)
    print(E_num/check_num)
