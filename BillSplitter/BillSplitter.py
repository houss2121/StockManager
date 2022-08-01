#Houssam Elkouhen
#Bill Splitter Problem

bill_total=float(input("enter total bill amount"))

sales_tax_rate=float(input("enter sales tax rate"))

gratuity_amount=float(input("enter gratuity amount"))

number_of_people_in_party=5

gratuity=bill_total * gratuity_amount

tax=bill_total * sales_tax_rate

total_amount=bill_total + tax + gratuity

amount_per_person=total_amount/5

print("the amount each person is to pay is ", format(amount_per_person, '2f'))