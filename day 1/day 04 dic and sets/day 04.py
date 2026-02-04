# students={"name":"avinash","branch":"cse","age":22,"location":"chikmagalur"}
# print(students["name"])
# print(students["age"])
# print(students["branch"])
# print(students["location"])
# print(students.get("history",0))
# print(students.get("history",))

# for subject,score in students.items():
#     print(subject,score)
# print(len(students))
# students.update(degree="B.E")
# print(students)
# students.pop("age")
# print(students)

#** creating a dictionary using user input

a=int(input("enter the number of customers  :"))
user_purchases={}

for i in range(a):
    name=input("enter the name of customers  :")
    amount=input("enter the amount   :")
    user_purchases[name]=amount
print("custermer purchase data",user_purchases)
  