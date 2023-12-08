
with open('file.txt', 'r') as f: # відкриваємо файл  построково
    lines = f.read().splitlines()


for i, line in enumerate(lines): #проходимось по строкам
    words = line.split()  # розділяємо строку на слова
    num_of_words = len(words)
    num_of_letters = 0

    for word in words:
        num_of_letters += len(word)

    print(str(num_of_letters) + '- к-сть символів; ' + str(num_of_words) + ' - к-сть слів , в рядку: ' + line)



