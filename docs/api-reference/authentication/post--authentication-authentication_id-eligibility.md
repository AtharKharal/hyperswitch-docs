# Authentication - Eligibility

**Endpoint:** `POST /authentication/{authentication_id}/eligibility`

Check if an authentication is eligible for a specific merchant.


**Operation ID:** `Check Authentication Eligibility`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/authentication/{authentication_id}/eligibility&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `payment_method_data` | string | YES |  |
| `payment_method` | string | YES |  |
| `payment_method_type` | string | NO |  |
| `client_secret` | string | NO | Optional secret value used to identify and authorize the client making the request.
This can help ensure that the payment session is secure and valid. |
| `profile_id` | string | NO | Optional identifier for the business profile associated with the payment.
This determines which configurations, rules, and branding are applied to the transaction. |
| `billing` | string | NO |  |
| `shipping` | string | NO |  |
| `browser_information` | string | NO |  |
| `email` | string | NO | Optional email address of the customer.
Used for customer identification, communication, and possibly for 3DS or fraud checks. |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/authentication/{{authentication_id}}/eligibility" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "payment_method_data": "example",
  "payment_method": "example",
  "payment_method_type": "example",
  "client_secret": "example",
  "profile_id": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/authentication/{authentication_id}/eligibility"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "payment_method_data": "example",
  "payment_method": "example",
  "payment_method_type": "example",
  "client_secret": "example",
  "profile_id": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/authentication/{authentication_id}/eligibility";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "payment_method_data": "example",
  "payment_method": "example",
  "payment_method_type": "example",
  "client_secret": "example",
  "profile_id": "example"
}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"id":"obj_xyz","status":"success"}
```

---

*Last updated: 2026-04-19*
