Tor Relay Setup Script

Version: Beta 0.0001

Description
-----------
This script provides a simple command-line interface (CLI) for setting up and managing a Tor relay. The script is designed to be user-friendly and guides users through the process of installing Tor, configuring the relay, starting and stopping the relay, and checking the relay's status.

Features
--------
- Installation: Automatically installs Tor on both Windows and Unix-based systems.
- Configuration: Helps you create a torrc configuration file with your chosen nickname and contact information.
- Management: Allows you to start, stop, and check the status of your Tor relay with easy-to-use commands.

Menu Options
------------
- 1. Install Tor: Checks if Tor is installed and installs it if necessary.
- 2. Configure Tor Relay: Prompts for a relay nickname and contact information, then creates the torrc configuration file.
- 3. Start Tor Relay: Starts the Tor relay.
- 4. Stop Tor Relay: Stops the Tor relay.
- 5. Check Tor Relay Status: Checks the current status of the Tor relay.
- 0. Exit: Exits the script.

Requirements
------------
- Python 3.x
- Administrative privileges: The script must be run as an administrator to perform installations and manage services.

Installation
------------
1. Clone the Repository:
   git clone https://github.com/yourusername/tor-relay-setup.git
   cd tor-relay-setup

2. Install Dependencies:
   Ensure you have chocolatey installed on Windows for installing Tor. On Unix-based systems, ensure you have apt-get.

   Install PyInstaller:
   pip install pyinstaller

Usage
-----
1. Run the Script:
   On Windows:
   python Tor_Relay.py

   On Unix-based systems:
   sudo python3 Tor_Relay.py

2. Create Executable:
   To create a standalone executable:
   pyinstaller --onefile Tor_Relay.py

   The executable will be located in the dist directory.

3. Run the Executable:
   cd dist
   Tor_Relay.exe

Example Output
--------------
Tor relay beta 0.002 by braydos
1. Install Tor
2. Configure Tor Relay
3. Start Tor Relay
4. Stop Tor Relay
5. Check Tor Relay Status
0. Exit

Enter your choice:

Contributing
------------
Feel free to fork this project, submit issues and pull requests.
