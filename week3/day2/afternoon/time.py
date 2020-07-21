from datetime import datetime
from time import gmtime, strftime

# [x] convert time now to utc
time_now = datetime.now().timestamp()
print('time_now: ', time_now)  # seconds

# [x] convert yyyy-mm-dd to utc
# this is the format that input type="date" sent to server
date_from_form = '2010-09-20'  # request.POST['date']
# convert it to a time struct
converted_date_time = datetime.strptime(date_from_form, "%Y-%m-%d").timestamp()
print('converted_date_time: ', converted_date_time)

is_future_date = time_now - converted_date_time

# check if it is a future date
if is_future_date < 0:
    print('future date')
else:
    print('past date')
