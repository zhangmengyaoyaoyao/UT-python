def lec1():
    print('hello python!')
    v = 3
    v2 = "2"

    print(type(v), v)
    v = str(v)
    print(type(v), v, v+v2)
    v = float(v)
    print(type(v), v)

    str = 'x'
    # print(int(str) + 1)
    print(str + chr(65))

def lec2():
    print("please input:")
    str = input()
    while(str != "quit"):
        print(str)
        str = input()

def lec3():
    x = 'hello'
    y = 'python!'
    m = x+y
    print(m)
    x1 = '1'
    x2 = '2'
    x3 = 3
    print(x1 + x2 + x3)

def quiz7():
    for i in range(6):
        print(i)

def quiz8():
    L = [0]*3
    print(L)
    L = [0, 1, 2] + [3, 4, 5]
    print(L)
    list1 = [0, 1, 2]

    list2 = list1

    list2[2] = 10

    print(list1) 

    print(list2)



if __name__ == "__main__":
    list1 = [0, 1, 2]

    list2 = list1

    list2[2] = 10 

    print(list2)
