from datetime import datetime
my_file = open("read_my_content2.txt","w")
my_file.write("hello from mars the time here is:" + str(datetime.now()))
my_file.close()
