#THE ULTIMATE MENU DRIVEN TASK MANAGER .
#GOAL:  Modify your task manager so that instead of automatically prompting to add a task , the user is presented with a numbered 
#menu of choices . they can choose to view task ,add a task ,complete (remove) a task or exit the program .

#STEP 1 set up your to do list .
to_do = ["clean rooom","learn pythom","read boook "]
menu = ["view tasks ","add a task","complete a task ","Exit"]#set up menu (a list of functions /options available in program.)
print("="*40)#indexing the list using enumerte.
for index,task in enumerate(to_do,start=1):
         print(f"{index}.{task}")
# step2 set up the while loop to keep the loop going till the user wants to exit the program .
while True:
    #print the to do list  so the user know what are the tasks that are allready mentioned in the list .
#step 3 print the available optons available for the user to choose from .
    print("="*40)
    print("this program have 4 functions listed below ")
    print("="*40)
    for index,task in enumerate(menu,start=1):
         print(f"{index}.{task}")
      #step 4 take the input from the user aboout the function they would like to acess .
    task = int(input("choose a number from (1-4) or enter '00' to 'EXIT':")) 
    if task == 1:# if the user enters "1" they get to se their to_do list as 1 function is listed as "view".
            print("your total tasks are :",to_do)
    elif task == 2 :#if the user enters 2 they get to add another task to the list and for that the program asks for the input .
           add_task = input("enter the task you'd like to add :")
           to_do.append(add_task)# after taking the input from the user we append (add) that input into the todo list .
           print("your updated list is :",to_do)
    elif task == 3:
           completed = int(input("enter the number of task you have completed :"))
           python_index = completed -1# as the python indexing starts from 0 we need to adjust the input ac to the python index .
           to_do.pop(python_index) # as per the function no 3 remove the completed task from the list .
           print("your updated list is :", to_do)
    elif task== 00:# as we are allowing the user to add any number of tasks we have to give a unique no for the exit command .
           print("you have chossen to 'EXIT' ,\n GOODBYE")
           break
    else:# if the user enters an invalid ans ask for a valid number .
            print("invalid choice please choose a valid number ") 

# step 5 print the final list after every changes have been made by the user.
print("="*40)
print("your final list is :",to_do)
print("="*40)                        
         