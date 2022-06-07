import mariadb
import random

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
            print("Connection already open!")
            return False
            
        self.connection = mariadb.connect(**conn_params)
        if not self.connection:
            print("Connection failed")
            return False

        self.write_log("Core started", "")
        
        print("Connected")
        return True
        
    def disconnect(self):
        if not self.connection:
            print("No connection to close!")
            return False
        
        self.write_log("Core stopped", "")
        
        self.connection.close()
        return True
    
    def write_log(self, log_text, log_data):
        if not self.connection:
            print("No connection to write log to!")
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