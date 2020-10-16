# for i in range(1, 100):
#     if i % 3 == 0:
#         print(str(i) + ' is a multiple of 3')
#     elif i % 5 == 0:
#         print(str(i) + ' is a multiple of 5')
#     else:
#         print(str(i))

i = 1
while i >= 1 and i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + " is a multiple of 3 and 5: FizzBuzz")
        i += 1
    elif i % 3 == 0:
        print(str(i) + ' is a multiple of 3: Fizz')
        i += 1
    elif i % 5 == 0:
        print(str(i) + ' is a multiple of 5: Buzz')
        i += 1
    else:
        print(str(i))
        i += 1
