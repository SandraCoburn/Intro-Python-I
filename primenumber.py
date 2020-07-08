#Stretch goal: Write a program to determine if a number, given on the command line, is prime.
import sys
# input = int(sys.argv[1])
# #input = 7
# halfway = round(input / 2)

# if input > 1
#     print("Input is not prime")
#     exit()
# for num in range(halfway):
#     print(num)
#     if num == 0 or num == 1:
#         pass
#     elif input % num == 0:
#             print("input is not prime")
#             exit()
# else:
#     print("input is prime")

#better solution:
input = 0

if input > 1:
    for num in range(2, input):
        if input % num == 0:
            print(f"{input} is not a prime number")
            break
    else: 
        print(f"{input} is a prime!")
else:
    print(f"{input} is not a prime number")

