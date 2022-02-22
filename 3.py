import re

symbols = ['!', ';', ':', ',', '.', '?']

def main(file_name):
    file_text = open(file_name, "r")
    lines = file_text.readlines()

    bit_arrays = []
    index_array = 0

    for line in lines:
        bit_arrays.append([])
        for i in range(len(line)):
            if line[i] in symbols \
                    or line[i].isupper() \
                    or bool(re.search('[a-zA-Z]', line[i])):
                bit_arrays[index_array].append(1)
            else:
                bit_arrays[index_array].append(0)
        index_array += 1

    print(bit_arrays)

    lines_yes = []
    lines_no = []
    index_str = 0
    for bits in bit_arrays:
        result = 0
        for bit in bits:
            result = result | bit
        if result == 1:
            #print("Строка " + str(index_str) + ": ДА")
            lines_yes.append(lines[index_str])
        else:
            #print("Строка " + str(index_str) + ": НЕТ")
            lines_no.append(lines[index_str])
        index_str += 1

    print("\nСтроки со скрытой информацией:")
    for line in lines_yes:
        print(line[:-1])

    print("\nСтроки без скрытой информации:")
    for line in lines_no:
        print(line[:-1])

    print("\n")

if __name__ == '__main__':
    print("Метод скрытия с помощью пунктуации:")
    main("laba3_1.txt")

    print("Метод скрытия с помощью регистров символов:")
    main("laba3_2.txt")

    print("Метод скрытия с изменения помощью числовых кодов символов:")
    main("laba3_3.txt")