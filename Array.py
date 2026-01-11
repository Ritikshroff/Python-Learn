# Hello world
import array

val = array.array('i', [1, 2, 3, 4, 5])

# print(val)
# print(val.typecode, "type of array")
# print(val.buffer_info(), "buffer info")
# print(val.reverse(), "reverse")

for i in val:
    print(i , end=" | ") 

print("\n")
val.reverse()
for i in val:
    print(i , end=" / ") 

print("\n")

val.insert(2, 90)
for i in val:
    print(i , end=" | ") 
    
print("\n")


val.append(100)
val[4] = 10
for i in val:
    print(i , end=" | ") 

print("\n")

copyArray = array.array(val.typecode, (x*3 for x in val))
for i in copyArray:
    print(i , end=" | ")


print("\n")
copyArray.insert(0 , 101)
for i in copyArray:
    print(i , end=" | ")
    
print("\n")

for i in val:
    print(i , end=" | ")

print("\n")


copyArray.pop(3)
for i in copyArray:
    print(i , end=" | ")
    
print("\n")


slicing  = copyArray[2:5]
for i in slicing:
    print(i , end=" | ")

print("\n")
print("\n")
print("\n")
print("\n")



newArr = array.array('i' , [23, 32, 1, 2, 3, 4, 5, 5])
for i in newArr:
    print(i , end=" | ")


print("\n")

abc = newArr[::-1]
for i in abc:
    print(i , end=" | ")



# inputArr = array.array('i', [])
# n = int(input("Enter the length of array : "))
# for i in range(n):
#     x = int(input("Enter the value : "))
#     inputArr.append(x)

# for i in inputArr:
#     print( i , end=" | ")


print("\n")

printindex = newArr.index(5)
print(printindex)