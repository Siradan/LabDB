import database
import pickle

db = database.Database()

def getList(key):
    if key == 0:
        return db.getGroups()
    else:
        return db.getStudents()

def addElement(key, value):
    if key == 0:
        db.addGroup(value)
    else:
        db.addStudent(value[0], value[1], value[2])
def modifyElement(key, value):
    if key == 0:
        db.modifyGroup(value[0], value[1])
    else:
        db.modifyStudent(value[0], value[1], value[2], value[3], value[4])
def deleteElement(key, value):
    if key == 0:
        db.deleteGroup(value)
    else:
        db.deleteStudent(value[0], value[1], value[2])

def deleteData(key):
    if key == 0:
        db.clearGroups()
    else:
        db.clearStudents()

def saveData():
    f = open('data0.pickle', 'wb')
    pickle.dump(db.getGroups(), f)
    f.close()
    f = open('data1.pickle', 'wb')
    pickle.dump(db.getStudents(), f)
    f.close()


def loadData():
    f = open('data0.pickle', 'rb')
    global db
    db.loadGroups(list(pickle.load(f)))
    f.close()
    f = open('data1.pickle', 'rb')
    db.loadStudents(list(pickle.load(f)))
    f.close()