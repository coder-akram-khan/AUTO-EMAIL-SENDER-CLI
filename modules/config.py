"""
Configuration module for Workerssal Mail Service
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application constants
APP_NAME = "wssal-mail-service"
VERSION = "1.0.0"
LOG_FILE = "email_log.xlsx"

# Email Configuration
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")
IMAP_PORT = int(os.getenv("IMAP_PORT", 993))
DEFAULT_EMAIL = os.getenv("EMAIL_ADDRESS", "")
DEFAULT_PASSWORD = os.getenv("EMAIL_PASSWORD", "")

# File paths
BRANDS_EXCEL_PATH = os.getenv("BRANDS_EXCEL_PATH", "./data/Brand Sheet.xlsx")
INFLUENCERS_EXCEL_PATH = os.getenv("INFLUENCERS_EXCEL_PATH", "./data/Influencers Sheet.xlsx")

# Email templates
BRAND_EMAIL_SUBJECT = "🚀 Get Influencers to Promote Your Brand – Hassle-Free!"
BRAND_EMAIL_TEMPLATE = """Hey {company} team,

Looking to get your products/services in front of the right audience? At Workerssal, we connect brands with top influencers who can drive real engagement and sales for you.

✅ Handpicked influencers in your niche
✅ Authentic promotions that build trust
✅ End-to-end campaign management – zero hassle for you

Let's discuss how we can bring you the perfect influencers for your brand. When's a good time to chat?

Best Regards,
Team Workerssal
official@workerssal.com
"""

INFLUENCER_EMAIL_SUBJECT = "🎯 Brands Want to Pay You – Let Workerssal Handle It!"
INFLUENCER_EMAIL_TEMPLATE = """Hey {username},

We're helping influencers like you land paid brand deals—without the stress of outreach or negotiations.

At Workerssal, we connect you with top brands that fit your niche, so you can focus on content while we bring the sponsorships to you.

Interested? Let's get you paid!!

Best Regards,
Team Workersal
official@workerssal.com
""" 