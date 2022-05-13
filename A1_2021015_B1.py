

pi1=int(input("Enter the price of Item 01: "))
pi2=int(input("Enter the price of Item 02: "))
pi3=int(input("Enter the price of Item 03: "))


d1=int(input("Enter the discount for combo 1(item 1 and item 2): "))
d2=int(input("Enter the discount for combo 2(item 1 and item 3): "))
d3=int(input("Enter the discount for combo 3(item 2 and item 3): "))

print("the dicount for super saver(item 1, item 2 and item 3) is 28 % ")

pno=input("kindly enter your phone number: ")
def combo(pia,pib,d):
    sc=(pia+pib)*(100-d)*0.01         #i used abs() from documentation sine checking for negative number via if else is waste of time here
    return sc

def super1(pia,pib,pic,d):            #fn for calculating super combo pack
    sc=(pia+pib+pic)*(100-d)*0.01 
    return sc






#print into formated text

print(f'''
*******************************start*******************************

######                            ######                      
#     # ###### #      #    # #    #     #   ##   #   #  ####  
#     # #      #      #    # #    #     #  #  #   # #  #      
#     # #####  #      ###### #    #     # #    #   #    ####  
#     # #      #      #    # #    #     # ######   #        # 
#     # #      #      #    # #    #     # #    #   #   #    # 
######  ###### ###### #    # #    ######  #    #   #    ####  
-------------------------------------------------------------------

-------------------------------------------------------------------
-------------------------------------------------------------------
-----------	      Price of Item 1: {pi1}         ---------------
-----------	      Price of Item 2: {pi2}         ---------------
-----------	      Price of Item 3: {pi3}         ---------------
-------------------------------------------------------------------
-------------------------------------------------------------------

*******************************************************************

-------------------------------------------------------------------
Discount details: Buy combo packs to get discount in MRP :
-------------------------------------------------------------------
- Discount percentage for Combo Pack 01  : Item 1 and item 2 : {d1} % -         
- Discount percentage for Combo Pack 02  : Item 1 and item 3 : {d2} % - 
- Discount percentage for Combo Pack 03  : Item 2 and item 3 : {d3} % - 
- Discount percentage for SuperSaver Pack: Item 1, 02 and 03 : 28 % - 
-------------------------------------------------------------------
-------------------------------------------------------------------
_____________________________________________________________________
                Item                        Price
_____________________________________________________________________                
                Item 01                     {pi1}
                Item 02                     {pi2}
                Item 03                     {pi3}
             Combo Pack 01      ———         {combo(pi1,pi2,d1)}
             Combo Pack 02      ———         {combo(pi1,pi3,d2)}
             Combo Pack 03      ———         {combo(pi2,pi3,d3)}
            Super Saver Pack    ———         {super1(pi1,pi2,pi3,28)}

_____________________________________________________________________
       contact {pno} for no contact free home delivery
---------------------------------------------------------------------
  insta-@delhidays                          @email-care@delhidays.com 
*******************************end***********************************
''')


