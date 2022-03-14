def new_game():
    """This sets up the trivia game to test your knowledge on all things Harry Styles
    
    PARAMETERS
    ------------------------
    none
   
    RETURNS
    ------------------------
    none
    """
    
   
    guesses = []
    correct_guesses = 0
    questions_num = 1
    
    questions = {
     "What is Harry's Full name?:" : "C",
     "What is Harry's Birthday?:" : "B",
     "Which song was his first solo release to go number 1?:" : "A",
     "Which of these is one of his favorite movies of all time?:" : "D",
     "What was the name of the bakery where Harry worked?:" : "D",
     "Which tattoo did Harry get first?:" : "B",
     "Which musical artist was the first to hear his album Fine Line?:" : "A",
     "Who dressed Harry for the 2019 Met Gala?:" : "D",
    }
    
    options = [["A. Harold Edward Styles", "B. Harry Ethan Styles", "C. Harry Edward Styles", "D. Harold   Emmett Styles"],
          ["A. January 31st 1994", "B. February 1st 1994", "C. December 15th 1995", "C. June 4th 1999"], 
          ["A. Sign of the Times", "B. Adore You", "C. Golden", "D. Fine Line"],
          ["A. Love Actually", "B. Dunkirk", "C. 10 Thing I Hate About You", "D. The Notebook"],
          ["A. Mongolia Bakery", "B. Magnolia Bakery", "C. Elizabeths Bakery", "D. W Mandeville Bakery"],
          ["A. Butterfly on his stomach", "B. A star on his left arm", "C. A ship on his left arm", "D. Tiger on his thigh"],
          ["A. Stevie Nicks", "B. Dolly Parton", "C. Cher", "D. Elton John"],
          ["A. Versace", "B. Givenchy", "C. Prada", "D. Gucci"]]

#loop all options, so when you put in a,b,c,d it will make result it as uppercase
    for key in questions:
        print(key)
        for i in options [questions_num-1]:
            print(i)
        guess = input ("Enter (A,B,C,D):")
        guess = guess.upper()
        guesses.append(guess)
        
#so when you put in your answer (a,b,c, or d) on the bottom it will say your score so it will say like 7/8 questions right        
        correct_guesses += check_answer(questions.get(key),guess)
        print (str(correct_guesses)+"/"+str(questions_num))
        questions_num += 1
        print ("--------------------------------------------------")
      
    questions_num -= 1
    display_score(correct_guesses, guesses, questions_num)
#--------------------------------------------------
def check_answer(answer,guess):
    """This checks your answer, if you get the answer correct it will say correct
    and gives you 1 point, if you get the question wrong it will say wrong.
    
    PARAMETERS
    --------------------
    answer: str
        it tells you if you got the answer wrong and tells you if you get 1 point
    guess: str
        guess is you putting in a,b,c,d
    
    RETURNS
    --------------------
    1,0: int
        if you get the question right it will give you 1 point, if you get the question 
        wrong it will give you 0 points
    """
      
    
#if your guess is correct it will print your correct and give you 1 point and it will say how many questions you have right so far. if you get it wrong it will print wrong and you wont get a point    
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print ("WRONG")
        return 0
#---------------------------------------
def display_score(correct_guesses,guesses, questions_num):
    """This functions shows your score, it shows your final score, so if you get a 
       7/8 it will say 7/8 and give you your %
    
    PARAMETERS
    ---------------------
    correct_guesses: int
        
    guesses: list
        
    questions_num: int
        
    
    RETURNS
    ---------------------
    none
    """
    
    print("RESULTS")
    
   # print("Answers:", end=" ")
   # for i in questions:
        #print(quesions.get(i), end=" ")
    #print()
    
    #print("Guesses:", end=" ")
    #for i in guesses:
       # print(i, end=" ")
    print (str(correct_guesses)+"/"+str(questions_num))
    score = int((correct_guesses/8)*100)
    print("Your score is: "+str(score)+"%")
#---------------------------------------
def play_again():
    """This function asks if you would like to play the trivia game again
    
    PARAMETERS
    -----------------------
    None
    
    RETURNS
    -----------------------
    True, False: boolean
        if you want to play again it will return True, if not it will return False
    """
    
    response = input("Would you like to play again?: (yes or no):")
    response = response.upper()
    
    if response == "YES":
        return True 
    
    else:
        return False
#----------------------------------------------
