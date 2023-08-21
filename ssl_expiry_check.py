import json
import requests
import os
from datetime import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend

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

def calculate_days_until_expiry(cert_data):
    cert = x509.load_pem_x509_certificate(cert_data, default_backend())
    expiration_date = cert.not_valid_after
    current_date = datetime.utcnow()
    days_until_expiry = (expiration_date - current_date).days
    return days_until_expiry

def main():
    try:
        with open("domains.json", "r") as file:
            domains_data = json.load(file)
            domains = domains_data["domains"]

            for domain in domains:
                try:
                    # Retrieve SSL certificate for the domain and calculate days_until_expiry
                    response = requests.get(f"https://{domain}")
                    cert_data = response.content
                    days_to_expire = calculate_days_until_expiry(cert_data)

                    if days_to_expire <= 30:
                        send_slack_notification(domain, days_to_expire)
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching SSL certificate for {domain}:", e)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading or processing domains:", e)

if __name__ == "__main__":
    main()
