'''Write a program which takes the following 3 inputs from the user. 
1. No. of hours spent working 
2. Has the person worked on a weekend (Y/N)? 
3. Days per weekend spent working?
Usually, a person normally spends 40 hours at work per week (5 days) and gets paid 5 πππ βππ’π. π΄ ππππππ π€ππππππ πππ¦ ππ  ππ 8 βππ’ππ . πΌπ π‘βπ ππ. ππ βππ’ππ  ππ  πππππ‘ππ π‘βππ 40,
π‘βππ ππ‘ πππππ  π‘βππ‘ π‘βπ ππππ ππ βππ  π€πππππ ππ£ππ π‘πππ πππ βπ/π βπ πππ‘π  10 per hour for the extra hours. Given the number of hours spent working, calculate the pay of a person 
in a week. 
β’ Requirement 1: Hours = Negative input Output = Error (Custom-made) 
β’ Requirement 2: Hours = 0 Output = No money made 
β’ Test Case 1: Hours = 40 Output = 200
β’ πππ π‘ πΆππ π 2 : π»ππ’ππ  = 50ππ’π‘ππ’π‘ = 300
If a person works on weekends, he/she gets paid 25 πππ πππ¦.πΆβπππ ππ π‘βπ ππππ ππ π€πππππ ππ π π€ππππππ πππ πππ£ππ π‘βπ ππ’ππππ ππ πππ¦π  π ππππ‘ π€ππππππ ππ π π€ππππππ, πππ π‘βππ  
ππππ’ππ‘ π‘π π‘βπ π‘ππ‘ππ π πππππ¦ πππ π π€πππ. The output will be as follows:
πΈππ‘ππ π‘βπ ππ. ππ βππ’ππ  π ππππ‘ ππ‘ π€πππ ππ π€ππππππ¦π  = 30; ππππππ ππ π π€ππππππ(π/π ππππ¦) = π; π·ππ¦π  ππ π€ππππππ = 1; πππ¦ = $150.0; Pay including weekend off shift = $175.0
πΈππ‘ππ π‘βπ ππ.ππ βππ’ππ  π ππππ‘ ππ‘ π€πππ ππ π€ππππππ¦π  = 50; ππππππ ππ π π€ππππππ (π/πππππ¦) = π; π·ππ¦π  ππ π€ππππππ = 2; πππ¦ = $300.0; Pay including weekend off shift = $350.0
πΈππ‘ππ π‘βπ ππ. ππ βππ’ππ  π ππππ‘ ππ‘ π€πππ ππ π€ππππππ¦π  = 0; ππππππ ππ π π€ππππππ (π/πππππ¦) = π; π·ππ¦π  ππ π€ππππππ = 2; πππ¦ πππππ’ππππ π€ππππππ ππππ βπππ‘ = $50;
Enter the No. of hours spent at work on weekdays = 48; Worked on a weekend (Y/N only) = N; Days on weekend = 0; Output: Pay = $280.0
Enter the No. of hours spent at work on weekdays = -1; Worked on a weekend (Y/N only) = N; Days on weekend = 0; Output: Input is incorrect! 
Enter the No. of hours spent at work on weekdays = 0; Worked on a weekend (Y/N only) = N; Days on weekend = 0; Output: You didn't make any money.'''
========================================================================================================================================================================
========================================================================================================================================================================

####CODE STARTS FROM HERE####
#Statement 1
working_hours = input ("No. of hours spent on working before weekend: ")
working_hours = int(working_hours)

if (working_hours < 0):
        print ("Error!!")
elif (working_hours == 40):   #Person normally spends 40 hours at work
    pay = working_hours * 5 #Normal working days are 5 and pay will be $5 for normal working hours 
    print ("Person gets paid $5 for normal working hours:")
    print ("Pay of the person is","$" + str(pay))
elif (working_hours > 40):
    working_hours = working_hours - 40  #50 hours - 40 hours = 10 hours
    #Normal working days are 5 and pay will be $10 for overtime work
    PAY = working_hours * 10 # 10 hours * 10$ = 100
    pay = 40 * 5 #200$
    overtime_pay = PAY + pay
    print ("The person has worked overtime and earn" , "\$10 per hour")
    print ("Total pay of person is","$" + str(overtime_pay))
    
else: 
    print ("No Money Made!!")
    
#Statement 2
print ("\n")
pay_of_working_weekends = 25
pay = input ("If pay of the person is: ")
pay = int(pay)
weekend = input ("If person works on weekend; Type: Yes/No: ")
No_of_Hours =  input ("No_of_Hours a person works on weekend: ")
No_of_Hours =  int (No_of_Hours)
Days_on_weekend = input ("Days on weekend: ")
Days_on_weekend = int(Days_on_weekend)

if (weekend == "yes" and No_of_Hours > 0): #The person works on weekend condition
    print ("Pay: " , "$" + str(pay))
    offshift_pay =(pay_of_working_weekends)  * (Days_on_weekend)
    salary = pay + (offshift_pay)
    print ("Total Salary: " , "$" + str(salary))
elif (weekend == "yes" and No_of_Hours == 0):
    offshift_pay =(pay_of_working_weekends)  * (Days_on_weekend)
    print ("$"+ str (offshift_pay))   #offshift pay is (25) * (days on weekend)
    
if(weekend == "no" and No_of_Hours > 0):  #The person is not working on weekend condition
    print ("Pay: " + "$" + str(pay))
elif(weekend == "no" and No_of_Hours == 0):
    print ("You did not make any money!!")
elif (weekend == "no" and No_of_Hours < 0):
    print ("Input is Incorrect!")
