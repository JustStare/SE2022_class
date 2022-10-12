import random
import random_run

probability = 85
student_dic = {}
class_num = ['A', 'B', 'C', 'D', 'E']
check_num = 0
E_num = 0
student_gpa = {}
X = 0


def creat_dic(T):
    global class_num, student_dic
    with open("student_gpa.data", 'r') as f:
        student_gpa = eval(f.read())
    student_name = []
    student_P = []
    for t in range(0, 5):
        for i in range(0, 90):
            student_ID = class_num[t] + str(i)
            student_name.append(student_ID)
            if student_gpa[student_ID] <= 4 - float(X / T):
                student_P.append(100)
            else:
                student_P.append(0)
    student_dic = dict(zip(student_name, student_P))
    print(student_dic)


## 检查函数
def check_run(add_p, sub_p, think_bad, this_day):
    one_check_num = 0.0
    one_E_num = 0.0
    global student_dic, check_num, E_num
    print(student_dic)
    for t in range(0, 5):
        for i in range(0, 90):
            random_int = random.randint(1, 100)
            student_name = str(class_num[t]) + str(i)
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
    if (one_check_num != 0):
        print("~~~~", one_E_num / one_check_num, one_E_num, one_check_num)


if __name__ == '__main__':

    while True:
        xiangguan = input("请输入绩点gpa是否与逃课学生具有相关性 (是或否):\n")
        if xiangguan == "是":
            X = 100
            break
        if xiangguan == "否":
            X = 0
            break
        else:
            print("请输入 (是或否)\n")
    random_run.run_bad_student(X)
    T = int(input(":请输入 抽点gpa与抽检人数的相关性 T的区间是(30-50) T越大抽取人数越多 但是会降低命中概率:\n"))
    creat_dic(T)
    add_p = 0
    while True:
        jug = input("是否开启全局抽检 全局抽检会降低命中概率 (默认关闭) [yes/no] : \n")
        if jug == "yes":
            add_p = float(input("请输入 局域化抽检系数 add_p [0~0.1]   局域化系数越小 概率越大 但是会减少其他人抽检概率  :\n"))
            break
        if jug == "no":
            add_p = 0
            break
        else:
            print("请输入yes/no\n")
    for i in range(0, 20):
        this_day = random_run.day_class_run()
        print(this_day)
        check_run(add_p, 100, 80, this_day)
    print(check_num, E_num)
    print(E_num / check_num)
