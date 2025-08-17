# def mult (a):
#     return a*a

list1 = [i for i in range(10)]

# list2 = list(map(mult, list1))
# print( list2)

def is_even(x):
    return x%2==0

even_num = list(filter(is_even, list1))
print(even_num)



