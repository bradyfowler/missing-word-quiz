# missing word game
# 20/05/2020
# brady fowler

score = 0
x = 0
words = [('<integer>', '_______'), ('<float>', '_____'), ('<string>', '______'), ('<debugger>', '________'), ('<shell>', '_____')]

print("Welcome to the missing word game")
print("Please enter the missing words")

sentences = open("sentences.txt","r")

while True:
    for k, v in words:
        question = sentences.readline()
        question = question.replace(k, v)
        answer = input(question).lower()
        if answer in k:
            print("Correct")
            score = score + 1
        else:
            print("Wrong")
            print("The answer is ", k)
    x = x + 1    
    if x >= 5:
        break

print(score)    
