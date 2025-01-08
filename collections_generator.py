# 1. Найти все числа от 1 до 1000, которые делятся на 7
multiples_seven = [x for x in range(1, 1001) if x % 7 == 0]

# 2. Сгенерировать список на основе чисел от 1 до 1000. Если число делится на 3 - положить результат деления в коллецию без изменений, в противном случае положить число записанное дважды друг за другом
modified_nums = [x // 3 if x % 3 == 0 else int(f'{x}{x}') for x in range(1, 1001)]

# 3. Посчитать кол-во пробелов в строке "  hel l o      world   "
str_3 = '  hel l o      world   '
spaces_count = len([x for x in str if x == ' '])

# 4. Сгенерировать список из слов строки “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”, которые начинаются на Y/y
str = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
lst = [word for word in str.split() if word[0].lower() == 'y']

# 5. Для каждого элемента строки  "hi, 3.44, 535  " сгенерировать коллекцию кортежей вида (индекс, значение), (индекс, значение)
str = "hi, 3.44, 535  "
lst_of_tuples = [(i, x) for i, x in enumerate(str)]

# 6. Сгенерировать коллекцию с числами из строки "In 1984 there were 13 instances of a protest with over 1000 people attending"
str = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
lst_of_nums = [x for x in str.split() if x.isdigit()]

# 7. Для чисел из промежутка [1, 20] сгенерировать коллекцию строк вида ("четное", "нечетное", "четное")
lst_even_or_not = ["четное" if x % 2 == 0 else "нечетное" for x in range(1, 21)]

# 8. Найти все слова из строки, длина которых меньше 4 символов "The trickiest part of learning list comprehension for me was really understanding the syntax."
str = "The trickiest part of learning list comprehension for me was really understanding the syntax."
lst_small_words = [x for x in str.split() if len(x) < 4]

# 9. Найти простые числа из промежутка [1, 50]. Простым числом называется число, которое делится только на единицу и на себя же
lst_prime_nums = [x for x in range(2, 51) if all(x % i != 0 for i in range(2, x))]
