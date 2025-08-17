# mylist= [1,2,3,4,5]

# iterator = iter(mylist)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))



def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  
print(next(gen)) 