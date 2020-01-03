from assignment import assignment as asgn
# Course holds the information concerning one course
# i.e Calculus:
# - 6 Quizzes
# - 2 Exams
# - 1 Final

class course:
    # Defining course variables
    def __init__(self, cname = '', dynamFinal = False):
        self.coursename = cname
        self.dynamFinal = dynamFinal
        self.assignDict = {}

    def addAssignType(self, userInput):
        # Initializing new assignment object and assignment type
        newAssign = asgn()
        newAssign.type = userInput

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

    def loadAssignType(self, asgnType, numAssigns, ovrWeight, finalExamGrade,
                    gradeList, dynamic, gradeWeights, staggered,
                    evenDist, dynamFinal):
        loadedAssign = asgn()
        loadedAssign.type = asgnType
        loadedAssign.numAssigns = numAssigns
        loadedAssign.ovrWeight = ovrWeight
        loadedAssign.finalExamGrade = finalExamGrade
        loadedAssign.gradeList = gradeList
        loadedAssign.dynamic = dynamic
        loadedAssign.gradeWeights = gradeWeights
        loadedAssign.staggered = staggered
        loadedAssign.evenDist = evenDist
        loadedAssign.dynamFinal = dynamFinal
        self.assignDict[loadedAssign.type] = loadedAssign

    def insertGrade(self, userInp):
        assignType = userInp
        if assignType not in self.assignDict:
            print("Error: This Assignment type does not exit..Returning to Menu\n")
        else:
            self.assignDict[assignType].addGrade(int(input("What assignment number is this? ")))

    # *TODO: Change for in menu to just take the input from the menu and not enter full assigntype*
    def changeGrade(self):
        print('-----------------------------------')
        assignType = input("Assignment type for changing grade: ")
        if assignType not in self.assignDict:
            print("Error: This Assignment type does not exit..Returning to Menu\n")
        else:
            self.assignDict[assignType].changeGrade(int(input("What assignment number is this? ")))
