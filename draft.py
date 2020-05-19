import time

named_tuple = time.localtime()
time_string = time.strftime("%d/%m/%Y", named_tuple)


print(time_string)