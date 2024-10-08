
#  // Written By : Mohammad Rayyan Adhoni 12B2

#   // Database Car_Dealership containing at least 5 tables

#     // Available_Cars, Car_Details, Car_Features, Customer_Details and Customer Entry. Respectively

#       // Connecting To MySQL

import mysql.connector as m

con = m.connect(host='localhost',user='root',password='root',database='Car_Dealership')

cur = con.cursor()

import pyttsx3

engine = pyttsx3.init()

#  // pyttsx3 --> Text To Voice Function

#    //  Have Different Voices acooroding To System's List of Voices

#      // My Current Sustem Has Two List Datatypes Voice[0] and Voice[1] having Cortana Male and Female Voices Respectively

#       // Inseting Values Of Tables


from tabulate import tabulate

#  // tabulate --> makes a table acoording the values contains in a tables values

#   // Used Type psql (Plain SQL) gives the table output as same as the table in MySQL



#  --------------------------------------------------------------------------------------------------------------------- INSERTING VALUES -----------------------------------------------------------------------------------------------------------------------------------------

def Table_Values():
    engine.setProperty('rate',130)
    answer = "Your Now Inserting Values!!"
    engine.say(answer)
    engine.runAndWait()
    while True:
        
        print()
        print('*----------------------------------------------------------------------*')
        print('Please Select Which One Of The Options You Want To INSERT VALUES From The Following :\n1.Values for All the Tables(Available Cars, Car Details, Car Features\n2.CUSTOMER DETAILS\n0.EXIT (Back To Menu)')
        print('*----------------------------------------------------------------------*')
        ch = int(input('Enter Your Choise from the above options: '))
       
        if ch == 1:
            
            while True :
                
                print("\nYou are now entering the Records ")
                #Table 1
                Car_ID = input('Enter Your CAR ID NUMBER: ') 
                Car_Name = input('Enter Your CAR NAME: ')
                Car_Model = input('Enter Your CAR MODEL ID: ')
                
                #Table 2
                Car_Plate = input('Enter Your CAR PLATE NUMBER: ')
                
                #Table 3
                Car_Features = input('Enter Your CAR FEATURE: ')
                
                Y_N = input('if you wish to continue Type "Yes" , if not then "No": ')
                sql1 = "insert into available_cars values('{}','{}','{}')".format(Car_ID,Car_Name,Car_Model) 
                sql2 = "insert into car_models values('{}','{}','{}')".format(Car_Name,Car_Plate,Car_Model)
                sql3 = "insert into car_features values('{}','{}','{}','{}')".format(Car_Plate,Car_Name,Car_Features,Car_Model)
                SQL_1= 'select * from Available_cars'
                SQL_2 = 'select * from car_models'
                SQL_3 = 'select * from car_features'
                
                #Table 1
                cur.execute(sql1)
                con.commit()
                cur.execute(SQL_1)
                rs1 = cur.fetchall()
                
                #Table 2
                cur.execute(sql2)
                con.commit()
                cur.execute(SQL_2)
                rs2 = cur.fetchall()
                
                #Table 3
                cur.execute(sql3)
                con.commit()
                cur.execute(SQL_3)
                rs3 = cur.fetchall()
                
                print('one record succesfully INSERTED in ALL tables')
                
                if Y_N.lower()=='no':
                    print("You've Succesfully Exited Entering the values in table --> 'AVAILABLE_CARS' ")
                    break
                
            print('\n')
            print(tabulate(rs1, headers=['Car ID','Car Name','Model ID'], tablefmt='psql'))
                
            print('\n')
            print(tabulate(rs2, headers=['Car Name','Car Plate','Model ID'], tablefmt='psql'))
            
            print('\n')
            print(tabulate(rs3, headers=['Car Plate','Car Name','Car Features','Model ID'], tablefmt='psql'))
            
        if ch == 2:
            
            while True:
                
#                 // Asking the User If they (Customer(s)) want to buy

#                  // in case if entered Wrong Choice (ch)
                
                
                print("\nYou are now entering the Records for table --> 'CUSTOMER_DETAILS'")
                print('Are You Sure To Enter The Values In Table --> "CUSTOMER_DETAILS" ?\n if yes, type "YES" or\n if no then, type "NO"')
                YN = input('Type HERE: ')
                
                if YN.lower() == 'yes':
                    
                    CHECK = input('Before Entering Values in The Customers table Do You Wish To See The Customers Entries Who Wish to Buy a Car ? [Yes/No] : ')
                    
#                     // If the Customer had filled the table "CUSTOMER ENTRY"

#                        // The Employee will go through the values contained in that table and will put their info according to that table
                    
                    if CHECK.lower() == 'yes':
                        
                        Sql = 'select * from Customer_Entry'
                        cur.execute(Sql)
                        RS = cur.fetchall()
                        print(tabulate(RS, headers=['Sr No','Customer Name','Age','Car Name and Model to Buy','EMAIL','Customer Contact Number'], tablefmt='psql'))
                        print('Now Entering Values of Customer(s) Details')
                        
                        if RS == []:
                            
                            print('Customers Entries Dosent Exists!!')
                            engine.setProperty('rate',130)
                            answer = 'Customer(s) Entries Dosent Exists'
                            engine.say(answer)
                            engine.runAndWait()
                            break
                        
                        age = int(input('Enter Customer(s) AGE: '))
                        
                        if age >= 20 or age <= 60:
                            
                            sr_no = int(input('Enter Customers Sr_No: ')) # Primary Key
                            Customer_Name = input('Enter Customer(s) FULL NAME: ')
                            Customer_Car = input('Enter The Car Name that Customer(s) wish to BUY: ')
                            Car_Model = input('Enter Customer(s) CAR MODEL ID: ')
                            Gen = input('Enter Customer(s) Gender [Male/Femal]: ')
                            Pay_Method = input('Enter Customer(s) Payment Method [Cash/Card/Cheque]: ')
                            Price = int(input('Enter The Price that Customer(s) Need to Pay [AED]: '))
                            Tax = int(input('Enter The Tax percentage : '))
                            total = Tax / 100 + Tax * Price
                            Total = int(total)
                            Total_Tax = print('The Total Ammount With Customer Needs to pay [Tax includes] is: ',Total)
                            Email = input('Enter The Customer(s) Email : ')
                            Phone = input('Enter Customer(s) Phone Number: ')
                            yn = input('if you wish to continue Type "Yes" , if not then "No": ')
                            sql="insert into customer_details values({},'{}',{},'{}','{}','{}','{}',{},{},{},'{}','{}')".format(sr_no,Customer_Name,age,Customer_Car,Car_Model,Gen,Pay_Method,Price,Tax,total,Email,Phone)
                            SQL='select * from Customer_Details'
                            cur.execute(sql)
                            con.commit()
                            cur.execute(SQL)
                            rs = cur.fetchall()
                            print('one record succesfully INSERTED')
                            
                            if yn.lower() == 'no':
                               break
                            
                            print('\n')
                            print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))
                    
                        if age < 20 or age > 61:
                            
                            print('Sorry\nYou Are Not Eligible To Buy A Car!! Minimum age 20 and Above')
                            engine.setProperty('rate',130)
                            answer = "Sorry! You Are Not Eligible To Buy A Car , Minimum age 20 and Above"
                            engine.say(answer)
                            engine.runAndWait()
                            continue
                        
                    

#          // If The Employee wanst to enter the customers details directly after\before cheacking

                    
                    if CHECK.lower() == 'no':
                        
                        age = int(input('Enter Customer(s) AGE: '))
                        
                        if age >= 20 and age <= 60:
                            
                            sr_no = int(input('Enter Customers Sr_No: ')) # Primary Key
                            Customer_Name = input('Enter Customer(s) FULL NAME: ')
                            Customer_Car = input('Enter The Car Name that Customer(s) wish to BUY: ')
                            Car_Model = input('Enter Customer(s) CAR MODEL ID: ')
                            Gen = input('Enter Customer(s) Gender [Male/Femal]: ')
                            Pay_Method = input('Enter Customer(s) Payment Method [Cash/Card/Cheque]: ')
                            Price = int(input('Enter The Price that Customer(s) Need to Pay [AED]: '))
                            Tax = int(input('Enter The Tax percentage : '))
                            total = Tax / 100 + Tax * Price
                            Total = int(total)
                            Total_Tax = print('The Total Ammount With Customer Needs to pay [Tax includes] is: ',Total)
                            Email = input('Enter The Customer(s) Email : ')
                            Phone = input('Enter Customer(s) Phone Number: ')
                            yn = input('if you wish to continue Type "Yes" , if not then "No": ')
                            sql="insert into customer_details values({},'{}',{},'{}','{}','{}','{}',{},{},{},'{}','{}')".format(sr_no,Customer_Name,age,Customer_Car,Car_Model,Gen,Pay_Method,Price,Tax,total,Email,Phone)
                            SQL='select * from Customer_Details'
                            cur.execute(sql)
                            con.commit()
                            cur.execute(SQL)
                            rs = cur.fetchall()
                            print('one record succesfully INSERTED')
                            
                            if yn.lower() == 'no':
                               break
                            
                            print('\n')
                            print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))
                    
                        if age < 20 or age > 61 :
                            
                            print('Sorry\nYou Are Not Eligible To Buy A Car!! Minimum age 20 and Above')
                            engine.setProperty('rate',130)
                            answer = "Sorry! You Are Not Eligible To Buy A Car , Minimum age 20 and Above"
                            engine.say(answer)
                            engine.runAndWait()
                            continue
                        
                if YN.lower() == 'no':
                    
                    print("You've Succesfully Exited Entering the values in table --> 'CUSTOMER_DETAILS' ")
                    break
           
        
        
#           // Exiits the Function

          
        if ch == 0:
            
            print("!!You've Succesfully Exited for Adding the values for tables!!\n")
            engine.setProperty('rate',130)
            answer = "You've Succesfully Exited for Adding the values for tables!!"
            engine.say(answer)
            engine.runAndWait()
            break
        
 




 
        
#   ---------------------------------------------------------------------------------------------------------------------------------------------------------------- EDITING VALUES -------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Edit_Values():
    
    engine.setProperty('rate',130)
    answer = "Your Now Editing Values!!"
    engine.say(answer)
    engine.runAndWait()
    
    while True:
        
        print()
        print('*----------------------------------------------------------------------*')
        print('Please Select Which One Of The Options You Want To EDITING THE VALUES From The Following :\n1.Values for All the Tables(Available Cars, Car Details, Car Features\n2.CUSTOMER DETAILS\n0.EXIT (Back To Menu)')
        print('*----------------------------------------------------------------------*')
        ch = int(input('Enter Your Choise from the above options: '))
        
        if ch == 1:
            
            while True :
                
                print('Your Tables Are: ')
                sql1 = 'select * from available_cars'
                sql2 = 'select * from car_models'
                sql3 = 'select * from car_features'
                cur.execute(sql1)
                RS1 = cur.fetchall()
                cur.execute(sql2)
                RS2 = cur.fetchall()
                cur.execute(sql3)
                RS3 = cur.fetchall()
                
                print('TABLE ----> "AVAILABLE CARS" ')
                print(tabulate(RS1, headers=['Car ID','Car Name','Model ID'], tablefmt='psql'))
                print('\n')
                
                  
                print('TABLE ----> "CAR MODELS"')
                print(tabulate(RS2, headers=['Car Name','Car Plate','Model ID'], tablefmt='psql'))
                print('\n')
                
                    
                print('TABLE ----> "CAR FEATURES"')
                print(tabulate(RS3, headers=['Car Plate','Car Name','Car Features','Model ID'], tablefmt='psql'))
                print('\n')
                
                print("\nYou are now EDITING the Records for table --> 'AVAILABLE_CARS'")
                car_name= input('Enter your Car Name you want to EDIT: ')
                cr_plate = input('Enter your NEW Car Plate: ')
                car_id= input('Enter your NEW Car ID: ')
                cr_model = input('Enter Your NEW CAR MODEL ID: ')
                car_features= input('Enter Your NEW CAR FEATURE: ')
                Y_N = input('if you wish to continue Type "Yes" , if not then "No": ')
                sql1 ="update available_cars set car_id = '{}' , model_id = '{}' where car_name = '{}'".format(cr_model,car_id,car_name)
                sql2="update car_models set plate = '{}', model_id = '{}' where car_name = '{}'".format(cr_plate,cr_model,car_name)
                sql3 = "update car_features set plate = '{}' , model_id = '{}' , features = '{}' where car_name = '{}'".format(cr_plate,cr_model,car_features,car_name)
                SQL_1 = 'Select * from Available_cars'
                SQL_2 = 'Select * from Car_Models'
                SQL_3 ='Select * from Car_Features'
                cur.execute(sql1)
                con.commit()
                cur.execute(SQL_2)
                rs1 = cur.fetchall()
                
                cur.execute(sql2)
                con.commit()
                cur.execute(SQL_2)
                rs2 = cur.fetchall()
                
                cur.execute(sql3)
                con.commit()
                cur.execute(SQL_3)
                rs3 = cur.fetchall()
                print('one record succesfully UPDATED')
                
                if Y_N.lower()=='no':
                    break
                
            print('Your Updated Table is: ')
            print(tabulate(rs1, headers=['Car Name','Car ID','Model ID'], tablefmt='psql'))
            print('\n')
            
            print('Your Updated Table is: ')
            print(tabulate(rs2, headers=['Car Name','Car Plate','Model ID'], tablefmt='psql'))
            print('\n')
            
            print('Your Updated Table is: ')
            print(tabulate(rs3, headers=['Car Plate','Car Name','Car Features','Model ID'], tablefmt='psql'))
            print('\n')
            
            
        if ch == 2:
            
            while True:
                
                print("\nYou are now EDITING the Records for table --> 'CUSTOMER_DETAILS'")
                print('\nThis Table Can Only be Edited IF The Records on the table "CUSTOMER_DETAILS" are Having Wrong Infomation or the details of the Customer to be Updated')
                print('\nIf Yes type --> "YES" if not then --> "NO"\nIf You Want To See Your Current Table the type --> "CURTBL"')
                yn = input('Type HERE: ')
            
#             // if User Input is ' YES '
            
                if yn.lower() == 'yes':
                    
                    print('Your Current Not Updated Table: ')
                    Sql = 'Select * from Customer_details'
                    cur.execute(Sql)
                    RS = cur.fetchall()
                    print(tabulate(RS, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))
                    print('\nWhich Of The Following Options You Want To Edit: \n1. Customer Name\n2. Customers Car\n3. Cars Model\n4. Payment Method\n5. Email\n6. OR Mobile Number\n0. EXIT  (Exits Updtaing Value for Customer Details)')
                    S = int(input('Type HERE: '))
                
                
#                 // Each IF Statement is ASKED, does the employee wants to edit the info

#                   // there can be human error in typing

#                     // if User wants to change info about Car Name (i.e No.2) the User May Press 1 or 3 or any input in INT

                
                    if S == 1:
                        
                        print('\nYou Are Now Going to CHANGE the wrong Info about Customer(s) Name from Table --> "CUSTOMER_DETAILS" ,\nIf You Wish To Change Then:\nType "Yes" ,\nif not then "No": ')
                        y_n = input('Type Here: ')
                        
                        if y_n.lower() == 'yes':
                            
                            
                            Sr_No = int(input('Enter Your Customers Serial Number [Example --> 102 or 747 etc...]: ' ))
                            Cust_Name = input('Enter The Updated Customer(s) Name to Be Change: ')
                            sql = "update customer_details set Customer_Name = '{}' where Sr_No = '{}'".format(Cust_Name,Sr_No)
                            SQL ='Select * from Customer_Details'
                            cur.execute(sql)
                            con.commit()
                            cur.execute(SQL)
                            rs = cur.fetchall()
                            print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))
                            print('one record succesfully UPDATED')
                            
                        if y_n.lower() == 'no':
                            break

                    if S == 2:
                        
                        print('\nYou Are Now Going to CHANGE the wrong Info about Customer(s) CAR from Table --> "CUSTOMER_DETAILS" ,\nIf You Wish To Change Then:\nType "Yes" ,\nif not then "No": ')
                        y_n = input('Type Here: ')
                        
                        if y_n.lower() == 'yes':
                            Sr_No = int(input('Enter Your Customers Serial Number [Example --> 102 or 747 etc...]: ' ))
                            Cust_Car = input('Enter The Updated Customer(s) Car to Be Change: ')
                            sql = "update customer_details set Customers_Car = '{}' where Sr_No = '{}'".format(Cust_Car,Sr_No)
                            SQL ='Select * from Customer_Details'
                            cur.execute(sql)
                            con.commit()
                            cur.execute(SQL)
                            rs = cur.fetchall()
                            print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))
                            print('one record succesfully UPDATED')
                        
                        if y_n.lower() == 'no':
                            break
                    
                    if S == 3:
                        
                        print('\nYou Are Now Going to CHANGE the wrong Info about Customer(s) CAR MODEL from Table --> "CUSTOMER_DETAILS" ,\nIf You Wish To Change Then:\nType "Yes" ,\nif not then "No": ')
                        y_n = input('Type Here: ')
                        
                        if y_n.lower() == 'yes':
                            
                            Sr_No = int(input('Enter Your Customers Serial Number [Example --> 102 or 747 etc...]: ' ))
                            Cust_Car_Model = input('Enter The Updated Customer(s) Car Model to Be Change: ')
                            sql = "update customer_details set Car_Model = '{}' where Sr_No = '{}'".format(Cust_Car_Model,Sr_No)
                            SQL ='Select * from Customer_Details'
                            cur.execute(sql)
                            con.commit()
                            cur.execute(SQL)
                            rs = cur.fetchall()
                            print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))
                            print('one record succesfully UPDATED')
                            
                        if y_n.lower() == 'no':
                            break
                    
                    if S == 4:
                        
                        print('\nYou Are Now Going to CHANGE the wrong Info about Customer(s) PAYMENT METHOD from Table --> "CUSTOMER_DETAILS" ,\nIf You Wish To Change Then:\nType "Yes" ,\nif not then "No": ')
                        y_n = input('Type Here: ')
                        
                        if y_n.lower() == 'yes':
                            
                            Sr_No = int(input('Enter Your Customers Serial Number [Example --> 102 or 747 etc...]: ' ))
                            Cust_payment = input('Enter The Updated Customer(s) Payment Method to Be Change: ')
                            sql = "update customer_details set Customer_Payment_Method = '{}' where Sr_No = '{}'".format(Cust_payment,Sr_No)
                            SQL ='Select * from Customer_Details'
                            cur.execute(sql)
                            con.commit()
                            cur.execute(SQL)
                            rs = cur.fetchall()
                            print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))
                            print('one record succesfully UPDATED')
                        
                        if y_n.lower() == 'no':
                            break
                    
                    
                    if S == 5:
                        
                        print('\nYou Are Now Going to CHANGE the wrong Info about Customer(s) EMAIL from Table --> "CUSTOMER_DETAILS" ,\nIf You Wish To Change Then:\nType "Yes" ,\nif not then "No": ')
                        y_n = input('Type Here: ')
                        
                        if y_n.lower() == 'yes':
                            Sr_No = int(input('Enter Your Customers Serial Number [Example --> 102 or 747 etc...]: ' ))
                            Cust_Email = input('Enter The Updated Customer(s) Email to Be Change: ')
                            sql = "update customer_details set EMAIL = '{}' where Sr_No = '{}'".format(Cust_Email,Sr_No)
                            SQL ='Select * from Customer_Details'
                            cur.execute(sql)
                            con.commit()
                            cur.execute(SQL)
                            rs = cur.fetchall()
                            print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))
                            print('one record succesfully UPDATED')
                        
                        if y_n.lower() == 'no':
                            break
                            
                    if S == 6:
                        
                        print('\nYou Are Now Going to CHANGE the wrong Info about Customer(s) MOBILE NUMBER from Table --> "CUSTOMER_DETAILS" ,\nIf You Wish To Change Then:\nType "Yes" ,\nif not then "No": ')
                        y_n = input('Type Here: ')
                        
                        if y_n.lower() == 'yes':
                            
                            Sr_No = int(input('Enter Your Customers Serial Number [Example --> 102 or 747 etc...]: ' ))
                            Cust_Mob_No = input('Enter The Updated Customer(s) Mobille Number to Be Change: ')
                            sql = "update customer_details set Mobile_Number = '{}' where Sr_No = '{}'".format(Cust_Mob_No,Sr_No)
                            SQL ='Select * from Customer_Details'
                            cur.execute(sql)
                            con.commit()
                            cur.execute(SQL)
                            rs = cur.fetchall()
                            print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))
                            print('one record succesfully UPDATED')
                       
                        if y_n.lower() == 'no':
                            break
                    
                    
                    if S == 0:
                        
                        print("You've Succesfully Exited Updating Values of table --> 'Customer Details'!!")
                        answer = "You've Succesfully Exited Updating Values of table Customer Details"
                        ans = "Your Updated Table is"
                        engine.say(answer)
                        engine.say(ans)
                        engine.runAndWait()
                        print('Your Updated Table is: ')
                        SQL = 'Select * from Customer_Details'
                        cur.execute(SQL)
                        rs = cur.fetchall()
                        print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))
                        print('\n')
                        break
                    
            
                           
                
    #             // if User input is ' Curtbl ' (Current Table)
          
    #              // May Give The Updated Table if the User does not Give Input as CURTBL at FIRST  Input Statement in EDITING Section

    #               // Must Be Use Before Editing To Check What is Currently the Data Stored in it

                if yn.lower() == 'curtbl':
                    
                    print('Your Current Table is: ')
                    SQL = 'Select * from Customer_Details'
                    cur.execute(SQL)
                    rs = cur.fetchall()
                    print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))  
                    print('\n')
                    
                    
    #               // if User Input is ' NO '

    #                 //Shows The Updated Table Values 
                    
                if yn.lower() == 'no':
                    
                    print("You've Succeesfully Exited form EDITING the table --> 'Customer_Details'")
                    print('Your Final Updated Table is: ')
                    SQL = 'Select * from Customer_Details'
                    cur.execute(SQL)
                    rs = cur.fetchall()
                    print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customer Gender','Customer Payment Method','Price of Car','Tax Applied','Total Charge [AED]','Email','Phone Number'], tablefmt='psql'))
                    print('\n')
                    break

#           // Exiits the Function

        if ch == 0:
            
            print("!!You've Succesfully Exited Editing The Tables!!\n")
            engine.setProperty('rate',130)
            answer = "You've Succesfully Exited for Editing the values for tables!!"
            engine.say(answer)
            engine.runAndWait()
            break
        
        
        

        
        
#  ------------------------------------------------------------------------------------------------------------------------------------------------ GROUPING VALUES (LIKE CLAUSE) ---------------------------------------------------------------------------------------------------------------------------------------------
        
def Group():
    
    engine.setProperty('rate',130)
    answer = "Your Now Grouping Values!!"
    engine.say(answer)
    engine.runAndWait()
    while True:
        
        print()
        print('*----------------------------------------------------------------------*')
        print('Please Select Which One Of The Options You Want To GROUP THE VALUES From The Following Tables:\n1.AVAILABLE CARS\n2.CAR MODEL\n3.CAR FEATURES\n4.CUSTOMER DETAILS\n0.EXIT (Back To Menu)')
        print('*----------------------------------------------------------------------*')
        ch = int(input('Enter Your Choise from the above options: '))
        
        if ch == 1:
            
            while True:
                
                print("\nYou are now GROUPING the Records for table --> 'AVAILABLE_CARS' ")
                cr_name= input('Type The CAR NAME that you want to Group: ')
                Y_N = input('if you wish to continue Type "Yes" , if not then "No": ')
                print('\n')
                sql="select * from available_cars where car_name like '{}%'".format(cr_name)
                cur.execute(sql)
                rs = cur.fetchall()
                print(tabulate(rs, headers=['Car ID','Car Name','Model ID'], tablefmt='psql'))
                print('\n')
                print('one record succesfully GROUPED')
                
                if Y_N.lower()=='no':
                    break
            
        if ch == 2:
            
            while True:
                
                print("\nYou are now GROUPING the Records for table --> 'CAR_MODELS'")
                cr_name= input('Type The CAR NAME that you want to Group: ')
                print('\n')
                Y_N = input('if you wish to continue Type "Yes" , if not then "No": ')
                sql="select * from car_models where car_name like '{}%'".format(cr_name)
                cur.execute(sql)
                rs = cur.fetchall()
                print(tabulate(rs, headers=['Car Name','Car Plate','Model ID'], tablefmt='psql'))
                print('\n')
                print('one record succesfully GROUPED')
                
                if Y_N.lower()=='no':
                    break
            
        if ch == 3:
            
            while True:
                
                print("\nYou are now GROUPING the Records for table --> 'CAR_FEATURES'")
                cr_name= input('Type The CAR NAME that you want to Group: ')
                Y_N = input('if you wish to continue Type "Yes" , if not then "No": ')
                print('\n')
                sql="select * from car_features where car_name like '{}%'".format(cr_name)
                cur.execute(sql)
                rs = cur.fetchall()
                print(tabulate(rs, headers=['Car Plate','Car Name','Car Features','Model ID'], tablefmt='psql'))
                print('\n')
                print('one record succesfully GROUPED')
                
                if Y_N.lower()=='no':
                    break
        
        if ch == 4:
            
            while True:
                
                print("\nYou are now GROUPING the Records for table --> 'CUSTOMER_DETAILS'")
                name= input('Type The CARS NAME that you want to Group the Details of Customers: ')
                Y_N = input('if you wish to continue Type "Yes" , if not then "No": ')
                print('\n')
                sql="select * from customer_details where Customers_Car like '{}%'".format(name)
                cur.execute(sql)
                rs = cur.fetchall()
                print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customers Gender','Customer(s) Payment Method','Price of Car','Tax Applied','Total Charge (AED)','Emial','Mobile Number'], tablefmt='psql'))
                print('\n')
                print('one record succesfully GROUPED')
                
                if Y_N.lower()=='no':
                    break
        
        
#           // Exiits the Function        
        
        
        if ch == 0:
            
            print("!!You've Succesfully Exited Grouping the Tables!!\n")
            engine.setProperty('rate',130)
            answer = "You've Succesfully Exited for Grouping the values for tables!!"
            engine.say(answer)
            engine.runAndWait()
            break
        
    



#  ------------------------------------------------------------------------------------------------------------------------------------------------------ DELETING VALUES ------------------------------------------------------------------------------------------------------------------------------------------

def Delete_Values():
    
    engine.setProperty('rate',130)
    answer = "Your Now Deleting Values!!"
    engine.say(answer)
    engine.runAndWait()
    
    while True:
        
        print()
        print('*----------------------------------------------------------------------*')
        print('Please Select Which One Of The Options You Want To DELETE THE VALUES From:\n1.Car Information from "ALL" Tables or\n2.CUSTOMER DETAILS\n0.EXIT (Back To Menu)')
        print('*----------------------------------------------------------------------*')
        ch = int(input('Enter Your Choise from the above options: '))
        
        if ch == 1:
            
            print('Your Tables Are: ')
            sql1 = 'select * from available_cars'
            sql2 = 'select * from car_models'
            sql3 = 'select * from car_features'
            cur.execute(sql1)
            rs1 = cur.fetchall()
            cur.execute(sql2)
            rs2 = cur.fetchall()
            cur.execute(sql3)
            rs3 = cur.fetchall()
            
            print('TABLE ----> "AVAILABLE CARS" ')
            print(tabulate(rs1, headers=['Car ID','Car Name','Model ID'], tablefmt='psql'))
            print('\n')
            
              
            print('TABLE ----> "CAR MODELS"')
            print(tabulate(rs2, headers=['Car Name','Car Plate','Model ID'], tablefmt='psql'))
            print('\n')
            
                
            print('TABLE ----> "CAR FEATURES"')
            print(tabulate(rs3, headers=['Car Plate','Car Name','Car Features','Model ID'], tablefmt='psql'))
            print('\n')
            
            while True:
                
                print("\nYou are now DELETING THE VALUES of the Records form table --> 'AVAILABLE_CARS' ")
                cr_model_id= input('Type The CAR MODEL ID that you want to DELETE: ')
                Y_N = input('if you wish to continue Type "Yes" , if not then "No": ')
                SQL1="Delete from available_cars where Model_ID = '{}' ".format(cr_model_id)
                SQL2="Delete from car_models where Model_ID = '{}' ".format(cr_model_id)
                SQL3="Delete from car_features where Model_ID = '{}' ".format(cr_model_id)
                SQL_1 = 'select * from Available_Cars'
                SQL_2 = 'select * from car_models'
                SQL_3 = 'select * from car_features'
                cur.execute(SQL1)
                con.commit()
                cur.execute(SQL_1)
                RS1 = cur.fetchall()
                
                cur.execute(SQL2)
                con.commit()
                cur.execute(SQL_2)
                RS2 = cur.fetchall()
                
                cur.execute(SQL3)
                con.commit()
                cur.execute(SQL_3)
                RS3 = cur.fetchall()
                
                print('\n')
                print('one record succesfully DELETED from ALL the Tables!!')
                
                if Y_N.lower()=='no':
                    break
                
            print('Your New Table after Deleting is: ')
            print(tabulate(RS1, headers=['Car ID','Car Name','Model ID'], tablefmt='psql'))
            print('\n')
            
              
            print('Your New Table after Deleting is: ')
            print(tabulate(RS2, headers=['Car Name','Car Plate','Model ID'], tablefmt='psql'))
            print('\n')
            
                
            print('Your New Table after Deleting is: ')
            print(tabulate(RS3, headers=['Car Plate','Car Name','Car Features','Model ID'], tablefmt='psql'))
            print('\n')
                
                
        if ch == 2:
            
            while True:
                
                SQL = 'select * from Customer_Details'
                cur.execute(SQL)
                rs = cur.fetchall()
                print('The Current Customer Table is: ')
                print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customers Gender','Customer(s) Payment Method','Price of Car','Tax Applies','Payment in AED','Email','Mobile Number'], tablefmt='psql'))
                print('\n')
                print("\nYou are now DELETING THE VALUES for table --> 'CUSTOMER_DETAILS'")
                name = input('Type The CUSTOMERS FULL NAME that you want to DELETE from table CUSTOMER_DETAILS: ')
                Y_N = input('if you wish to continue Type "Yes" , if not then "No": ')
                sql="Delete from Customer_Details where Customer_Name = '{}'".format(name)
                SQL1 = 'select * from Customer_Details'
                cur.execute(sql)
                con.commit()
                cur.execute(SQL1)
                rs = cur.fetchall()
                print('one record succesfully DELETED!!')
                
                if Y_N.lower()=='no':
                    break
                
            print('Your New Table after Deleting is: ')
            print(tabulate(rs, headers=['Sr No','Customer Name','Age','Customers Car','Car Model','Customers Gender','Customer(s) Payment Method','Price of Car','Tax Applies','Payment in AED','Email','Mobile Number'], tablefmt='psql'))
            print('\n')
        
            
#           // Exiits the Function           
                
        if ch == 0:
            
            print("!!You've Succesfully Exited Deleting the Values of Tables!!\n")
            engine.setProperty('rate',130)
            answer = "You've Succesfully Exited for Deleting the values for tables!!"
            engine.say(answer)
            engine.runAndWait()
            break
        
        

        


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- TIME DATE -------------------------------------------------------------------------------------------------------------------------------------

def timedate():
    
    import datetime

#   // Checks Date and time from the USER's system

#    // will say Good Morning, Evening and Afternoon according Sustems Time

    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        
        engine.setProperty('rate',130)
        answer = "Good Morning "
        engine.say(answer)
        engine.runAndWait()

    elif hour >= 12 and hour < 18:
        
        engine.setProperty('rate',130)
        answer = "Good Afternoon "
        engine.say(answer)
        engine.runAndWait()


    else:
        
        engine.setProperty('rate',130)
        answer = "Good Evening "
        engine.say(answer)
        engine.runAndWait()


    engine.setProperty('rate',130)
    answer = "I'm your's Assistant For Today !"
    engine.say(answer)
    engine.runAndWait()

timedate()

       
#    --------------------------------------------------------------------------------------------------------------------------------------------------------------- MAIN CODE STARTS  ------------------------------------------------------------------------------------------------------------------------------------------------ 
       
       
engine.setProperty('rate',130)
answer = "If your customer type CUSTOMER or If Your Employee type EMPLOYEE "
Answer ="If You Wish to Exit type EXIT "
engine.say(answer)
engine.say(Answer)
engine.runAndWait()

while True:

#      // Asking User if He/She is an Employee or Customer


#       // if customer, line jumps to ' 731 '


#        // if Employee, line jumps to  ' 920 '


    print('\nIf your customer type --> "CUSTOMER or customer"\nIf Your Employee type --> "EMPLOYEE or employee"\nIf You Wish to Exit type --> "EXIT or exit" ')
    Ch = input('Type HERE: ')
    
    if Ch.lower() == 'customer':
        
        engine.setProperty('rate',130)
        answer = "Welcome Dear Customer to 'Davis Auto Group Dealership' "
        engine.say(answer)
        engine.runAndWait()
        
        
#         // Logo Provided If it's a Customer

        
        print('''
                ..........,,::::::::::::::::::::::::::::::::,.......................................................
                ........,+?%S##############SSSSSSS%%%%%%????*+,.....................................................
                .......:*%@@@@@#%%SSSSSSS%%%%%%%%%SSSS%%%%%%?**.....................................................
                .......**@@@@@@@#%?****************%#SSSSS%%S**++++++++++++++++++++++++++++++++++++++++++++++++;;:,.
                ......;?#@@@@@@@@@@#%%%%%%?********?####SSSSSSSSSSS#SSS###########@@@####@@@########@@@@@@@@@@##S%*,
                .....,?%@@@@@????????%@@@@S********%@######S?????S#@%???S@@@S????#@@S??*S@@S??????*?@@@@@@@@@@@@@S%;
                .....+*#@@@@%;+++++++#@@@@%;+++++++#@###@#?++;++++#@S++;?@#*;+;*#@@@++;*@@@+;;*%%%%#@@@@??%%%%%%%?*,
                ....:*%@@@@@;:::::::?@@@@#::::::::%@@@@@S+:::*%:::%@@+::;%;:::?@@@@?:::%@@?:::;;;;*@@@@#%%%%%%?+*;,.
                ....*?@@@@@?;;;;;;;+@@@@@?;;;;;;;+@@@@@S+;;;%S%;;;*@@%;;;;;;+S@@@@@+;;+@@@%????;;;S@@@#?%%%%%%%+,...
                ...;%#@@@@@********S@@@@#********#@@@@%***?#S******#@@?****?@@@@@@S***#@@S*******%@@@@#S###S%?:.....
                ..,?%@@@@@%???????%@@@@@%???????%@@@#%???%@@#######@@@##@#@@@@@@@@@##@@@@#@@@@#@@@@@@S????%%+,......
                ..+*#@@@@S+*******%#SS%*********#@@%****S@#########@##########@@@@##########@@##@@@@@@@#?**,........
                .:*?@@@@@+;;;;;;;;;;;;;;;;;;;;*#@@#%%%%#@@@@@@@@@@@@@@################################S?*;..........
                .;*#@@@@S******************?%#@@@@@@@@@##############S?+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:,...........
                .,*%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#?+;;;;;;;;;;;;;;.............................................
                ..,;*?%SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS%*;............................................................
                
                
                ''')                                                                                                      
        
        while True:
            
            print()
            print('*----------------------------------------------------------------------*')
            print('Choose the following options:\n1. Display Cars (Available, Models, and its Features)\n2. Search a SPECIFIC CAR (Available, Models, and its Features)\n3. If You Wish To Buy You Can Enter Your Name and Contact Details to Table --> "CUSTOMER ENTRY"\n0. Exit (From Customers to Main Menu)')
            print('*----------------------------------------------------------------------*')
            choose = int(input('Enter Your Choise from above options: '))
            if choose == 1:
                
                
#                 // Directly Shows All contents inside the Tables from the car_dealership database

#                  // Excluding Customer Details and Customer(s)

                
                print('\nThis is the Number Of Available Cars : ')
                sql = 'select Car_Name,count(Car_Name) from available_cars group by car_name'
                cur.execute(sql)
                rs = cur.fetchall()
                print(tabulate(rs, headers=['Car Name','Count(Car Name)'], tablefmt='psql'))
                print('\n')
                
                print('\nThis are the Models of the Corresponding Cars : ')
                sql = 'select * from car_models '
                cur.execute(sql)
                rs = cur.fetchall()
                print(tabulate(rs, headers=['Car ID','Car Name','Model ID','Car Plate'], tablefmt='psql'))
                print('\n')

                print('\nThis are the FEATURES of the Corresponding Cars :  ')
                sql = 'select * from car_features '
                cur.execute(sql)
                rs = cur.fetchall()
                print(tabulate(rs, headers=['Car Name','Model ID' ,'Car Features','Plate'], tablefmt='psql'))
                print('\n')
                
                continue
            
                    
            if choose == 2:
                

#               // Separate While Loops are give to ask use if they want to serach more cars

#                // Depends on the values in the tables


                while True:
                    
                    print('\nThis are the Total Number Of Available Cars you have Searched : ')
                    cr_name = input('\nEnter Your Car Name to be Searched : ')
                    sql="select Car_ID,Car_Name from available_cars where car_name like '{}%'".format(cr_name)
                    cur.execute(sql)
                    rs = cur.fetchall()
                    print(tabulate(rs, headers=['Car ID','Car Name','Model ID'], tablefmt='psql'))
                    yn = input('\nif you wish to continue Type "Yes" , if not then "No": ')
                    
                    if yn.lower() == 'no':
                        break
                    
                while True:
                    
                    print('\nThis are the Total Number Of Models of the Corresponding Cars You have Searched : ')
                    name = input('\nEnter Your Car Name to be Searched : ')
                    sql="select * from car_models where car_name like '{}%'".format(name)
                    cur.execute(sql)
                    rs = cur.fetchall()
                    print(tabulate(rs, headers=['Car Name','Car Plate','Model ID'], tablefmt='psql'))
                    yn = input('\nif you wish to continue Type "Yes" , if not then "No": ')
                    
                    if yn.lower() == 'no':
                        break
                    
                while True:
                    
                    print('\nThis are the Total Number Of FEATURES of the Corresponding Cars You have Searched  :  ')
                    Name = input('\nEnter Your Car Name to be Searched : ')
                    sql="select * from car_features where car_name like '{}%'".format(Name)
                    cur.execute(sql)
                    rs = cur.fetchall()
                    print(tabulate(rs, headers=['Car Plate','Car Name','Car Features','Model ID'], tablefmt='psql'))
                    yn = input('\nif you wish to continue Type "Yes" , if not then "No": ')
                    
                    if yn.lower() == 'no':
                        break
                


#             // After Checking Through The Details of the Cars

#               // They Can Input THeir Names in this table (i.e Customer Entry) , if they want to


            
            if choose == 3:
                
                print('\nYou Are Now Going To Enter Your Details and Car Name And Model To Buy (ONLY IF YOU WANT TO BUY)\n Willing To Buy ?? if so Type "Yes", if NOT then "NO"')
                buy = input('Type HERE: ')
                    
                if buy.lower() == 'yes':
                    
                    print('\nThese Records Will be Further Added in Table --> "CUSTOMER DETAILS" By an Employee') 
                    age = int(input('Type Your Age Here: '))
                    
                    if age >= 20 or age <= 60 :
                        tbl = 'select * from Customer_entry'
                        cur.execute(tbl)
                        sr = cur.fetchall()
                        print(tabulate(sr, headers=['Sr No','Name','Age','Car Name and Model to Buy','Email','Contact Number'], tablefmt='psql'))
                        Sr_No = int(input('Enter Serisl Number To Be Recorded [Serial Number Cannot Be Same]: '))
                        Name = input('Enter Your Full Name To Be Recorded: ')
                        Car_Name_Model = input('Enter Your Car Name and its Model [Model Must be in ROUND BRACKETS " () "]: ')
                        Email = input('Enter Your EMAIL address: ')
                        Phone = input('Enter Your Phone Number: ')
                        sql = "insert into customer_entry values({},'{}',{},'{}','{}','{}')".format(Sr_No,Name,age,Car_Name_Model,Email,Phone)
                        SQL = 'Select * from Customer_Entry'
                        cur.execute(sql)
                        con.commit()
                        cur.execute(SQL)
                        rs = cur.fetchall()
                        print('Your Details are recorded succesfully !!')
                        print(tabulate(rs, headers=['Sr No','Name','Age','Car Name and Model','Email','Phone Number'], tablefmt='psql'))
                        print('\n')
                        print('Thank You For Entering Your Details!!\nWill Keep You Updated With You If The Order is Placed!!\nGoodBye!!')
                        engine.setProperty('rate',130)
                        answer = "Thank You For Entering Your Details!!"
                        ans = "Will Keep You Updated With You If The Order is Placed!!"
                        Answer = "GoodBye"
                        engine.say(answer)
                        engine.say(ans)
                        engine.say(Answer)
                        engine.runAndWait()
                    
                    if age < 20 or age > 61:
                        
                        print('You Are Not Eligible To Buy A Car!!\nGoodBye')
                        engine.setProperty('rate',130)
                        answer = "You Are Not Eligible To Buy A Car"
                        Answer = " GoodBye"
                        engine.say(answer)
                        engine.say(Answer)
                        engine.runAndWait()
                        continue
            
                if buy.lower() == 'no':
                    
                    print('Thank You for Your Cooperation, You Have Chosen Not To Buy a Car ')
                    engine.setProperty('rate',130)
                    answer = "Thank You for Your Cooperation"
                    Ans = 'You Have Chosen Not To Buy a Car'
                    ans = "But We Will Keep You Updated For New Arrivals of Cars and Their Models!"
                    Answer = "GoodBye"
                    engine.say(answer)
                    engine.say(Ans)
                    engine.say(ans)
                    engine.say(Answer)
                    engine.runAndWait()
                    continue
                        
                    
            
            if choose == 0:
                
                engine.setProperty('rate',130)
                answer = "Succesfully Exited"
                Answer = " Thank You For Being With Us, See You Soon!!"
                engine.say(answer)
                engine.say(Answer)
                engine.runAndWait()
                print('Thank You For Being With Us.\nSee You Soon!!')
                
                print('''
████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗██╗                  
╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║██║                  
   ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║    ██║██║                  
   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║    ╚═╝╚═╝                  
   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝    ██╗██╗                  
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝     ╚═╝╚═╝                  
                                                                                                      
██╗   ██╗██╗███████╗██╗████████╗    ██╗   ██╗███████╗     █████╗  ██████╗  █████╗ ██╗███╗   ██╗    ██╗
██║   ██║██║██╔════╝██║╚══██╔══╝    ██║   ██║██╔════╝    ██╔══██╗██╔════╝ ██╔══██╗██║████╗  ██║    ██║
██║   ██║██║███████╗██║   ██║       ██║   ██║███████╗    ███████║██║  ███╗███████║██║██╔██╗ ██║    ██║
╚██╗ ██╔╝██║╚════██║██║   ██║       ██║   ██║╚════██║    ██╔══██║██║   ██║██╔══██║██║██║╚██╗██║    ╚═╝
 ╚████╔╝ ██║███████║██║   ██║       ╚██████╔╝███████║    ██║  ██║╚██████╔╝██║  ██║██║██║ ╚████║    ██╗
  ╚═══╝  ╚═╝╚══════╝╚═╝   ╚═╝        ╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝
                                                                                                      
                        
                    ''')
                    
                break            
            
            
            

#      // If Entered Employee


    if Ch.lower() == 'employee':
        
        Pass = input('\nIf Your an Employee Enter your Pass Code [Same Pass Code Applies to ALL EMPLOYEES] : ')
        
        if Pass.lower() == 'emp123':
            
            engine.setProperty('rate',130)
            answer = "Access Granted!!"
            engine.say(answer)
            engine.runAndWait()
            print('Access Granted!!')
            
            while True:
                print()
                print('*---------------------------------------------------------------*')
                print('MENU:\n1.INSERT the Values of the Tables\n2.EDIT Values of the table\n3.GROUP the table with specific Name or Plate\n4.DELETE value(s) from a Table\n0.EXIT (WHOLE PROGRAM)')
                print('*---------------------------------------------------------------*')
                print()
                ch = int(input('\nEnter Your Choise from the above options: '))
                
#                 // if user Choses any options UNTIL NOT GIVEN an INPUT OF option ' 0 ' the loop will continue to loop 
                
                if ch == 1:
                    
                    Table_Values()
                    
                if ch == 2:
                    
                    Edit_Values()
                    
                if ch == 3:
                    
                    Group()
                    
                if ch == 4:
                    
                    Delete_Values()
                    
                if ch == 0:
                    
                    engine.setProperty('rate',130)
                    answer = "Thank You For Your Cooporation!"
                    ans = 'Goodbye'
                    engine.say(answer)
                    engine.say(ans)
                    engine.runAndWait()
                    print("\n!!You've Succesfully Exited!!")
                    break

    
    
    

    
    
#     // Password Check if its an Employee

#      // if entered Wrong Password then returns back to line ' 727 '  (INPUT Statement)

        if Pass.lower() != 'emp123':
            
                    engine.setProperty('rate',130)
                    answer = "Access Denied!!"
                    engine.say(answer)
                    engine.runAndWait()
                    continue
                    
                    
    
    
                    
#  ------------------------------------------------------------------------------------------------------------------------------ EXIT WHOLE PROGRAM ---------------------------------------------------------------------------------------------------------------------------------------------------                     
                    
#     // if user wish to exit can type " exit "
    
    if Ch.lower() == 'exit' :
        
        engine.setProperty('rate',130)
        answer = "Exited Succesfully!"
        Answer = 'Goodbye'
        engine.say(answer)
        engine.say(Answer)
        engine.runAndWait()
        print("\n!!You've Succesfully Exited!!\nGoodBye!!")
        print('''
 ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗    ██╗██╗
██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝    ██║██║
██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗      ██║██║
██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝      ╚═╝╚═╝
╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗    ██╗██╗
 ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝╚═╝
                                                                      ''')
        break
    
#---------------------------------------------------------------------------------------------------------------------------------------- END OF CODE ----------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    



