# Developed by: Dennis Luna Acuna
# Technical Test

import random



def persons(x):

    persons=[]
    
    for i in range(x):
        
        member=str(input("Please insert a member name: "))
        print("")
        print("Member ",i+1," has been inserted successfully\n")
        persons.append(member)         # Add member to the list persons

    persons=list(persons)              # Convert to persons to list

    return persons



def teams(x):

    teams=[]
    
    for i in range(x):
        
        member=str(input("Please insert a Team Name: "))
        print("")
        print("Team ",i+1," has been created successfully\n")
        teams.append(member)         # Add member to the list teams

    teams=list(teams)               # Convert to teams to list

    return teams


def random_teams(x,y):
 
    c=0
    
    for i in range(len(y)):
            
        new_team=[]  # Final List for each one team, that allows me to insert the members for each cycle increment  
            
        if 2 <= len(x):                             # We require at minimum 2 members                     
                
            qm= random.randint(2,len(x))             # Generates the size for each team

            while c < qm:                            # How many times we need to generate new index in accordance with size for each team 
                    
                index = random.randint(0,len(x)-1)   # Getting the random indexes 
                f=x.pop(index)                       # I used this method in order to avoid repetition from members between teams
                new_team.append(f)                   # Adding the member
                c+=1
                        
            c=0 
        
        print (y[i],": ", new_team)
            
        
       
    
# Main Function where I can call the random function, provide the main inputs

if __name__ == "__main__":

   
    while(True):
       
        try:
            print("**********Welcome to Data Generation Solution**********\n")
            print("   Main Menu  ")
            print("")
            print("1. Start Program ")
            print("2. Exit\n")

            menu=int(input("Please select an option:   "))
            print("")
        
            if menu==1:

                while(True):

                    p=int(input("Please insert the quantity of members:   "))

                    if p<2:
                        print("Error, it needs at least 2 members")
                        input("Press any Key to continue")    

                    else:
                        break
                

                while(True):

                    t=int(input("Please insert the quantity of teams:  "))

                    if t<2:
                        print("Error, it needs at least 2 teams")
                        input("Press any Key to continue")    

                    else:
                        break
                
                pe=persons(p)
                
                te=teams(t)
                
                temp=tuple(pe)  # In this way we don't lost the information from the persons list after execution function


                print("Welcome to the First Solution\n")  

                random_teams(pe,te)

    
                while True:
                    
                    r= input(str("Do you want to perform one execution more (Y/N):  "))   # Repeat execution
            
                    if r=="Y" or r=="y":

                        k=list(temp)          # To convert the temp tuple to list again, in order to modify the list againcd 
                        random_teams(k,te) 
                        

                    elif r=="N" or r=="n":
                        
                        break
                else:
                    
                    print("Error.....Please choice a valid option\n")
                    input("Press any Key to Continue")  
                    print("")
                    input("Press any Key to back main menu\n")           


            if menu==2:
                print("")
                print("Thank you for using this program.....\n")
                input("Press any Key to continue")
                break

        except:

            print("Error, please select a correct option \n")
            input("Press any key to continue \n")




  



        






       
       
       
       
       
       
       
       
       
       
       
       
       
         
    
   
    

        


    















