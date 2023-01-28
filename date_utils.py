from datetime import datetime, date

def print_with_date(msg):
    print(msg + " " + datetime_now_readable())

def datetime_now_readable():
    today = datetime.now()
    return print_dates(today)
    
def print_dates(date_obj):
    return date_obj.strftime("%d-%m-%Y %H:%M:%S")
    
    # Examples of date formats for date operations:
    # print("YYYY-MM-DD:", date_obj.strftime("%Y-%m-%d"))
    # print("DD-MM-YYYY:", date_obj.strftime("%d-%m-%Y"))
    # print("MM-DD-YYYY:", date_obj.strftime("%m-%d-%Y"))
    
    # Examples of date formats for end users:
    # print("Full date and time:", date_obj.strftime("%d-%m-%Y %H:%M:%S")) #default
    # print("Full date and time:", date_obj.strftime("%A, %B %d %Y %I:%M:%S %p"))
    # print("Short date and time:", date_obj.strftime("%x %X"))
    # print("Only time:", date_obj.strftime("%I:%M:%S %p"))
