rows=int(input("Please Enter the total number of rows:"))
number=1

print("FLOYD'S TRIANGLE:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=' ')
        number=number+1
    print()