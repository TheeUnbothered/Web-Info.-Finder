# Domain Information Gathering Script

This script gathers various types of information about a specified domain, such as WHOIS details, IP address, HTTP headers, and DNS records. The script is designed to be user-friendly and allows you to choose which information you want to retrieve. It uses ANSI colors to enhance readability and displays a styled name at the top of the interface.

## Features

- **IP Address Retrieval**: Retrieves the IP address of the given domain.
- **HTTP Headers**: Fetches HTTP headers of the given domain.
- **WHOIS Information**: Fetches WHOIS information using the WHOIS XML API.
- **DNS Records**: Retrieves DNS records (A, NS, MX, TXT) using the `dig` command.
- **Styled User Interface**: Displays a styled name (`THEEUNBOTHERED`) at the top and uses color-coded options for clarity.

## Requirements

- Python 3.x
- `requests` module: Install via `pip install requests`
- `socket` and `subprocess` (built-in Python libraries)
- `dig` command-line tool for DNS queries (installable via package managers like `apt`, `yum`, or `brew`)

## Setup

1. **Clone the repository** or download the script files to your local machine.
2. **Create a configuration file** named `config.py` in the same directory as the script.
3. In `config.py`, add your WHOIS API key as follows:

    ```python
    WHOIS_API_KEY = "your_whois_xml_api_key_here"
    ```

4. **Install dependencies**:
   ```bash
   pip install requests

   USAGE
Run the script:

python run.py
The script will clear the screen, display your styled name, and list available options. You will see the following options:

(1. IP Address)
(2. HTTP Headers)
(3. WHOIS Information)
(4. DNS Records)
(5. All of the above)
Enter your choice (1-5) and provide the target domain (e.g., example.com or https://example.com).

The script will retrieve and display the information based on your choice.

Example
THEEUNBOTHERED

Select the information you want to gather:
(1. IP Address)
(2. HTTP Headers)
(3. WHOIS Information)
(4. DNS Records)
(5. All of the above)

Enter your choice (1-5): 3
Enter target domain (e.g., example.com or https://example.com): example.com
Notes
WHOIS API: You need a WHOIS XML API key to retrieve WHOIS information. Visit WHOIS XML API to get an API key.
DNS Queries: The dig command is required for DNS queries. Ensure it is installed on your system.

License
This project is open-source and available for anyone to use.

Happy domain information gathering!

This `README.md` provides detailed instructions on setting up, configuring, and running your script. Let me know if there’s anything specific you’d like added or adjusted!


