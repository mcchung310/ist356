import beautiful_date as bd

# print(dir(bd)) 
    #  shows all the methods and attributes of the beautiful_date module

today = bd.BeautifulDate.fromisoformat('2026-09-08') 
    # Create a BeautifulDate object for September 8, 2026 
    # iso format = year-month-day

# add 2 months to the date
today = today + 2 * bd.months

print(today)
print(today.month)