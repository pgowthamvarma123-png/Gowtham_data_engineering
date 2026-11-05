details = {
    'name' : 'gowtham varma',
    'account_number' : 12345,
    'balance' : 2222.00
}
passcode = 9999
details_input = 0

pin = int(input('enter atm pin :'))

def option(details_input):
        print("hello Gowtham Please select below options")
        print("1.account details")
        print("2.balance")
        print("3.exit")
        details_input = int(input('option :'))
        return details_input
    

for i in range(1,4):
    if passcode == pin:
       details_input = option(details_input)
       break
    else:
        print('please enter correct pin')
        pin = int(input('enter atm pin :'))
if details_input == 1:
    print(f'{details}')

elif    details_input == 2 :
    print(f'{details['balance']}')
    details_input = option(details_input)
else :
     print('good bye')






