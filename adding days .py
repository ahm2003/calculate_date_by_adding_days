# FCAI – Programming 1 – 2022 - Assignment 2
# Program Name: adding days.py 
#  Program Description: calculiting the date after adding days.
# Last Modification Date: 28 /03/2003
# Author and ID and Group: Ahmed Ashrf Zaki .. 20210010 .. Groub: A









def adding_days(year,month,day,adding):
    int(year)
    int(month)
    int(day)
    int(adding)
    m = day + adding 
    for i  in range(0,1000) :
        # this two if condtion for febrayer month as it sometimes have 28 days and sometimes 29 days
        if m  > 29 and month ==2 and year%4==0 :
            day = m - 29 
            month = month +1
        if m > 28 and month ==2 and year%4!=0 :
            day = m - 28  
            month = month + 1
        #this if condition for months which have 31 days 
        if m >31 and (month == 1 or month==3 or month ==5 or month==8 or month==10 or month==12 ) : 
            day = m -31 
            month = month+1
        # fro months with 30 days 
        if m > 30 : 
            day = m - 30 
            month = month+i
        #when start new year 
        if month > 12 : 
            year = year+1
            month = i+0 
            day = m - 31 
    
    return(day , month , year )
print("please enter the date in form year month day like 1999 2 19")
y = int(input("enter the yaer : "))
m = int(input("enter the month :"))
d = int(input("enter the day :"))
a = int(input("enter the adding days: "))
result= adding_days(y,m,d,a)
print(result)