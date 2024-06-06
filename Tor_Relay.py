import os
import subprocess
import sys
import ctypes

def check_admin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def check_dependencies():
    try:
        subprocess.run(['tor', '--version'], check=True)
        print("Tor is installed.")
    except FileNotFoundError:
        print("Tor is not installed or not in the PATH. Installing Tor...")
        install_tor()
    except subprocess.CalledProcessError:
        print("Tor is installed but there was an issue running it.")

def install_tor():
    if os.name == 'nt':  # Windows
        print("Installing Tor on Windows using Chocolatey...")
        subprocess.run(['choco', 'install', 'tor'], check=True)
    else:  # Unix-based systems
        print("Installing Tor on Unix-based system using apt-get...")
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'tor'], check=True)
    print("Tor has been installed.")

def create_torrc(nickname, contact_info):
    torrc_content = f"""
Nickname {nickname}
ContactInfo {contact_info}

ORPort 9001
DirPort 9030
ExitPolicy reject *:*
"""
    if os.name == 'nt':  # Windows
        torrc_path = os.path.join(os.getenv('APPDATA'), 'tor', 'torrc')  # Adjust path for Windows
        os.makedirs(os.path.dirname(torrc_path), exist_ok=True)
    else:  # Unix-based systems
        torrc_path = '/etc/tor/torrc'
    
    with open(torrc_path, 'w') as file:
        file.write(torrc_content)
    print(f"torrc file created at {torrc_path}")

def start_relay():
    if os.name == 'nt':  # Windows
        subprocess.run(['sc', 'start', 'tor'], check=True)
    else:  # Unix-based systems
        subprocess.run(['sudo', 'systemctl', 'start', 'tor'], check=True)
    print("Tor relay started.")

def stop_relay():
    if os.name == 'nt':  # Windows
        subprocess.run(['sc', 'stop', 'tor'], check=True)
    else:  # Unix-based systems
        subprocess.run(['sudo', 'systemctl', 'stop', 'tor'], check=True)
    print("Tor relay stopped.")

def status_relay():
    if os.name == 'nt':  # Windows
        subprocess.run(['sc', 'query', 'tor'], check=True)
    else:  # Unix-based systems
        subprocess.run(['sudo', 'systemctl', 'status', 'tor'], check=True)

def main():
    if not check_admin():
        print("This script must be run as an administrator. Please run it again with administrative privileges.")
        sys.exit(1)

    while True:
        print("\nTor relay beta 0.001 by braydos")
        print("1. Install Tor")
        print("2. Configure Tor Relay")
        print("3. Start Tor Relay")
        print("4. Stop Tor Relay")
        print("5. Check Tor Relay Status")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            check_dependencies()
        elif choice == '2':
            nickname = input("Enter relay nickname: ")
            contact_info = input("Enter contact info: ")
            create_torrc(nickname, contact_info)
        elif choice == '3':
            start_relay()
        elif choice == '4':
            stop_relay()
        elif choice == '5':
            status_relay()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

if __name__ == "__main__":
    main()
