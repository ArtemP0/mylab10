lviv_numbers = []
numbers_starting_with_4 = []
kyiv_count = 0

with open('numbers.txt', 'r', encoding='utf-8' ) as file:
    for line in file:
        if line.startswith('AI'):
            kyiv_count += 1
        if line.startswith('BC'):
            lviv_numbers.append(line)
        if line[2:].startswith('4'):
            numbers_starting_with_4.append(line)
with open('results.txt', 'w' , encoding='utf-8' ) as result_f:
    result_f.write(f'Кількість номерів Київської області: {kyiv_count}\n')
    result_f.write('Номери Львівської області:\n')

    for number in lviv_numbers:
        result_f.write(f'{number}\n')
    result_f.write('Номери, що починаються з цифри 4:\n')
    for number in numbers_starting_with_4:
        result_f.write(f'{number}\n')
