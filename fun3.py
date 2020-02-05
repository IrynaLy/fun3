from random import randint as rnd

a = (int(input("бажана довжина списку №1")))
b = (int(input("бажане максимальне значення елементів списку №1")))
c = (int(input("бажана довжина списку №2")))
d = (int(input("бажане максимальне значення елементів списку №2")))

def listFunc1 (a, b, c, d):
    list1 = []
    for i in range(a):
        list1.append(rnd(0, b+1))

        list2 = []
        for e in range(c):
            list2.append(rnd(0, d+1))

            list3 = []
            for s in list1:
                for s in list2:
                    list3.append(s)

                    if len(list3) == 0:
                        print("співпадінь не знайдено")

                    else:
                        return list(set(list3))

                    print (listFunc1(a, b, c, d))
