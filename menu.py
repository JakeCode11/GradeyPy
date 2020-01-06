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
            endFlag = True;
        elif userInp == 'L':
            loadData()
        elif userInp == 'P':
            printAllData()

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

# TODO: Add algorithm to calculate grades (based on dynamic, staggered, or evenDist)
# def curGrade():


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
            saveCourses[item]['assignDict'][asgnType]['ovrWeight'] = courseList[item].assignDict[asgnType].ovrWeight
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

def loadData():
    file = open('data.json')
    savedCourses = json.load(file)
    for item in savedCourses:
        loadCourse(savedCourses[item]['coursename'], savedCourses[item]['dynamFinal'])
        for asgnType in savedCourses[item]['assignDict']:
            loadAsgnType(savedCourses[item]['coursename'],
                        savedCourses[item]['assignDict'][asgnType]['type'],
                        savedCourses[item]['assignDict'][asgnType]['numAssigns'],
                        savedCourses[item]['assignDict'][asgnType]['ovrWeight'],
                        savedCourses[item]['assignDict'][asgnType]['finalExamGrade'],
                        savedCourses[item]['assignDict'][asgnType]['gradeList'],
                        savedCourses[item]['assignDict'][asgnType]['dynamic'],
                        savedCourses[item]['assignDict'][asgnType]['gradeWeights'],
                        savedCourses[item]['assignDict'][asgnType]['staggered'],
                        savedCourses[item]['assignDict'][asgnType]['evenDist'],
                        savedCourses[item]['assignDict'][asgnType]['dynamFinal'])

def loadCourse(coursename, dynamFinal):
    newCourse = course()
    newCourse.coursename = str(coursename)
    courseList[newCourse.coursename] = newCourse
    courseList[newCourse.coursename].dynamFinal = dynamFinal

def loadAsgnType(coursename, asgnType, numAssigns, ovrWeight, finalExamGrade,
                gradeList, dynamic, gradeWeights, staggered,
                evenDist, dynamFinal):
    courseList[coursename].loadAssignType(asgnType, numAssigns, ovrWeight, finalExamGrade,
                                        gradeList, dynamic, gradeWeights, staggered,
                                        evenDist, dynamFinal)

def printAllData():
    for item in courseList:
        print("Course name: " + str(courseList[item].coursename))
        print("Dynam Final: " + str(courseList[item].dynamFinal))
        print("Assign Dictionary: " + str(courseList[item].assignDict))
        for asgnType in courseList[item].assignDict:
            print("Type: "+ str(courseList[item].assignDict[asgnType].type))
            print("Num Assigns: " + str(courseList[item].assignDict[asgnType].numAssigns))
            print("Overall weight: "+ str(courseList[item].assignDict[asgnType].ovrWeight))
            print("Final Grade: "+ str(courseList[item].assignDict[asgnType].finalExamGrade))
            print("GradeList: "+ str(courseList[item].assignDict[asgnType].gradeList))
            print("tempGradeList: "+ str(courseList[item].assignDict[asgnType].tempGradeList))
            print("Dynamic: "+ str(courseList[item].assignDict[asgnType].dynamic))
            print("gradeWeights: "+ str(courseList[item].assignDict[asgnType].gradeWeights))
            print("Staggered: "+ str(courseList[item].assignDict[asgnType].staggered))
            print("Evendist: "+ str(courseList[item].assignDict[asgnType].evenDist))
            print("DynamFinal: "+ str(courseList[item].assignDict[asgnType].dynamFinal))
            print("\n")
        print("\n")

if __name__ == '__main__':
    mainMenu()
