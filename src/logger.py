import logging  #for creating the logger file
import os
from datetime  import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   #for the formate of the file
log_path= os.path.join(os.getcwd(),"logs",LOG_FILE)   #for the storing log file
os.makedirs(log_path,exist_ok=True)       # creating the file and exit_ok is denoting even if file is there the we need to keep appending the log file

LOG_FILE_PATH =os.path.join(log_path,LOG_FILE) 

logging.basicConfig(
    
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s-%(levelname)s - %(message)s",
    level= logging.INFO,

)

