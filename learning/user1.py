list1= [1,2,3,4,5]
lenght= len(list1)
#print the length of the list and the list itself
print("The length of the list is", lenght)
print("The list is", list1)

#enter ther user input to replace the value at the index number
user_input= int(input("Enter a index number to be repalced: "))
user_value = int(input("Enter a new value to be replaced: "))

#check if the user input is within the range of the list
if 0<=user_input < lenght:
    print("The index number is valid")
else:
    print("The index number is invalid")
    new_user_input = int(input("Enter a new index number to be replaced :"))
    new_user_value = int(input("Enter a new value to be replaced: "))

#repace the value at the index number with the user input
list1[user_input] = user_value
print("The updated list is", list1)



