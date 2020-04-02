class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        

question_prompts = [
    "Which player won 6 championships with the Chicago Bulls?\n(a) Michael Jordan\n(b) LeBron James\n(c) Jason Kidd\n(d) Carmelo Anthony\n\n",
    "What player had the famous quote 'anything is possible' after winning the NBA Finals?\n(a) Raymond Felton\n(b) Rajon Rondo\n(c) Kevin Garnett\n(d) Ray Allen\n\n",
    "In what year was Kristaps Porzingis drafted?\n(a) 2005\n(b) 2015\n(c) 2016\n(d) 1997\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def basketball_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    #print("you got " + str(score) + "out of " +str(len(questions)))
    print("you got ", score, "out of ",len(questions), "correct")    
        
basketball_test(questions)

if __name__ == "__main__":
    main