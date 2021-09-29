
fixedCash=60000
userbalnce=70000
n=3
lst=[]


def main():
    print("Total amount in ATM :",fixedCash)
    print("Total amount in your account",userbalnce)
    amount=int(input("How much amount you want to withdraw ?"))
    
    def withdraw(amount): 
        global fixedCash
        global userbalnce
        global n  
        if(amount>userbalnce or amount>(90*fixedCash)/100):
            print("Insufficient balance")
        else:
            n=n-1  
            userbalnce=userbalnce-amount
            fixedCash=fixedCash-amount
              
            lst.append(amount)
            print(amount,"debited from your account")
            if(n!=0):
                print("You can do ",n," more transations")
                amount=int(input("How much amount you want to withdraw ?"))
                withdraw(amount)
            else:
                i=input("Do you want to see your last 3 transaction and Total balance, Y|N ? ")
                if(i=="Y"):
                    print("Balnace amount :",userbalnce)
                    for i in range(0,3):
                        print("Transaction ",i+1 ,"is", lst[i])
        
    withdraw(amount) 
    
main()
