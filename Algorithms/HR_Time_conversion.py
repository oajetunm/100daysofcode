def timeConversion(s):
    time = str(s)
    hour, min,  secs, period  = time[0:2], time[3:5], time[6:8], time[8:]
    if period == 'PM' and hour == '12':
        hour = 12
    elif period == 'PM' and hour != '12':
        hour = int(hour)+12
    elif period == 'AM' and hour == '12':
        hour =str(int(hour)-12) + '0'

    return "{}:{}:{}".format(hour, min, secs)



a = '07:05:45PM'
b = '12:40:22AM'
print(timeConversion(b))
