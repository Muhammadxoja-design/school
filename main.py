import json

def read_teachers(file_path):
    teachers_data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split()
            class_name = parts[1].strip('“-”')  
            teacher_name = " ".join(parts[2:])
            teachers_data[class_name] = teacher_name
    return teachers_data

# Update the students.json with teacher names
def update_students_json(students_file, teachers_data):
    with open(students_file, 'r', encoding='utf-8') as file:
        students_data = json.load(file)
    
    for class_name in students_data:
        if class_name in teachers_data:
            students_data[class_name]["Teacher"] = teachers_data[class_name]
    
    # Save updated data to the JSON file
    with open(students_file, 'w', encoding='utf-8') as file:
        json.dump(students_data, file, ensure_ascii=False, indent=4)

teachers_file = 'teachers.txt'
students_file = 'students.json'

teachers_data = read_teachers(teachers_file)
update_students_json(students_file, teachers_data)

print("Teachers have been successfully updated in the students.json file.")
