import smtplib
import datetime as dt
import random
import pandas

my_email = "pratikgadkar1996@gmail.com"
password = "gqwuhilteifjqfcf"
now = dt.datetime.now()
today = (now.month, now.day)


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    # print(birthdays_dict[today]['name'])
    with open(f'./letter_templates/letter_{random.randint(1, 3)}.txt', mode='r') as file:
        letter_name = "[NAME]"
        content = file.read()
        updated_content = content.replace(letter_name, f"{birthdays_dict[today]['name']}")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=f"{birthdays_dict[today]['email']}",
                            msg=f"Subject:Happy Birthday !! \n\n{updated_content}")
        connection.close()
