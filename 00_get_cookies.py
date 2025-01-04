from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import psutil
import os
import signal


# Preprocessing to avoid bot detection
def open_Driver():
    options = Options()

    # Set the user-agent to simulate using Chrome on Windows 10
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    # Set the language to Korean for localized web pages
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


# Function to save cookies for X (formerly Twitter)
def save_cookie_x(driver):
    """
    Navigate to the X (formerly Twitter) login page, allow manual login, and save cookies after confirmation.

    :param driver: Selenium WebDriver instance
    """
    url = 'https://x.com/'
    driver.get(url)

    # Prompt user to confirm after successful login
    input("Press Enter after you successfully log in...")

    # Save cookies to a file
    pickle.dump(driver.get_cookies(), open('./x_cookies.pkl', 'wb'))
    print("Cookies saved successfully.")

    # Close the browser
    driver.quit()


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
                os.kill(pid, signal.SIGKILL)  # Forcefully terminate the process
                print(f"Process {proc.info['name']} killed successfully")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Error killing process {proc.info.get('name', 'unknown')} (PID {proc.info.get('pid', 'unknown')}): {e}")


if __name__ == '__main__':
    try:
        # Preprocessing to avoid bot detection
        driver = open_Driver()

        # Run only once to save cookies
        save_cookie_x(driver)

    finally:
        # Ensure Chrome processes are terminated
        terminate_process_by_name("chrome")
