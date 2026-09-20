import json
import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class Homework:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed


class HomeworkList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def all_completed(self):
        completed = True

        for item in self.items:
            if item.completed == False:
                completed = False
                print(item.name)

        if completed:
            print("All finished!")


hw_list = HomeworkList()

hw_list.add_item(Homework("Lap trinh App Producer", 3))
hw_list.add_item(Homework("Lam van", 2, True))
hw_list.add_item(Homework("Lap trinh GameMaker", 3))


class Dialog(QMainWindow):
    def __init__(self) -> None:
        super().__init__() # ke thua tu lop cha QMainWindow
        # khai bao bien input/ output
        self.input = ""

        # hien thi giao dien
        ui_path = "cp2/cp2.ui"
        uic.loadUi(ui_path, self)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dialog()
    sys.exit(app.exec())


# Lưu vào JSON
data = []

for item in hw_list.items:
    data.append({
        "name": item.name,
        "priority": item.priority,
        "completed": item.completed
    })

with open("new_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

