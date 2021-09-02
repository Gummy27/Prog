mb_per_month = int(input("How much data (in Mb) do you get per month?: "))
n = int(input("How many months have you had this plan?: "))

result = 0
for x in range(n):
    mb_used = int(input("How much data did you use this month?: "))
    result += mb_per_month - mb_used

print(result+mb_per_month)
