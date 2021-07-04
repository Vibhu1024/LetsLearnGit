#declaring list
list1=[10,20,30,40,50]
print(list1)

#getting elements
print(list1[0])
print(list1[1])
print(list1[2])
#print(list1[6]) index out ofrange
print(list1[3])
print("index 4 value", list1[4])
print("index -1 value", list1[-1])

#multiple types of values inside list
list2=[10,'A',"hello",12.12,True]
print("values are:",list2)

#list inside list
list3=[10,'A',"hello",12.12,True,['A','B','c']]
print(list3[5])

#check boolean
a=True 
print(a*50)

b=False
print(b*50)

#welcome in python class
a="welcome"
print(a*5)

#list slicing
print(list2[0:2])
print(list2[:-1]) #drop -1 place
print(list2[0:3])
print(list2[:])
print(list2[-4:-1])

#list sorting in ascending order
list4=[12,1,5,8,40,50]
list4.sort()
print(list4)
#desorting of list
list4.sort(reverse=True)
print(list4)


#how many times zero occurs
list4=[12,1,0,40,50,0,0,0,0]
list4.count(0)
print(" 0 is present",list4.count(0), "times")
 #
list5=[12,1,0,40,50,0,0,0,50]
print(list5.index(12))
print(list5.index(1))
print(list5.index(0))
print(list5.index(50))

list6 = (912,1,['a','b','c'],'A')
print(list6.index(['a','b','c']))



#appending elements in list
list7=[12,1,0,40,50,0,0,0]
x=['A','B','C']
Y=('1','2','3')
z="welcome"
print(list7)

list7.append(x)
print(list7)

list7.append(Y)
print(list7)
 
list7.append(z)
print(list7)


#extending the list
list7=[12,1,0,40,50,0,0,0]
x=['A','B','C']
Y=('1','2','3')
z="welcome"
print(list7)

list7.extend(x)
print(list7)

list7.extend(Y)
print(list7)
 
list7.extend(z)
print(list7)

#pop function  #we can use this function in stack implementation 
#(decrease the list element)
list7.pop()
list7.pop()
list7.pop()
list7.pop()
print(list7)

#length of length
list8=[12,1,0,40,50,0,0,0]
print(len(list8))

#for loop
for temp in list8:
    print(temp)

#in or not in function    
print(12 in list8)
print(12 not in list8)
print(1 not in list8)
print(1 in list8)

#insert function
list8.insert(0,[1,2,3,4])
list8.insert(4,[1,4,8])
print(list8)