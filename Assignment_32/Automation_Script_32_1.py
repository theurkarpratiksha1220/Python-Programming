# Please follow below rules while designing automation script as
# - Accept input through command line or through file
# - Display any message in log file instead of console
# - For separate task define separate function
# - For robustness handle every expected exception
# - Perform validations before taking any action
# - Create user defined modules to store the functionality

# Design automation script which accept directory name and display checksum of all Files.
# Usage : DirectoryChecksumpy “Demo” 
# Demo is name of directory.
# -----------------------------------------------------------------------------------------------------------------------------

import sys
from Directory_Checksum_Module import DirectoryChecksum
from Creation_LogFille_Module import Creation_LogFile

def main():
    try :
        Border = "-"*50
        print(Border)
        print("-------- Automation script 1 - Assignment 32 ---------")
        print(Border)

        fobj = Creation_LogFile("Automation_Script_32_1")
        if fobj is None:
            print("Unable to create log file")
            return
        
        if len(sys.argv) != 2:
            print("Invalid number of arguments")
            print("Usage : scriptname.py Demo")
            fobj.close()
            return

        Directory_Name = sys.argv[1]

        Ret = DirectoryChecksum(Directory_Name, fobj)

        if Ret:
            fobj.write("Displayed checksum successfully.\n")
            print("Displayed checksum successfully.")
        else:
            fobj.write("No checksum was displayed.\n")
            print("No checksum was displayed.")

        fobj.write(Border+"\n")
        fobj.close()

    except Exception as error_msg:
        print("Not able to perform action. Please verify!", error_msg)
    
    finally:
        print("End of Automation Script")

if __name__ == "__main__":
    main()

