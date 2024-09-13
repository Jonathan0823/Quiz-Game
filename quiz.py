import time

questions = ("What is the most used programming language in 2019?",
             "Who is the father of Python?",
             "What year was Python developed?",
             "Is the Earth round?",
             "What is the capital of India?",)

options = (("A. Java", "B. C", "C. Python", "D. C++"),
           ("A. Guido van Rossum", "B. Yukihiro Matsumoto", "C. Monty Python", "D. None of the above"),  
           ("A. 1989", "B. 1991", "C. 2000", "D. 2016"),
           ("A. True", "B. False", "C. None", "D. None of the above"),
           ("A. Delhi", "B. Mumbai", "C. Kanpur", "D. None of the above"))

answers = ("C",
            "A",
            "B",
            "A",
            "A")

guess = []
quistion_num = 0
score = 0

for question in questions:
    print("------------------------------")
    print(question)
    for option in options[quistion_num]:
        print(option)

    guess.append(input("Enter (A, B, C, or D): ").upper())
    if guess[quistion_num] == answers[quistion_num]:
        print("\nCorrect!")
        score += 1
    else:
        print("\nWrong!")
    print("Score: ", score)
    print()
    time.sleep(1)
    quistion_num += 1

print("------------------------------")
print("The final score is: ", score)