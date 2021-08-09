class File:
    list_file =[]
    def __init__(self, name):
        self.name = name
        self.len = len
        self.value = []
        self.list_file.append(self)

    def __lt__(self, other):
        return self.len < other.len

with open("1.txt", encoding="utf8") as file:
    file_1 = File("1.txt")
    file_data = file.readlines()
    file_1.value = file_data
    file_1.len = len(file_data)
    print(file_1.len)

with open("2.txt", encoding="utf8") as file:
    file_2 = File("2.txt")
    file_data = file.readlines()
    file_2.value = file_data
    file_2.len = len(file_data)
    print(file_2.len)

with open("3.txt", encoding="utf8") as file:
    file_3 = File("3.txt")
    file_data = file.readlines()
    file_3.value = file_data
    file_3.len = len(file_data)
    print(file_3.len)

def func(list):
    list_1 = sorted(list)
    with open("4.txt", "w", encoding='utf8') as file_4:
            for file in list_1:
                print(file_4.writelines(file.name))
                print(file_4.writelines("\n"))
                len = str(file.len)
                print(file_4.writelines(len))
                print(file_4.writelines("\n"))
                ddd = file.value
                print(file_4.writelines(ddd))
                print(file_4.writelines("\n"))
                print(file_4.writelines("\n"))

func(File.list_file)



