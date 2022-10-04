a = int(input('первое число: '))
b = int(input('второе число: '))
deistvie = input('ввидите действие: ')
if deistvie == 'addition':
    print(a + b)
if deistvie == 'multiplication':
    print(a * b)
if deistvie == 'subtraction':
    print(a - b)
if deistvie == 'division':
    if b == 0:
        print('на ноль делить нельзя!!!')
    else:
      print(a / b)