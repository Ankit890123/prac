#!/usr/bin/env python3
import requests
import json

# Test just the services endpoint first
try:
    response = requests.get("http://127.0.0.1:5000/api/services/")
    print(f"Services Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Services working - Found {len(data)} services")
    else:
        print(f"❌ Services failed: {response.text}")
except Exception as e:
    print(f"❌ Services error: {e}")

# Test send OTP
try:
    response = requests.post(
        "http://127.0.0.1:5000/api/auth/send-otp/",
        headers={"Content-Type": "application/json"},
        json={"email": "test@example.com"}
    )
    print(f"Send OTP Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Send OTP working - OTP: {data.get('otp')}")
        otp = data.get('otp')
        
        # Test login
        try:
            response = requests.post(
                "http://127.0.0.1:5000/api/auth/login/",
                headers={"Content-Type": "application/json"},
                json={"email": "test@example.com", "otp": otp}
            )
            print(f"Login Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Login working - Token: {data.get('token')[:20]}...")
            else:
                print(f"❌ Login failed: {response.text}")
        except Exception as e:
            print(f"❌ Login error: {e}")
    else:
        print(f"❌ Send OTP failed: {response.text}")
except Exception as e:
    print(f"❌ Send OTP error: {e}")