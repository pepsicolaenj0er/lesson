students = {
       "Аня": 5,
       "Борис": 3,
       "Вика": 4,
       "Глеб": 2,
       "Даша": 5
}
for key, value in students.items():
   if value == 5 :
    print(key)
NumberOfRatings = sum(students.values())
NumberStudents = len(students)
averageBall = NumberOfRatings / NumberStudents
print (averageBall)

students.update({
    "Егор":4
})
print(students)
