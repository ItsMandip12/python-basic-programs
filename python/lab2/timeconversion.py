
seconds_input = int(input("Enter seconds: "))


hours = seconds_input // 3600
minutes = (seconds_input % 3600) // 60
remaining_seconds = seconds_input % 60


print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remaining_seconds)
