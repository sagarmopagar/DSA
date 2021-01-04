import math

# print('Enter a, b and c for creating a quadratic equation ax^2 + bx + c:')
# a = int(input('a - '))
# b = int(input('b - '))
# c = int(input('c - '))
#
#
# print(f'The equation you entered is: {a}x^2 + {b}x + {c}')
#
# d = b**2 - 4 * a * c
# root1 = 0
# root2 = 0
# if d > 0:
#     root1 = (- (b) + math.sqrt(d)) / (2 * a)
#     root2 = (- (b) - math.sqrt(d)) / (2 * a)
# else:
#     first_sqrt_of_d = f'+sqrt({d})'
#     second_sqrt_of_d = f'-sqrt({d})'
#     root1 = '-' + str(b) + first_sqrt_of_d + ' / ' + str((2 * a))
#     root2 = '-' + str(b) + second_sqrt_of_d + ' / ' + str((2 * a))
#
# print(f'D: {d}')
# print(f'Roots are: root 1: {root1}, root2: {root2} ')

def randomQuadraticEquationGenerator():

    roots_real = []

    for a in range(1,11):
        for b in range(1,11):
            for c in range(1,11):
                print(f'The equation is: {a}x^2 + {b}x + {c}')
                d = b ** 2 - 4 * a * c
                root1 = 0
                root2 = 0
                if d >= 0:
                    root1 = (- (b) + math.sqrt(d)) / (2 * a)
                    root2 = (- (b) - math.sqrt(d)) / (2 * a)
                    equation = [a,b,c, root1, root2]
                    roots_real.append(equation)
                else:
                    first_sqrt_of_d = f'+sqrt({d})'
                    second_sqrt_of_d = f'-sqrt({d})'
                    root1 = '-' + str(b) + first_sqrt_of_d + ' / ' + str((2 * a))
                    root2 = '-' + str(b) + second_sqrt_of_d + ' / ' + str((2 * a))

                print(f'D: {d}')
                print(f'Roots are: root 1: {root1}, root2: {root2} ')
                print('------------------------------------------------------')

    return roots_real

roots_real_list = randomQuadraticEquationGenerator()

mnk = 0