class Database:
    def __init__(self):
        self.ListGroup = []
        self.ListStudent = []

#Group segment
    def addGroup(self, Name):
        if not [group for group in self.ListGroup if group.get('name', "") == Name]:
            i = 0
            for student in self.ListStudent:
                if (student.get('group', "") == Name):
                    i += 1
            self.ListGroup.append({'name':Name, 'count':i})

    def clearGroups(self):
        del self.ListStudent[:]
        del self.ListGroup[:]

    def deleteGroup(self, Group):
        self.ListStudent[:] = [student for student in self.ListStudent if not (student['group'] == Group)]
        self.ListGroup[:] = [group for group in self.ListGroup if not (group['name'] == Group)]

    def modifyGroup(self, Name, newName):
        for group in self.ListGroup:
            if (group['name'] == Name):
                for student in self.ListStudent:
                    if (student['group'] == Name):
                        student['group'] = newName
                group['name'] = newName
                break

    def loadGroups(self, List):
        self.ListGroup = List

    def getGroups(self):
        return self.ListGroup
#Student segment
    def addStudent(self, FirstName, LastName, Group):
        self.ListStudent.append({'firstname': FirstName, 'lastname': LastName, 'group': Group})
        if not [group for group in self.ListGroup if group.get('name', "") == Group]:
            self.addGroup(Group)
        else:
            for group in self.ListGroup:
                if (group.get('name', "") == Group):
                    group['count'] += 1

    def clearStudents(self):
        self.ListStudent[:] = []
        for group in self.ListGroup:
            group['count'] = 0

    def deleteStudent(self, FirstName, LastName, Group):
        a = {'firstname': FirstName, 'lastname': LastName, 'group': Group}
        if a in self.ListStudent:
            for group in self.ListGroup:
                if (group.get('name', "") == Group):
                    group['count'] -= 1
                    break
            self.ListStudent.remove(a)

    def modifyStudent(self, FirstName, LastName, Group, code, value):
        a = {'firstname': FirstName, 'lastname': LastName, 'group': Group}
        if code == 0: key = 'firstname'
        elif code == 1: key = 'lastname'
        elif code == 2:
            key = 'group'
        if a in self.ListStudent:
            self.ListStudent[self.ListStudent.index(a)][key] = value
            if code == 2:
                for group in self.ListGroup:
                    if (group.get('name', "") == Group):
                        group['count'] -= 1
                        break
                if any(d['main_color'] == 'red' for d in self.ListGroup):
                    for group in self.ListGroup:
                        if (group.get('name', "") == value):
                            group['count'] += 1
                            break
                else:
                    self.addGroup(value)

    def loadStudents(self, List):
        self.ListStudent = List

    def getStudents(self):
        return self.ListStudent