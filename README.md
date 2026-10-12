# Tool Name: IOC Extractor

### Objective:
To parse and extract key Indicators of Compromise (IPs and Domains) from security logs or unstructured text data.

### Features:
- Regular Expression-based high-speed extraction.
- Deduplication of extracted threats using sets.
- Command-line argument handling.

### Requirements:
- Python 3.x Installed.

### How to Run:
python3 tool.py sample.txt

### Example Usage:
python3 tool.py <logfile_path>

### Example Output:
[+] IP Addresses Found (1): 192.168.43.10
[+] Domains Found (1): evil-hacker.com

### Challenges Faced:
Fixed parameter parsing bugs and handled file processing without external third-party dependencies (offline compatibility).

### Future Improvements:
- Add integration with VirusTotal API to check malicious scores.
- Support for parsing multi-format logs (.json, .csv).
-
