import os

def shutdown():
    """Shutdown the computer."""
    os.system("shutdown /s /t 1")

def logout():
    """Log out the current user."""
    os.system("shutdown /l")

def restart():
    """Restart the computer."""
    os.system("shutdown /r /t 1")

# Prompt the user for their choice
print("1. Shutdown")
print("2. Logout")
print("3. Restart")
choice = input("Enter your choice (1/2/3): ")

# Call the appropriate function based on the user's choice
if choice == '1':
    shutdown()
elif choice == '2':
    logout()
elif choice == '3':
    restart()
else:
    print("Invalid choice.")
