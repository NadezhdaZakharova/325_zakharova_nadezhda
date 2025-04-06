def create_table(key, message):
    key = "".join(sorted(set(key), key=lambda k: key.index(k)))
    num_columns = len(key)
    rows = [message[i:i + num_columns] for i in range(0, len(message), num_columns)]
    if len(rows[-1]) < num_columns:
        rows[-1] += ' ' * (num_columns - len(rows[-1]))
    table = [key] + rows
    
    return table

def sort_table(table):
    header = table[0]
    sorted_indices = sorted(range(len(header)), key=lambda i: header[i])
    sorted_table = []
    for row in table:
        sorted_row = ''.join(row[i] for i in sorted_indices)
        sorted_table.append(sorted_row)
    
    return sorted_table

def main():
    key = input("Введите слово-ключ (без повторяющихся букв): ")
    
    if len(set(key)) != len(key):
        print("Ошибка: слово-ключ должно содержать только уникальные буквы.")
        return
    
    message = input("Введите основное сообщение: ")

    table = create_table(key, message)
    sorted_table = sort_table(table)
    result = ''.join(sorted_table[1:])
    print("Результат:", result)
if __name__ == "__main__":
    main()