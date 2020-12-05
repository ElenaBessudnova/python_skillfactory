field = [['*', '1', '2', '3'], ['1', '-', '-', '-'], ['2', '-', '-', '-'], ['3', '-', '-', '-']]
def show(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()
def askUserZero():
    while True:
        inputX = input('Введите номер строки нолика')
        inputY = input('Введите номер столбца нолика')

        if inputX.isdigit() and inputY.isdigit():
            zeroPosX = int(inputX)
            zeroPosY = int(inputY)
            if zeroPosX in [1, 2, 3] and zeroPosY in [1, 2, 3]:
                if field[zeroPosX][zeroPosY] != '-':
                    print("Позиция уже занята :( Попробуйте снова")
                else:
                    return [zeroPosX, zeroPosY]
            else:
                print("Такой позиции не существует, попробуйте снова")
        else:
            print("Значение должно принимать значения от 1 до 3. Попробуйте снова")


def askUserCross():
    while True:
        inputX = input('Введите номер строки крестика')
        inputY = input('Введите номер столбца крестика')
        if inputX.isdigit() and inputY.isdigit():
            crossPosX = int(inputX)
            crossPosY = int(inputY)
            if crossPosX in [1, 2, 3] and crossPosY in [1, 2, 3]:
                if field[crossPosX][crossPosY] != '-':
                    print("Позиция уже занята :(\nПопробуйте снова")
                else:
                    return [crossPosX, crossPosY]
            else:
                print("Такой позиции не существует, попробуйте снова")
        else:
            print("Значение должно принимать значения от 1 до 3. Попробуйте снова")



def winCombo(a):
    n=0
    m=0
    t=0
    r=0
    for i in range(1, len(a)):
        for j in range(1, len(a[i])-1):
            if a[i][j] == a[i][j+1] and a[i][j] == 'X' or a[i][j] == a[i][j+1] and a[i][j] == '0':
                n += 1
                s = a[i][j+1]
                if n == len(a[i])-2:
                    print("Выйграл", s)
                    return "Congratulations!"

    for i in range(1, len(a[1])):
        for j in range (1,len(a)-1):
            if a[j][i] == a[j+1][i] and a[j][i] == 'X' or a[j][i] == a[j+1][i] and a[j][i] == '0':
                m += 1
                k = a[j][i]
                if m == len(a)-2:
                    print("Выйграл", k)
                    return "Congratulations!"

    for i in range(1, len(a)-1):
        if a[i][i] == a[i+1][i+1] and a[i][i] == 'X' or a[i][i] == a[i+1][i+1] and a[i][i] == '0':
            t += 1
            z = a[i][i]
            if t == len(a)-2:
                print("Выйграл", z)
                return "Congratulations!"

    for i in range(1, len(a)-1):

        if a[i][len(a)-i] == a[i+1][len(a)-i-1] and a[i][len(a)-i] == 'X' or a[i][len(a)-i] == a[i+1][len(a)-i-1] and a[i][len(a)-i] == '0':
            r += 1
            b = a[i][len(a)-i]

            if r == len(a)-2:
                print("Выйграл", b)
                return "Congratulations!"

while True:
    show(field)
    crossPos = askUserCross()
    field[crossPos[0]][crossPos[1]]='X'
    show(field)
    result=winCombo(field)
    if result:
        show(field)
        break
    zeroPos = askUserZero()
    field[zeroPos[0]][zeroPos[1]]='0'
    result = winCombo(field)
    if result:
        show(field)
        break
    print(result)










