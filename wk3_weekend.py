def calculate_roi(down_payment, closing_costs, repair_budget, miscellaneous, income, expenses):
    total_investment = down_payment + closing_costs + repair_budget + miscellaneous
    monthly_income = income
    monthly_expenses = sum(expenses)
    monthly_net_income = monthly_income - monthly_expenses
    roi_percentage = (monthly_net_income / total_investment) * 100
    return roi_percentage

down_payment = 40000
closing_costs = 3000
repair_budget = 7000
miscellaneous = 0

income = 2000
expenses = [1610]

roi = calculate_roi(down_payment, closing_costs, repair_budget, miscellaneous, income, expenses)
print(f"The monthly ROI percentage for the rental property is: {roi:.2f}%")
#:.2f is a formatting specifier that tells Python to format the value of roi as a floating-point number with 2 decimal places


#Down payment = $40,000
#closing costs = $3000
#Repair budget = $7000
#miscellaneous = 

#This is monthly.
#Income = $2000 
#expenses:
#tax = $150
#Insurance = $100
#Vacancy = $100
#Repairs = $100
#Capital expenditures = $100
#property management = $200
#Mortgage = $860