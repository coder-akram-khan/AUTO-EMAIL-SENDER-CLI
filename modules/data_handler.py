"""
Data handler module for Workerssal Mail Service
"""

import os
import sys
import pandas as pd
import logging
from colorama import Fore

from modules.config import BRANDS_EXCEL_PATH, INFLUENCERS_EXCEL_PATH

logger = logging.getLogger(__name__)


class DataHandler:
    """Data handler class for loading and processing data"""
    
    def load_brands_data(self):
        """Load data from brands Excel file"""
        return self._load_data(BRANDS_EXCEL_PATH, "brands")
    
    def load_influencers_data(self):
        """Load data from influencers Excel file"""
        return self._load_data(INFLUENCERS_EXCEL_PATH, "influencers")
    
    def _load_data(self, file_path, data_type):
        """Load data from Excel files"""
        print(f"{Fore.CYAN}Loading {data_type} data from: {file_path}")
        try:
            if not os.path.exists(file_path):
                print(f"{Fore.RED}Error: File not found: {file_path}")
                print(f"{Fore.YELLOW}Please make sure the file exists and the path is correct in your .env file.")
                sys.exit(1)
                
            df = pd.read_excel(file_path)
            return df.to_dict(orient="records")
        except Exception as e:
            print(f"{Fore.RED}Error loading {data_type} data: {str(e)}")
            sys.exit(1)
    
    def save_log(self, log_data, log_file):
        """Save log data to Excel file"""
        try:
            df = pd.DataFrame(log_data)
            df.to_excel(log_file, index=False)
            logger.info(f"Log saved to {log_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to save log: {str(e)}")
            return False 