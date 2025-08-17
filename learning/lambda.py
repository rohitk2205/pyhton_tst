def myfilter(name):
    return name[1]

String = "those are the words"
stringlist = String.split()
print(stringlist)
sortedlist = sorted(stringlist)
print(sortedlist)
# def funcname(param1,param2,*args,):



print(sorted(stringlist,key = lambda name:myfilter(name)))
#     # print("rohit")