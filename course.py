from assignment import assignment as asgn
# Course holds the information concerning one course
# i.e Calculus:
# - 6 Quizzes
# - 2 Exams
# - 1 Final

class course:
    # Defining course variables
    coursename = ''
    dynamFinal = False
    # Initializing assignDictionary to store different assignment types
    # Quizzes, class assignments,
    assignDict = {}

    def addAssignType(self):
        # Initializing new assignment object
        newAssign = asgn()

        # Prompting user for assignment type
        newAssign.type = input("What is the assignment type? ")

        if newAssign.type.lower() == 'final':
            self.dynamFinal = True if input("Does your final replace your lowest midterm grade? [y/n] ").lower() else False

        # Prompting user on information regarding assignment type; contingent on if it's a final
        # or not
        if newAssign.type.lower() != 'final':
            newAssign.numAssigns = int(input("How many of this type are there? "))

            # Prompting user about the grading weighting type
            # ****TODO: This will change when GUI is created****
            newAssign.setevenDist(input("Is this assignment type evenly distributed? [y/n] "))
            if newAssign.evenDist != True:
                newAssign.setDynamic(input("Is this assignment type dynamic? [y/n] "))
            if newAssign.evenDist != True and newAssign.dynamic != True:
                newAssign.setStagger(input("Is this assignement type staggered? [y/n] "))

            # Initalizing the Assignment type in the dictionary with its
            # respective assignement count
            self.assignDict[newAssign.type] = newAssign
            self.assignDict[newAssign.type].setGradeList()

            # Setting the gradeweights based on the grading type of the assignment
            if newAssign.evenDist == True:
                newAssign.ovrWeight = int(input("What's this assignment type's overall weight? "))/100.00
                self.assignDict[newAssign.type].setGradeWeights()
            elif newAssign.dynamic == True:
                self.assignDict[newAssign.type].setGradeWeights()
            elif newAssign.staggered == True:
                self.assignDict[newAssign.type].setGradeWeights()

        elif newAssign.type.lower() == 'final':
            # Adding final type to assign dictionary and initializing the overall weight
            self.assignDict[newAssign.type] = newAssign
            newAssign.ovrWeight = int(input("How much does the final weigh: "))/100.00

    # *TODO: Change for in menu to just take the input from the menu and not enter full assigntype*
    def insertGrade(self):
        assignType = input("Assignment type for inserting grade: ")
        self.assignDict[assignType].addGrade(int(input("What assignment number is this? ")))

    # *TODO: Change for in menu to just take the input from the menu and not enter full assigntype*
    def changeGrade(self):
        assignType = input("Assignment type for changing grade: ")
        self.assignDict[assignType].changeGrade(int(input("What assignment number is this? ")))


if __name__ == '__main__':
    print("\n")

    newCourse = course()
    newCourse.addAssignType()
    newCourse.insertGrade()
    newCourse.changeGrade()

    print("----------BASIC INFO---------")
    print(newCourse.assignDict['Quiz'].type)
    print(newCourse.assignDict['Quiz'].numAssigns)
    print(newCourse.assignDict['Quiz'].gradeList)
    print("----------ASSIGNTYPE TOGGLES---------")
    print(newCourse.assignDict['Quiz'].evenDist)
    print(newCourse.assignDict['Quiz'].dynamic)
    print(newCourse.assignDict['Quiz'].staggered)
    print("----------WEIGHTS---------")
    print(newCourse.assignDict['Quiz'].ovrWeight)
    print(newCourse.assignDict['Quiz'].gradeWeights)


    # print(newCourse.assignDict['Final'].type)
    # print(newCourse.assignDict['Final'].numAssigns)
    # print(newCourse.assignDict['Final'].gradeList)
    # print(newCourse.assignDict['Final'].dynamic)
    # print(newCourse.assignDict['Final'].ovrWeight)
    # print(newCourse.assignDict['Final'].gradeWeights)
