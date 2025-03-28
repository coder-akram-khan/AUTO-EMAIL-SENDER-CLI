"""
Email sender module for Workerssal Mail Service
"""

import os
import sys
import time
import getpass
import logging
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from colorama import Fore

from modules.config import (
    SMTP_SERVER, SMTP_PORT, IMAP_SERVER, IMAP_PORT, LOG_FILE, 
    BRAND_EMAIL_SUBJECT, BRAND_EMAIL_TEMPLATE,
    INFLUENCER_EMAIL_SUBJECT, INFLUENCER_EMAIL_TEMPLATE,
    DEFAULT_EMAIL, DEFAULT_PASSWORD
)
from modules.data_handler import DataHandler
from modules.ui import UI
from modules.templates import get_email_signature, get_brand_email_template, get_influencer_email_template

logger = logging.getLogger(__name__)


class EmailSender:
    """Email sender class for handling all email operations"""
    
    def __init__(self):
        """Initialize the email sender"""
        self.email = DEFAULT_EMAIL
        self.password = DEFAULT_PASSWORD
        self.smtp_server = SMTP_SERVER
        self.smtp_port = SMTP_PORT
        self.imap_server = IMAP_SERVER
        self.imap_port = IMAP_PORT
        self.log_data = []
        self.data_handler = DataHandler()
        self.ui = UI()
    
    def activate(self):
        """Activate the email sender with user credentials"""
        self.ui.display_banner()
        
        # Only prompt for credentials if they're not already set
        if not self.email or not self.password:
            print(f"{Fore.CYAN}Please enter your email credentials:")
            self.email = input(f"{Fore.YELLOW}Email [{self.email if self.email else 'none'}]: ") or self.email
            if not self.email:
                print(f"{Fore.RED}Email is required.")
                sys.exit(1)
            
            self.password = getpass.getpass(f"{Fore.YELLOW}Password: ") or self.password
            if not self.password:
                print(f"{Fore.RED}Password is required.")
                sys.exit(1)
        
            # Verify credentials
            try:
                self.verify_credentials()
                print(f"\n{Fore.GREEN}✓ Activation successful!")
                print(f"{Fore.GREEN}Welcome, {self.email}!\n")
                print(f"{Fore.RED}WARNING: Do not try to modify the application --© 2024 - WORKERSSAL.\n")
            except Exception as e:
                print(f"\n{Fore.RED}✗ Activation failed: {str(e)}")
                sys.exit(1)
        else:
            # Just verify the credentials without prompting
            try:
                self.verify_credentials()
            except Exception as e:
                print(f"\n{Fore.RED}✗ Authentication failed: {str(e)}")
                print(f"{Fore.YELLOW}Please run 'wssal-mail-service activate' to update your credentials.")
                sys.exit(1)
    
    def verify_credentials(self):
        """Verify email credentials using both SMTP and IMAP"""
        try:
            # Verify SMTP credentials
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.ehlo()
            server.starttls()
            server.login(self.email, self.password)
            server.quit()
            
            # Verify IMAP credentials
            imap = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            imap.login(self.email, self.password)
            imap.logout()
            
        except Exception as e:
            raise Exception(f"Invalid credentials or email server configuration: {str(e)}")
    
    def send_email_to_brands(self):
        """Send emails to brands with modern HTML templates"""
        if not self.email or not self.password:
            print(f"{Fore.RED}Please activate the service first with 'wssal-mail-service activate'")
            return
            
        brands = self.data_handler.load_brands_data()
        total = len(brands)
        
        print(f"{Fore.CYAN}Starting email campaign to {total} brands...")
        
        for i, brand in enumerate(brands):
            try:
                # Extract fields from the Excel sheet
                company = brand.get("COMPANY", "")
                poc_name = brand.get("POC NAME", "")
                email = brand.get("Gmail", "")
                
                if not email:
                    self.log_result(company, email, "FAILED", "Missing email address")
                    continue
                
                # Create email content using HTML template
                subject = BRAND_EMAIL_SUBJECT
                
                # Get HTML content from templates
                html_body = get_brand_email_template(company)
                
                # Send the email with HTML template
                result = self.send_email(email, subject, html_body)
                self.log_result(company, email, "SUCCESS" if result else "FAILED", 
                               "" if result else "Failed to send email")
                
                # Progress
                progress = (i + 1) / total * 100
                self.ui.display_progress(i + 1, total, progress)
                
                # Sleep to avoid being flagged as spam
                time.sleep(2)
                
            except Exception as e:
                company_name = brand.get("COMPANY", "Unknown")
                email = brand.get("Gmail", "Unknown")
                self.log_result(company_name, email, "FAILED", str(e))
                print(f"{Fore.RED}Error sending to {email}: {str(e)}")
        
        # Save log to Excel
        self.data_handler.save_log(self.log_data, LOG_FILE)
        print(f"\n{Fore.GREEN}Email campaign completed! Log saved to {LOG_FILE}")
    
    def send_email_to_influencers(self):
        """Send emails to influencers"""
        if not self.email or not self.password:
            print(f"{Fore.RED}Please activate the service first with 'wssal-mail-service activate'")
            return
            
        influencers = self.data_handler.load_influencers_data()
        total = len(influencers)
        
        print(f"{Fore.CYAN}Starting email campaign to {total} influencers...")
        
        for i, influencer in enumerate(influencers):
            try:
                username = influencer.get("USERNAME ", "").strip()
                email = influencer.get("EMAIL", "").strip()
                link = influencer.get("LINK", "").strip()
                
                if not email:
                    self.log_result(username, email, "FAILED", "Missing email address")
                    continue
                
                # Create email content
                subject = INFLUENCER_EMAIL_SUBJECT
                
                # Get HTML content from templates
                html_body = get_influencer_email_template(username)
                
                # Send the email with HTML template
                result = self.send_email(email, subject, html_body)
                self.log_result(username, email, "SUCCESS" if result else "FAILED", 
                               "" if result else "Failed to send email")
                
                # Progress
                progress = (i + 1) / total * 100
                self.ui.display_progress(i + 1, total, progress)
                
                # Sleep to avoid being flagged as spam
                time.sleep(2)
                
            except Exception as e:
                username = influencer.get("USERNAME ", "Unknown")
                email = influencer.get("EMAIL", "Unknown")
                self.log_result(username, email, "FAILED", str(e))
                print(f"{Fore.RED}Error sending to {email}: {str(e)}")
        
        # Save log to Excel
        self.data_handler.save_log(self.log_data, LOG_FILE)
        print(f"\n{Fore.GREEN}Email campaign completed! Log saved to {LOG_FILE}")
    
    def send_email(self, recipient, subject, html_body):
        """Send an email to a recipient with modern styling"""
        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = self.email
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Extract plain text from HTML for fallback
            plain_body = subject + "\n\nPlease view this email in an HTML-compatible email client."
            
            # Get signature
            signature = get_email_signature()
            
            # Create HTML version with modern styling that matches signature exactly
            html_content = f"""
            <div style="width: 100%; max-width: 650px; font-family: 'Segoe UI', Helvetica, Arial, sans-serif; margin: 0 auto;">
                <!-- Email Body Section -->
                <div style="width: 100%; padding: 24px; background: linear-gradient(to right, #ffffff, #f7f9fc); border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05); margin-bottom: 20px;">
                    {html_body}
                </div>
                
                <!-- Signature Section (already has its own container) -->
                {signature}
            </div>
            """
            
            # Attach parts
            text_part = MIMEText(plain_body, 'plain')
            html_part = MIMEText(html_content, 'html')
            
            msg.attach(text_part)
            msg.attach(html_part)
            
            # Connect to server and send
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.ehlo()
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(msg)
            server.quit()
            
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {str(e)}")
            return False
    
    def log_result(self, name, email, status, note=""):
        """Log the result of an email send operation"""
        self.log_data.append({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name,
            "Email": email,
            "Status": status,
            "Note": note
        }) 
        