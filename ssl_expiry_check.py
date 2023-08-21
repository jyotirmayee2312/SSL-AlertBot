import json
import requests
import os

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

def main():
    try:
        with open("domains.json", "r") as file:
            domains_data = json.load(file)
            domains = domains_data["domains"]

            for domain in domains:
                # Here you can implement the logic to check SSL expiry for each domain and calculate days_to_expire
                days_to_expire = 30  # Replace with your actual calculation

                if days_to_expire <= 30:
                    send_slack_notification(domain, days_to_expire)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading or processing domains:", e)

if __name__ == "__main__":
    main()

