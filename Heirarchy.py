from college import college_info
from class1 import teacher_info

teacher_info_1 = teacher_info()

print(teacher_info_1.salary(2345))
print(teacher_info_1.department("Computer Science"))

college_infomation = college_info()
print(college_infomation.departments("IT"))