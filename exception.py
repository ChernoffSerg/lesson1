def cut_cake(people):
    try:
        z = 1 / people
        print(f'Каждый получит {z} пирога')
    except ZeroDivisionError:
        print("Не надо делить на 0!")
#cut_cake(0)

a = 8
a /= 2
print(a +    2)

def foo(a):
   print(a)

foo(a=1)
