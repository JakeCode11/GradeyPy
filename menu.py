# Importing required dependencies and requirements
from course import course


courseList = {}

def mainMenu():
    endFlag = False
    while endFlag == False:
        userInp = input(
'''
------ MENU -----
1. Create New Course
2. Add Assignment Type to Course
3. Insert Grade
4. Change Grade
5. Output Current Grade
6. Save and Exit Program

(Enter 1, 2, 3, or etc.) \n
''')

        if userInp == '1':
            createCourse()
        elif userInp == '2':
            addAsgnType()
        elif userInp == '3':
            insertGrade()
        elif userInp == '4':
            changeGrade()
        elif userInp == '5':
            curGrade()
        elif userInp == '6':
            endFlag = True;

def createCourse():
    newCourse = course()
    newCourse.coursename = str(input("What's the name of this course? "))
    courseList[newCourse.coursename] = newCourse

def addAsgnType():
    coursename = str(input("What's the course you want to add an assignment type to? "))
    courseList[coursename].addAssignType()

if __name__ == '__main__':
    mainMenu()
