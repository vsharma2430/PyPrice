class security:
    security_name:str
    security_desc:str
    fetch_address:str
    
    def __init__(self,security_name,fetch_address:str):
        self.security_name = security_name
        self.fetch_address = fetch_address
        pass