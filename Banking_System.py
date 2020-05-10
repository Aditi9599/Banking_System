
r={}
d={}
pa={}#password
bl_list={}
def new_customer():
          global r
          global d
          list1=["Name","Age","mob_no","amount","Add"]
             
          list2=[]
          l=len(r)

          
          #name=input("Enter your name")
          #age=input("Enter your age")
          for item in list1:
               list2.append(input("Enter %s:"%item))
                                 
          if(l==0):
                s_no=str(1)
                                   
          else:
                k=list(r.keys())
                ind=int(len(k)-1)
                record=k[ind].split('_')
                s_no=str(int(record[2])+1)
          Uid=list2[0]+'_'+list2[1]+'_'+s_no
          print("  Hello!!!!  "+list2[0]+ "  Your Uid is  "+Uid)      

          d[Uid]=dict(zip(list1,list2))
          print(d)
          r[Uid]="zxc"
          p=input("Create your password:")
          pa[Uid]=p
          print("Congratulations!! Your account created")  

def existing_customer():
       global d
       global bl_list
       Uid=input("Enter your uid")
       p=input("Enter your password")  
        
                        
  
   
       if(pa[Uid]==p):
            if Uid in d:
                 print("Record found")

                 ch=int(input("1.Check balance\n2.Withdraw\n3.Update\n4.Delete AccountEnter choice"))
                 if(ch==1):
                      print("Available balance",d[Uid]["amount"])
                      
                 elif(ch==2):
                      
                      amt=int(input("Enter the amount you want to withdraw"))
                      new_amt=int(d[Uid]["amount"])-amt
                      d[Uid]["amount"]=new_amt                              #updating the new amount
                      print("Withdraw Successful!!!")
                      print("Available balace is:",d[Uid]["amount"])
                 elif(ch==3):
                      c=int(input("What do you want to update:\n1.mob_no\n2.Address"))
                      if(c==1):
                          new_mob_no=input("Enter your mobile no.")       
                          d[Uid]["mob_no"]=new_mob_no
                          print("Mobile num successfully updated")
                          print(d)
                      elif(c==2):
                          new_add=input("Enter your mobile no.")       
                          d[Uid]["Add"]=new_add
                          print("Address successfully updated")
                          
                 elif(ch==4):
                      admin_id=(input("Enter admins Id"))
                      admin_pass=(input("Enter admins password"))
                      if(admin_id=="Aditi_9599" and admin_pass=="IITK@123"):
                            print("Successfully loged in!!")
                            delete=input("Enter the user Id to be deleted")
                            if(Uid in d):
                               bl_list=dict(d[Uid])
                               
                               print("account in blacklist:",bl_list)
                               
                               
                            else:
                                 print("User data not found!")
                            
                            del d[Uid]
                            print("account deleted")   
                                  
                      else:
                                print("Please try again!")
            else:
                 print("Record not found")
                          
       else:
           print("Invalid password")
                     
                 
              
            

        





    
