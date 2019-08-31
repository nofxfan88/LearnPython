def collatz(number):

    if number % 2 == 0:
        return number // 2
    else:
        return (number * 3) + 1

while True:
    print('Enter a number: ', end='')
    try:
        num = int(input())
        break
    except:
        print('Invalid input!')


while num != 1:
    num = collatz(num)
    print(num)
