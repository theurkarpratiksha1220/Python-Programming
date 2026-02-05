import os

def DirectoryValidate(DirName, fobj):

    try:
        if(os.path.exists(DirName) == False):
            fobj.write(f"There is no such directory named : {DirName}\n")
            return False

        if(os.path.isdir(DirName) == False):
            fobj.write(f"It is not a directory : {DirName}\n")
            return False
        
        return True
    
    except Exception as error_msg:
        fobj.write(f"Not able to validate the directory. Please verify Error : {error_msg}\n")
        return False