# 쿠키 변조를 통한 세션 유지 (Session Persistence via Cookie Tampering)

**요약:**

**쿠키를 변조하여 세션을 유지하고, 로그인 과정을 우회하여 무제한 데이터 접근이 가능한 치명적인 취약점**을 발견했습니다. 이 문제는 서비스의 보안성과 데이터 보호에 심각한 위협을 초래할 수 있습니다.

---

**설명:**

이 취약점은 **세션 만료 검증 부족**과 클라이언트 쿠키의 잘못된 처리에서 발생합니다. 인증 쿠키의 `expires` 값을 변조하거나 이전에 수집된 쿠키를 재사용하면 공격자가 재인증 없이 세션을 유지하거나 복구할 수 있습니다.

또한, 쿠키의 보안 속성(`HttpOnly`, `SameSite`)이 적절히 설정되지 않아 XSS, CSRF와 같은 클라이언트 측 공격에 노출됩니다.

### 주요 취약점:

1. **변조된 쿠키를 통한 세션 유지**: 공격자는 인증 쿠키를 변조하거나 재사용하여 세션 만료를 우회할 수 있습니다.
2. **쿠키 만료 검증 부족**: 서버가 만료된 쿠키를 검증하지 않아 클라이언트에서 임의로 설정한 만료 값이 허용됩니다.
3. **로그인 과정 우회**: 변조된 쿠키를 사용해 로그인 인증 없이 데이터를 무제한으로 접근할 수 있습니다.

---

**재현 방법**

1. **쿠키 수집**:
    - 로그인 후 스크립트 `00_get_cookies.py`를 실행하여 사용자의 인증 쿠키(`auth_token`, `kdt`)를 수집합니다.
2. **쿠키 변조**:
    - 스크립트 `01_modify_cookie.py`를 사용하여 수집된 쿠키의 만료 시간(`expires`)을 수정합니다. 예: 만료 시간을 `2025-12-31`로 변경.
3. **변조된 쿠키로 요청**:
    - 스크립트 `02_login_with_cookies.py`를 실행하여 변조된 쿠키를 포함한 HTTP 요청을 전송하고 서비스에 접근합니다.
4. **결과 확인**:
    - 세션이 여전히 유지되며, 변조된 쿠키로 인증 없이 서비스에 접근할 수 있음을 확인합니다.

---

**영향**

1. **무제한 데이터 접근**:
공격자는 변조된 쿠키를 악용하여 추가 인증 없이 민감한 데이터에 접근할 수 있습니다.
2. **크롤링으로 인한 데이터 유출**:
비인가 사용자가 인증 절차를 우회하여 대량으로 데이터를 수집하고 악용할 가능성이 있습니다.
3. **서비스 리소스 남용**:
무제한 데이터 접근으로 인해 서버 자원이 과도하게 소모되어 서비스 품질이 저하될 수 있습니다.

---

**참고 자료 및 증거**

1. **증거 자료**:
    - 수집된 쿠키, 변조된 쿠키 요청, 성공적인 응답의 영상.
    - 세션이 유지되는 것을 보여주는 쿠키파일
2. **참고 자료**:
    - CWE-613: 세션 만료 검증 부족.
    - CWE-384: 세션 고정(Session Fixation).

---

**권장 사항 및 개선 방안**

1. **서버 측 쿠키 검증 강화**:
    - 쿠키의 만료 시간과 무결성을 서버에서 철저히 검증하고, 세션 만료를 서버에서 관리합니다.
2. **활동 기반 세션 만료 도입**:
    - 사용자의 활동이 일정 시간 동안 없을 경우 세션을 자동으로 만료하고, 활동 시 세션 유효 기간을 갱신합니다.
3. **쿠키 보안 속성 강화**:
    - `HttpOnly`, `Secure`, `SameSite` 속성을 적용하여 클라이언트 측 쿠키 수정 및 노출을 방지합니다.

---

**결론**

이 취약점은 쿠키를 변조하여 세션을 유지하고 인증을 우회할 수 있게 하며, 서비스 보안 및 데이터 보호에 심각한 위험을 초래합니다. 이를 통해 무제한 데이터 접근, 데이터 유출, 서버 자원 남용 등의 문제가 발생할 수 있습니다.

즉각적인 보안 조치를 통해 이 문제를 해결할 것을 권장합니다.

추가적인 논의나 설명이 필요하다면 언제든 말씀해 주세요.

감사합니다.

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


