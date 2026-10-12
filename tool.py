import re
import sys

def show_help():
    print("📌 IOC Extractor Tool")
    print("Usage: python3 tool.py <filename>")
    print("Example: python3 tool.py logs.txt")

def extract_iocs(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            
        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        domain_pattern = r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}\b'
        
        ips = set(re.findall(ip_pattern, content))
        domains = set(re.findall(domain_pattern, content))
        
        print("=====================================")
        print("🔍 EXTRACTED INDICATORS OF COMPROMISE 🔍")
        print("=====================================")
        
        print(f"\n[+] IP Addresses Found ({len(ips)}):")
        for ip in ips:
            print(f"  📍 {ip}")
            
        print(f"\n[+] Domains Found ({len(domains)}):")
        for domain in domains:
            if not domain.endswith(('.txt', '.log', '.sh', '.py')):
                print(f"  🌐 {domain}")
        print("=====================================")
        
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

def main():
    if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help']:
        show_help()
        sys.exit(1)
        
    extract_iocs(sys.argv[1])

if __name__ == "__main__":
    main()
