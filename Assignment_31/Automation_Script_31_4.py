# Please follow below rules while designing automation script as
# - Accept input through command line or through file
# - Display any message in log file instead of console
# - For separate task define separate function
# - For robustness handle every expected exception
# - Perform validations before taking any action
# - Create user defined modules to store the functionality

# Design automation script which accept two directory names and one file extension . Copy All files with specified 
# extension from first directory into second directory. Second directory should be created at run time.
# Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
# Demo is name of directory which is existing and contains files in it. We have to create new directory as Temp and copy all Files 
# with extension .exe from Demo to Temp.
# -----------------------------------------------------------------------------------------------------------------------------

import sys
import os
from Creation_LogFile_Module import Creation_LogFile
from Directory_Validation_Module import DirectoryValidate 

def DirectoryCopy(DirName_Source, DirName_Target, extension, fobj):
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

                if os.path.isfile(Dir_Source_Path) and fname.lower().endswith(extension.lower()):
                     File_Source = open(Dir_Source_Path, "rb")
                     File_Target = open(Dir_Target_Path, "wb")

                     Content = File_Source.read()
                     File_Target.write(Content)

                     File_Source.close()
                     File_Target.close()

                     fobj.write("File copied successfully\n")
                     fobj.write(f"File Name : {fname}\n")
                     fobj.write(f"Source path : {Dir_Source_Path}\n")
                     fobj.write(f"Target path : {Dir_Target_Path}\n")
                     fobj.write(Border+"\n")

                     files_copied = files_copied + 1
            
            if files_copied == 0:
                fobj.write(f"No files with '{extension}' extension found in '{DirName_Source}'\n")
                fobj.write(Border+"\n")
                return False
            
            return True
        
        except Exception as error_msg:
            fobj.write(f"Not able to copy files! Plaese verify the error : {error_msg}\n")
            return False
    
def main():

        Border = "-"*65
        print(Border)
        print("-------- Automation script 4 - Assignment 31 ---------")
        print(Border)

        fobj = Creation_LogFile("Automation_Script_31_4")
        if fobj is None:
            print("Unable to create log file")
            return

        if(len(sys.argv) != 4):
            print("Invalid Number of arguments")
            print("Please specify the name of directory or extension of file to be search")
            fobj.close()
            return

        DirName_Source = sys.argv[1]
        DirName_Target = sys.argv[2]
        extension = sys.argv[3]

        if not DirectoryValidate(DirName_Source, fobj):
            fobj.close()
            return

        Ret = DirectoryCopy(DirName_Source, DirName_Target, extension, fobj)

        if Ret:
            fobj.write("All files copied from existing directory to new target directory with specified extension\n")
            print("All files copied from existing directory to new target directory with specified extension.")
        else:
            fobj.write("No files were copied.\n")
            print("No files were copied.")

        fobj.write(Border+"\n")
        fobj.close()

if __name__ == "__main__":
    main()