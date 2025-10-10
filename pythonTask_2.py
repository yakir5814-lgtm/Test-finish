# Assuming the server names are stored in the 'servers' list from Task 1
servers = []
for _ in range(3):
    server = input("Enter the name of a server: ")
    servers.append(server)

# Step 2: Assign IP Addresses to Servers
ip_addresses = {}  # Create an empty dictionary

for server in servers:
    ip = input(f"Enter the IP address for {server}: ")
    ip_addresses[server] = ip  # Populate the dictionary

# Print the dictionary in a readable format
print("\nThe IP addresses assigned to the servers are:")
for server, ip in ip_addresses.items():
    print(f"Server: {server}, IP Address: {ip}")