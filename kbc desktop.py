from tkinter import*
root=Tk()
root.title("my first window")
x=Label(root,text=" welcome to kon banega cororpati",bg="white",fg="black",font=("ariel",17))
x.pack()
label=Label(root,text="[1]. navgurukul me ham kya sikhte hai ",bg="black",fg="white",font=("ariel",13))
label.pack()
root.geometry("500x600+600+300")
root.resizable(0,0)
myButton1=Button(root,text="(A)    SOFTWARE ENGINEYERING " ,bg="orange",padx=10,font=("ariel",10))
myButton2=Button(root,text="(B)    GRAPIC SIKAI JATI HAI ",bg="orange",padx=10,font=("ariel",10))
myButton3=Button(root,text="(C)    MODLING SIKAI JATI HAI",bg="orange",padx=10,font=("ariel",10))
myButton4=Button(root,text="(D)    DANCE SIKAYA JATA HAI ",bg="orange",padx=10,font=("ariel",10))
myButton1.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()
root.mainloop()



# from tkinter import Tk, Frame, Label, Button
# from time import sleep

# class Question:
#     def _init_(self, question, answers, correctLetter):
#         self.question = question
#         self.answers = answers
#         self.correctLetter = correctLetter

#     def check(self, letter, view):
#         global right
#         if(letter == self.correctLetter):
#             label = Label(view, text="Right!")
#             right += 1
#         else:
#             label = Label(view, text="Wrong!")
#         label.pack()
#         view.after(1000, lambda *args: self.unpackView(view))


#     def getView(self, window):
#         view = Frame(window)
#         Label(view, text=self.question).pack()
#         Button(view, text=self.answers[0], command=lambda *args: self.check("1", view)).pack()
#         Button(view, text=self.answers[1], command=lambda *args: self.check("2", view)).pack()
#         Button(view, text=self.answers[2], command=lambda *args: self.check("3", view)).pack()
#         Button(view, text=self.answers[3], command=lambda *args: self.check("4", view)).pack()
#         return view

#     def unpackView(self, view):
#         view.pack_forget()
#         askQuestion()

# def askQuestion():
#     global questions, window, index, button, right, number_of_questions 
#     if(len(questions) == index + 1):
#         Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
#         return
#     button.pack_forget()
#     index += 1
#     questions[index].getView(window).pack()

# questions = []
# file = open("questions.txt", "r")
# line = file.readline()
# while(line != ""):
#     questionString = line
#     answers = []
#     for i in range (4):
#         answers.append(file.readline())

#     correctLetter = file.readline()
#     correctLetter = correctLetter[:-1]
#     questions.append(Question(questionString, answers, correctLetter))
#     line = file.readline()
# file.close()
# index = -1
# right = 0
# number_of_questions = len(questions)

# window = Tk()
# button = Button(window, text="Start", command=askQuestion)
# button.pack()
# from tkinter import *
# from random import randint
# img=PhotoImage(file="/home/jayshri/Downloads/jayshri.png")
# image_list=[img]
# pick_number=randint(0,0)
# image_label=Label(image=image_list[pick_number])
# image_label.pack(pady=50)
# window.mainloop()