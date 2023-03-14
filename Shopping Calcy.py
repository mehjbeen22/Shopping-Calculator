# # Write a Python Program which will keep adding a stream of numbers inputted
# # by the user. The adding stop as soon as user Presses "Q/q" on the Keyboard.

sum=0
while True:
    userInput = input('Enter the Item Price and Press (Q/q) for Quit: \n')

    if userInput !='q' and 'Q':
        sum = sum+ int(userInput)
        # print(f'Order total so far : {sum}')
    else:
        print(f'Your Total Bill Amount is {sum}.')
        print('\nThanks for Shooping with Us')
        break
