#Manipulating
fruits=["apple","banana","orange"]
fruits.append("orange")
fruits.remove("banana")
print(fruits)


#creating aictionary
book={
    "title" :"python basics",
    "author":"John Doe",
    "year"  :2021

}
book


#Working with sets
set1={1,2,3,4}
set2={3,4,5,6}
print("union:",set1|set2)
print("intersection:",set1&set2)
print("difference:",set1-set2)


list1=[1,2,3]
list2=[4,5,6]
merged_list=list1+list2
merged_list
