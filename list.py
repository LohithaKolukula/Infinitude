l = [1,9,33,2,80,54,4,10,7,6]
print(l[:8])

print(l[8])

# with sort function
print(l.sort())

# without sort function
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i] , l[j] = l[j] , l[i]
print(l)

# with reverse function
# print(l.reverse())

# without reverse function
print(l[::-1])

s = input("Enter a string: ")
print(s[::-1])