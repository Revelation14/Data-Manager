import os,sys

def existing_folder(ff,main_folder):
    for file in os.listdir("Data\\{}".format(ff)):
                if file in os.listdir("Data\\{}\\{}".format(main_folder,ff)):
                    fn,fext=os.path.splitext(file)
                    os.rename("Data\\{}\\{}".format(ff,file),"Data\\{}\\{}\\{}".format(main_folder,ff,fn+"1"+fext))
                else:
                    os.rename("Data\\{}\\{}".format(ff,file),"Data\\{}\\{}\\{}".format(main_folder,ff,file))
    os.rmdir("Data\\{}".format(ff))

for f in os.listdir():
    fn,fext=os.path.splitext(f)
    if not os.path.isdir("Data"):
        os.mkdir("Data")
    if not os.path.isdir("Data\\Photos"):
        os.mkdir("Data\\Photos")
    if not os.path.isdir("Data\\Videos"):
        os.mkdir("Data\\Videos")
    if not os.path.isdir("Data\\Music"):
        os.mkdir("Data\\Music")
    if not os.path.isdir("Data\\Programs"):
        os.mkdir("Data\\Programs")
    if not os.path.isdir("Data\\Documents"):
        os.mkdir("Data\\Documents")
    if not os.path.isdir("Data\\Compressed"):
        os.mkdir("Data\\Compressed")
    if not os.path.isdir("Data\\Others"):
        os.mkdir("Data\\Others")
    
    if f == os.path.basename(sys.argv[0]):
        continue
    if fext[1:] not in os.listdir("Data") and fext !="":
        os.mkdir("Data\\{}".format(fext[1:]))
    try:
        if fext!="":
            os.rename("{}".format(f),"Data\\{}\\{}".format(fext[1:],f))
    except FileExistsError:
        print(f)
for ff in os.listdir("Data"):
    if ff in ['mp3','wav']:
        if ff in os.listdir("Data\\Music"):
            existing_folder(ff,"Music")
        else:
            os.rename("Data\\{}".format(ff),"Data\\Music\\{}".format(ff))
    elif ff in ['mp4','avi','mpeg','flv','wmv','3gp']:
        if ff in os.listdir("Data\\Videos"):
            existing_folder(ff,"Videos")
        else:
            os.rename("Data\\{}".format(ff),"Data\\Videos\\{}".format(ff))
    elif ff in ['csv','docx','pdf','rtf','py']:
        if ff in os.listdir("Data\\Documents"):
            existing_folder(ff,"Documents")
        else:
            os.rename("Data\\{}".format(ff),"Data\\Documents\\{}".format(ff))
    elif ff in ['exe']:
        if ff in os.listdir("Data\\Programs"):
            existing_folder(ff,"Programs")
        else:
            os.rename("Data\\{}".format(ff),"Data\\Programs\\{}".format(ff))
    elif ff in ['rar','zip','iso']:
        if ff in os.listdir("Data\\Compressed"):
            existing_folder(ff,"Compressed")
        else:
            os.rename("Data\\{}".format(ff),"Data\\Compressed\\{}".format(ff))    
    elif ff in ['jpg','png','jpeg','ico']:
        if ff in os.listdir("Data\\Photos"):
            existing_folder(ff,"Photos")
        else:
            os.rename("Data\\{}".format(ff),"Data\\Photos\\{}".format(ff))
    elif ff not in ['Music','Videos','Documents','Programs','Others','Photos','Compressed']:
        if ff in os.listdir("Data\\Others"):
            existing_folder(ff,"Others")
        else:
            os.rename("Data\\{}".format(ff),"Data\\Others\\{}".format(ff))
    

            
