a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = float(input("Choose a number: "))

new_list = []

for i in a:
    if i<num:
        new_list.append(i)


print (new_list)

## to write the above code in 1 line
print([ i for i in a if i < 10])

