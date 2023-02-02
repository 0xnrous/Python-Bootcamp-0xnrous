names= input("Write the names of provider (Sparate each name with a comma)").split(",")
costs =(input ("Write the Cost of offers (Sparate each cost with a comma)")).split(",")
rates=[]
accepted_names= []
accepted_costs= []

if len(names) != 5 or len (costs) !=5:
    print ("The count of names and costs must be 5 ")
else :
    rate1=float( input (f"Write the rate of {names[0]} bid , with cost {costs[0]}: "))
    if rate1 >=5 :
        accepted_names.append(names[0])
        accepted_costs.append(float(costs[0]))
        rates.append(rate1)
    rate2=float( input (f"Write the rate of {names[1]} bid , with cost {costs[1]}: "))
    if rate2 >=5 :
        accepted_names.append(names[1])
        accepted_costs.append(float(costs[1]))
        rates.append(rate2)
    rate3=float( input (f"Write the rate of {names[2]} bid , with cost {costs[2]}: "))
    if rate3 >=5 :
        accepted_names.append(names[2])
        accepted_costs.append(float(costs[2]))
        rates.append(rate3)
    rate4=float( input (f"Write the rate of {names[3]} bid , with cost {costs[3]}: "))
    if rate4 >=5 :
        accepted_names.append(names[3])
        accepted_costs.append(float(costs[3]))
        rates.append(rate4)
    rate5=float( input (f"Write the rate of {names[4]} bid , with cost {costs[4]}: "))
    if rate5 >=5 :
        accepted_names.append(names[4])
        accepted_costs.append(float(costs[4]))
        rates.append(rate5)
    winner_cost= min (accepted_costs)
    accepted_offer= accepted_costs.index(winner_cost)
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    print (f'Number of offer bid : {len(names)}')
    print(f'Number of accepted offer: {len(accepted_names)}')
    if len(accepted_names)==0 :
        print("offer not accepted ")
    else:

        print (f"The winner offer is: {accepted_names[accepted_offer]}, with costs {accepted_costs[accepted_offer]}, with Rate: {rates[accepted_offer]} ")