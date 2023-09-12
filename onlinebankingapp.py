import math
print('welcome to the online banking application')
def signin():
   global name #username
   global pin #password
   global cb #current balance
   name=str(input('please create your username :'))
   pin=str(input('please create your 6 digits pin :'))
   if len(pin)==6:
       pin=pin
   else:
        print('The pin has to be 6 digits')
        newpin=str(input('please create your 6 digits pin :'))
        if len(newpin)!=6:
            print('The pin has to be 6 digits')
            signin()
        else:
            pin=newpin
   print('Thanks for creating your bank account')
    
def forgotpin():
    recoverpin=str(input('Please create your pin'))
    if len(recoverpin)!=6:
      print('The pin has to be 6 digits')
      forgotpin() 
    else: 
       print('The new pin has been stored, please log in')
       pin=recoverpin
       login()

def depositinterest(p,r,t):
    p=float(p)
    r=float(r)
    t=float(t)
    rt=r*t
    e=math.exp(rt)
    a=p*e
    return a

def login():
    name1=str(input('please enter your username :'))
    pin1=str(input('please enter your pin :'))
    if name1==name and pin1==pin:
        print('welcome to the online banking application'+ '' +name)
        print('please choose the menu down here')
        listmenu=('1-Deposit','2-Withdraw','3-Transfer','4-check blance','5-Deposit interest rate','6-calculate compound interest')
        for b in listmenu:
            print(b)
        choose=int(input('please enter your choice :'))
        d=0
        w=0
        cb=0
        if choose==1:
            d=int(input('enter your amount of deposit :'))
            cb=d
            print('Your current balance is' + '' + str(cb))
        elif choose==2:
            w=int(input('Enter the amount of money that you want to withdraw :'))
            if w>cb:
                print('Your current balance not sufficent')
                login()
            else:
                cb=d-w
                print(str(w)+''+'has been withdrawn for your account'+ '' +'and your current balance is' + '' + str(cb))
        elif choose==3:
            dest=str(input('Please enter the account number of your destination in 10 digits :'))
            if len(dest)==10:
                amount=int(input('Please enter the amount of money that you want to transfer :'))
                if amount>cb:
                    print('Your current balance not sufficent')
                else:
                    cb=d-amount
                    print('The transaction'+ '' +str(amount)+ '' +'has been transfered to' + '' +str(dest)+ '' +'your current balance is' + '' + str(cb))
            else:
                print('Account number invalid')
                login()
        elif choose==4:
            print('Your current balance is' + '' + str(cb))
        elif choose==5:
            if d>50000:
                rate=3
            elif d>30000:
                rate=2
            else:
                rate=1.5
            print('Your current deposit intrest rate is' + '' + str(rate)+'%')
        elif choose==6:
            listoption=['1-calculate your deposit compound intrest based on your current balance','2-calculate your deposit compound intrest based on your deposit input ']
            for n in listoption:
                print(n)
            choice=int(input('Please enter your choice from the options above :'))
            if choice==1:
                timing=str(input('How long do you want to invest your money :'))
                if d>50000:
                    ratex=3/100
                elif d>300000:
                    ratex=2/100
                else:
                    ratex=1.5/100
                print('Your current balance in' + 'timing' +''+ 'years will be')
                print(depositinterest(cb,ratex,timing))
            if choice==2:
                timing1=str(input('How long do you want to invest your money :'))
                money=str(input('Please enter the amount you would like to deposit :'))
                money=int(money)
                if d>50000:
                    ratex=3/100
                elif d>300000:
                    ratex=2/100
                else:
                    ratex=1.5/100
                print('Your current balance in' + 'timing' +''+ 'years will be')
                print(depositinterest(money,ratex,timing))
        else:
            print('invalid option')
    else:
        print('Either of your username or pin is wrong, did you create your account?')
        list1=('1-YES','2-NO')
        for i in list1:
            print(i)
        inp=int(input('Enter your choice below :'))
        if inp==1:
            list2=('1-do you want to attmept to login again?','2-you forgot your pin?')
            for e in list2:
                print(e)
            theanswer=str(input('please enter your choice :'))
            theanswer=int(theanswer)
            if theanswer ==1:
                login()
            elif theanswer==2:
                forgotpin()
            else:
                print('option not available')
                login()
        elif inp==2:
            print('please create your account')
            signin()
    exit()
    
def mainmenu():
    optionone=int(input('Choose 1 to sign in and Choose 2 to login :'))
    if optionone==1:
        signin()
    elif optionone==2:
        login()
    else:
        print('invalid option')
        mainmenu()
    exit()

def exit():
    answer=str(input('Do you still want to conduct a transation? Yes or No : '))
    if answer=='yes':
        login()
    elif answer=='no':
        print('Thank you for banking with us')
    else:
        print('invalid option')
        mainmenu()

