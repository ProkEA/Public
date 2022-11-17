def check_if_str_valid(str_pattern):
    valid_str_flag = 0

    for i in str_pattern:
        if i.isdigit() or i == ' ':
            valid_str_flag = 1
        else:
            valid_str_flag = 0
            break
    if str_pattern.endswith(' '):
        valid_str_flag = 0
    return valid_str_flag


def create_digits_list(str_pattern):
    digits_list = []
    tmp = ''
    for i in str_pattern:
        if i.isdigit():
            tmp += i
        if i == ' ':
            digits_list.append(int(tmp))
            tmp = ''
    digits_list.append(int(tmp))
    return digits_list


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def sorting(list_patern):
    if len(list_patern) < 2:
        return list_patern
    else:
        middle = len(list_patern) // 2
        left = sorting(list_patern[:middle])
        right = sorting(list_patern[middle:])
        return merge(left, right)


def binary_search(numbers_list, user_num, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if numbers_list[middle] == user_num:
            return middle
        elif user_num < numbers_list[middle]:
            return binary_search(numbers_list, user_num, left, middle - 1)
        else:
            return binary_search(numbers_list, user_num, middle + 1, right)
    except IndexError:
        return "number out of range"


if __name__ == '__main__':
    user_digits_string = input('Введите целые числа через пробел:')

    if check_if_str_valid(user_digits_string) == 1:
        number = int(input('Введите число: '))
        sorted_list = sorting(create_digits_list(user_digits_string))
        print(f'Упорядоченный по возрастанию список: {sorted_list}')
        if not binary_search(sorted_list, number, 0, len(sorted_list)):
            rI = min(sorted_list, key=lambda x: (abs(x - number), x))
            ind = sorted_list.index(rI)
            max_ind = ind + 1
            min_ind = ind - 1
            if rI < number:
                print(f'''В списке нет введенного элемента 
            Ближайший меньший элемент: {rI}, его индекс: {ind}
            Ближайший больший элемент: {sorted_list[max_ind]} его индекс: {max_ind}''')
            elif min_ind < 0:
                print(f'''В списке нет введенного элемента
            Ближайший больший элемент: {rI}, его индекс: {sorted_list.index(rI)}
            В списке нет меньшего элемента''')
            elif rI > number:
                print(f'''В списке нет введенного элемента
            Ближайший больший элемент: {rI}, его индекс: {sorted_list.index(rI)}
            Ближайший меньший элемент: {sorted_list[min_ind]} его индекс: {min_ind}''')
            elif sorted_list.index(rI) == 0:
                print(f'Индекс введенного элемента: {sorted_list.index(rI)}')
        else:
            print(f'Индекс введенного элемента: {binary_search(sorted_list, number, 0, len(sorted_list))}')
    else:
        print("Строка должна содержать только цифры и пробелы")
