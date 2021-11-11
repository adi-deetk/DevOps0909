def save_names(name_to_save):
    my_file = open("names.txt", "a")
    my_file.write(name_to_save + "\n")
    my_file.close()


def show_name():
    my_file = open("names.txt")
    for name in my_file.readlines():
         print(f"hello {name}", end='')
    my_file.close()

save_names("haim")
save_names("moshe")
save_names("david")
show_name()



    # with open("names.txt", "r") as my_file:
    #     for name in my_file.readlines():
    #         print("current name is: " + name, end='')

#for i in range(4):
 #   save_names()

#show_name()