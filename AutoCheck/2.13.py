# Зчитуємо фразу та зміщення з клавіатури
phrase = input("Введіть фразу: ")
shift = int(input("Введіть число для зсуву: "))

result = ""
for char in phrase:
    if char.isalpha():  # Перевірка, чи символ є літерою
        if char.islower():
            base = ord('a')
        else:
            base = ord('A')
        # Виконуємо зсув для літери, зберігаючи регістр
        offset = (ord(char) - base + shift) % 26
        result += chr(base + offset)
    else:
        result += char  # Зберігаємо символи, які не є літерами

# Виводимо закодовану фразу
print("Закодована фраза:", result)