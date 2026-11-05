# INTRO warm up for 3-6-1

import datetime

# from datetime import datetime, date, timedelta
# from "folder" import "module", "module", "module"

# today's date (python date, not a string, so you can do math on it)
today = datetime.date.today()

# add 30 days to today
today_plus_30 = today + datetime.timedelta(days =30)

#print today and 30days
print("Todays Date:", today)
print("Dater after 30 days:", today_plus_30)

# Formatting string ("f") = taking a date and turning it into a string (strftime())
# Parsing string ("p") = taking string and turning it into a date (strptime())

date_string = datetime.datetime.strftime("%a, %B, %m %Y")
print("Today's date in string format:", date_string)


# Dates as strings (you cannot do date math on strings) - so you want to get these into a date format
my_birthday = "Mar 10, 2005"
my_birthday2 = "2005-03-10"

my_birthday = datetime.datetime.strptime(my_birthday, "%m %d, %Y")
born_on = datetime.datetime.strftime(my_birthday, "%A")
print("I was born on a", born_on)