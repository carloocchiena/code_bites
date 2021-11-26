initial = 50000
recurring = 500
interest = 0.1
maturity = 4

capital_amount = initial * (1 + interest)**maturity

recurring_amount = 0

maturity -= 1 # this to evaluate the recurring amout at the end of each year

while maturity > 0:
    temp = recurring * (1 + interest) ** maturity
    maturity -= 1
    recurring_amount += temp
    
print(capital_amount + recurring_amount + recurring)    
