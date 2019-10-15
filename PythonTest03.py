
def add(a,b):
    print(a+b)

add(1,2)


def add1(*params):
    sum = 0
    for item in params:
        sum += item
    print(sum)

add1(1,2,3,4,5)


def addInfo(name, age, **others):
    info = "name: %s, age: %s" % (name, age)
    for item in others:
        info = info + ", " + item + ": %s" % others[item]
    print(info)

addInfo("小明", 12, score=98,class1=10)