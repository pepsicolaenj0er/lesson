students = {
"student 1" : {"name": "Юрий", "age": "20 лет", "course": "Математический" },
"student 2" : {"name": "Максим", "age": "17 лет", "course": "Информационный" },
"student 3" : {"name": "Иван", "age": "19 лет", "course": "Юристический" },
}
for key, info in students.items():
    print(info ["name"] ,info ["age"],info ["course"])
    