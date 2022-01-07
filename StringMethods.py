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