# TODO  Напишите функцию count_letters
def count_letters(text):
    lower_text = text.lower()

    number_of_letters = {}
    for symbol in lower_text:
        if symbol.isalpha():
            if symbol in number_of_letters:
                number_of_letters[symbol] += 1
            else:
                number_of_letters[symbol] = 1
    return number_of_letters

# TODO Напишите функцию calculate_frequency
def calculate_frequency(number_of_letters):
    total_letters = sum(number_of_letters.values())

    letter_frequency = {}
    for current_letter, count in number_of_letters.items():
        letter_frequency[current_letter] = count / total_letters

    return letter_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
count_dict = count_letters(main_str)
frequency_dict = calculate_frequency(count_dict)

for letter, frequency in frequency_dict.items():
    print(f"{letter}: {frequency:.2f}")