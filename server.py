from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Create an authorizer object with a user
authorizer = DummyAuthorizer()
authorizer.add_user("user", "pass", "./", perm="elradfmw")

# Instantiate an FTP handler with the authorizer
handler = FTPHandler
handler.authorizer = authorizer

# Create the FTP server
server = FTPServer(("0.0.0.0", 5000), handler)

# Start the server
server.serve_forever()
