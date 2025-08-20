

hours = int(input())
minutes = int(input())
hours_arriving_time = int(input())
minutes_arriving_time = int(input())

time_exam = hours * 60 + minutes
arrive_time = hours_arriving_time * 60 + minutes_arriving_time
diff = abs(arrive_time - time_exam)
hour = diff // 60
minute = diff % 60
if time_exam == arrive_time:
    status = "On time"
    time = "before"

if time_exam != arrive_time:


    if arrive_time > time_exam:
        status = "Late"
        diff = arrive_time - time_exam
        time = "after"

    if arrive_time < time_exam:
        if time_exam - arrive_time > 30:
            status = "Early"
            diff = time_exam - arrive_time
            time = "before"

        else:
            status = "On time"
            time = "before"
            diff = time_exam - arrive_time

if hour and not minute:
    print(status)
    print(f'{hour}:00 hours {time} the start')
elif hour and minute:
    print(status)
    print(f'{hour}:{minute:02d} hours {time} the start')
elif not hour and minute:
    print(status)
    print(f'{minute} minutes {time} the start')
else:
    print(status)