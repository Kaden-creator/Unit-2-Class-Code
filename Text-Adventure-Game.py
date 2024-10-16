title = r"""
 _____ _            _____ _             _            _     _     _  __     
|_   _| |          /  ___| |           | |          | |   | |   (_)/ _|    
  | | | |__   ___  \ `--.| |_ _   _  __| | ___ _ __ | |_  | |    _| |_ ___ 
  | | | '_ \ / _ \  `--. | __| | | |/ _` |/ _ | '_ \| __| | |   | |  _/ _ \
  | | | | | |  __/ /\__/ | |_| |_| | (_| |  __| | | | |_  | |___| | ||  __/
  \_/ |_| |_|\___| \____/ \__|\__,_|\__,_|\___|_| |_|\__| \_____|_|_| \___|                                                                                                                                              
"""
print(title)

print("BEEP BEEP BEEP BEEP, you slowly open your eyes to see the alarm going off")
print(f"1. Go back to sleep\n2. Get up")
choice_one = int(input("> "))
if choice_one == 1:
    print("You turn off your alarm and fall back to sleep and dream about sheeps? That's a weird dream.")
elif choice_one == 2:
    print("You turn off your alarm and get out off bed.")
else: 
    print("You split in half, one side gets up and the other one stays in bed. YOU DIED!! ")