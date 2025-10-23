# main
import numpy as np
import turtle


print(f"Hello, World!")

year = 2025
month = 10
day = 23

def monthToWord(int n):
    out = ""
    if (n==2): out="February"
    elif (n==3): out="March"
    elif (n==4): out="April"
    elif (n==5): out="May"
    elif (n==6): out="June"
    elif (n==7): out="July"
    elif (n==8): out="August"
    elif (n==9): out="September"
    elif (n==10): out="October"
    elif (n==11): out="November"
    elif (n==12): out="December"
    else: out="January"
    return out

def addDay(int n):
    day += n
    smaller = [4, 6, 9, 11]
    while(day > 28 or month > 12):
        if (month >= 13):
            month -= 12
            year += 1

        if (day >= 29 and month == 2):
            day -= 28
            month += 1
        elif (day >= 31 and month is in smaller):
            day -= 30
            month += 1
        elif (day >= 31):
            day -= 31
            month += 1
        else: break

print(f"{monthToWord(month)} {day}, {year}")
