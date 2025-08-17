import traceback
file= "/Users/rohit/Python-test/maps_filter.py"
try:
    filepointer = open(file, "r",newline= "\n")
    out = filepointer.readlines()
    print(out)

except Exception as e:
    print(trackback.format.exe())

finally:

    filepointer.close()

# context manager with
with open(file, "r", newline="\n") as filepointer:
    out = filepointer.readlines()
    
