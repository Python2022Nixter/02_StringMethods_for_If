test_string = "Hello, world!"
# index    0123456789
# index   -6-5-4-3-2-1
print(F"My string:\t\t {test_string}")
print(F"My string:\t\t {test_string}\nstring length: {len(test_string)}")
print(F"String slice: \t {test_string[6:len(test_string)]} [START:STOP:STEP]")

str2 = "מחרוזת מבחן בעברית"
str3 = str2[::-1]
print(str2)
print("reverse: ", str3)

print(f"test_string[-6::1] = {test_string[-6::1]}")

# String methods

print(f"test_string.upper() = {test_string.upper()}")
print(f"test_string.lower() = {test_string.lower()}")
# проверяет на наличие последнего символа
print(f"test_string.endswith(\"!\") = {test_string.endswith('!')}")
# возвращает индекс первого вхождения символа
print('test_string.find', test_string.find("H"))
# заменяет все вхождения символа
print(f"test_string.replace(\"H\",\"X\") = {test_string.replace('H','X')}")

time = "12:07:23"
print(f"time.split(\":\") = {time.split(':')}")

str4 = "  time  "
print(f"str4.strip() = {str4.strip()}")
print(" - ".join(["a", "b", "c"]))

# моё приложение
str = "Hello, world!"
print(f"str.casefold() = {str.casefold()}") # переводит в нижний регистр
print(f"str.capitalize() = {str.capitalize()}") # первая буква в верхний регистр
print(f"str.center(20) = {str.center(20)}") # выравнивание по центру
print(f"str.center(40) = {str.center(40, '.')}") # выравнивание по центру
print(f"str.center(70) = {str.center(70, '*')}") # выравнивание по центру
str = "test\tstring\tend"
print(str)
print(f"str.expandtabs() = {str.expandtabs()}") # заменяет табуляции на пробелы
# string encode
str = "test for encode!"
print("str.encode() = ", str.encode("ascii", "ignore"))
print("str.encode() = ", str.encode("ISO-8859-5", "ignore"))

# string decode
str = b"test for decode!"
print("str.decode() = ", str.decode("ascii", "ignore"))

# string isalnum()
str = "testSstring12"
print(f"str.isalnum() = {str.isalnum()}")
str = "test string!"
print(f"str.isalnum() = {str.isalnum()}")

# string isidentifier()
str = "testSstring12"
print(f"str.isidentifier() = {str.isidentifier()}")

# string isnumeric()
str = "1234"
print(f"str.isnumeric() = {str.isnumeric()}")
str = "1234.5"
print(f"str.isnumeric() = {str.isnumeric()}")
str = "1234.5.6"
print(f"str.isnumeric() = {str.isnumeric()}")
# swap case
str = "test string!"
print(f"str.swapcase() = {str.swapcase()}")
str = "TesTinG StRiNg!"
print(f"str.swapcase() = {str.swapcase()}")

# partition
str = "test string!"
a = str.partition(" ")
print(type(a))
print(f"str.partition(\"string\") = {str.partition('string')}")

# maketrans
str = "test string!"
print(f"str.maketrans() = {str.maketrans('t', 'T')}")

# zfill
str = "test string!"
print(f"str.zfill(10) = {str.zfill(20)}")