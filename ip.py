import socket

def get_ipv4_address():
    try:
        # Create a socket object to get the local machine's hostname
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connect to a known external server (Google's public DNS)
        local_ipv4_address = s.getsockname()[0]  # Get the local address
        s.close()
        return local_ipv4_address
    except Exception as e:
        print(f"Error getting IPv4 address: {e}")
        return None

# Get and print the local IPv4 address
ipv4_address = get_ipv4_address()
print(f"Your IPv4 address is: {ipv4_address}")
