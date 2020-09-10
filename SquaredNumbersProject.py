#count constant
count = 1

#asking what the user would like to do
question = int(input("What would you like to do? \n"
      "1 = generate 1-100 \n"
      "2 = reach the limit of 200 \n"
      "3 = enter your own number \n"))

#answer 1
if question == 1:
    print("Number", "Squared")
    while count <= 100:
        squared = count * count
        #printing count and squared with a space
        print(count, squared)
        count = count + 1

#answer 2
if question == 2:
    print("Number", "Squared")
    #while loop only stopping when hitting 100
    while count <= 100:
        squared = count * count
        #if the squared number is greater than 200 it'll break
        if squared <= 200:
            print(count, squared)
            count = count + 1
            #count only added here so that it doesn't skip

#answer 3
if question == 3:
    user_request = int(input("Please enter a number: "))
    print("Number", "Squared")
    #user request must alwas be lower than 100 to work
    while user_request <= 100:
        if count <= user_request:
            squared = count * count
            print(count, squared)
            count = count + 1
