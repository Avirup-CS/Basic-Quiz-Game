import sys

class quizGame:

    def __init__(self,questionList):
        self.questionList = questionList
        self.marks = 0
        self.correct_ans = 0
        self.wrong_ans = 0

    def startQuiz(self):
        print(f'''======================================================\nRules of the Quiz:\na) Total number of questions: {len(questionList)}\nb) Full Marks: {len(questionList)*2}\nc) Each question carries 2 marks for a correct answer\nd) 1 mark will be deducted for a wrong answer\ne) Go ahead and all the best!\n======================================================''')
        
        name = input("Enter Your Name: ")
        print("\nLet's Start the Quiz . . . ")
        print("======================================================") 

        qno = 0 #
        for questions in self.questionList:
            # qno = questions[0]
            qno += 1  #
            print(f"\nQ{qno}. {questions[1]}")
            optno = 1
            for question in questions[2:6]:
                print(f"{optno}) ",end='')
                print(question)
                optno += 1
            
            while(True):
                try:
                    choice = int(input("Ans: "))
                    if choice in [1,2,3,4]:
                        break
                    else:
                        print("Option is not present!! Enter a suitable option number (1-4).")
                except ValueError:
                    print("Problem: Invalid input!! Please enter a option number between 1 and 4.")
            

            if(choice == questions[6]):
                self.marks += 2
                self.correct_ans += 1
                print("Remarks: Correct!!")
            else:
                self.marks -= 1
                self.wrong_ans += 1
                print("Remarks: Wrong!!")

            print(f"Correct Answer: {questions[questions[6]+1]}")


        print("\n======================================================")    
        print("Status: Exam is Completed...")
        print("Result:")
        print(f"Name of the User: {name}")
        print(f"Total marks obtained: {self.marks}")
        print(f"Total no. of correct answers: {self.correct_ans}")
        print(f"Total no. of wrong answers: {self.wrong_ans}")
        print("======================================================\n")


questionList = [[1, "Who developed Python Programming Language?","Wick van Rossum","Rasmus Lerdorf","Guido van Rossum","Niene Stom",3],
                
                [2, "Which type of Programming does Python support?","object-oriented programming","structured programming","functional programming","all of the mentioned",4],

                [3, "Which of the following is the correct extension of the Python file?",".python",".pl",".py",".p",3],

                [4, "All keywords in Python are in _________.","Capitalized","lower case","UPPER CASE","None of the mentioned",4],

                [5, "Which keyword is used for function in Python language?","Function","def","Fun","Define",2]]



while(True):
    
    def display_menu():
        print("Welcome to the Quiz Game!")
        print("======================================================")
        print("1. Admin Mode")
        print("2. User Mode")
        print("3. Exit the Game")
        print("======================================================")
        
        choice = input("Enter Your Choice: ")
        return choice


    user_choice = display_menu()

    match user_choice:
        case '1':
            print("\nWelcome to the Admin Mode. . . ")
            while(True):
                print("======================================================")     
                print("1. Modify Question Statement\n2. Modify Question Option\n3. Modify Correct Answer\n4. Delete Question\n5. Display All Questions\n6. Exit")
                print("======================================================")
                try: 
                    inp = int(input("Enter Your Choice: "))
                except ValueError:
                    print("Problem: Invalid input!! Please enter a number between 1 and 6.")
                    continue

                print("\n======================================================") 

                match inp:
                    case 1:
                        qno = int(input("Enter the Question No.: "))
                        updateQuestion = input("Enter the new Question Statement: ")
                        questionList[qno-1][1] = updateQuestion
                        print(f"Status: Question-{qno} is updated successfully. . .")

                    case 2:
                        qno = int(input("Enter the Question No.: "))
                        optno = int(input("Enter the Option no.: "))
                        updateOption = input("Enter the new Option: ")
                        questionList[qno-1][optno+1] = updateOption
                        print(f"Status: Question-{qno} is updated successfully. . .")

                    case 3:
                        qno = int(input("Enter the Question No.: "))
                        updateAnswerNo = int(input("Enter the new Answer no.: "))
                        questionList[qno-1][6] = updateAnswerNo
                        print(f"Status: Question-{qno} is updated successfully. . .")

                    case 4:
                        qno = int(input("Enter the Question No.: "))
                        questionList.pop(qno-1)
                        print(f"Status: Question-{qno} is deleted successfully. . .")

                    case 5:
                        for i, question in enumerate(questionList,start=1):
                            print(f"Q{i}. {question[1]}")
                            print(f"1) {question[2]}\n2) {question[3]}\n3) {question[4]}\n4) {question[5]}\nAnswer: {question[question[6]+1]}\n")
                    case 6:
                        break

                    case _:
                        print("Invalid choice!! Please enter a number between 1 and 6.\n")

        case '2':
            quiz = quizGame(questionList)
            quiz.startQuiz()

        case '3':
            sys.exit()

        case _:
             print("Invalid choice!! Please enter a number between 1 and 3.\n")




    



