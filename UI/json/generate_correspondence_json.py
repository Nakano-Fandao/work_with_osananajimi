import os

qrc_path = os.path.join(
    os.path.normpath(os.path.dirname(__file__)),
    "..\\files.qrc"
)
file_list = []
with open(qrc_path, 'r') as f:
    for line in f.readlines():
        file_name = line.split()[0].split("</file>")[0].split("<file>")[-1]

        if file_name.find("RCC") != -1:
            continue
        elif file_name.find("qresource") != -1:
            continue
        print(file_name)
        file_list.append(file_name)

write_path = os.path.join(os.path.dirname(__file__), "..\json\correspondence.json")
with open(write_path, "w") as f:
    f.write("{\n")
    for line in file_list:
        f.write("\t" + '"": ' + f'":voice/{line}"' + ",\n")
    f.write("}\n")
