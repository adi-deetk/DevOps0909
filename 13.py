def save_names
    my_file_class = open("save_names.txt", "a")
    for concurrent_name in my_file_class():
        concurrent_name = input("inter your name:")
        my_file_class.write(concurrent_name + "\n")
my_file_class.close()

def show_names
    my_file_class = open("save_names.txt", "r")
    for concurrent_name in my_file_class.readlines():
        print(concurrent_name + "\n")
my_file_class.close()