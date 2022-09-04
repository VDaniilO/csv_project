import csv


greeting_list = ['Добры', 'добры', 'Здрав', 'здрав', 'Прив', 'прив']  # can be a file and use how a libary and can add more solution
solution = []

name_list = ['ангелина', 'анастасия', 'максим', 'дмитрий']  # can be a file and use how a libary and can add more name
name_manager = []

farewell_list = []

comp_names = []

with open('test_data.csv', 'r', encoding="utf8") as file:
    file_read = csv.reader(file, delimiter=',')
    line_count = 0
    temp_comp_names = []
    for row in file_read:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            for i in greeting_list:  # check were maanger had solution
                if i in row[3] and 'manager' in row[2]:
                    solution.append(f'dialog_id - {row[0]} | msg_num {row[1]} | message {row[3]}')

            for i in name_list:  # check on name manager
                if f'зовут {i}' in row[3] or f'{i} зовут' in row[3] or f'это {i}' in row[3]:
                    if row[2] in 'manager':
                        name_manager.append(f'dialog_id - {row[0]} | msg_num {row[1]} | manager_name {i}')

            if 'компания ' in row[3]:  # get name company
                string_name_comp = row[3].split()
                for i in range(len(string_name_comp)):
                    if string_name_comp[i] == "компания":
                        temp_comp_names.append(string_name_comp[i + 1])

            if 'свидания' in row[3] or 'доброго' in row[3]:  # check on farewell
                if 'manager' in row[2]:
                    farewell_list.append(f'dialog_id - {row[0]} | msg_num {row[1]}')
            line_count += 1


with open('out_info.txt', 'w', encoding="utf8") as newfile:
    newfile.write(f'Приветсвие:\n {solution}, \n Имя менеджера: \n{name_manager}, \n Имя компании: \n{temp_comp_names}, \n Прощание: \n{farewell_list}')

print(f'\n{solution}, \n{name_manager}, \n{temp_comp_names}, \n{farewell_list}')
