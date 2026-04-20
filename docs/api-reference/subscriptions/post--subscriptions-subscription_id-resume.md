# Subscription - Resume Subscription

**Endpoint:** `POST /subscriptions/{subscription_id}/resume`

Resume the subscription

**Operation ID:** `Resume Subscription`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/subscriptions/{subscription_id}/resume&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `resume_option` | string | NO |  |
| `resume_date` | string | NO | Optional date when the subscription should be resumed (if not provided, resumes immediately) |
| `charges_handling` | string | NO |  |
| `unpaid_invoices_handling` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/subscriptions/{{subscription_id}}/resume" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "resume_option": "example",
  "resume_date": "example",
  "charges_handling": "example",
  "unpaid_invoices_handling": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/subscriptions/{subscription_id}/resume"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "resume_option": "example",
  "resume_date": "example",
  "charges_handling": "example",
  "unpaid_invoices_handling": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/subscriptions/{subscription_id}/resume";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "resume_option": "example",
  "resume_date": "example",
  "charges_handling": "example",
  "unpaid_invoices_handling": "example"
}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"subscription_id":"sub_xyz123","status":"active"}
```

---

*Last updated: 2026-04-19*
