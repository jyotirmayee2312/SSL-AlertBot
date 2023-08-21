## SSL Expiry Check GitHub Actions Documentation

### Overview

The SSL Expiry Check GitHub Actions project automates the monitoring of SSL certificate expiration for a list of domains. It sends Slack notifications when certificates are about to expire within a certain threshold. This documentation offers a detailed understanding of how to set up, configure, and customize the project.

### Prerequisites

- A GitHub account with access to a repository.
- Basic familiarity with GitHub Actions, Python, and JSON.

### Workflow Components

The workflow consists of several key components, each serving a specific purpose in the SSL Expiry Check process:

1. **GitHub Actions Workflow (ssl_expiry_check.yml)**:

   This YAML file defines the workflow's structure, triggers, and steps. It automates the SSL certificate check process and sends Slack notifications.

2. **Python Script (ssl_expiry_check.py)**:

   The Python script performs SSL certificate expiration checks and sends Slack notifications based on predefined conditions.

3. **Domains List (domains.json)**:

   This JSON file contains the list of domains you want to monitor for SSL certificate expiration.

4. **Requirements File (requirements.txt)**:

   The requirements file lists project dependencies needed for proper execution.

### Configuration

1. **domains.json**:

   Create this JSON file to specify the list of domains you want to monitor. The JSON format ensures ease of data storage and retrieval for the script.

   ```json
   {
     "domains": [
       "example.com",
       "google.com",
       "github.com",
       "facebook.com",
       "wikipedia.org"
     ]
   }
   ```

2. **Slack Webhook**:

   Obtain a Slack webhook URL to send notifications. Store it as the `SLACK_WEBHOOK` secret in your GitHub repository settings. The webhook enables automated communication to Slack.

### Customization

- **Notification Content**:

  Customize Slack notifications by modifying the `send_slack_notification` function in `ssl_expiry_check.py`. Tailor message formats, variables, and other details to match your team's preferences.

- **Certificate Expiration Calculation**:

  Adjust the `check_ssl_expiry` function in `ssl_expiry_check.py` to match your certificate format or retrieval method. This customization ensures accurate expiration calculations.

- **Scheduled Run Interval**:

  Modify the cron schedule in `ssl_expiry_check.yml` to control the workflow's execution frequency. This flexibility allows you to adapt to your monitoring needs.

### Troubleshooting

- **Workflow Not Triggering**:

  If the workflow doesn't trigger, review your cron schedule in `ssl_expiry_check.yml`. Ensure that the schedule aligns with your expectations.

- **Certificate Retrieval Issues**:

  If you encounter problems fetching SSL certificates, confirm that domains are accessible over HTTPS and that port 443 is configured.

- **Webhook Configuration**:

  Double-check that the `SLACK_WEBHOOK` secret is correctly set in the repository settings. This secret enables secure communication with Slack.

### Workflow Overview

The GitHub Actions workflow automates the SSL certificate expiration check process. It uses the Python script to assess certificate validity and sends Slack notifications for certificates nearing expiration. The workflow ensures regular monitoring without manual intervention.

### Getting Started

1. Configure the `domains.json` file with the domains you want to monitor.

2. Set up the Slack webhook and store it as the `SLACK_WEBHOOK` secret in your repository.

3. Trigger the workflow manually using the "Run workflow" button in the Actions tab, or allow it to run automatically based on the cron schedule.

### Conclusion

The SSL Expiry Check GitHub Actions project offers an automated way to oversee SSL certificate expiration and receive timely notifications. With the flexibility for customization and the provided explanations, you can adapt the project to meet your specific requirements and preferences.
