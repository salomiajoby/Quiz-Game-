print("Welcome to my computer quiz game!")

playing = input("Do you want to play? (yes/no) ").lower() 

if playing != "yes":
    quit()
    
print("Okay! Let's play!")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
else: 
    print("Incorrect!")