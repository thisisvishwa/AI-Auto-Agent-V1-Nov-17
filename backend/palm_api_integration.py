```python
import requests
from schemas import transaction_schema, wallet_schema, smart_contract_schema

class PalmAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json'}

    def transaction_processing(self, transaction_data):
        validate = transaction_schema.validate(transaction_data)
        if validate:
            return {"error": validate}
        response = requests.post(f"{self.base_url}/transactions", headers=self.headers, json=transaction_data)
        return response.json()

    def wallet_management(self, wallet_data):
        validate = wallet_schema.validate(wallet_data)
        if validate:
            return {"error": validate}
        response = requests.post(f"{self.base_url}/wallets", headers=self.headers, json=wallet_data)
        return response.json()

    def smart_contract_interaction(self, contract_data):
        validate = smart_contract_schema.validate(contract_data)
        if validate:
            return {"error": validate}
        response = requests.post(f"{self.base_url}/contracts", headers=self.headers, json=contract_data)
        return response.json()

palm_api = PalmAPI("https://api.palm.io")
```
