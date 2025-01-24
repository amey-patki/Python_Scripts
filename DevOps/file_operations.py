with open("devops_notes.txt", "w") as file:
    file.write("Learning Python scripting for DevOps is fun!\n")
    file.write("Automation makes life easier.\n")

# Reading from the file
with open("devops_notes.txt", "r") as file:
    content = file.read()
    print(content)