mass=[]

class OlimpTask:
    name=""
    count_all=0
    count_complate=0
    def __init__(self):
        self.name
        self.count_all
        self.count_complate
    def get_name(self):
        return self.name
    def get_count_all(self):
        return self.count_all
    def get_count_complate(self):
        return self.count_complate
    def set_name(self,nm):
        self.name=nm
    def set_count_all(self,all):
        self.count_all=all
    def set_count_complate(self,comp):
        self.count_complate=comp

class TheMoreTheBetter(OlimpTask):
    max_point=0

    def __init__(self):
        super().__init__()
        self.max_point

    def get_max(self):
        return  self.max_point

    def set_max(self,max):
        self.max_point=max

    def CalcPoint(self):
        return ((self.get_count_complate()*self.get_max())/self.get_count_all())


    def __str__(self):
        return "Ім'я - {}  " \
               "Кількість прикладів = {}   " \
               "Кількість вирішених = {}    " \
               "Максимальна кількість балів = {}    " \
               "Отримані бали = {}".format(mass[i].get_name(),
                                            mass[i].get_count_all(),
                                            mass[i].get_count_complate(),
                                            mass[i].get_max(),
                                            round(mass[i].CalcPoint(),2))



max = int(input("Максимальна кількість балів для учасників олімпіади\n"))
menu = 1
while menu == 1:
    a = 1
    n = int(input("Виберіть дію \n"
                  "1-додати учасника \n"
                  "2-вивести список \n"
                  "3-відсортувати по сумі балів\n"
                  "4-сума балів, які здобули всі учасники\n"
                  "0-вийти з програми\n"))

    if(n==1):
        while a==1:
            name = str(input("ім'я\n"))
            all = int(input("кількість прикладів\n"))
            comp = int(input("кількість вирішених\n"))
            b=1
            while b == 1:
                if int(all)>=int(comp):
                    obj = TheMoreTheBetter()

                    obj.set_name(name)
                    obj.set_count_all(all)
                    obj.set_count_complate(comp)
                    obj.set_max(max)

                    mass.append(obj)
                    b=0
                else:
                    comp = input("кількість вирішених, не може бути більшою за загальну введіть ще раз\n")
                    b=1
            a = int(input("Продовжити - 1\n"))
    if (n == 2):
        for i in range (len(mass)):
            print (mass[i])
    if (n == 3):
        N = len(mass)
        for i in range(N - 1):
            m = mass[i].CalcPoint()
            p = i
            for j in range(i + 1, N):
                if m > mass[j].CalcPoint():
                    m = mass[j].CalcPoint()
                    p = j
            if p != i:
                t = mass[i]
                mass[i] = mass[p]
                mass[p] = t

        print("Відсортовані учасники по балах")
        for i in range (len(mass)):
            print(mass[i])

    if (n == 4):
        print("Сума всіх балів набраних учасниками")
        sumall=0
        for i in range (len(mass)):
            sumall+=mass[i].CalcPoint()
        print(str(round(sumall,2)))
    if (n == 0):
        menu=0


