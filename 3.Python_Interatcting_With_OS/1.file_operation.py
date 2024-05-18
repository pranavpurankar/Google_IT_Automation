import os
import datetime

# remove the file 
#os.remove("/home/prns/Downloads/GoogleAutomation/2.Interact_with_OS/novel.txt")

# rename the file
#os.rename("/home/prns/Downloads/GoogleAutomation/2.Interact_with_OS/first_draft.tx", "/home/prns/Downloads/GoogleAutomation/2.Interact_with_OS/final_draft.txt")

# check path exist or not
path_exist = os.path.exists("/home/prns/Downloads/GoogleAutomation/2.Interact_with_OS/finished_masterpiece.txt")

path_exist_1 = os.path.exists("/home/prns/Downloads/GoogleAutomation/2.Interact_with_OS/first_draft.txt")

# getsize
size = os.path.getsize("/home/prns/Downloads/GoogleAutomation/2.Interact_with_OS/size.txt")
print(f"Size of file {size}")

#timestamp
timestamp=os.path.getmtime("/home/prns/Downloads/GoogleAutomation/2.Interact_with_OS/size.txt")
print(datetime.datetime.fromtimestamp(timestamp))

print(path_exist)
print(path_exist_1)

print("\n\nDirectories in OS module\n")
print("This prints the current working directory",os.getcwd())
print("This changes the current working diretory",os.chdir("/home/prns/Downloads/GoogleAutomation/"))
print("This creates a new directory",os.mkdir("/home/prns/Downloads/GoogleAutomation/2.Interact_with_OS/Newer_dir"))


dir = "/home/prns/Downloads/GoogleAutomation/2.Interact_with_OS/"
for name in os.listdir(dir):
    fullname = os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))



print("This deletes a new directory",os.rmdir("/home/prns/Downloads/GoogleAutomation/2.Interact_with_OS/Newer_dir"))
