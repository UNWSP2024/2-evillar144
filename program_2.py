def average_age():
    # Get User Input
    age1 = float(input("What is the age of friend 1: "))
    age2 = float(input("What is the age of friend 2: "))
    age3 = float(input("What is the age of friend 3: "))
    age4 = float(input("What is the age of friend 4: "))
    age5 = float(input("What is the age of friend 5: "))
    # Sum ages
    sum_of_ages = (age1 + age2+ age3+ age4+ age5)
    # Average the ages
    avg_of_ages = sum_of_ages/5
    # Print the results
    print(avg_of_ages)
# Line which calls the above function.
average_age()
