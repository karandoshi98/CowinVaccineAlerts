# Importing libraries
import app
import requests
import json
import time
from datetime import datetime, date
import smtplib

date_str = str(date.today())
y = date_str[:4]
m = date_str[5:7]
d = str(int(date_str[8:10]) + 1)
DATE = d+"-"+m+"-"+y

MY_EMAIL = "testdummy2024@gmail.com"
MY_PASS = 'krds1998'

# Palghar = str(394)
# Mumbai = str(395)
# Thane = str(392)
#url_district = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+Palghar+"&date="+DATE

# with requests.session() as state_session:
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
#     response = state_session.get("https://cdn-api.co-vin.in/api/v2/admin/location/states", headers=headers)
#     print(response.json())

# with requests.session() as dist_session:
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
#     response = dist_session.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/21", headers=headers)
#     print(response.json())

# with requests.session() as appointment_dist_session:
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
#     response = appointment_dist_session.get(url_district, headers=headers)
#     response = response.json()

while True:
    cur = open("user_details_18.json", "r")
    user_details = json.loads(cur.read())
    cur.close()
    print(user_details)

    for PINCODE in user_details:
        print(PINCODE)
        mail_to = []
        mail_to = user_details[PINCODE]
        url_pincode = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=" + PINCODE + "&date=" + DATE
        with requests.session() as appointment_pin_session:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
            response = appointment_pin_session.get(url_pincode, headers=headers)
            print(response)
            try:
                response = response.json()
            except Exception as e:
                print(e)
            print(response)
            if response['sessions'] == []:
                print("No slots available at this moment")
            for center in response['sessions']:
                # print(center['fee_type'])
                # print(center['fee'])
                # print(center['min_age_limit'])
                # print(center['available_capacity'])
                # print(center['available_capacity_dose1'])
                # print(center['available_capacity_dose2'])
                # print(center['vaccine'])
                # print(center['slots'])
                if center['min_age_limit'] == 18 and center['available_capacity'] != 0:
                    message_string = f"Subject: {date_str}'s Vaccine Alert'!! \nVaccine available at-\n{center['name']} for the age above {center['min_age_limit']} \n\nSlots available- {center['available_capacity']}\nSlots for 1st Dose - {center['available_capacity_dose1']}\nSlots for 2nd Dose - {center['available_capacity_dose2']} \n\nAddress: {center['address']}\nhttps://www.cowin.gov.in/home"
                    with smtplib.SMTP("smtp.gmail.com") as connection:
                        connection.starttls()
                        connection.login(MY_EMAIL, MY_PASS)
                        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=mail_to,
                            msg=message_string
                        )
                        print("Mail sent to "+mail_to+" for pincode "+PINCODE+" for age above 18")
                else:
                    print("No slots available for above 18")
    time.sleep(60)



