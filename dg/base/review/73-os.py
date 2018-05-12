import os

#os.rename("a.txt", "b.txt")
#os.remove("b.txt")
res = os.listdir("./anli")
print(res)
print(os.path.isdir("./anli/game"))
#os.mkdir("./anli/dirtest")
#os.rmdir("./anli/dirtest")
print(os.getcwd())
