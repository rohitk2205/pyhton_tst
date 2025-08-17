x= 1024
count= 0
while x>0:
    x= x // 2
    count+= 1
print(  "Number of times x can be divided by 2 until it becomes 0:", count)

binary_representation = bin(1024)
print("Binary representation of 1024 is:", binary_representation)
hexadecimal_representation = hex(1024)
print("Hexadecimal representation of 1024 is:", hexadecimal_representation)