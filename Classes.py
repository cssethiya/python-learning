class teacher_info:
    def __init__(self,name,age,degree,position,class_assigned):
        self.name = name
        self.age = age
        self.degree = degree
        self.position = position
        self.class_assigned = class_assigned

    def on_position(self):
        if self.position == "HOD":
            return True

        else:
            return False

