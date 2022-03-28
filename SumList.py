def sum_list(n):
    li = []
    for i in range(1,n+1):
        i = int(input("ënter a element : "))
        li.append(i)
    print(li)
    print("sum of list",sum(li))

n = int(input("enter a no. of element you want in list : "))
sum_list(n)