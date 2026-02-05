import hashlib
import os

def CalculateChecksum(Filename):
    try:
        if os.path.getsize(Filename) == 0:
            return None
        
        file1 = open(Filename, "rb")
        content = file1.read()
        file1.close()

        hobj = hashlib.md5()
        hobj.update(content)
        return hobj.hexdigest()
    
    except Exception:
        return f"Error calculating Checksum"
    
def FindDuplicate(DirName, fobj):
    Border = "-" * 50
    Duplicate = {}

    try:
        if(os.path.exists(DirName) == False):
            fobj.write(f"There is no such directory named : {DirName}\n")
            return False

        if (os.path.isdir(DirName) == False):
            fobj.write(f"It is not a directory : {DirName}\n")
            return False

        fobj.write(f"{Border}\n")
        fobj.write("-------------Duplicate Files------------\n")
        fobj.write(f"{Border}\n")
        
        for FolderName, SubFolderName, Filename in os.walk(DirName):
            for fname in Filename:
                fname = os.path.join(FolderName,fname)
                Checksum = CalculateChecksum(fname)

                #fobj.write(f"{Border}\n")
                #fobj.write(f"File Name : {fname}\n")
                #fobj.write(f"Checksum  : {Checksum}\n")
                #fobj.write(f"{Border}\n")

                if Checksum is None:
                    continue

                if Checksum in Duplicate:
                    Duplicate[Checksum].append(fname)
                else:
                    Duplicate[Checksum] = [fname]

        duplicate_found = False
        for checksum, files in Duplicate.items():
            if len(files) > 1:
                duplicate_found = True
                fobj.write(f"\nChecksum : {checksum}\n")
                for file in files:
                    fobj.write(f"{file}\n")

        if duplicate_found:
            fobj.write("Duplicate files found in directory.\n")
        else:
            fobj.write("No duplicate files found in directory.\n")

        return Duplicate

    except Exception as error_msg:
        fobj.write(f"Error occures. Please verify : {error_msg}\n")
        return False
