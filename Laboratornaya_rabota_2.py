def getdata():
    file = open("students.txt", 'r', encoding="utf8")
    listStudents = list(file.read().split("\n"))
    listStudents.remove("")
    file.close()
    return listStudents


def writedata(listStudents):
    listStudents.sort(key=str.lower)
    file = open("students.txt", 'w', encoding="utf8")
    for student in listStudents:
        file.write(student + "\n")
    file.close()
    
        
def add(surname, name):
    student = surname + " " + name
    listStudents=getdata()
    if (student in listStudents):
        return "Учащийся " + student + " уже есть в списке"
    else:
        listStudents.append(student)
        writedata(listStudents)
        return "Учащийся " + student + " добавлен"


def getstudent(surname, name=None):
    listStudents=getdata()
    if (name==None):
        allSurnames=[]
        for student in listStudents:
            surnameStud=student.split()[0]
            allSurnames.append(surnameStud)
        if surname in allSurnames:
           firstIndex = allSurnames.index(surname)
           studentsWithSuch=""
           for i in range(firstIndex, firstIndex+allSurnames.count(surname)):
               studentsWithSuch = studentsWithSuch + listStudents[i]+" " 
           return "Учащиеся с фамилией "+ surname + ": " + studentsWithSuch
        else:
            return "Учащийся с фамилией " + surname + " нет в списке"
    else:
        student = surname + " " + name
        if (student in listStudents):
            return "Учащийся " + student + " есть в списке"
        else:
            return "Учащегося " + student + " нет в списке"


def change (old_surname, old_name, new_surname=None, new_name=None):
    listStudents=getdata()
    student = old_surname + " " + old_name
    if (student in listStudents):
        listStudents.remove(student)
        new_student=""
        if (new_surname!=None):
            new_student = new_student + new_surname + " "
        else:
            new_student = new_student + old_surname + " "
        if (new_name!=None):
            new_student = new_student + new_name
        else:
            new_student = new_student + old_name
        listStudents.append(new_student)
        writedata(listStudents)
        return "Учащийся " + student + " изменен на " + new_student
    else:
        return "Учащегося " + student + " нет в списке"



def removestudent (surname, name=None):
    listStudents=getdata()
    if (name!=None):
        student = surname + " " + name
        if (student in listStudents):
            listStudents.remove(student)
            writedata(listStudents)
            print( "Учащийся " + student + " удален")
        else:
            print("Учащегося " + student + " нет в списке")
    else:
        allSurnames=[]
        for student in listStudents:
            surnameStud=student.split()[0]
            allSurnames.append(surnameStud)
        if (allSurnames.count(surname)==0):
            print("Учащегося с фамилией " + surname + " нет в списке")
        elif (allSurnames.count(surname)==1):
            studentIndex=allSurnames.index(surname)
            print ("Учащийся "+ listStudents[studentIndex] + " удален" )
            listStudents.pop(studentIndex)
            writedata(listStudents)
        else:
            print(getstudent(surname))
            name_new = input ("Введите имя учащегося, которого хотите удалить: ").replace(" ", "")
            removestudent (surname, name=name_new)
            

while (True):
    print ("Список команд: \n"
               "add - добавить учащегося \n"
               "get - найти учащегося по фамилии и имени или только по фамилии \n"
               "change - изменить у заданного учащегося имя и фамилию или только фамилию \n"
               "remove - удалить учащегося по фамилии и имени или только по фамилии \n"
               "q - конец программы")
    function=input("Введите команду: ").replace(" ", "")
    if (function=="add"):
        surname = input ("Введите фамилию учащегося который вам нужен: ").replace(" ", "")
        name = input ("Введите имя учащегося который вам нужен: ").replace(" ", "")
        print(add(surname, name))
    elif (function=="get"):
        surname = input ("Введите фамилию учащегося который вам нужен: ").replace(" ", "")
        name = input ("Введите имя учащегося или '', если надо искать учащегося только по фамилии: ").replace(" ", "")
        if (name=="''"):
            print(getstudent(surname))
        else:
            print (getstudent(surname, name))       
    elif (function=="change"):
        surname = input ("Введите фамилию учащегося, данные которого хотите поменять: ").replace(" ", "")
        name = input ("Введите имя учащегося, данные которого хотите поменять: ").replace(" ", "")
        new_surname = input ("Введите новую фамилию учащегося или '', если не хотите менять фамилию: ").replace(" ", "")
        new_name = input ("Введите новое имя учащегося или '', если не хотите менять имя: ").replace(" ", "")
        if (new_name=="''" and new_surname=="''"):
            print ("Вы не ввели, как поменять фамилию и имя учащегося")
            
        elif (new_name=="''"):
            print(change(surname, name, new_surname=new_surname, new_name=None))
        else:
            print(change(surname, name, new_surname=None, new_name=new_name))       
    elif (function=="remove"):
        surname = input ("Введите фамилию учащегося: ").replace(" ", "")
        name = input ("Введите имя учащегося или '', если надо удалять учащегося только по фамилии: ").replace(" ", "")
        if (name=="''"):
            removestudent (surname)
        else:
            removestudent (surname, name=name)
    elif (function=="q"):
        print ("Пока! До новых встреч!")
        break
    else:
        print ("Введите правильную команду \n"
               "add - добавить учащегося по имени и фамилии\n"
               "get - найти учащегося по фамилии и имени или только по фамилии \n"
               "change - изменить у заданного по фамилии и имени учащегося имя и фамилию или только фамилию \n"
               "remove - удалить учащегося по фамилии и имени или толкьо по фамилии \n"
               "q - конец программы")
