""" Awkward Silence Reliever 3000 """

import random, os, sys, json

def run(command):
    os.system(command)
    
def clear():
    run("clear")
    
def say(speech):
    run("say {}".format(speech))
    
def fetch_file(path):
    with open("data/"+path, "r") as f:
        return f.read()
        
def random_question(text):
    return random.choice(text.split("\n"))
        
# =============== 
        
CONVERSATION_STARTERS = fetch_file("conversation_starters.txt")
DEEP_TOPICS = fetch_file("deep_topics.txt")
FUNNY_QUESTIONS = fetch_file("funny_questions.txt")
GOOD_QUESTIONS = fetch_file("good_questions.txt")
WOULD_YOU_RATHER = fetch_file("would_you_rather.txt")

REAL_NEWS = fetch_file("real_news.txt").split("\n#-#-#")
FAKE_NEWS = fetch_file("fake_news.txt").split("\n#-#-#")

GENERAL_QUIZ = fetch_file("general_quiz.txt")

# ===============

if __name__ == "__main__":
    while True:
        clear()
        print("                  _                          _    _____ _ _                       _____      _ _                       ____   ___   ___   ___  \n     /\          | |                        | |  / ____(_) |                     |  __ \    | (_)                     |___ \ / _ \ / _ \ / _ \ \n    /  \__      _| | ___      ____ _ _ __ __| | | (___  _| | ___ _ __   ___ ___  | |__) |___| |_  _____   _____ _ __    __) | | | | | | | | | |\n   / /\ \ \ /\ / / |/ | \ /\ / / _` | '__/ _` |  \___ \| | |/ _ \ '_ \ / __/ _ \ |  _  // _ \ | |/ _ \ \ / / _ \ '__|  |__ <| | | | | | | | | |\n  / ____ \ V  V /|   < \ V  V / (_| | | | (_| |  ____) | | |  __/ | | | (_|  __/ | | \ \  __/ | |  __/\ V /  __/ |     ___) | |_| | |_| | |_| |\n /_/    \_\_/\_/ |_|\_\ \_/\_/ \__,_|_|  \__,_| |_____/|_|_|\___|_| |_|\___\___| |_|  \_\___|_|_|\___| \_/ \___|_|    |____/ \___/ \___/ \___/ ")
        print("\nWelcome to Awkward Silence Reliever 3000 - the thing that relieves awkard silence (obviosuly).")
        print("There are a few options when it comes to the Awkward Silence Reliever 3000:\n")

        print("\tQuestion Types:")
        print("\t1) Conversation Starters - Some questions that spark a conversation.")
        print("\t2) Good Questions - Casual questions, aka just a bit of 'caj convo'.")
        print("\t3) Deep Topics - Questions about life, death and the inevitable death of the human race as we know it.")
        print("\t4) Funny Questions - Questions that are supposed to be funny.")
        print("\t5) Would You Rather - Scenarios where you have to choose one thing or the other.\n")

        print("\tQuizzes:")
        print("\t6) General Quiz - A quiz with varied categories and topics.")
        print("\t7) Fake News Quiz - Guess which news is fake and which news is real.")
        print("")

        while True:
            try:
                choice = int(input("Please input the option you would like: "))
                
            except ValueError:
                print("\nI'm afraid you can't do that.")
                continue
                
            except KeyboardInterrupt:
                print("\nOk, quiting...")
                clear()
                sys.exit()
            
            if choice < 1 or choice > 7:
                print("\nI'm afraid you can't do that.")
                continue
                
            break
        
        if choice >= 1 and choice <= 5:
            clear()
            
            choices = ["Conversation Starters", "Good Questions", "Deep Topics", "Funny Questions", "Would You Rather"]
            variable_choices = [CONVERSATION_STARTERS, GOOD_QUESTIONS, DEEP_TOPICS, FUNNY_QUESTIONS, WOULD_YOU_RATHER]
            
            chosen = choices[choice - 1]
            subject = variable_choices[choice - 1]
            
            print("You have selected: {}".format(chosen))
            amount = input("How many questions would you like? (default 1) ")
            
            if amount == "":
                amount = 1
                
            else:
                amount = int(amount)
            
            while True:
                clear()
                print("Ok, printing {} random '{}' {}:".format(amount, chosen, "question" if amount == 1 else "questions"))
                
                print("\n")
                
                random_questions = []
                
                for i in range(amount):
                    current = random_question(subject)
                    print("\t{}) {}".format(str(i+1), current))
                    
                    random_questions.append(current)
                    
                print("\n")
                
                options = input("Press enter for another, or type 'exit' to quit: ")
                
                if options == "exit" or options == "quit" or options == "q" or options == "e":
                    break
                    
                else:
                    continue
            
            
        elif choice == 6:
            # Genral Quiz
            clear()
            quiz_data = GENERAL_QUIZ.split("\n\n")
            
            print("You have selected: General Quiz")
            print("Due to the DANK programming, there may be errors and some repeat questions.")
            print("This quiz has a variety of question types, stretching from 'Chemistry' to 'Movie Trivia'. This is an example question:")
            print("\n" + random.choice(quiz_data))
            
            print("")
            
            try:
                choice = input("Press enter to continue: ")
                
            except KeyboardInterrupt:
                print("\nOk, quiting...")
                clear()
                sys.exit()
                
                
            question_count = 0
            
            wrong_count = 0
            correct_count = 0
                
            while True:
                question_count += 1
                clear()
                print("QUESTION {}: General Quiz - {}/{} correct so far, or {}% correct.".format(question_count, correct_count, question_count - 1, round(( (correct_count/(question_count - 1))*100 ) * 100)/100 if (question_count - 1) != 0 else 0.0 ))
                print("\n")
                
                current = random.choice(quiz_data).split("\n")
                
                category = current[0].replace("Category: ", "")
                question = current[1].replace("Question: ", "")
                answer = current[2].replace("Answer: ", "")
                
                print("\tCategory: {}".format(category))
                print("\tQuestion: {}".format(question))
                
                print("\n")
                
                input("Press enter to reveal the answer. ")
                
                print("\n\tAnswer: {}".format(answer))
                
                print("")
                
                while True:
                    try:
                        correct = input("Did you get it right? [y, n]: ")
                        
                    except KeyboardInterrupt:
                        print("\nOk, quiting...")
                        clear()
                        sys.exit()
                        
                    except:
                        print("There was an error with your response.")
                
                    if correct == "y" or correct == "yes" or correct == "1" or correct == "true":
                        correct_count += 1
                        break
                    
                    elif correct == "n" or correct == "no" or correct == "0" or correct == "false":
                        wrong_count += 1
                        break
                        
                    else:
                        print("There was an error with your response.")
                        
                print("\nY")
                        
        
        elif choice == 7:
            clear()
            print("You have selected: Fake News Quiz")
            print("In this quiz, you'll be shown either a fake news article or a real news article, which are both from BuzzFeed. You then need to guess whether it is fake or true. Simple!")
                    
            print("")
            
            try:
                choice = input("Press enter to continue: ")
                
            except KeyboardInterrupt:
                print("\nOk, quiting...")
                clear()
                sys.exit()
                
            question_count = 0
            
            wrong_count = 0
            correct_count = 0
                    
            while True:
                question_count += 1
                clear()
                print("QUESTION {}: General Quiz - {}/{} correct so far, or {}% correct.".format(question_count, correct_count, question_count - 1, round(( (correct_count/(question_count - 1))*100 ) * 100)/100 if (question_count - 1) != 0 else 0.0 ))
                print("\n")
                
                decider = random.randint(0, 1)
                answer = ""
                    
                while True:
                    try:
                        if decider == 0:
                            # News is real
                            news = json.loads(random.choice(REAL_NEWS))
                            answer = "real"
                            
                        else:
                            # News is fake
                            news = json.loads(random.choice(FAKE_NEWS))
                            answer = "fake"
                        
                        headline = news["meta_data"]["og"]["title"]
                        article = news["text"]
                        
                        seperator = "-" * (len(news["meta_data"]["og"]["title"]) + len("HEADLINE: "))
                        
                    except:
                        continue
                        
                    finally:
                        break
                    
                print("HEADLINE: {}".format(headline))
                print("")
                print(seperator)
                print("")
                print("ARTICLE: {}".format(article))
                print("")
                print(seperator)
                print("")
                
                try:
                    correct = input("So what do you think? Is this fake news or real? [fake, real, error]: ")
                    
                except KeyboardInterrupt:
                    print("\nOk, quiting...")
                    clear()
                    sys.exit()
                    
                except:
                    print("There was an error with your response.")
                    
                if correct == "quit" or correct == "exit" or correct == "q" or correct == "e":
                    break
                    
                
                if answer == "real":
                    if correct == "real" or correct == "r" or correct == "true" or correct == "1":
                        correct_count += 1
                        input("Well done, you got it right!")
                    
                    elif correct == "fake" or correct == "f" or correct == "fale" or correct == "0":
                        wrong_count += 1
                        input("You got it wrong. This is real!")
                        
                    elif correct == "error":
                        question_count -= 1
                        input("Oh. I'm sorry about that. However, it wasn't my fault, it was the website's. Don't blame me. Please.")
                        
                    else:
                        print("There was an error with your response.")
                        
                if answer == "fake":
                    if correct == "real" or correct == "r" or correct == "true" or correct == "1":
                        wrong_count += 1
                        input("Unfortunately, this is FAAKEEE NEEEEEWWWWS.")
                    
                    elif correct == "fake" or correct == "f" or correct == "fale" or correct == "0":
                        correct_count += 1
                        input("Well done, this is indeed fake.")
                        
                    elif correct == "error":
                        question_count -= 1
                        input("Oh. I'm sorry about that. However, it wasn't my fault, it was the website's. Don't blame me. Please.")
                        
                    else:
                        print("There was an error with your response.")
                    


