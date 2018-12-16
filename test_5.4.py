#序列 20181216
#手动实现list方法
strtemp = ('1','2','3','4','5')
#strtemp = '12345'
print(type(strtemp))
print(strtemp)
strtemp2 = []
print(type(strtemp2))
for c in strtemp:
    strtemp2 += c
#    print(strtemp2) 
print(strtemp2)

#list()
#tuple()
#str()
#max()
#min()
#sum

tuple1 = 1,2,3,4,5
print(sum(tuple1))
print(sum(tuple1,10)) #从10开始累加

#sorted()
print('sort test')
list1 = [1,2,3,4,5,4,3,2,1]
list2 = list1[:]
print('list1:' + str(list1))
print('list2:' + str(list2))
list1.sort()
print('list1 .sort():' + str(list1))
list3 = sorted(list2)
print('list2 sorted():' + str(list2))
print(type('list3:' + str(list3)))
print('list3:' + str(list3))
strtemp = "strtmep print format"
print(type(strtemp))
print(strtemp)

#reversed()
#zip()
print('zip test')
str1 = '12345'
str2 = 'abcde'
tuple1 = ('x','y','z')
for each in zip(str1,str2,tuple1):
    print(each)
