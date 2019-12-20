class assignment:
    type = ''
    numAssigns = 0
    ovrWeight = 0
    finalExamGrade = 0
    gradeList = []

    # For what-if grading
    tempGradeList = []

    # Variables are for dynamic grading only
    dynamic = False
    gradeListSorted = []
    gradeWeights = []

    # Variable for staggered grading
    staggered = False

    # Variable for even distrib grading
    evenDist = False

    # Variable for dynamic Final grading
    dynamFinal = False

    # Initializes all values in gradeList to None
    def setGradeList(self):
        for x in range(0, self.numAssigns):
            self.gradeList.append(None)

    # Adding a new grade in for the first time
    def addGrade(self, assignNum):
        if self.gradeList[assignNum-1] == None:
            self.gradeList[assignNum-1] = round(int(input("Grade received? (i.e 50=50%) "))/100, 2)
        else:
            print("There's a grade already for this assignment. Maybe you meant change grade?")

    # Changing an already established grade
    def changeGrade(self, assignNum):
        if self.gradeList[assignNum-1] == None:
            print("Error: You cannot change a grade that hasn't been set yet..Returning to menu\n")
        else:
            self.gradeList[assignNum-1] = round(int(input("Change Grade to? (i.e 50=50%) "))/100, 2)

    # Initializes value of evenDist to user's preference
    def setevenDist(self, inpTog):
        if inpTog.lower() == 'y':
            self.evenDist = True
        elif inpTog.lower() == 'n':
            self.evenDist = False

    # Initializes value of Dynamic to user's preference
    def setDynamic(self, inpTog):
        if inpTog.lower() == 'y':
            self.dynamic = True
        elif inpTog.lower() == 'n':
            self.dynamic = False

    # Initializes value of Staggered to user's preference
    def setStagger(self, inpTog):
        if inpTog.lower() == 'y':
            self.staggered = True
        elif inpTog.lower() == 'n':
            self.staggered = False

    # Initializes/assigns the weights of each of the assignments
    # ***TODO: Modify to consider the different grading weight types
    def setGradeWeights(self):
        if self.ovrWeight > 0:
            for x in range(0, self.numAssigns):
                self.gradeWeights.append(round(self.ovrWeight/self.numAssigns, 2))
        else:
            print("Add the differing weights for this assignment (ex. 50 means 50%)\n")
            for x in range(0, self.numAssigns):
                self.gradeWeights.append(int(input())/100.00)
            self.gradeWeights.sort()
