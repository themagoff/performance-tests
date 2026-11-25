import time

import httpx

user_payload = {
  "email": f"user{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}
user_response = httpx.post("http://localhost:8003/api/v1/users", json=user_payload)
user_id = user_response.json()["user"]["id"]

deposit_payload = {"userId": user_id}
deposit_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json=deposit_payload)

print("Deposit account response", deposit_response.json())
print("Status code", deposit_response.status_code)
