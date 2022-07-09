print("Welcome to my Quiz game!")
playing = input("Do you want to play ? ")
if playing.lower() != "yes":
     quit()
print("Okay! Let's play :) ")
score = 0
answer = input("What is the capital of India ? ")
if answer.title() == "New Delhi":
    print("Correct!")
    score = score + 10
else:
    print("Incorrect!")

answer = input(" Who is the Father of our Nation ? ")
if answer.title() == "Mahatma Gandhi":
    print("Correct!")
    score = score + 10
else:
    print("Incorrect!")

answer = input("Which is the most sensitive organ in our body ? ")
if answer.title() == "Skin":
    print("Correct!")
    score = score + 10
else:
    print("Incorrect!")

answer = input("Which is the heavier metal of these two ? Gold or Silver ? ")
if answer.title() == "Gold":
    print("Correct!")
    score = score + 10
else:
    print("Incorrect!")

answer = input(" What city is the statue of liberty in ? ")
if answer.title() == "New York":
    print("Correct!")
    score = score + 10
else:
    print("Incorrect!")
print("Total score = ", score)
