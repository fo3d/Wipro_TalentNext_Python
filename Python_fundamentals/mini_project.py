# Travel Recommendation Mini Project

def travel_advisor(distance):
    if distance < 3:
        return "Bicycle"
    elif distance < 300:
        return "Motor-cycle"
    else:
        return "Super-Car"

distance = int(input("How far would you like to travel in miles? "))
print(f"I suggest {travel_advisor(distance)} to your destination.")
