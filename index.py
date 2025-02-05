#Datatypes
#complex numbers - m+in
#m + jn
cmp1 = 9 + 3j
cmp2 = 8 - 5j
print(cmp1 + cmp2)
print(cmp1 - cmp2)
print(cmp1 * cmp2)
print(cmp1 / cmp2)
print(cmp1 ** cmp2)
#print(cmp1 // cmp2)
#print(cmp1 % cmp2)

#Boolean - True or False
print(3 > 9)
print(3 >= 9)
print(3 <= 9)

bool1 = True
print(type(bool1))
print(type(False))
print(type(True))

print(int(True))
print(int(False))

#sequences
#list - indexing and mutable
list1 = [2,3,4,6,9,10,-1, 'String', True,[1, 2, 3]]
print(type(list1))
print(list1)

print(list1[4])
print(list[9])
print(list[len(list1)-1])
print(list1[-1])

#slicing
print("---slicing---")
print(list1[2:6])
print(list1[1:6:8])
print(list1[8:6:-3])
print(list1[-6:-3])
print(list1[-3:-6:-1])

temp = list1[9]
print(temp[2])
print(list1[9][2])

#Tuple - () - Immutable

tup1 = (1, 2, True, "Str1",0.9)
print(tup1[1:4])
print(tup1[1:3:5])
print(tup1[5:3:-1])
print(tup1[-5:-3])
#Range
range(0, 100)
print(list(range(0, 50)))
print(list(range(50, 0, -1)))
print(list(range(0,50, 2)))
print(list(range(0,50, 3)))
print(list(range(50, 0, -3)))





                                                                                                        