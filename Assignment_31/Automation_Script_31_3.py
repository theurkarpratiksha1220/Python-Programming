# Please follow below rules while designing automation script as
# - Accept input through command line or through file
# - Display any message in log file instead of console
# - For separate task define separate function
# - For robustness handle every expected exception
# - Perform validations before taking any action
# - Create user defined modules to store the functionality

# Design automation script which accept two directory names. Copy all Files from first directory into second directory. 
# Second directory should be created at run time.
# Usage : DirectoryCopy.py “Demo” “Temp”
# Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files from Demo to Temp.
# -----------------------------------------------------------------------------------------------------------------------------

import sys
import os
from Creation_LogFile_Module import Creation_LogFile
from Directory_Validation_Module import DirectoryValidate 

def DirectoryCopy(DirName_Source, DirName_Target, fobj):
        try:
            Border = "-"*65

            if not os.path.exists(DirName_Target):
                 os.makedirs(DirName_Target)
                 fobj.write(f"New Target '{DirName_Target}' directory created successfully\n")
                 fobj.write(Border+"\n")

            files_copied = 0

            for fname in os.listdir(DirName_Source):
                Dir_Source_Path = os.path.join(DirName_Source, fname)    
                Dir_Target_Path = os.path.join(DirName_Target, fname)  

                if os.path.isfile(Dir_Source_Path):
                     File_Source = open(Dir_Source_Path, "rb")
                     File_Target = open(Dir_Target_Path, "wb")

                     Content = File_Source.read()
                     File_Target.write(Content)

                     File_Source.close()
                     File_Target.close()

                     fobj.write("File copied successfully\n")
                     fobj.write(f"Source path : {Dir_Source_Path}\n")
                     fobj.write(f"Target path : {Dir_Target_Path}\n")
                     fobj.write(f"File Name - Source : {fname}\n")
                     fobj.write(f"File Name - Target : {fname}\n")
                     fobj.write(Border+"\n")


                     files_copied = files_copied + 1

            fobj.write(f"Total number of files copied from Source Directory into Target Directory : {files_copied}\n")
            fobj.write(Border+"\n")
            
            if files_copied == 0:
                fobj.write(f"No files found in '{DirName_Source}'\n")
                fobj.write(Border+"\n")
                return False
            
            return True
        
        except Exception as error_msg:
            fobj.write(f"Not able to perform the action. Please verify the error : {error_msg}\n")
            return False
    
def main():
        try:
            Border = "-"*65
            print(Border)
            print("-------- Automation script 3 - Assignment 31 ---------")
            print(Border)

            fobj = Creation_LogFile("Automation_Script_31_3")
            if fobj is None:
                print("Unable to create log file")
                return

            if(len(sys.argv) != 3):
                print("Invalid Number of arguments")
                print("Please specify the name of directory or extension of file to be search")
                fobj.close()
                return

            DirName_Source = sys.argv[1]
            DirName_Target = sys.argv[2]

            if not DirectoryValidate(DirName_Source, fobj):
                fobj.close()
                return

            Ret = DirectoryCopy(DirName_Source, DirName_Target, fobj)

            if Ret:
                fobj.write("All files copied from existing directory to new target directory\n")
                print("All files copied from existing directory to new target directory.")
            else:
                fobj.write("No files were copied.\n")
                print("No files were copied.")

            fobj.write(Border+"\n")
            fobj.close()

        except Exception as error_msg:
            print("Not able to perform the action. Please verify!", error_msg)
    
        finally:
            print("End of Automation Script")

if __name__ == "__main__":
    main()