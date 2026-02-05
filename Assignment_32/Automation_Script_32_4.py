# Please follow below rules while designing automation script as
# - Accept input through command line or through file
# - Display any message in log file instead of console
# - For separate task define separate function
# - For robustness handle every expected exception
# - Perform validations before taking any action
# - Create user defined modules to store the functionality

# Design automation script which accept directory name and delete all Duplicate files from that directory. 
# Write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory. 
# Display execution time required for the script.
# Usage : DirectoryDuplicateRemoval.py “Demo”
# Demo is name of directory.
# -----------------------------------------------------------------------------------------------------------------------------

import sys
import os
import time
from Creation_LogFille_Module import Creation_LogFile
from DuplicatesFiles_Find_module import FindDuplicate

def main():
    start_time = time.time()
    fobj = None

    try: 
        Border = "-"*50
        print(Border)
        print("-------- Automation script 4 - Assignment 32 ---------")
        print(Border)

        fobj = Creation_LogFile("Automation_Script_32_4")
        if fobj is None:
            print("Unable to create log file")
            return
        
        if len(sys.argv) != 2:
            print("Invalid number of arguments\n")
            print("Usage : Scriptname.py <DirectoryName>\n")
            fobj.close()
            return

        Directory_Name = sys.argv[1]
        Ret = FindDuplicate(Directory_Name, fobj)

        Result = list(filter(lambda x : len(x) > 1, Ret.values()))

        Count = 0
        Cnt = 0
        for value in Result:
            for subvalue in value:
                Count = Count + 1
                if(Count > 1):
                    fobj.write(Border+"\n")
                    fobj.write(f"Deleted file : {subvalue}\n")
                    fobj.write(Border+"\n")
                    os.remove(subvalue)
                    Cnt = Cnt + 1
            Count = 0

        fobj.write(Border+"\n")
        fobj.write(f"Total deleted files : {Cnt}\n")
        fobj.write(Border+"\n")
        fobj.write("\nDuplicate file removal completed successfully\n")
        fobj.write(Border+"\n")

    except Exception as error_msg:
        print("Not able to perform action. Please verify!", error_msg)
    
    finally:
        print("End of Automation Script")
        end_time = time.time()
        if fobj:
            fobj.write(f"Execution time : {end_time - start_time: } seconds\n")
            fobj.write("Automation Script execution completed.\n")
            fobj.close()

if __name__ == "__main__":
    main()
