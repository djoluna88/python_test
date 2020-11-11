# Developed by: Dennis Luna Acuna
# Technical Test

import random



def random_teams(x,y):
    
   
    new_team=[]                      # Final List
    temp_count1=random.randint(2,3)  # First all I defined randomly the quantity for first team, initial condition
 
    for i in range(len(y)):
        
        # Build Team 1 Cycle
        
        if i==0:
        
            new_team=random.sample(x,temp_count1)    # I used the sample function in order to select aleatory members from persons list without repetition
       

            if temp_count1==2:                       # This conditional to select the temporal count for second and third array respectively

                temp_count2=3
                temp_count2=random.randint(2,3)
                temp_count3=random.randint(2,3)

                if temp_count2==2:                      
                    temp_count3=3

                else:

                    temp_count3=2


            else:

                temp_count2=2
                temp_count3=2

            
        # Build Team 2 Cycle

        if i==1:
            
            new_team=random.sample(x,temp_count2)



        # Build Team 3 Cycle

        if i==2:
            
            new_team=random.sample(x,temp_count3)


        print (y[i],": ", new_team)       



# Main Function where I can call the random function, provide the main inputs

if __name__ == "__main__":

    p=7
    m=[]
    persons=["P1","P2","P3","P4","P5","P6","P7"]
    teams  =["T1","T2","T3"] 
   
   
   
    while(True):
       
        try:
            print("**********Welcome to generation teams program**********\n")
            print("   Main Menu  ")
            print("")
            print("1. First Solution ")
            print("2. Second Solution")
            print("3. Exit\n")

            menu=int(input("Please select an option:   "))
            print("")
        
            if menu==1:

                print("Welcome to the First Solution\n")
                random_teams(persons,teams)
                print("")
                input("Press any Key to back main menu\n")
                

            if menu==2:

                # Dynamic way fill members 
                
                for i in range(p):
                    member=str(input("Please insert a member: "))
                    print("")
                    print("Member ",i+1," has been inserted successfully\n")
                    m.append(member)   # Add member to the list m

                m=list(m)              # Convert to m to list
               
                print("Welcome to the Second Solution\n")
                random_teams(m,teams)  # Call the function random
                print("")
                input("Press any Key to back main menu\n")

            if menu==3:
                print("")
                print("Thank you for using this program.....\n")
                input("Press any Key to continue")
                break


        except:

            print("Error, please select a correct option \n")
            input("Press any key to continue \n")




  



        






       
       
       
       
       
       
       
       
       
       
       
       
       
         
    
   
    

        


    















