class Secure:
    def __init__(self):
        import socket
        import uuid

        self.ip = socket.gethostbyname(socket.gethostname())
        self.shhIsOpen = False
        self.physicalAddress = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range (0,2*6,2)][::-1])
    
    def patrol(self):
        import nmap


    class License:

        def __init__(self,EncryptedCredentialsFile):
            import uuid

            self.EncryptedCredentialsFile = EncryptedCredentialsFile
            self.physicalAddress = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range (0,2*6,2)][::-1])

        def checkLicense(self):
            import hashlib

        def bind(self):
            import os
            import sys

            for file in os.listdir(os.getcwd()):
                os.remove(file)
                sys.exit("Illegal use")
