
cricket = {"samaviya","neha","salman","shahrukh","aamir","zubaida","gaurav","nisha"}
chess = {"samaviya","atharv","renuka","sama","ali","salman","nisha"}

print(cricket.union(chess))
print(cricket.intersection(chess))

print(cricket.difference(chess))
print(chess.difference(cricket))


group1 = {1,3,5,6,7,9,10,11,12,25,20}
group2 = {2,4,5,6,10,16,17,29}

print(group1.union(group2))
print(group1.intersection(group2))

print(group1.difference(group2))
print(group2.difference(group1))

print(cricket.symmetric_difference(chess))
print(group1.symmetric_difference(group2))