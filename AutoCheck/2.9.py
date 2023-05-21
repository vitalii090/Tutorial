first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

if first > 0 and second > 0:
    if first <= second:
        gcd = first
    else:
        gcd = second

    while first % gcd != 0 or second % gcd != 0:
        gcd -= 1
 
else:
    print('Error')
print(gcd)