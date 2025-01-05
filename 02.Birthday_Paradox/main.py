from datetime import date
from random import randint

def generate_birthdays(num_birthdays):
    # Replacing year = 4 to capture leap days and to be able to match birthdays without 
    # worrying about years 
    return [date.fromordinal(randint(1, date.max.toordinal())).replace(year=4) for _ in range(num_birthdays)]

def matching_birthday(birthdays):
    unique_bdays = set()
    for bday in birthdays:
        if bday in unique_bdays: return bday
        unique_bdays.add(bday)
    return None

if __name__ == '__main__':
    num_trials = 100000

    # Assuming correct input from user
    num_birthdays = int(input("How many birthdays shall I generate?\n> "))
    birthdays = generate_birthdays(num_birthdays)

    print()
    print("Here are 23 birthdays:")
    print(", ".join( [f'{bday.strftime("%B")[:3]} {bday.strftime("%d")}' for bday in birthdays] ))
    matching = matching_birthday(birthdays)
    if matching:
        print(f'In this simulation, multiple people have a birthday on {matching.strftime("%B")[:3]} {matching.strftime("%d")}')
    else:
        print("In this simulation, there are no matching birthdays")

    print(f"Generating {num_birthdays} birthdays {num_trials} times...")
    print("Press Enter to begin...")

    print("0 simulations run...")
    matching_trials = 0
    for trial in range(num_trials):
        if matching_birthday(generate_birthdays(num_birthdays)):
            matching_trials += 1
        if (trial+1) % (num_trials // 10) == 0:
            print(f"{trial+1} simulations run...")

    print(f"""Out of {num_trials} of {num_birthdays} people, there was a
    matching birthday in tha group {matching_trials} times. This means
    that {num_birthdays} people have a {matching_trials*100/num_trials:0.2f}% chance of
    having a matching birthday in their group.
    That's probably more than you would think!""")

        
