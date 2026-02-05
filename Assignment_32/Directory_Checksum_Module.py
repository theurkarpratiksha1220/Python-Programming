import os
import hashlib

def CalculateChecksum(Filename):
    try:
        file1 = open(Filename, "rb")
        content = file1.read()
        file1.close()

        hobj = hashlib.md5()
        hobj.update(content)
        return hobj.hexdigest()
    
    except Exception:
        return f"Error calculating Checksum"

def DirectoryChecksum(DirName, fobj):
    Border = "-" * 50

    try:
        if(os.path.exists(DirName) == False):
            fobj.write(f"There is no such directory named : {DirName}\n")
            return False

        if (os.path.isdir(DirName) == False):
            fobj.write(f"It is not a directory : {DirName}\n")
            return False
    
    except Exception as error_msg:
        fobj.write(f"Not able to validate the directory. Please verify : {error_msg}\n")
        return False

    fobj.write(f"{Border}\n")
    fobj.write("-------------Directory Checksum Report------------\n")
    fobj.write(f"{Border}\n")

    for FolderName, SubFolderName, Filename in os.walk(DirName):
        for fname in Filename:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(fname)

            fobj.write(f"{Border}\n")
            fobj.write(f"File Name : {fname}\n")
            fobj.write(f"Checksum  : {checksum}\n")
            fobj.write(f"{Border}\n")

    return True