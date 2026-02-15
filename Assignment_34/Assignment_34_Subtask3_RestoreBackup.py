import os
import time
import sys
import schedule
import shutil
import hashlib
import zipfile
import logging
import smtplib
from email.message import EmailMessage

#----------------------------- Restore Feature ----------------------------------#
def RestoreBackup(zip_file, destination):

    try:
        print("Starting restore process...")

        if not os.path.exists(zip_file):
            print("Error: Zip file does not exist.")
            return

        os.makedirs(destination, exist_ok=True)

        zobj =  zipfile.ZipFile(zip_file, 'r')
        zobj.extractall(destination)

        logging.info(f"Backup restored from {zip_file} to {destination}")

        print("Restore completed successfully.")
        print("Restored to:", destination)

    except Exception as e:
        logging.error(f"Error during restore: {str(e)}")
        print("Restore failed:", str(e))

#----------------------------- Logging System ----------------------------------#
def LogSystem_Setup():
    os.makedirs("Logs", exist_ok=True)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = os.path.join("Logs", f"BackupLog_{timestamp}.log")

    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return log_filename

#----------------------------- Email Notification ----------------------------------#
def EmailNotification_send(log_file, zip_file):
    try:
        sender_email = "pratspythontest@gmail.com"
        sender_password = "xxxxxxxxxxxx" #add app password
        receiver_email = "prats1220314md@gmail.com"

        msg = EmailMessage()
        msg["Subject"] = "Backup Completed Successfully"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        msg.set_content(f"""
Backup Completed Successfully.
                        
Zip file created : {zip_file}

Please find attached:
1. Log File
2. Zip file
""")

        # Attach log file
        LogFileData = open(log_file, "rb")
        file_data = LogFileData.read()
        file_name = os.path.basename(log_file)
        msg.add_attachment(file_data, maintype="application",
                            subtype="octet-stream", filename=file_name)

        # Attach zip file
        if zip_file and os.path.exists(zip_file):
            ZipFileData = open(zip_file, "rb")
            file_data = ZipFileData.read()
            file_name = os.path.basename(zip_file)
            msg.add_attachment(file_data, maintype="application",
                                   subtype="octet-stream", filename=file_name)

        # Send email
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

        logging.info("Email notification sent successfully")

    except Exception as e:
        logging.error(f"Failed to send email: {str(e)}")


def make_zip(folder):
    try:
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

        zip_name = folder + "_" + timestamp + ".zip"

        #open the zip file
        zobj = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                relative = os.path.relpath(full_path, folder) 

                zobj.write(full_path, relative) 
        
        zobj.close()

        logging.info(f"Zip file created: {zip_name}")
        return zip_name
    
    except Exception as error_e:
        logging.error(f"Error while creating zip: {str(error_e)}")
        return None

def Calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path, "rb")
    
    while True:
        Data = fobj.read(1024)
        if not Data:
            break
        else:
            hobj.update(Data)
    
    fobj.close()
    return hobj.hexdigest()

def BackupFiles(Source, Destination):
    copied_files = []

    print("Creating the backup folder for backup process")

    try:
        os.makedirs(Destination, exist_ok= True)

        for root, dirs, files in os.walk(Source):
            for file in files:
                src_path = os.path.join(root, file)

                relative = os.path.relpath(src_path, Source)                   #relativepath
                dest_path = os.path.join(Destination, relative) 

                os.makedirs(os.path.dirname(dest_path), exist_ok= True)

                #copy the files if its new
                if(( not os.path.exists(dest_path)) or (Calculate_hash(src_path) != Calculate_hash(dest_path))): 
                    shutil.copy2 (src_path, dest_path) 
                    copied_files.append(relative)
                    logging.info(f"File copied: {relative}")

        return copied_files

    except Exception as error_e:
        logging.error(f"Error during backup: {str(error_e)}")
        return copied_files
    
def MarvellousDataShieldStart(Source = "Data"):

    log_file = LogSystem_Setup()

    Border = "-"*50   
    BackupName = "MarvellousBackup" 

    print(Border)
    print("Backup process started successfully at : ", time.ctime())
    print(Border)

    logging.info("Backup process started")
    logging.info(f"Source Directory: {Source}")

    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

    logging.info(f"Total files copied: {len(files)}")

    print(Border)
    print("Backup completed successfully")
    print("Files copied : ", len(files))
    print("zip file gets created : ", zip_file)
    print("Log file gets created : ", log_file)
    print(Border)

    # Send email after backup take completion
    EmailNotification_send(log_file, zip_file)

def main():

    Border = "-"*50
    print(Border)
    print("---- Marvellous Data Shield System -----")
    print(Border)

    if len(sys.argv) == 4 and sys.argv[1] == "--restore":

        zip_file = sys.argv[2]
        destination = sys.argv[3]

        log_file = LogSystem_Setup()
        RestoreBackup(zip_file, destination)

    elif(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This scipt is used to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")
            print("4 : Restore backup using --restore")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("Backup ")
            print("ScriptName.py TimeInterval SourceDirectory ")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to backed up")
            print("Restore ")
            print("ScriptName.py --restore ZipFileName DestinationFolder ")


        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    
    # python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])
        print(Border)
        print("Data Shield System started succesfully")
        print("Time interval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details") 

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)
    
if __name__ == "__main__":
    main()
