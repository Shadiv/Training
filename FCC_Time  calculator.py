def add_time(start, duration, start_day=''):
    name_days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    names_days = list(name_days.values())
    time_format = {
        0: ('12', 'AM'),
        1: ('1', 'AM'),
        2: ('2', 'AM'),
        3: ('3', 'AM'),
        4: ('4', 'AM'),
        5: ('5', 'AM'),
        6: ('6', 'AM'),
        7 : ('7', 'AM'),
        8: ('8', 'AM'),
        9: ('9', 'AM'),
        10: ('10', 'AM'),
        11: ('11', 'AM'),
        12: ('12', 'PM'),
        13: ('1', 'PM'),
        14: ('2', 'PM'),
        15: ('3', 'PM'),
        16: ('4', 'PM'),
        17: ('5', 'PM'),
        18: ('6', 'PM'),
        19: ('7', 'PM'),
        20: ('8', 'PM'),
        21: ('9', 'PM'),
        22: ('10', 'PM'),
        23: ('11', 'PM'),
        24: ('12', 'AM')
    }
    def to_minutes(time):
        hours_and_mins = time.split(':')
        return int(hours_and_mins[0]) * 60 + int(hours_and_mins[1])
    elements = start.split()
    start_mins = to_minutes(elements[0])
    if elements[1] == 'PM':
        start_mins += 60*12
    dur_mins = to_minutes(duration)
    added_time = start_mins + dur_mins
    hrs_pure = added_time // 60
    days = hrs_pure // 24
    hrs_c = hrs_pure % 24
    hrs_formatted = time_format[hrs_c][0]
    desc = time_format[hrs_c][1]

    mins = str(added_time % 60)
    if len(mins) == 1:
        mins = '0' + mins

    if start_day == "":
        new_time = f'{hrs_formatted}:{mins} {desc}'
        if days >= 1:
            if days == 1:
                new_time = f'{hrs_formatted}:{mins} {desc} (next day)'
            else:
                new_time = f'{hrs_formatted}:{mins} {desc} ({days} days later)'
        return new_time
    else:
        s_day = start_day.capitalize()
        cur_day_num = names_days.index(s_day)+1
        add_day_num = days % 7 + cur_day_num
        if add_day_num > 7:
            n_day = add_day_num - 7
            cur_day = name_days[n_day]
        else:
            cur_day = name_days[add_day_num]
        new_time = f'{hrs_formatted}:{mins} {desc}, {cur_day}'
        if days >= 1:
            if days == 1:
                new_time = f'{hrs_formatted}:{mins} {desc}, {cur_day} (next day)'
            else:
                new_time = f'{hrs_formatted}:{mins} {desc}, {cur_day} ({days} days later)'
        return new_time


print(add_time("11:06 PM", "2:02"))
print(add_time("3:30 PM", "2:12"))
print(add_time("2:59 AM", "24:00", 'sunday'))
print(add_time("8:16 PM", "466:02", "tuesday"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("11:40 AM", "0:25"))
print(add_time("11:59 PM", "24:05"))
print(add_time("11:59 PM", "24:05", "Wednesday"))

# if desc == 'PM':
#     hrs_formatted = str(hrs_c - 12)
#     if hrs_formatted == '12':
#         hrs_formatted = '0'
# else:
#     hrs_formatted = str(hrs_c)
#     if hrs_formatted == '0':
#         hrs_formatted = '00'
# if hrs_c > 12:
#     desc = 'PM'
# else:
#     desc = 'AM'