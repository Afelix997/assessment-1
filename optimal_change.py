import math

def optimal_change(item_cost,amount_paid):

    #Special cases to check for before running rest of program
    if amount_paid < item_cost:
        return 'Insufficent Funds.'
    elif amount_paid==item_cost:
        return 'Exact payment recieved. Have a good day!'
    elif amount_paid == 0 and item_cost== 0:
        return 'No Transaction.'
    elif item_cost == 0 and amount_paid>0:
        return f'The item is Free! You will be refunded your ${amount_paid}.'

    #Dictionary created to hold all currency types and associated values
    currency_dict={"$100 bill": 100.00,"$50 bill": 50.00,"$20 bill": 20.00,"$10 bill": 10.00,
                    "$5 bill": 5.00,"$1 bill": 1.00,"quarter": 00.25,"dime": 00.10,
                    "nickel": 00.05,"penny": 00.01} 

    #Find amount we will be working with and set up variables we will be using in upcoming loop
    change = amount_paid-item_cost
    rem = change
    res_list = []

    #A for in loop is used to cycles through dictionary and root out remaining quantity after consecutivly deviding our remainder
    #against currency in decending order up until the last penny. All optimal currency quantatities will be input into a list of lists.
    for currency in currency_dict:
            rep = math.floor(rem/currency_dict[currency])
            rem -= rep * currency_dict[currency]
            rem = round(rem,2)
            if rep != 0:
                if rep>1 and currency == 'penny':
                    res_list.append([f'{rep} pennies'])
                elif rep>1:
                    res_list.append([f'{rep} {currency}s'])
                    
                else:
                    res_list.append([f'{rep} {currency}'])

    #Adding a 'and' preceding the last index in the list unless there is only 1 currency used
    if len(res_list)>1:
        res_list[-1]= ['and '+ res_list[-1][0]]      

    #Turn our list of lists into a along string with proper comma placement.
    for i in range(len(res_list)):
        res_list[i]= ''.join(res_list[i]) 
    res_str= ', '.join(res_list)

    #Declare our answer as a string with our 2 parameters and 1 answer inserted. 
    answer= f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is {res_str}."

    # B^) <- smiley face with sunglasses  
    return answer   


      

