#FizzBuzzあぷり
try:
    suuzi = int(input("数字を入力して"))
except ValueError:
    print("エラー:数字を入力してください")
    exit()


for i in range(1,suuzi + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
