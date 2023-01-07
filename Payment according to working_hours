'''Write a program which takes the following 3 inputs from the user. 
1. No. of hours spent working 
2. Has the person worked on a weekend (Y/N)? 
3. Days per weekend spent working?
Usually, a person normally spends 40 hours at work per week (5 days) and gets paid 5 𝑝𝑒𝑟 ℎ𝑜𝑢𝑟. 𝐴 𝑛𝑜𝑟𝑚𝑎𝑙 𝑤𝑜𝑟𝑘𝑖𝑛𝑔 𝑑𝑎𝑦 𝑖𝑠 𝑜𝑓 8 ℎ𝑜𝑢𝑟𝑠. 𝐼𝑓 𝑡ℎ𝑒 𝑁𝑜. 𝑜𝑓 ℎ𝑜𝑢𝑟𝑠 𝑖𝑠 𝑔𝑟𝑒𝑎𝑡𝑒𝑟 𝑡ℎ𝑎𝑛 40,
𝑡ℎ𝑒𝑛 𝑖𝑡 𝑚𝑒𝑎𝑛𝑠 𝑡ℎ𝑎𝑡 𝑡ℎ𝑒 𝑝𝑒𝑟𝑠𝑜𝑛 ℎ𝑎𝑠 𝑤𝑜𝑟𝑘𝑒𝑑 𝑜𝑣𝑒𝑟 𝑡𝑖𝑚𝑒 𝑎𝑛𝑑 ℎ𝑒/𝑠ℎ𝑒 𝑔𝑒𝑡𝑠 10 per hour for the extra hours. Given the number of hours spent working, calculate the pay of a person 
in a week. 
• Requirement 1: Hours = Negative input Output = Error (Custom-made) 
• Requirement 2: Hours = 0 Output = No money made 
• Test Case 1: Hours = 40 Output = 200
• 𝑇𝑒𝑠𝑡 𝐶𝑎𝑠𝑒 2 : 𝐻𝑜𝑢𝑟𝑠 = 50𝑂𝑢𝑡𝑝𝑢𝑡 = 300
If a person works on weekends, he/she gets paid 25 𝑝𝑒𝑟 𝑑𝑎𝑦.𝐶ℎ𝑒𝑐𝑘 𝑖𝑓 𝑡ℎ𝑒 𝑝𝑒𝑟𝑠𝑜𝑛 𝑤𝑜𝑟𝑘𝑒𝑑 𝑜𝑛 𝑎 𝑤𝑒𝑒𝑘𝑒𝑛𝑑 𝑎𝑛𝑑 𝑔𝑖𝑣𝑒𝑛 𝑡ℎ𝑒 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑑𝑎𝑦𝑠 𝑠𝑝𝑒𝑛𝑡 𝑤𝑜𝑟𝑘𝑖𝑛𝑔 𝑜𝑛 𝑎 𝑤𝑒𝑒𝑘𝑒𝑛𝑑, 𝑎𝑑𝑑 𝑡ℎ𝑖𝑠 
𝑎𝑚𝑜𝑢𝑛𝑡 𝑡𝑜 𝑡ℎ𝑒 𝑡𝑜𝑡𝑎𝑙 𝑠𝑎𝑙𝑎𝑟𝑦 𝑓𝑜𝑟 𝑎 𝑤𝑒𝑒𝑘. The output will be as follows:
𝐸𝑛𝑡𝑒𝑟 𝑡ℎ𝑒 𝑁𝑜. 𝑜𝑓 ℎ𝑜𝑢𝑟𝑠 𝑠𝑝𝑒𝑛𝑡 𝑎𝑡 𝑤𝑜𝑟𝑘 𝑜𝑛 𝑤𝑒𝑒𝑘𝑑𝑎𝑦𝑠 = 30; 𝑊𝑜𝑟𝑘𝑒𝑑 𝑜𝑛 𝑎 𝑤𝑒𝑒𝑘𝑒𝑛𝑑(𝑌/𝑁 𝑜𝑛𝑙𝑦) = 𝑌; 𝐷𝑎𝑦𝑠 𝑜𝑛 𝑤𝑒𝑒𝑘𝑒𝑛𝑑 = 1; 𝑃𝑎𝑦 = $150.0; Pay including weekend off shift = $175.0
𝐸𝑛𝑡𝑒𝑟 𝑡ℎ𝑒 𝑁𝑜.𝑜𝑓 ℎ𝑜𝑢𝑟𝑠 𝑠𝑝𝑒𝑛𝑡 𝑎𝑡 𝑤𝑜𝑟𝑘 𝑜𝑛 𝑤𝑒𝑒𝑘𝑑𝑎𝑦𝑠 = 50; 𝑊𝑜𝑟𝑘𝑒𝑑 𝑜𝑛 𝑎 𝑤𝑒𝑒𝑘𝑒𝑛𝑑 (𝑌/𝑁𝑜𝑛𝑙𝑦) = 𝑌; 𝐷𝑎𝑦𝑠 𝑜𝑛 𝑤𝑒𝑒𝑘𝑒𝑛𝑑 = 2; 𝑃𝑎𝑦 = $300.0; Pay including weekend off shift = $350.0
𝐸𝑛𝑡𝑒𝑟 𝑡ℎ𝑒 𝑁𝑜. 𝑜𝑓 ℎ𝑜𝑢𝑟𝑠 𝑠𝑝𝑒𝑛𝑡 𝑎𝑡 𝑤𝑜𝑟𝑘 𝑜𝑛 𝑤𝑒𝑒𝑘𝑑𝑎𝑦𝑠 = 0; 𝑊𝑜𝑟𝑘𝑒𝑑 𝑜𝑛 𝑎 𝑤𝑒𝑒𝑘𝑒𝑛𝑑 (𝑌/𝑁𝑜𝑛𝑙𝑦) = 𝑌; 𝐷𝑎𝑦𝑠 𝑜𝑛 𝑤𝑒𝑒𝑘𝑒𝑛𝑑 = 2; 𝑃𝑎𝑦 𝑖𝑛𝑐𝑙𝑢𝑑𝑖𝑛𝑔 𝑤𝑒𝑒𝑘𝑒𝑛𝑑 𝑜𝑓𝑓𝑠ℎ𝑖𝑓𝑡 = $50;
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
