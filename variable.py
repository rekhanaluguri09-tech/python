#remove element from list
marks=[80,90,75]
marks.remove(90)
print(marks)

#insert method
numbers=[10,20,30]
numbers.insert(1,15)
print(numbers)

#extend method
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)

#clear method 
numbers=[10,20,30]
numbers.clear()
print(numbers)

#index method 
numbers=[10,20,30,40]
print(numbers.index(20))

#count method
numbers=[10,20,20,30,20]
print(numbers.count(20))

#sort method
numbers=[40,10,30,20]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#reverse method
numbers=[10,20,30,40,]
numbers.reverse()
print(numbers)

#copy method
numbers=[10,20,30,40]
numbers.copy()
print(numbers)
a=[1,2,3]
b=a.copy()
print(b)

#ratio method
numbers=[10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

#tuples in python ()perthasis
#Tuple is a collection of multiple values that is ordered and cannot be changed after creation
student=("Bhargavi",98,"python")
print(student[0])

#access values in a tuple
student=("Bhargavi",21,85.5)
print(student[0])
print(student[1])
print(student[2])

#tuples are immutable,meaning they cannot be changed after

#index method 
numbers=(10,20,30,40)
print(numbers.index(30))

#lenth,maximum,minimum,sum
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python {}currly braces
#set is a collection of uniqe values that is unordered and mutable
numbers={10,20,30,20,10}
print(numbers)

#suppose students have selected subjects
subjects={"python","java","python","SQL","java"}
print(subjects)

#add values to a set
subjects={"python","java"}
subjects.add("SQL")
print(subjects)

#remove values from a set
subjects.remove("java")
print(subjects)

#sets do not allow duplicate values
numbers={1,2,2,3,3,4}
print(numbers)