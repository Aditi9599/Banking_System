import Banking_System as bs
val='True'
while(val=='True'):
    choice=int(input("1.New customer"'\n'"2.Existing customer"))
    if(choice==1):
        bs.new_customer()
    elif(choice==2):
        bs.existing_customer()
                             
