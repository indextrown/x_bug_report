from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import psutil
import os
import signal
import time


def terminate_process_by_name(process_name):
    """
    Forcefully terminate processes with a specific name.

    :param process_name: Name of the process to terminate (string)
    """
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                pid = proc.info['pid']
                print(f"Forcefully killing process {proc.info['name']} with PID {pid}")
                os.kill(pid, signal.SIGKILL)  # Send SIGKILL signal to forcefully terminate
                print(f"Process {proc.info['name']} killed successfully")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Error killing process {proc.info.get('name', 'unknown')} (PID {proc.info.get('pid', 'unknown')}): {e}")


# Preprocessing to avoid bot detection
def open_Driver():
    options = Options()

    # Set user-agent to simulate Chrome browser on Windows 10
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    # Set language to Korean for localized web pages
    options.add_argument('lang=ko_KR')

    # Set browser window size (width=430px, height=932px)
    options.add_argument('--window-size=932,932')

    # Disable GPU acceleration to prevent potential rendering issues
    options.add_argument('--disable-gpu')

    # Disable browser info bars (e.g., notifications or messages at the top of Chrome)
    options.add_argument('--disable-infobars')

    # Disable Chrome extensions
    options.add_argument('--disable-extensions')

    # Prevent Chrome from detecting automated environments
    options.add_argument('--disable-blink-features=AutomationControlled')

    # Disable automation detection
    options.add_argument('--disable-automation')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    return driver

if __name__ == '__main__':
    try:
        # Preprocessing to avoid bot detection
        driver = open_Driver()
        
        # Navigate to X login page
        url = 'https://x.com/'
        driver.get(url)

        # Insert cookies
        cookies = pickle.load(open('./x_cookies.pkl', 'rb'))
        for cookie in cookies:
            driver.add_cookie(cookie)

        time.sleep(2)

        # Refresh the page and wait for elements to load
        driver.refresh()
        driver.implicitly_wait(15)
        time.sleep(20)
        
    except Exception as e:
        # Quit driver and terminate processes in case of an exception
        driver.quit()
        terminate_process_by_name("chrome")
        print("Forcefully terminated due to an error:", e)
    finally:
        # Ensure the driver and Chrome processes are properly terminated
        driver.quit()
        terminate_process_by_name("chrome")
        print("Graceful termination")
