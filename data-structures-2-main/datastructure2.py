
fruits = ("apple","banana","mango","strawberry")

print(fruits)
print(type(fruits))

print(fruits[0])

print(fruits[0:3])

print(fruits[::-1])


name,age,grade,school,country,city= ("samaviya","19","12","fgc","pakistan","peshawar")
print(name,age,grade,school,country,city)
print(name,age)
print(grade,school)
print(country,city)
print(len(fruits))



cricket = {"samaviya","neha","salman","shahrukh","aamir","zubaida","gaurav","nisha"}
chess = {"samaviya","atharv","renuka","sama","ali","salman","nisha"}

print(cricket.union(chess))
print(cricket.intersection(chess))