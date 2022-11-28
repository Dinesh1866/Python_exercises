# File Handling

# open() function - opens a file and returns a file object and takes two parameters: filename and mode
# mode - r - read, w - write, a - append, r+ - read and write
# f = open("file.txt","r")
# f = open("file.txt","w")
# f = open("file.txt","a")
# f = open("file.txt","r+")

'''
mode w - write - if the file does not exist, it creates a new file. If the file exists, it overwrites the existing file.'''
# f = open("file.txt","w")
# f.write("Hello World")
# f.close()