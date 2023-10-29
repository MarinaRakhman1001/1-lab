# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, sep=","):
    a_list = set(a.split(sep))
    b_list = set(b.split(sep))
    return list(a_list.intersection(b_list))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, sep="|"))