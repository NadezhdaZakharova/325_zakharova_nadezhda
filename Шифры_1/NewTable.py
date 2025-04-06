def create_table(key, message):
    key = "".join(sorted(set(key), key=lambda k: key.index(k)))
    key = key.lower()
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
    
    for i in range(len(table)):
        sorted_row = ''.join(table[i][j] for j in sorted_indices)
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

    result = []
    
    for col in range(len(sorted_table[0])):
        for row in range(1, len(sorted_table)): 
            result.append(sorted_table[row][col])
    
    print("Результат:", ''.join(result))

if __name__ == "__main__":
    main()