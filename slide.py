#to recommend a ride based on the user's age

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age!")
elif age <= 3:
    print("You're too young!")
elif age <= 10:
    print("Try the Carrousel!")
elif age <= 15:
    print("Try the Ride of Doom!")
elif age <= 18:
    print("Try the Cranium Shaker!")
else:
    print("Try the Not-So-Safe-Coaster  (adult content)!")

def age_recommend(f_age):
    if f_age < 0:
        print("Invalid age!")
    elif f_age <= 3:
        print("You're too young!")
    elif f_age <= 10:
        print("Try the Carrousel!")
    elif f_age <= 15:
        print("Try the Ride of Doom!")
    elif f_age <= 18:
        print("Try the Cranium Shaker!")
    else:
        print("Try the Not-So-Safe-Coaster  (adult content)!")

age_recommend(age)
'''
Enter your age: 16
Try the Cranium Shaker!
Try the Cranium Shaker!

Enter your age: 5
Try the Carrousel!
Try the Carrousel!
'''