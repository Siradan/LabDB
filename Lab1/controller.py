import view
import model

Command0 = 0
Command1 = 0

def getCommand(key, i):
    global Command0
    global Command1

    if key == 0:
        if i == 1:
            Command0 = 1
            return 1
        if i == 2:
            Command0 = 2
            return 1
        if i == 3:
            Command0 = 3
            return 1
        if i == 4:
            Command0 = 4
            return 1
        if i == 5:
            Command0 = 5
            return 1
        if i == 6:
            Command0 = 6
            return 1
        if i == 7:
            Command0 = 7
            return 1
        return 0
    else:
        if i == 1:
            Command1 = 1
            return 1
        if i == 2:
            Command1 = 2
            return 1
        return 0

while getCommand(0, view.main_menu()):
    if Command0 == 1:
        if getCommand(1, view.sec_menu()):
            if Command1 == 1:
                view.showList(0, model.getList(0))
            else:
                view.showList(1, model.getList(1))
    elif Command0 == 2:
        if getCommand(1, view.sec_menu()):
            if Command1 == 1:
                model.addElement(0, view.getValue(0))
            else:
                model.addElement(1, view.getValue(1))
    elif Command0 == 3:
        if getCommand(1, view.sec_menu()):
            if Command1 == 1:
                model.modifyElement(0, view.getValue(2))
            else:
                model.modifyElement(1, view.getValue(3))
    elif Command0 == 4:
        if getCommand(1, view.sec_menu()):
            if Command1 == 1:
                model.deleteElement(0, view.getValue(0))
            else:
                model.deleteElement(1, view.getValue(1))
    elif Command0 == 5:
        if getCommand(1, view.sec_menu()):
            if Command1 == 1:
                model.deleteData(0)
            else:
                model.deleteData(1)
    elif Command0 == 6:
        model.saveData()
    elif Command0 == 7:
        model.loadData()