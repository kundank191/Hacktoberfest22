# Calendar Optimization

The files that I get after exporting .ics files dont have a notification.
In this project I will read the ics files and append notification for every event before 5 min.

## Use case

add_alarm_to_calender_events(filepath = 'files/iu_cal.ics')

function will take an .ics file and then add notif to the file
Args:
    filepath : the location of the file
    num_day_before_notif : The num days before which notif will be scheduled
    num_hour_before_notif : The num hour before which notif will be scheduled
    num_min_before_notif : The num  min before notif will be scheduled
    num_sec_before_notif : The num sec before which notif will be schedules