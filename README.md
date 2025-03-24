# Workerssal Mail Service

Automated Email Marketing Tool for Brands & Influencers

## Overview

Workerssal Mail Service is a command-line application that automates email marketing campaigns for brands and influencers. It reads data from Excel sheets and sends personalized emails to recipients.

## Features

- Send personalized emails to brands and influencers
- Track email campaign progress with a visual progress bar
- Log all email activities to an Excel file
- Cross-platform support (Windows, macOS, Linux)
- Secure credential management

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Install from source

1. Clone the repository:
   ```
   git clone https://github.com/workerssal/wssal-mail-service.git
   cd wssal-mail-service
   ```

2. Install the package:
   ```
   pip install -e .
   ```

## Configuration

Create a `.env` file in the root directory with the following variables:

# SMTP Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_ADDRESS=your-email@example.com
EMAIL_PASSWORD=your-password

# File Paths
BRANDS_EXCEL_PATH=./data/Brand Sheet.xlsx
INFLUENCERS_EXCEL_PATH=./data/Influencers Sheet.xlsx

## Usage

### Activate the service

Before sending emails, you need to activate the service with your credentials:

## Data Format

### Brand Sheet Format

The brand Excel sheet should have the following columns:
- COMPANY: Company name
- POC NAME: Point of contact name
- Gmail: Email address

Example:
```
COMPANY,POC NAME,Gmail
HERSAY,Avishkar Sonawane,example@gmail.com
Svarasya,Deepti Sehgal,contact@example.com
```

### Influencer Sheet Format

The influencer Excel sheet should have the following columns:
- USERNAME: Influencer's username
- LINK: Link to influencer's profile
- EMAIL: Email address

Example:
```
USERNAME,LINK,EMAIL
anshi_lifestyle316,https://www.instagram.com/anshi_lifestyle316,example@gmail.com
mridul tripathi,https://www.instagram.com/mridultripathi_,example@gmail.com
```

## Logs

All email activities are logged to an Excel file named `email_log.xlsx` in the root directory. The log includes:
- Timestamp
- Recipient name
- Email address
- Status (SUCCESS/FAILED)
- Error message (if any)

## License

Copyright (c) 2024 - Workerssal. All rights reserved.

### Send emails to brands

To start sending emails to all brands in your Excel sheet:

```
wssal-mail-service start --brands
```

### Send emails to influencers

To start sending emails to all influencers in your Excel sheet:

```
wssal-mail-service start --influencers
```

### Display the user manual

There are two ways to display the user manual:

```
wssal-mail-service manual
```

or

```
wssal-mail-service --manual
```

### Display version information

```
wssal-mail-service version
```