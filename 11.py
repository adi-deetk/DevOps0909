#my_file = open("read_my.txt")
#contents = my_file.readline():
   # print(line)
# for line in contents:
#   print(line)


# my_file.close()

import io
try:
    my_file = open("read_my_contents.txt", "r")
    contents = my_file.write("blabla")
except io.UnsupportedOperation:
    print("Unsupported Operation")

my_file = open("names.txt", "w")
for i in range(3):
    concurrent_name = input("inter your name:")
    my_file.write(concurrent_name + "\n")
my_file.close()

my_file = open("names.txt", "r")
for name in my_file.readline():
    print(f"hello {name}", end='')


