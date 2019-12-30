# Importing required dependencies and requirements
import json
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
            addGrade()
        elif userInp == '4':
            changeGrade()
        elif userInp == '5':
            curGrade()
        elif userInp == '6':
            saveData()
            # endFlag = True;

def createCourse():
    newCourse = course()
    newCourse.coursename = str(input("What's the name of this course? "))
    courseList[newCourse.coursename] = newCourse

def addAsgnType():
    coursename = str(input("What's the course you want to add an assignment type to? "))
    if coursename in courseList:
        courseList[coursename].addAssignType(str(input("What is the assignment type?")))
    else:
        print("ERROR: The course you entered does not exist")

def addGrade():
    coursename = str(input("What's the course you want to add a grade into? "))

    if coursename in courseList:
        courseList[coursename].insertGrade(str(input("Assignment type for inserting grade: ")))
    else:
        print("ERROR: The course you entered does not exist")

def changeGrade():
    coursename = str(input("What's the course you want to change a grade? "))

    if coursename in courseList:
        courseList[coursename].changeGrade()
    else:
        print("ERROR: The course you entered does not exist")

# TODO: Add algorithm to calculate grades
# Temp: Print out all the data stored in courseList
def curGrade():
    print(courseList)

    for item in courseList:
        print(courseList[item].coursename)
        for asgnType in courseList[item].assignDict:
            print(courseList[item].assignDict[asgnType].type)
            print(courseList[item].assignDict[asgnType].gradeList)
            print(courseList[item].assignDict[asgnType].gradeWeights)
        print('\n')

def saveData():
    saveCourses = {}

    for item in courseList:
        saveCourses[item] = {}
        saveCourses[item]['coursename'] = courseList[item].coursename
        saveCourses[item]['dynamFinal'] = courseList[item].dynamFinal
        saveCourses[item]['assignDict'] = {}
        for asgnType in courseList[item].assignDict:
            saveCourses[item]['assignDict'][asgnType] = {}
            saveCourses[item]['assignDict'][asgnType]['type'] = courseList[item].assignDict[asgnType].type
            saveCourses[item]['assignDict'][asgnType]['numAssigns'] = courseList[item].assignDict[asgnType].numAssigns
            saveCourses[item]['assignDict'][asgnType]['finalExamGrade'] = courseList[item].assignDict[asgnType].finalExamGrade
            saveCourses[item]['assignDict'][asgnType]['gradeList'] = courseList[item].assignDict[asgnType].gradeList
            saveCourses[item]['assignDict'][asgnType]['tempGradeList'] = courseList[item].assignDict[asgnType].tempGradeList
            saveCourses[item]['assignDict'][asgnType]['dynamic'] = courseList[item].assignDict[asgnType].dynamic
            saveCourses[item]['assignDict'][asgnType]['gradeWeights'] = courseList[item].assignDict[asgnType].gradeWeights
            saveCourses[item]['assignDict'][asgnType]['staggered'] = courseList[item].assignDict[asgnType].staggered
            saveCourses[item]['assignDict'][asgnType]['evenDist'] = courseList[item].assignDict[asgnType].evenDist
            saveCourses[item]['assignDict'][asgnType]['dynamFinal'] = courseList[item].assignDict[asgnType].dynamFinal

    with open('data.json', 'w') as file:
        json.dump(saveCourses, file)


# **TODO** FINISH OFF THE LOADING FROM THE JSON ************

def loadData():
    file = open('data.json')
    savedCourses = json.load(file)
    for item in savedCourses:
        loadCourse(savedCourses[item].coursename, savedCourses[item].dynamFinal)
        for asgnType in savedCourses[item].assignDict:
            loadAsgnType(savedCourses[item].coursename, savedCourses[item][asgnType].type)
            loadGrade(savedCourses[item].coursename, savedCourses[item][asgnType].type)


def loadCourse(coursename, dynamFinal):
    newCourse = course()
    newCourse.coursename = str(coursename)
    courseList[newCourse.coursename] = newCourse
    courseList[newCourse.coursename].dynamFinal = dynamFinal


# **TODO** Load in the variables for assignment
def loadAsgnType(coursename, asgnType):
    if coursename in courseList:
        courseList[coursename].addAssignType(asgnType)
        # courseList[coursename].
    else:
        print("ERROR: The course you entered does not exist")

# **TODO** Load in the grades from the arrays
def loadGrade(coursename, grade):
    if coursename in courseList:
        courseList[coursename].insertGrade(grade)
    else:
        print("ERROR: The course you entered does not exist")



if __name__ == '__main__':
    mainMenu()
