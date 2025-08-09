while True:
    speed = float (input ("Enter speed (meters/seconds):"))
    time = float (input("Enter time (seconds):"))
    distance = speed * time
    print(f"The distance traveld = {distance} meters")
    again = input("Do you want to calculate again? (yes/no):").lower()
    if again !="yes":
      break