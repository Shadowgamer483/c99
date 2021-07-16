import time
import shutil
import os

def main():
    deletedfolderscount=0
    deletedfilescount=0
    path="/path_to_delet"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootfolders,folder,files in os.walk(path):
            removefolder(rootfolders)
            deletedfolderscount=deletedfolderscount+1
            break
    else:
        for folder in folders:
            folder_path=os.path.join(rootfolders,folder)
            if seconds >=getfolderage(folder_path):
                 removefolder(folder_path)
                 deletedfolderscount+=1
        for file in files:
            file_path=os.path.join(rootfolders,file)
             if seconds >=getfolderage(folder_path):
                 removefile(file_path)
                 deletedfilescount+=1
    else:
        if seconds>=getfolderage(path):
            removefile(path)
            deletedfilescount+=1
    else:
        print(f'"{path}"is not found' )         
        deletfilescount+=1  
    print(f'total folder deleted:{deletedfoldercount}')     
    print(f'total files deleted:{deletedfilescount}')
def removefolder(path):
    if not shutil.rmtree(path):
        print(f'{path}is removed sucessfully')
    else:
        print(f'unable to delet'+path)
def removefile(path):
    if not os.remove(path):
        print(f'{path}is removed sucessfully')
    else:
        print(f'unable to delet'+path)
def getfolderage(path):
    ctime=os.stat(path).st_ctime
    return ctime
if __name__=="__main__":
    main()




