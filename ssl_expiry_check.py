import json
import requests
import os
import ssl
import socket
import datetime

def send_slack_notification(domain, days_to_expire):
    message = f"SSL Expiry Alert\n   * Domain: {domain}\n   * Warning: The SSL certificate for {domain} will expire in {days_to_expire} days."
    payload = {
        "text": message
    }

    try:
        response = requests.post(os.environ["SLACK_WEBHOOK"], json=payload)
        response.raise_for_status()
        print(f"Notification sent for {domain}")
    except requests.exceptions.RequestException as e:
        print("Error sending Slack notification:", e)

def check_ssl_expiry(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as tls_sock:
            cert = tls_sock.getpeercert()
            expiry_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
            days_until_expiry = (expiry_date - datetime.datetime.now()).days
            return days_until_expiry

def main():
    try:
        with open("domains.json", "r") as file:
            domains_data = json.load(file)
            domains = domains_data["domains"]

            for domain in domains:
                try:
                    days_to_expire = check_ssl_expiry(domain)

                    if days_to_expire <= 30:
                        send_slack_notification(domain, days_to_expire)
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching SSL certificate for {domain}:", e)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading or processing domains:", e)

if __name__ == "__main__":
    main()
