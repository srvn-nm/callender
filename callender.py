# author : Sarvin Nami
def dateConvertor (day , month , year) :
    if month >= 10 or month == 10 and day > 10 :
        enteredYear = year + 622
    elif month < 10 or month == 10 and day <= 10 :
        enteredYear = year + 621
    if month <= 6 :
        allDay = year / 4 + ( year - 1 ) * 365 + day + ( month-1 ) * 31 + 226899
    elif month > 6 :
        allDay = year / 4 + ( year - 1 ) * 365 + day + ( month - 7 ) * 30 + 6 * 31 + 226899
    allDay %= enteredYear 
    if allDay <= 31 :
        enteredMonth = "January"
        enteredDay = allDay
    elif allDay <= 59 and year % 4 != 3 or allDay <= 60 and year % 4 == 3 :
        enteredDay = allDay - 31
        enteredMonth = "February"
    elif allDay <= 90 and year % 4 != 3 :
        enteredMonth = "March"
        enteredDay = allDay - 31 - 28
    elif allDay <= 91 and year % 4 == 3 :
        enteredMonth = "March"
        enteredDay = allDay - 31 - 29
    elif allDay <= 120 and year % 4 != 3 :
        enteredMonth = "April"
        enteredDay = allDay - 31 - 28 - 31
    elif allDay <= 121 and year % 4 == 3 :
        enteredMonth = "April"
        enteredDay = allDay - 31 - 29 - 31
    elif allDay <= 151 and year % 4 != 3 :
        enteredMonth = "May"
        enteredDay = allDay - 31 - 28 - 31 - 30
    elif allDay <= 152 and year % 4 == 3 :
        enteredMonth = "May"
        enteredDay = allDay - 31 - 29 - 31 - 30
    elif allDay <= 181 and year % 4 != 3 :
        enteredMonth = "June"
        enteredDay = allDay - 31 - 28 - 31 - 30 - 31
    elif allDay <= 182 and year % 4 == 3 :
        enteredMonth = "June"
        enteredDay = allDay - 31 - 29 - 31 - 30 - 31
    elif allDay <= 212 and year % 4 != 3 :
        enteredMonth = "July"
        enteredDay = allDay - 31 - 28 - 31 - 30 - 31 - 30
    elif allDay <= 213 and year % 4 == 3 :
        enteredMonth = "July"
        enteredDay = allDay - 31 - 29 - 31 - 30 - 31 - 30
    elif allDay <= 243 and year % 4 != 3 :
        enteredMonth = "August"
        enteredDay = allDay - 31 - 28 - 31 - 30 - 31 - 30 - 31
    elif allDay <= 244 and year % 4 == 3 :
        enteredMonth = "August"
        enteredDay = allDay - 31 - 29 - 31 - 30 - 31 - 30 - 31
    elif allDay <= 273 and year % 4 != 3 :
        enteredMonth = "September"
        enteredDay = allDay - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31
    elif allDay <= 274 and year % 4 == 3 :
        enteredMonth = "September"
        enteredDay = allDay - 31 - 29 - 31 - 30 - 31 - 30 - 31 - 31
    elif allDay <= 304 and year % 4 != 3 :
        enteredMonth = "October"
        enteredDay = allDay - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31 - 30
    elif allDay <= 305 and year % 4 == 3 :
        enteredMonth = "October"
        enteredDay = allDay - 31 - 29 - 31 - 30 - 31 - 30 - 31 - 31 - 30
    elif allDay <= 334 and year % 4 != 3 :
        enteredMonth = "November"
        enteredDay = allDay - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31 - 30 - 31
    elif allDay <= 335 and year % 4 == 3 :
        enteredMonth = "November"
        enteredDay = allDay - 31 - 29 - 31 - 30 - 31 - 30 - 31 - 31 - 30 - 31
    elif allDay <= 365 and year % 4 != 3 :
        enteredMonth = "December"
        enteredDay = allDay - 31 - 28 - 31 - 30 - 31 - 30 - 31 - 31 - 30 - 31 - 30
    elif allDay <= 366 and year % 4 == 3 :
        enteredMonth = "December"
        enteredDay = allDay - 31 - 29 - 31 - 30 - 31 - 30 - 31 - 31 - 30 - 31 - 30
    print (f"your date is {enteredYear} / {enteredMonth} / {enteredDay} ")
dayi = int(input('enter the day of the date : '))
monthi = int(input('enter the month of the date : '))
yeari = int(input('enter the year of the date : '))
dateConvertor(dayi , monthi , yeari)