def create_table(key, message):
    key = key.lower()
    num_columns = len(key)
    rows = [message[i:i + num_columns] for i in range(0, len(message), num_columns)]
    if len(rows[-1]) < num_columns:
        rows[-1] += ' ' * (num_columns - len(rows[-1]))
    table = [key] + rows
    return table

def sort_table(table):
    header = table[0]
    sorted_indices = sorted(range(len(header)), key=lambda i: (header[i], i))
    sorted_table = []
    for row in table:
        sorted_row = ''.join(row[i] for i in sorted_indices)
        sorted_table.append(sorted_row)
    
    return sorted_table

def encrypt(key, message):
    table = create_table(key, message)
    sorted_table = sort_table(table)

    result = []
    
    for col in range(len(sorted_table[0])):
        for row in range(1, len(sorted_table)):  
            result.append(sorted_table[row][col])
    
    return ''.join(result)

def decrypt(key, encrypted_message):
    key = key.lower()
    num_columns = len(key)
    num_rows = (len(encrypted_message) + num_columns - 1) // num_columns
    table = [''] * (num_rows + 1)
    table[0] = key
    index = 0
    for col in range(num_columns):
        for row in range(1, num_rows + 1):
            if index < len(encrypted_message):
                if col < len(table[0]):
                    if row <= len(table) - 1:
                        table[row] += encrypted_message[index]
                        index += 1
    
    sorted_indices = sorted(range(len(table[0])), key=lambda i: (table[0][i], i))
    decrypted_message = []
    for row in range(1, len(table)):
        decrypted_row = ''.join(table[row][i] for i in sorted_indices)
        decrypted_message.append(decrypted_row)
    return ''.join(decrypted_message).strip()

def main():
    action = input("Введите 'e' для шифрования или 'd' для дешифрования: ").strip().lower()
    
    if action == 'e':
        key = input("Введите слово-ключ: ")
        message = input("Введите основное сообщение: ")
        result = encrypt(key, message)
        print("Зашифрованный текст:", result)

    elif action == 'd':
        key = input("Введите слово-ключ: ")
        encrypted_message = input("Введите зашифрованный текст: ")
        result = decrypt(key, encrypted_message)
        print("Расшифрованный текст:", result)

if __name__ == "__main__":
    main()