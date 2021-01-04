# #
# #
# # print('LCM_FINDER: Enter any tow numbers:')
# # num1 = int(input('Number 1: '))
# # num2 = int(input('Number 2: '))
#
# # quitWhile = False
# # i = 1
# # product = num1 * num2
# #
# # while not quitWhile:
# #     num1_multiple = num1 * i
# #     if num1_multiple % num1 == 0 and num1_multiple % num2 == 0:
# #         print(f'LCM of {num1} and {num2} is: '+str(num1_multiple))
# #         quitWhile = True
# #         break
# #     i = i + 1
#
# print('HCM_FINDER: Enter any to numbers')
# num1 = int(input('Number 1: '))
# num2 = int(input('Number 2: '))
# Factors = [[],[]]
# quitWhile = False
# i = 2
#
# nBig = num1 if num1 > num2 else num2
# nSmall = num1 if num1 < num2 else num2
# print(f'The bigger number among {num1} and {num2} is: {nBig}')
#
# while i < nSmall/2:
#     if nBig % i == 0:
#         Factors[0].append(i)
#     if nSmall % i == 0:
#         Factors[1].append(i)
#     i= i + 1
#
#
# Factors[0] = [i if (i%2 != 0) for i in Factors[0]]
# set1 = set(Factors[0])
# set2 = set(Factors[1])
# set3 = set1.intersection(set2)
# hcf = 1
# print(set1, set2)
# print(f'Set 3: {set3}')
# for n in set3:
#     hcf = hcf * n
#
# print(f'HCF of {num1} and {num2} is {hcf}')
#

num1 = 2400
num2 = 42


def factors(n):
    Factors = set()
    mid = int(n/2)+1
    for factor in range(2, mid):
        if n % factor == 0:
            Factors.add(factor)

    return Factors


Factors_of_Num1 = factors(8)
Factors_of_Num2 = factors(20)

Factors = Factors_of_Num1.intersection(Factors_of_Num2)
Factors_list = list(Factors)
Factors_list.sort()
# print(Factors_list)
print(Factors_list[len(Factors_list)-1])



















