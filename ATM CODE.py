print('***___WELCOME TO *AASS* ATM $ERVICE___***\n')
password=int(input('PLEASE SET A PASSWORD(PIN) TO YOUR ACCOUNT:'))
print(password,' IS YOUR PIN SET SUCCUSSFULLY...')
balance=10000
print('CONGRATULATIONS...! OUR ATM PROVIDES 10000 CREDITED TO YOUR ACCOUNT')
count,x=0,0
ms={}
while(True):
    pin=int(input('\nENTER YOUR ATM PIN NUMBER : '))
    while(pin!=password):
            print('/// INVALID PIN ///\n')
            count+=1
            pin=int(input('ENTER YOUR ATM PIN CORRECTLY : '))
            if count>3:
                print('YOU ENTERED YOUR PIN WRONGLY MANY TIMES SO YOU HAVE TO QUITE TO THE ATM\n')
                quit()
    print('\nSELECT A OPTION IN THE FOLLOWING\n 1. BALANCE ENQUERY\n 2. DEPOSIT\n 3. WITHDRAW\n 4. CHANGE PIN \n 5. MINI STATEMENT \n 6. EXIT\n')
    opt=int(input('ENTER YOUR OPTION : '))
    if opt==1:
        print('\nAVAILABLE BALANCE IN YOUR ACCOUNT :',balance)
        
    elif opt==2:
        dpt=int(input('\nENTER THE AMOUNT TO DEPOSITE : '))
        balance+=dpt
        print(dpt,' SUCCESSFULLY DEPOSITED IN YOUR ACCOUNT')
        x+=1
        ms[f'{x}.DEPOSITE']=dpt
        
    elif opt==3:
        wd=int(input('\nENTER THE AMOUNT TO WITHDRAW : '))
        if wd>balance:
            print('INSUFFICIENT BALANCE ...!')
        else:
            balance-=wd
            print(wd,' SUCCESSFULLY WITHDRAWN IN YOUR ACCOUNT')
            x+=1
            ms[f'{x}.WITHDRAWN']=wd
            
    elif opt==4:
        pin=int(input('\nENTER YOUR OLD PASSWORD(PIN):'))
        if(pin==password):
            password=int(input('ENTER YOUR NEW PASSWORD(PIN) : '))
            print('PIN CHANGED SUCCESSFULLY...')
        else:
            print('ENTERED PIN DOES NOT MATCH TO YOUR OLD PIN!')
            
    elif opt==5:
        print('\n***MINI STATEMENT***')
        for key in ms:
            print(key,'=',ms[key])
        print("AVAILABLE BALANCE IS :",balance)        
       
    elif opt==6:
        print('THANKS FOR VISITING OUR ATM')
        quit()
        
    if opt not in(1,2,3,4,5,6):
        print('INVALID OPTION\n')
    
    
