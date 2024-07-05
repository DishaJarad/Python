bs=float(input("Enter your basic salary:"))

if bs>1500:
    hra=bs*0.1
    da=0.9*bs
    t_salary=bs+hra+da
    print("Gross Salary:",t_salary)
else:
    hra=500
    da=(bs*98)/100
    t_salary=bs+hra+da
    print("Gross Salary:",t_salary)
    
    
    

         
         
                
        