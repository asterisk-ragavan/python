# import random
# uplim = 100
# number = random.randint(1,uplim)
# score = 100
# ans = int(input("""for every wrong answer 10 points will be reduced
#  and your current score is {1}
#  guess the number between 1 to {0}: """.format(uplim,score)))
# while(ans != number):
#     if (number < ans):
#         ans = int(input("try number which is less then {}: ".format(ans)))
#         score -= 10
#         continue
#     elif(number > ans):
#         ans = int(input("try number which is greater then {}: ".format(ans)))
#         score -= 10
#         continue
#     else:
#         print("well done u did it correct '_'\n your sore is {}".format(score))
#         break
# if (ans == number):
#     print("well done u did it correct '_'\n your sore is {}".format(score))

# num = 2
# max = 1000
# min = 0
# ans = None
# while(ans != num):
#     if(num < int((max+min)/2)):
#         max = int((max+min)/2)
#         ans = max
#     else:
#         min = int((max+min)/2)
#         ans = min
# print(num)
# print(ans)

# a = ["ab", "bc", "ca"]
# b = a
# print(id(a))
# print(a)
# print(id(b))
# print(b)
# a = a + ["abc"]
# b = a
# print(id(a))
# print(a)
# print(id(b))
# print(b)