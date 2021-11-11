from random import choice

people_no = int(input("Enter the number of friends joining (including you):\n"))
pay_data_dict = {}

if people_no <= 0:  
    print("No one is joining for the party")
else: 
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(people_no):
        pay_data_dict[input()] = 0
    
    pay_total = float(input("Enter the total bill value:\n"))
    pay_split = round(pay_total / people_no, 2)
    for person in pay_data_dict:
        pay_data_dict[person] = pay_split
        
    lucky_option = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_option == 'Yes':
        lucky_person = choice(list(pay_data_dict.keys()))
        print(f"{lucky_person} is the lucky one!")
        lucky_pay_split = round(pay_total / (people_no - 1), 2)
        for person in pay_data_dict:
            if person != lucky_person:
                pay_data_dict[person] = lucky_pay_split
            else:
                pay_data_dict[person] = 0
    else:
        print("No one is going to be lucky")
    
    print(pay_data_dict)
