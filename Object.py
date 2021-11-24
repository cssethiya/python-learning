from Classes import teacher_info

teacher_info1 = teacher_info("Rashmi", 34, "M.Tech", "Assitant Professer", True)
teacher_info2 = teacher_info("Safi", 42, "PHD", "HOD", False)
teacher_info3 = teacher_info("Vinod", 36, "PHD", "Professer", True)

'''print(teacher_info1.name)
print(teacher_info1.position)

print(teacher_info2.age)
print(teacher_info1.class_assigned)

print(teacher_info3.position)
print(teacher_info1.name)'''

print(teacher_info1.on_position())
print(teacher_info2.on_position())
print(teacher_info3.on_position())
