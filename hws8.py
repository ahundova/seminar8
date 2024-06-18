# Создаем файл и записываем в него 5 строк
with open('phones.txt', 'w') as file:
    file.write('Ivanov Ivan,123-456-7890\n')
    file.write('Petrov Petr,987-654-3210\n')
    file.write('Vasilchenko Vasiliy,456-789-0123\n')
    file.write('Mamedli Mamed,321-654-9876\n')
    file.write('Aliyev Ali,789-123-4567\n')

# Читаем данные из файла и сохраняем их в список
data = []
with open('phones.txt', 'r') as file:
    for line in file:
        data.append(line.strip())

def write_to_file(filename, index):
    if index < 0 or index >= len(data):
        print("Неверный номер строки.")
        return
    
    with open(filename, 'w') as file:
        file.write(data[index])
    print(f"Строка '{data[index]}' записана в файл {filename}.")

# Запрашиваем у пользователя номер строки и записываем ее в другой файл
user_input = int(input("Введите номер строки (0-4): "))
write_to_file('phonebooks.txt', user_input)





