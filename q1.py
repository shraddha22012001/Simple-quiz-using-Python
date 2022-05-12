class Question:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
      "1) Who developed Python programming language\n",
      "2) Is Python case sensitive when dealing with identifiers\n",
      "3) What is the extenstion of python file\n",
      "4) What will be the value of the following python expression\n  4 + 3 % 5 \n",
      "5) Which keyword is used for function in Python language\n"

]
questions = [
    Question(question_prompts[0],"guido van rossum"),
    Question(question_prompts[1],"no"),
    Question(question_prompts[2],".py"),
    Question(question_prompts[3],"7"),
    Question(question_prompts[4],"def")
    
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if (answer.lower()).strip() == question.answer:
            score +=1
    print("\n\nYou got " + str(score) + " score out of 5")

run_quiz(questions)
