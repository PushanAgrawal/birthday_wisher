##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv

data=pandas.read_csv("birthdays.csv")
info=data.to_dict(orient="list")
month=info["month"]
day=info["day"]
name_list=info["name"]
email_list=info["email"]
#----------------create day------------#
date=dt.datetime.now()
today_month=date.month
today_day=date.day
n=0

def sendemail(n):
    P_holder="[NAME]"
    with open(f".\letter_templates\letter_{random.randint(1,3)}.txt","r") as f:
        letter_contents=f.read()
        new_letter=letter_contents.replace(P_holder,name_list[n])

    # 4. Send the letter generated in step 3 to that person's email address.
    my_email=""
    password=""
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #         connection.starttls()
    #         connection.login(user=my_email,password=password)
    #         connection.sendmail(from_addr=my_email,to_addrs=email_list[n],msg=new_letter)  

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(my_email, password)
        smtp_server.sendmail(my_email, email_list[n], new_letter)
        print("Message not sent!")        




# 2. Check if today matches a birthday in the birthdays.csv
for i in month :
    
    if today_month==i: 
        if day[n]==today_day:
            sendemail(n)
            break
    n+=1        
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
