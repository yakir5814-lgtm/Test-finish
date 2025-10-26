# Task: Automate Ping Requests

while True:
    # Prompt the user to enter a server name
    server_name = input("Enter a server name to ping (or type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if server_name.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop
    
    # Simulate the ping response
    print(f"Pinging {server_name}... Ping successful.")