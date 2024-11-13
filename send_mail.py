import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
smtp_server = 'smtp.example.com'  # Replace with your SMTP server
smtp_port = 587                   # Use 587 for TLS or 465 for SSL
sender_email = 'your_email@example.com'
sender_password = 'your_password'
receiver_email = 'recipient@example.com'

# Email content
subject = 'Test Email'
body = 'Hello, this is a test email sent using Python!'

# Set up the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS
        server.login(sender_email, sender_password)
        server.send_message(message)
        print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")
