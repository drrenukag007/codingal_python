num = int(input("enter a number to check whether it is an armstrong number or not: "))
armstrong = num
sum = 0
n = len(str(num))
 
while num > 0:
    digit = num % 10
    sum += digit ** n
    num //= 10
 
if sum == armstrong:
    print(f"{armstrong}== is an armstrong number.")
else:
    print(f"{armstrong} is not an armstrong number.")

