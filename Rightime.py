from datetime import datetime
odds = list(range(1,60,2))
ritht_this_minute = datetime.today().minute
if ritht_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")
