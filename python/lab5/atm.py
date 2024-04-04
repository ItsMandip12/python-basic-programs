max_amt=10000
user_amt=60000

withdraw_amt=int(input("Enter amount that you want to withdraw: "))

if withdraw_amt<=10000 and withdraw_amt<=60000:
      print(f"You have withdraw {withdraw_amt}RS")
      left_amt=user_amt-withdraw_amt
      print(f"You have  {left_amt}RS left in your acount")