"""
file = open("example.txt","w")
file.write("HEllO WORLD")
file.close()


file = open("example.txt","r")
contents = file.read()
print(contents)
file.close()
"""

file = open("example.txt","a")
file.write("\nTHis is sandeep")
file.close()