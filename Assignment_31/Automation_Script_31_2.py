# Please follow below rules while designing automation script as
# - Accept input through command line or through file
# - Display any message in log file instead of console
# - For separate task define separate function
# - For robustness handle every expected exception
# - Perform validations before taking any action
# - Create user defined modules to store the functionality

# Design automation script which accept directory name and two file extensions from user. 
# Rename All files with first file extension with the second file extension.
# Usage : DirectoryRename.py “Demo” “.txt” “.doc”
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc. 
# After execution this script each .txt file gets renamed as .doc.   
# -----------------------------------------------------------------------------------------------------------------------------

import sys
import os
from Creation_LogFile_Module import Creation_LogFile
from Directory_Validation_Module import DirectoryValidate 

def FileExtensionRename(DirName, extension_Prev, extension_New, fobj):
        try:
            Border = "-"*65
            fobj.write(f"\nSearching for file with '{extension_Prev}' extension in '{DirName}' and replace with '{extension_New}' extension\n")
            fobj.write(Border + "\n")

            renamed_count = 0
            files_found = False

            for FolderName, SubFolder, FileName in os.walk(DirName):
                for fname in FileName:
                    if fname.lower().endswith(extension_Prev.lower()):
                        files_found = True
                        file_path_old = os.path.join(FolderName, fname)

                        filename_new = fname[:-len(extension_Prev)] + extension_New
                        file_path_new = os.path.join(FolderName, filename_new)

                        if not os.path.exists(file_path_new):
                            os.rename(file_path_old, file_path_new)
                            renamed_count = renamed_count + 1

                        fobj.write("File Name - Previous : "+fname+"\n")
                        fobj.write("File Name - New after Renamed : "+filename_new+"\n")
                        fobj.write("File Path of previous extension : "+file_path_old+"\n")
                        fobj.write("File Path of new renamed extension : "+file_path_new+"\n")
                        fobj.write("File Extension - Previous : "+extension_Prev+"\n")
                        fobj.write("File Extension - New : "+extension_New+"\n")
                        fobj.write(Border+"\n")
                        fobj.write(f"Renamed done successfully: {file_path_old} --> {file_path_new}\n")
                        fobj.write(Border+"\n")

            fobj.write(f"Total files renamed in directory : {renamed_count}\n")
            fobj.write(Border+"\n")

            if files_found == False:
                fobj.write(f"No files with '{extension_Prev}' extension found in '{DirName}'\n")
                fobj.write(Border+"\n")
                return False

            return True
        
        except Exception as error_msg:
            fobj.write(f"Not able to rename files. Please verify the error : {error_msg}\n")
            return False
    
def main():
        try:
             
            Border = "-"*65
            print(Border)
            print("-------- Automation script 2 - Assignment 31 ---------")
            print(Border)

            if(len(sys.argv) != 4):
                print("Invalid Number of arguments")
                print("Please specify the name of directory or extension of file to be search")
                return

            DirName = sys.argv[1]
            old_ext = sys.argv[2]
            new_ext = sys.argv[3]

            fobj = Creation_LogFile("Automation_Script_31_2")
            if fobj is None:
                print("Unable to create log file")
                return

            if not DirectoryValidate(DirName, fobj):
                fobj.close()
                return

            Ret = FileExtensionRename(DirName, old_ext, new_ext, fobj)

            if Ret:
                fobj.write("Renaming completed successfully.\n")
                print("Renaming completed successfully.")
            else:
                fobj.write("No files were renamed.\n")
                print("No files were renamed.")

            fobj.write(Border+"\n")
            fobj.close()

        except Exception as error_msg:
            print("Not able to perform the action. Please verify!", error_msg)
    
        finally:
            print("End of Automation Script")

if __name__ == "__main__":
    main()
