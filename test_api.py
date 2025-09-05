#!/usr/bin/env python3
import requests
import json

# Test the API endpoints
base_url = "http://127.0.0.1:5000/api"

def test_services():
    try:
        response = requests.get(f"{base_url}/services/")
        print(f"Services API Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data)} services")
            return True
        else:
            print(f"Error: {response.text}")
            return False
    except Exception as e:
        print(f"Error testing services: {e}")
        return False

def test_send_otp():
    try:
        response = requests.post(
            f"{base_url}/auth/send-otp/",
            headers={"Content-Type": "application/json"},
            json={"email": "test@example.com"}
        )
        print(f"Send OTP Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"OTP Response: {data}")
            return data.get('otp')
        else:
            print(f"Error: {response.text}")
            return None
    except Exception as e:
        print(f"Error testing send OTP: {e}")
        return None

def test_login(otp):
    try:
        response = requests.post(
            f"{base_url}/auth/login/",
            headers={"Content-Type": "application/json"},
            json={"email": "test@example.com", "otp": otp}
        )
        print(f"Login Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Login Response: {data}")
            return data.get('token')
        else:
            print(f"Error: {response.text}")
            return None
    except Exception as e:
        print(f"Error testing login: {e}")
        return None

if __name__ == "__main__":
    print("Testing Django API...")
    
    # Test services
    if test_services():
        print("✅ Services API working")
    else:
        print("❌ Services API failed")
    
    # Test OTP flow
    otp = test_send_otp()
    if otp:
        print("✅ Send OTP working")
        token = test_login(otp)
        if token:
            print("✅ Login working")
        else:
            print("❌ Login failed")
    else:
        print("❌ Send OTP failed")