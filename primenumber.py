a=int(input("Enter start number "))
b=int(input("Enter last number "))
prime=[]
for num in range(a,b+1):
    fact=0
    for c in range(2,num):
        if num %c==0:
            fact=1
            break
    if fact==0:
        prime.append(num)
print("prime numbers are ",prime)
