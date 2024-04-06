print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill? $'))
tip_percent = int(input('What percent(%) you like to tip? '))
patrons = int(input('How many people are splitting the bill? '))
total_tip = round(total_bill * (tip_percent / 100), 2)
tip_per_patron = round(total_tip / patrons, 2)
total_per_patron = round(total_bill/ patrons, 2) + tip_per_patron

print(f'Each person will pay: ${total_per_patron}')  
124.56