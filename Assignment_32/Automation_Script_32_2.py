# Please follow below rules while designing automation script as
# - Accept input through command line or through file
# - Display any message in log file instead of console
# - For separate task define separate function
# - For robustness handle every expected exception
# - Perform validations before taking any action
# - Create user defined modules to store the functionality

# Design automation script which accept directory name and write names of duplicate files from that directory into log
# file named as Log.txt. Log.txt file should be created into current directory.
# Usage : DirectoryDuplicate.py “Demo”
# Demo is name of directory.
# -----------------------------------------------------------------------------------------------------------------------------

import sys
from Creation_LogFille_Module import Creation_LogFile
from DuplicatesFiles_Find_module import FindDuplicate

def main():
    try: 
        Border = "-"*50
        print(Border)
        print("-------- Automation script 2 - Assignment 32 ---------")
        print(Border)

        fobj = Creation_LogFile("Automation_Script_32_2")
        if fobj is None:
            print("Unable to create log file")
            return
        
        if len(sys.argv) != 2:
            print("Invalid number of arguments\n")
            print("Usage : scriptname.py <DirectoryName>\n")
            fobj.close()
            return

        Directory_Name = sys.argv[1]

        Ret = FindDuplicate(Directory_Name, fobj)
         
        if Ret:
            fobj.write("Displayed duplicate files successfully.\n")
            print("Displayed duplicate files successfully.")
        else:
            fobj.write("No duplicate files were displayed.\n")
            print("No duplicate files were displayed.")

        fobj.write(Border+"\n")
        fobj.close()

    except Exception as error_msg:
        print("Not able to perform action. Please verify!", error_msg)
    
    finally:
        print("End of Automation Script")

if __name__ == "__main__":
    main()
