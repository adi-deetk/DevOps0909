print(list(range(100, 1, -5)))
names = ["ariel", "adi", "eran", "adir", "shahar"]
string_to_print = "hello world!"
for i in range(5):
    print(names[i])

for name in names:
    print(name)

a = 0
while a < 10:
    a = a + 1
    if a == 5:
        continue
    print(a)
else:
    print("finished successfully")





