import os
import subprocess
from datetime import datetime

def run_command(command):
    try:
        print(f"[*] Running: {' '.join(command)}")
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running command: {' '.join(command)}\n{e.stderr}")
        return f"Error running command: {e.stderr}"

def run_theharvester(domain):
    print("[*] Running theHarvester...")
    return run_command(["theHarvester", "-d", domain, "-b", "google"])

def run_shodan(domain):
    print("[*] Running Shodan...")
    return run_command(["shodan", "host", domain])

def run_whois(domain):
    print("[*] Running WHOIS...")
    return run_command(["whois", domain])

def run_dnsrecon(domain):
    print("[*] Running DNS Recon...")
    return run_command(["dnsrecon", "-d", domain])

def generate_report(domain, results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"recon_report_{domain}_{timestamp}.txt"
    print("\n[*] Generating report...")
    with open(report_file, "w") as report:
        report.write(f"Reconnaissance Report for {domain}\n{'='*40}\n")
        report.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for tool, output in results.items():
            report.write(f"{tool} Results\n{'-'*20}\n{output}\n\n")
    print(f"[+] Report saved to {report_file}")

def display_results(results):
    print("\n[*] Displaying results...")
    for tool, output in results.items():
        print(f"\n{tool} Results\n{'-'*20}\n{output}")

def main():
    print("Welcome to Reconnaissance Automation")
    domain = input("Enter the domain to investigate: ")

    print("\nChoose Output Format:")
    print("1. Display results on the terminal")
    print("2. Save results as a report")
    choice = input("Enter your choice (1 or 2): ")

    if choice not in ["1", "2"]:
        print("[!] Invalid choice. Exiting.")
        return

    # Run tools and collect results
    results = {
        "theHarvester": run_theharvester(domain),
        "Shodan": run_shodan(domain),
        "WHOIS": run_whois(domain),
        "DNS Recon": run_dnsrecon(domain),
    }

    if choice == "1":
        display_results(results)
    elif choice == "2":
        generate_report(domain, results)

    print("\n[+] Process completed. Thank you!")

if __name__ == "__main__":
    main()

