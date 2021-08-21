secs_str = input("Input seconds: ") # do not change this line
hours = int(secs_str) // (60*60)

secs_str = int(secs_str) % (60*60)

minutes = int(secs_str) // 60

secs_str = int(secs_str) % 60

seconds = int(secs_str)

print(hours,":",minutes,":",seconds) # do not change this line