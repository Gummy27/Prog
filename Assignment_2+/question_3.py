temp_now = int(input("Current temperature (C°): "))
temp_prev = int(input("Previous temperature (C°): "))

RAISE = "raise"
KEEP = "keep"
LOWER = "lower"
SHUTDOWN = "shutdown"

# ... implement control logic and print the appropriate action

if(temp_now >= 350):
    print(SHUTDOWN)
elif(temp_now < 300 and temp_now <= temp_prev):
    print(RAISE)
elif(temp_now < 300 and temp_now > temp_prev):
    print(KEEP)
elif(temp_now == 300):
    print(KEEP)
elif(temp_now > 300 and temp_now >= temp_prev):
    print(LOWER)
elif(temp_now > 300 and temp_now < temp_prev):
    print(KEEP)
