prices= [int(input(f"Enter prices for product {i+1}: ")) for i in range(5)]

avg=sum(prices)/5

print(f"The average price is: {avg}")
