import logging
import os
from datetime import datetime

class LogGen:
    @staticmethod
    def loggen():
        # Create 'logs' folder if it doesn't exist
        LogGen.create_logs_folder()
        # Delete log files before initializing the logger
        LogGen.delete_old_logs()

        logger = logging.getLogger()
        log_file_path = os.path.join('logs', f'automation_{datetime.now().strftime("%Y-%m-%d_%H.%M.%S")}.log')
        fhandler = logging.FileHandler(filename=log_file_path, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def delete_old_logs():
        log_folder = 'logs'
        for file_name in os.listdir(log_folder):
            file_path = os.path.join(log_folder, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    @staticmethod
    def create_logs_folder():
        log_folder = 'logs'
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

if __name__ == "__main__":
    # Example of usage
    logger = LogGen.loggen()
    logger.info("This is an informational message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
