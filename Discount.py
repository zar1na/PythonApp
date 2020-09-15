#This can be adjusted to any value to represent product price 

PRICE = 150

#valid discount
discount = [
    'STUDENT10',
    'SPRING10',
    'MEMBER123'
]

buyer_code = input('Please type in discount code: ')

print('Processing...\n')
#IF logic for applying discount 
if buyer_code in discount:
    final_price = PRICE * 0.9
    print('10% discount applied! \n')
else:
    final_price = PRICE
    
print("Please pay £{} at checkout".format(final_price))
