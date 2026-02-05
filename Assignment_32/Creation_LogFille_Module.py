import time

def Creation_LogFile(script_name = "AutomationScript"):

    try: 
        Border = "-"*65
        timestamp = time.ctime()

        Logfilename = f"{script_name}_{timestamp}.log"
        Logfilename = Logfilename.replace(" ","_")
        Logfilename = Logfilename.replace(":","_")

        fobj = open(Logfilename,"w")

        fobj.write(Border+"\n")
        fobj.write(f"This is a log file created by {script_name}\n")
        fobj.write(Border+"\n")

        return fobj
    
    except Exception as error_msg:
        fobj.write(f"Not able to create/open log file. Please verify Error: {error_msg}\n")
        return False