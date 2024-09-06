initial = 60000
recurring = 500
interest = 0.1
maturity = 5
 
final_amount = initial * (1 + interest) ** maturity + recurring * ((1 + interest) ** maturity -1) / interest   
 
print(f'Amount:{(round(final_amount,2))}')
