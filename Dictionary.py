#Dictionary opertor in python {}
#dictionary is a collection of key-value pairs that is unordered and mutable
student ={
"name":"bhargavi",
"age":00,
"course":"python"
}

print(student)

#access elements in dictionary
print(student["name"])
print(student["age"])
print(student["course"])


#change values in a dictionary
student ["age"]=11
print(student["age"])

#add new data to a dictionary
student["city"] = "vijayawada"
print(student)

#remove data
student.pop("city")
print(student)

print(student.get("name"))
#get()returns the value of the specified key
student.update({"age":22})
#student updates the value of the 
print(student)

student.pop("age")
#pop ()removes the specified key and 

#pop item ()removes the last inserted key-value pair
student={
"name": "Bhargavi",
"age":"21",
"course":"python"
}
#pop item 
student.popitem()
print(student)
student={
"name":"Bhargavi"
}

#setdefalut
student.setdefault("age",21)
print(student)

#clear method 
student.clear()
print(student)

#copy method 
student={
    "name":"Bhargavi",
    "age":21
}
new_student=student.copy()
print(new_student)

#order of evaluvation(BODMAS)
result=(10+3)*2
print(result)

result=2+13*2
print(result)