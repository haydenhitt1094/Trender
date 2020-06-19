class Secure:
    def __init__(self):
        import socket
        self.ip = socket.gethostbyname(socket.gethostname())
        self.shhIsOpen = False
    
    def closeExploits(self):
        import nmap

        