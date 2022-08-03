#Houssam Elkouhen
#Stock Manager Problem

commission_rate=.03

number_of_shares=float(input("enter number of shares"))

amount_each_share_costs=float(input("enter how much each share costs"))

amount_share_sells_for=float(input("enter how much each share sells for"))

commission_for_purchase=(number_of_shares * amount_each_share_costs)*commission_rate

commission_for_sale=(number_of_shares * amount_share_sells_for)*commission_rate

amount_paid_for_stock=number_of_shares * amount_each_share_costs

total_amount_stocks_sold=number_of_shares * amount_share_sells_for

profit=total_amount_stocks_sold - amount_paid_for_stock -commission_for_purchase - commission_for_sale

print("The amount paid for the stock is ",format(amount_paid_for_stock, '2f'))

print("The commission paid on the purchase is ", format(commission_for_purchase, '2f'))

print("The amount the stock sold for is ",format(total_amount_stocks_sold, '2f'))

print("The commission paid on the sale is ", format(commission_for_sale, '2f'))

print("The Profit is ", format(profit, '2f'))



