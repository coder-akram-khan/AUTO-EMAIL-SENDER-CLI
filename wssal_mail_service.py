#!/usr/bin/env python3
"""
Workerssal Mail Service - Automated Email Marketing Tool
Copyright (c) 2024 - Workerssal
"""

import os
import sys
import time
from datetime import datetime
import logging
import colorama
from colorama import Fore
import click

from modules.email_sender import EmailSender
from modules.config import APP_NAME, VERSION, LOG_FILE
from modules.ui import UI

# Initialize colorama
colorama.init(autoreset=True)

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@click.group()
@click.option('--manual', is_flag=True, help='Display the user manual')
@click.pass_context
def cli(ctx, manual):
    """Workerssal Mail Service - Automated Email Marketing Tool"""
    if manual:
        ui = UI()
        ui.show_manual()
        ctx.exit()


@cli.command()
def activate():
    """Activate the email service with your credentials"""
    sender = EmailSender()
    sender.activate()


@cli.command()
@click.option('--brands', is_flag=True, help='Send emails to brands')
@click.option('--influencers', is_flag=True, help='Send emails to influencers')
def start(brands, influencers):
    """Start sending emails to brands or influencers"""
    sender = EmailSender()
    
    # Check if credentials are already set
    if not sender.email or not sender.password:
        sender.activate()
    
    if brands:
        sender.send_email_to_brands()
    elif influencers:
        sender.send_email_to_influencers()
    else:
        click.echo(f"{Fore.RED}Please specify either --brands or --influencers")
        click.echo(f"Use 'wssal-mail-service --help' for more information")


@cli.command(name='manual')
def show_manual():
    """Display the user manual"""
    ui = UI()
    ui.show_manual()


@cli.command(name='version')
def show_version():
    """Display version information"""
    click.echo(f"{Fore.CYAN}{APP_NAME} v{VERSION}")


def main():
    """Main entry point for the application"""
    try:
        cli()
    except KeyboardInterrupt:
        click.echo(f"\n{Fore.YELLOW}Operation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        click.echo(f"{Fore.RED}An error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()