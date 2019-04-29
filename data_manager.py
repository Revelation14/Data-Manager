import os

for f in os.listdir():
    fn,fext=os.path.splitext(f)
    if not os.path.isdir("Data"):
        os.mkdir("Data")
    if f == "data_manager.py":
        continue
    if fext[1:] not in os.listdir("Data") and fext !="":
        os.mkdir("Data\\{}".format(fext[1:]))
    try:
        if fext!="":
            os.rename("{}".format(f),"Data\\{}\\{}".format(fext[1:],f))
    except FileExistsError:
        print(f)
