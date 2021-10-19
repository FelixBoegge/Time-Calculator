def add_time(start, duration, day = False):

  days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

  days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  dur_tuple = duration.partition(":")
  durh = int(dur_tuple[0])
  durmin = int(dur_tuple[2])

  start_tuple = start.partition(":")
  startmin_tuple = start_tuple[2].partition(" ")
  starth = int(start_tuple[0])
  startmin = int(startmin_tuple[0])
  ampm = startmin_tuple[2]
  ampm_change = {"AM": "PM", "PM": "AM"}

  number_days = int(durh / 24)

  new_time_min = startmin + durmin
  if (new_time_min > 59):
    durh = durh + 1
    new_time_min = new_time_min % 60
  number_ampm_change = int((starth + durh) / 12)
  new_time_h = (starth + durh) % 12

  new_time_min = new_time_min if new_time_min > 9 else "0" + str(new_time_min)
  new_time_h = new_time_h = 12 if new_time_h == 0 else new_time_h
  if (ampm == "PM" and starth + (durh % 12) > 11):
    number_days = number_days + 1

  ampm = ampm_change[ampm] if number_ampm_change % 2 == 1 else ampm

  new_time = str(new_time_h) + ":" + str(new_time_min) + " " + ampm
  if (day):
    day = day.lower()
    index = int((days_of_the_week_index[day]) + number_days) % 7
    new_day = days_of_the_week_array[index]
    new_time = new_time + ", " + new_day

  if(number_days == 1):
    new_time = new_time + " " + "(next day)"
  elif (number_days > 1):
    new_time = new_time + " (" + str(number_days) + " days later)"

  return new_time
