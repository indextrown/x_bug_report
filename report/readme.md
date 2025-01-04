# X(Twitter) Auto Login Tool

A tool for saving cookies and automatically logging into X (formerly Twitter) accounts.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### 1. Save Cookies (First Time Only)

```bash
python 00_get_cookies.py
```

- When browser opens, manually log in  
- Press Enter after login to save cookies

### 2. Modify Cookie Expiry (Optional)

```bash
python 01_modify_cookie.py
```

### 3. Auto Login with Saved Cookies

```bash
python 02_login_with_cookies.py
```

## File Structure

- `00_get_cookies.py`: Initial login and cookie saving
- `01_modify_cookie.py`: Modify cookie expiration date
- `02_login_with_cookies.py`: Auto login using saved cookies
- `requirements.txt`: Required package list
- `x_cookies.pkl`: Saved cookie file
- `x_cookies.json`: Cookie file in JSON format

## Features

- Cookie-based automatic login
- Browser settings to prevent bot detection
- Cookie expiration date modification

## Caution

- This tool should only be used for personal purposes
- Please comply with X's Terms of Service
