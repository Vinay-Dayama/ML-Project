import logging,os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #most probably name of the log file
# unique log file would be created evertime
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# if error arises , then in the above line remove ,LOG_FILE
 #most probably folder in which it would be stored
os.makedirs(logs_path,exist_ok=True) # 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) # selecting the file from folders (just duplicating)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] - %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
