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


if __name__ == "__main__":
    lec3()