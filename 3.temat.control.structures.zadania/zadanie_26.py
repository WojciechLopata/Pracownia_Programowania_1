pin='0805'
for i in range(3):
    user_input=input("Enter the pin code: ")
    if(user_input==pin):
        print("Correct pin")
        break
    else: print("incorrect...")
else: print ("Sorry, your payment card has been blocked.")