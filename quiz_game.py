print("Welcome to my general knowledge quiz game!")

playing = input("Do you want to play? (yes/no) ").lower() 
print("You will be asked 5 questions. For each question, type your answer and press enter.")

if playing != "yes":
    quit()
    
print("Okay! Let's play!")
score = 0 

answer = input("What is the 4th letter of the Greek Alphabet? ").lower()
if answer == "delta":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


answer = input("What is the smallest unit of matter? ").lower()
if answer == "atom":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    

answer = input("What is acrophobia the fear of? ").lower()
if answer == "heights":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What is the scientific theory that explains the origin of the universe? ").lower()
if answer == "the big bang theory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


print("You got " + str(score) + " questions correct!!")
print("That will be " + str((score / 5) * 100) + "%") 
print("Thanks for playing!")