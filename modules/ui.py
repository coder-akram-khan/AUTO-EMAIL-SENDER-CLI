"""
UI module for Workerssal Mail Service
"""

import colorama
from colorama import Fore

from modules.config import APP_NAME, VERSION, LOG_FILE

# Initialize colorama
colorama.init(autoreset=True)


class UI:
    """UI class for handling all user interface elements"""
    
    def display_banner(self):
        """Display a colorful banner for the application"""
        print("\n")
        print(f"{Fore.BLUE}{'=' * 80}")
        print(f"{Fore.CYAN}{'=' * 80}")
        print(f"{Fore.MAGENTA}{'=' * 30}{Fore.WHITE} WSSAL-MAIL-SERVICE {Fore.MAGENTA}{'=' * 30}")
        print(f"{Fore.CYAN}{'=' * 80}")
        print(f"{Fore.BLUE}{'=' * 80}")
        print(f"{Fore.YELLOW}              Automated Email Marketing Tool for Brands & Influencers")
        print(f"{Fore.GREEN}                            Version {VERSION}")
        print(f"{Fore.BLUE}{'=' * 80}\n")
        
        # Add warning message
        print(f"{Fore.RED}WARNING: Don't Try To Modify The Application --© 2024 - WORKERSSAL.")
        print(f"{Fore.RED}For support contact WORKERSSAL-DEV Team\n")
    
    def display_progress(self, current, total, percentage):
        """Display a progress bar"""
        import sys
        
        bar_length = 40
        filled_length = int(bar_length * current // total)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        
        sys.stdout.write(f"\r{Fore.CYAN}Progress: |{Fore.GREEN}{bar}{Fore.CYAN}| {current}/{total} ({percentage:.1f}%)")
        sys.stdout.flush()
    
    def show_manual(self):
        """Display user manual"""
        self.display_banner()
        
        print(f"{Fore.CYAN}{'=' * 40} USER MANUAL {'=' * 40}")
        print(f"\n{Fore.YELLOW}COMMANDS:")
        print(f"{Fore.GREEN}  wssal-mail-service activate{Fore.WHITE}: Activate the service with your credentials")
        print(f"{Fore.GREEN}  wssal-mail-service start --brands{Fore.WHITE}: Send emails to all brands")
        print(f"{Fore.GREEN}  wssal-mail-service start --influencers{Fore.WHITE}: Send emails to all influencers")
        print(f"{Fore.GREEN}  wssal-mail-service manual{Fore.WHITE}: Display this user manual")
        print(f"{Fore.GREEN}  wssal-mail-service --manual{Fore.WHITE}: Alternative way to display this manual")
        print(f"{Fore.GREEN}  wssal-mail-service version{Fore.WHITE}: Display the version information")
        
        print(f"\n{Fore.YELLOW}CONFIGURATION:")
        print(f"{Fore.WHITE}  Create a .env file with the following variables:")
        print(f"{Fore.CYAN}  SMTP_SERVER{Fore.WHITE}=smtp.gmail.com")
        print(f"{Fore.CYAN}  SMTP_PORT{Fore.WHITE}=587")
        print(f"{Fore.CYAN}  EMAIL_ADDRESS{Fore.WHITE}=your-email@example.com")
        print(f"{Fore.CYAN}  EMAIL_PASSWORD{Fore.WHITE}=your-password")
        print(f"{Fore.CYAN}  BRANDS_EXCEL_PATH{Fore.WHITE}=./data/Brand Sheet.xlsx")
        print(f"{Fore.CYAN}  INFLUENCERS_EXCEL_PATH{Fore.WHITE}=./data/Influencers Sheet.xlsx")
        
        print(f"\n{Fore.YELLOW}LOGS:")
        print(f"{Fore.WHITE}  Email logs are saved to {LOG_FILE}")
        
        print(f"\n{Fore.RED}WARNING: Do not try to modify the application --© 2024 - WORKERSSAL.\n") 