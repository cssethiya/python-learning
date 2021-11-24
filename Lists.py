employees = ["Sanjay","Sanjay","Karthik","Kushagra","Ayush","Deepak"]
employees_code=[49,50,48,52,37]
print (employees [1]) 
print(employees[-2])
print(employees[1:])
print(employees[1:3])

#Lists functions --------------------------------------------------------------

#employees.extend (employees_code)
employees.append("Punit")
employees.append("Rakesh")
employees.insert(2,"Suresh")
employees.remove("Ayush")
employees_code.clear()
employees.pop()
employees.index("Karthik")
#employees.count("Sanjay")
#print (employees.count("Sanjay"))
employees.sort() 
employees.sort(reverse=True) 
#print(employees.copy())
print (employees)
