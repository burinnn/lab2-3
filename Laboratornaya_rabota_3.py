import json

flag="1"
fileName=input("Введите имя файла: ").replace(" ", "")
if (fileName.split(".")[-1]=="json"):
    fileNameFull=fileName
else:
    fileNameFull=fileName+".json"
try:
    file = open(fileNameFull, "r+", encoding='utf-8')
    data = json.load(file)
except:
    flag="4"
    print("Файл не найден или имя файла введено неправильно")

if (flag!="4"):
    print("Простой todo: \n"
          "  1. Добавить задачу. \n"
          "  2. Вывести список задач. \n"
          "  3. Выход.")

while (flag!="4"):
    flag=input("Введите команду: ").replace(" ", "")
    if (flag=="1"):
        task=input("Название задачи: ")
        category=input("Категория задачи: ")
        time=input("Время задачи: ")
        data.append({"Задача": task, "Категория":category, "Время": time})
        file.seek(0)
        json.dump(data, file)
    elif (flag=="2"):
        print ("Все задачи:")
        for task in data:
            output=""
            for key, value in task.items():
                output = output + f"{key}: {value} "
            print(output)
    elif(flag=="3"):
        print("Всё сохранено в файл")
        file.close()
        print ("Пока! До новых встреч!")
        flag="4"
    else:
        print("Данной команды нет в спиcке!")

        

