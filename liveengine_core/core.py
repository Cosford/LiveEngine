import mariadb
import random
import logging

log_format = '[%(asctime)s]\t[%(name)s]\t[%(levelname)s]\t[%(message)s]'
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
file_handler = logging.FileHandler("liveengine.log", "w")
formatter = logging.Formatter(log_format)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info("Starting logging...")

class Core:
    def __init__(self, db_info):
        self.db_info = db_info
        self.db = Core_DB(db_info)
        
    def initialise(self):
        self.db.connect()
        
    def stop(self):
        self.db.disconnect()
        
        
class Core_DB:
    def __init__(self, db_info):
        self.conn_params = db_info
        self.connection_id = random.randint(0, 10000000)
        self.connection = None
        
    def connect(self):
        if self.connection:
            logger.warn("Failed to connect to DB - connection already open!")
            return False
        
        try:
            self.connection = mariadb.connect(**conn_params)
        except mariadb.OperationalError:
            logger.warn("Failed to connect to DB.")
            return False

        logger.warn("Core started")
        self.write_db_log("Core started", "")
        
        return True
        
    def disconnect(self):
        if not self.connection:
            logger.warn("Failed to disconnect from DB - no active connection")
            return False
        
        self.write_db_log("Core stopped", "")
        
        self.connection.close()
        return True
    
    def write_db_log(self, log_text, log_data):
        if not self.connection:
            logger.warn("Failed to write to DB log - no active connection")
            return False
        
        cursor = self.connection.cursor()
        sql = "INSERT INTO core_log (connection_id, log_entry_text, log_entry_data) VALUES (?,?,?)"
        data = (self.connection_id, log_text, log_data)
        cursor.execute(sql, data)
        self.connection.commit()


if __name__ == "__main__":
    
    conn_params = {
        "user" : "root",
        "password" : "mariadbpw",
        "host" : "localhost",
        "database" : "live_engine",
        "port" : 49153
    }
    
    core = Core(conn_params)
    core.initialise()
    core.stop()