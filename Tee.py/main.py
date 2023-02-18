# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


"""def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from math import sqrt

print('Pythagorean theorem calculator! Calculate your triangle sides.')
print('Assume the sides are a, b, c and c is the hypotenuse (the side opposite of the right angle')
formula = input('Which side (a, b, c) do you wish to calculate? side ')

if formula == 'c':
    side_a = int(input('Input the length of the side a: '))
    side_b = int(input('Input the length of the side b: '))

    side_c = sqrt(side_a * side_a + side_b * side_b)

    print('The length of side c is, ')
    print(side_c)



elif formula == 'a':
    side_b = int(input('Input the length of the side b: '))
    side_c = int(input('Input the length of the side c: '))

    side_a = sqrt((side_c * side_c) - (side_b * side_b))

    print('The length of side a is, ')
    print(side_a)


elif formula == 'b':
    side_a = int(input('Input the length of the side a: '))
    side_c = int(input('Input the length of the side c: '))

    side_b = sqrt((side_c * side_c) - (side_a * side_a))

    print('The length of side b is, ')
    print(side_b)


else:
    print('Please select a side between a, b, c')

def binarySearch(numbers, 1, -1, h, x):
    if h >= 1:
        mid = 1 + (h-1)//2
        if numbers[mid] == x:
            return mid
        elif numbers[mid] > x:
            return binarySearch(numbers, 1, mid-1, x)
        else:
            return binarySearch(numbers, mid+1, h, x)
    else:
            return -1

numbers = [1,8,6,8,3]
print(binarySearch(numbers, 0, len(numbers)-1, 6))

def missing_number(l):
    first = 0
    second = 0
    for i in range(1,101):
        first ^= i
    for i in l:
        second ^= i
    return first ^ second """



