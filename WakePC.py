import paramiko

IP = ""
USER = ""
PASS = ""
CMD = ""

# Create a new SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote machine
client.connect(IP, username=USER, password=PASS)

# Execute the command
stdin, stdout, stderr = client.exec_command(CMD)

# Print the output of the command
for line in stdout:
    print(line.strip())

# Close the SSH client
client.close()
