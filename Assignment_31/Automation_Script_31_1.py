# Please follow below rules while designing automation script as
# - Accept input through command line or through file
# - Display any message in log file instead of console
# - For separate task define separate function
# - For robustness handle every expected exception
# - Perform validations before taking any action
# - Create user defined modules to store the functionality

# Design automation script which accept directory name and file extension from user. Display all Files with that extension.
# Usage : DirectoryFileSearch.py “Demo” “.txt”
# Demo is name of directory and .txt is the extension that we want to search.
# -----------------------------------------------------------------------------------------------------------------------------

import sys
import os
from Creation_LogFile_Module import Creation_LogFile
from Directory_Validation_Module import DirectoryValidate 

def ScanDirectory(DirName, extension, fobj):
        try:
            Border = "-"*65
            fobj.write(f"\nSearching for file with '{extension}' extension in '{DirName}'\n")
            fobj.write(Border + "\n")

            files_found = False

            for FolderName, SubFolder, FileName in os.walk(DirName):
                for fname in FileName:
                    if fname.lower().endswith(extension.lower()):
                        files_found = True
                        file_path = os.path.join(FolderName, fname)

                        fobj.write("File Name : "+fname+"\n")
                        fobj.write("File Path : "+file_path+"\n")
                        fobj.write("File Extension : "+extension+"\n")
                        fobj.write(Border+"\n")

            if files_found == False:
                fobj.write(f"No files with '{extension}' extension found in '{DirName}'\n")
                fobj.write(Border+"\n")
                return False

            return True

        except Exception as error_msg:
            fobj.write(f"Not able to scan the directory. Please verify the error : {error_msg}\n")
            return False
        
def DirectoryScanner(DirName, extension):

    fobj = Creation_LogFile("Automation_script_31_1")
    if fobj is None:
        return False
        
    try:
        if not DirectoryValidate(DirName, fobj):
            return False
        
        if not extension.startswith("."):
            extension = "." + extension

        ScanDirectory(DirName, extension, fobj)
        return True

    except Exception  as error_msg:
        fobj.write(f"Not able to scan the directory. Please verify the error : {error_msg}\n")
        return False

    finally:
        fobj.close()
    
def main():
    try:
        Border = "-"*65
        print(Border)
        print("-------- Automation script 1 - Assignment 31 ---------")
        print(Border)

        if(len(sys.argv) != 3):
            print("Invalid Number of arguments")
            print("Please specify the name of directory or extension of file to be search")
            return

        Directory_Name = sys.argv[1]
        Extension_Name = sys.argv[2]

        fobj = Creation_LogFile("Automation_Script_31_1")
        if fobj is None:
            print("Unable to create log file")
            return
        
        Ret = DirectoryScanner(Directory_Name, Extension_Name)

        if Ret:
            fobj.write("Displayed files successfully.\n")
            print("Displayed files successfully.")
        else:
            fobj.write("No files were displayed.\n")
            print("No files were displayed.")

        fobj.write(Border+"\n")
        fobj.close()

    except Exception as error_msg:
        print("Not able to perform action. Please verify!", error_msg)
    
    finally:
        print("End of Automation Script")

if __name__ == "__main__":
    main()
