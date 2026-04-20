# Customers - Update

**Endpoint:** `POST /customers/{customer_id}`

Updates the customer's details in a customer object.

**Operation ID:** `Update a Customer`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/customers/{customer_id}&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `name` | string | NO | The customer's name |
| `email` | string | NO | The customer's email address |
| `phone` | string | NO | The customer's phone number |
| `description` | string | NO | An arbitrary string that you can attach to a customer object. |
| `phone_country_code` | string | NO | The country code for the customer phone number |
| `address` | string | NO |  |
| `metadata` | object | NO | You can specify up to 50 keys, with key names up to 40 characters long and values up to 500
characters long. Metadata is useful for storing additional, structured information on an
object. |
| `tax_registration_id` | string | NO | Customer's tax registration ID |
| `document_details` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/customers/{{customer_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "name": "example",
  "email": "example",
  "phone": "example",
  "description": "example",
  "phone_country_code": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/customers/{customer_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "name": "example",
  "email": "example",
  "phone": "example",
  "description": "example",
  "phone_country_code": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/customers/{customer_id}";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "name": "example",
  "email": "example",
  "phone": "example",
  "description": "example",
  "phone_country_code": "example"
}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"customer_id":"cus_abc123","email":"customer@example.com","name":"John Doe"}
```

---

*Last updated: 2026-04-19*
