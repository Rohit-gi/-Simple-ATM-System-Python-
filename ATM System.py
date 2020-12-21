#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Simple ATM System

print("Welcome to ******YOUR BANK******")
print("Enter your 4 digit Pin Number: ")

p=int(input("Enter the PIN number here: "))

m = 10000
if(p == 1234,5678,9101):
    print("1- Withdraw")
    print("2- Balance Enquiry")
    print("3- Cash Withdrawal")
    c = int(input("Please choose from above options: "))
    if (c == 1):
        w=int(input("Enter amount to be withdrawn: "))
        if (w < m and w%100 == 0):
            print("Please collect your amount:", w)
        else:
            print("Invalid amount of cash,Input correct value")

    elif (c==2):
        print("Your balance is  : ",m)

    elif (c == 3):
        print("1-> 2,000")
        print("2-> 4,000")
        print("3-> 8,000")
        print("4-> 10,000")
        
        f = int(input("Select one option from above: "))
        if (f == 1 and 2000 < m):
            print("Please collect cash 2000")
        elif (f == 2 and 4000 < m):
            print("Please collect  cash 4000")
        elif (f == 3 and 8000 < m):
            print("Please collect cash 8000")
        elif (f == 4 and 10000 < m):
            print("Please collect cash 10000")
        else:
            print("Invalid cash option")
    else:
        print("Wrong choice")
else:
    print("Wrong Pin entered")


# In[ ]:





# In[ ]:




