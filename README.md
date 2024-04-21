# WiFiPassAndEncrypt
# WiFi Information Extraction and Email Sending Script

This script is designed to extract WiFi network information from different operating systems (Windows, macOS, Linux), compile it into a single file, and send it via email. It also includes functionalities to sign setup scripts, encrypt information files, and delete temporary files.

## Features

- **Cross-platform**: Works on Windows, macOS, and Linux.
- **WiFi Information Extraction**: Extracts WiFi network names and keys from the system.
- **Email Sending**: Sends the extracted WiFi information via email using SMTP.
- **Security**: Includes functions to sign setup scripts using GPG and encrypt information files.
- **Clean-up**: Removes temporary files after execution.

## How to Use

1. Clone the repository to your local machine.
2. Make sure you have Python installed on your system.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Modify the script to include your email credentials (`YOUR_USERNAME` and `YOUR_PASSWORD`).
5. Run the script using `python main.py`.
6. Check your email for the sent message containing WiFi information.

## Dependencies

- `smtplib`: For sending emails via SMTP.
- `email`: For constructing email messages.
- `csv`: For working with CSV files.
- `subprocess`: For executing system commands.
- `os`: For interacting with the operating system.
- `glob`: For file pattern matching in Linux.
  
## Note

- Make sure to use a testing email account or a disposable email service for sending emails to avoid disclosing sensitive information.
- Use caution when running scripts that delete files from your system.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

