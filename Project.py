count = 1
#print columns to make it easier to read
print("Number", "Squared")

#while loop only stopping when hitting 100
while count <= 100:
    squared = count * count
    #if the squared number is greater than 200 it'll break
    if squared <= 200:
        print(count, squared)
        count = count + 1
        #count only added here so that it doesn't skip 1
    else:
        break
