import random


def random_teams():
    

    x=['Dennis','Luna','Acuna','Josue','Katherine','bus','sun','car']
    y=['TX','TY','TZ']



    c=0    
  
          
    for i in range(len(y)):

        new_team=[]  # Final Team List 
        
        print(len(x))
        
        
        if 2 <= len(x):

            qm= random.randint(2,len(x))
            #print(qm)

            while c < qm:
                
                index = random.randint(0,len(x)-1)
                f=x.pop(index)
                new_team.append(f)
                c+=1
                #k+=1
                
            c=0 
        

        print (y[i],": ", new_team)
       
       
   

random_teams()