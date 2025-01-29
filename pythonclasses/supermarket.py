from datetime import datetime

name=input("Enter your name:")

#LISTS of items
lists='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
salt    Rs 20/kg
oil     Rs 80/liter
paneer  Rs 110/kg
Maggi   Rs 50/kg
Boost   Rs 90/each
colgate Rs 85/each
'''

#decleration
price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates of items

items={'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,'maggi':50,
'boost':90,'colgate':85}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
        inp1=int(input("if you want to buy press 1 or 2 for exit:"))
        if inp1==2:
                break
        if inp1==1:
                item=input("Enter your items:")
                quantity=int(input("Enter quantity:"))
                if item in items.keys():
                        price=quantity*(items[item])
                        pricelist.append((item,quantity,items,price))
                        totalprice+=price
                        ilist.append(item)
                        qlist.append(quantity)
                        plist.append(price)
                        gst=(totalprice*5)/100
                        finalamount=gst+totalprice
                else:
                        print("sorry you entered item is not available")
        else:
                print("you entered wrong number")
        inp=input("can i bill the items yes or no:")
        if inp=='yes':
                pass
                if finalamount!=0:
                        print(25*"=","sunny supermarket",25*"=")
                        print(28*" ","mancherial")
                        print("Name:",name,30*" ","Date:",datetime.now())
                        print(75*"-")
                        print("Sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
                        for i in range(len(pricelist)):
                                print(i,10*' ',ilist[i],10*' ',qlist[i],8*' ',plist[i])
                        print(75*"-")
                        print(50*" ",'TotalAmount:','Rs',totalprice)
                        print("Gst Amount",52*" ",'Rs',gst)
                        print(75*"-")
                        print(50*" ",'FinalAmount:','Rs',finalamount)
                        print(75*"-")
                        print(25*" ","Thanks for visiting")
                        print(75*"-")

                        