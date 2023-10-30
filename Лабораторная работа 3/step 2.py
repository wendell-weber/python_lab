# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants2, separator=','):
    list1 = participants1.split(separator)
    list2 = participants2.split(separator)

    common_participants = list(set(list1).intersection(list2))
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(participants)
