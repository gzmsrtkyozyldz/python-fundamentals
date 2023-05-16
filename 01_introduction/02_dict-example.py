# boş bir students sözlüğün oluştur
# kullanıcıdan yapmak istediği işlemi isteyelim işlemler => create,read,update,delete,exit
# yukarıdaki işlemlere kısaca CRUD denir.
# Kullanıcının yapacağı işlemlere göre inputlanır olarak işlemler gerçekleştirelim.
# Kullanıcı exit diyene kadar istediği kadar işlem yapabilsin
# CRUD operasyonlarında 'student_id' anahtarına ilerleri


students = {

}

while True:
    process = input("Enter process (create, read, update, delete, exit): ")

    if process == "create":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        lastname = input("Enter student lastname: ")
        students[student_id] = {'name': name, 'lastname': lastname}
        print("Student created.")

    elif process == "read":
        student_id = input("Enter student ID: ")
        if student_id in students:

            print(f"Name: {students[student_id]['name']}")
            print(f"Lastname: {students[student_id]['lastname']}")
        else:
            print("Student not found.")

    elif process == "update":
        student_id = input("Enter student ID: ")
        if student_id in students:
            name = input("Enter new student name: ")
            lastname = input("Enter new student lastname: ")
            students[student_id]['name'] = name
            students[student_id]['lastname'] = lastname
            print("Student updated.")
        else:
            print("Student not found.")

    elif process == "delete":
        student_id = input("Enter student ID: ")
        if student_id in students:
            del students[student_id]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif process == "exit":
        print("Exiting the program...")
        break

    else:
        print("Invalid process. Please try again.")
