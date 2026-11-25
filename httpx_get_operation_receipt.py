import time

import httpx

user_data = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
user_response = httpx.post("http://localhost:8003/api/v1/users", json=user_data)
user_id = user_response.json()["user"]["id"]

credit_data = {"userId": user_id}
credit_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account", json=credit_data)
credit_response_data = credit_response.json()
account_id = credit_response_data["account"]["id"]
card_id = credit_response_data["account"]["cards"][0]["id"]

purchase_data = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "category": "taxi",
    "cardId": card_id,
    "accountId": account_id
}
purchase_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=purchase_data
)
operation_id = purchase_response.json()["operation"]["id"]

receipt_response = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}")
print("Operation receipt response:", receipt_response.json())
