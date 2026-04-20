# Authentication - Create

**Endpoint:** `POST /authentication`

Create a new authentication for accessing our APIs from your servers.


**Operation ID:** `Create an Authentication`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/authentication&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `authentication_id` | string | NO | The unique identifier for this authentication. |
| `profile_id` | string | NO | The business profile that is associated with this authentication |
| `amount` | string | YES |  |
| `authentication_connector` | string | NO |  |
| `currency` | string | YES |  |
| `return_url` | string | NO | The URL to which the user should be redirected after authentication. |
| `force_3ds_challenge` | boolean | NO | Force 3DS challenge. |
| `psd2_sca_exemption_type` | string | NO |  |
| `profile_acquirer_id` | string | NO | Profile Acquirer ID get from profile acquirer configuration |
| `acquirer_details` | string | NO |  |
| `customer_details` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/authentication" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "authentication_id": "example",
  "profile_id": "example",
  "amount": "example",
  "authentication_connector": "example",
  "currency": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/authentication"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "authentication_id": "example",
  "profile_id": "example",
  "amount": "example",
  "authentication_connector": "example",
  "currency": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/authentication";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "authentication_id": "example",
  "profile_id": "example",
  "amount": "example",
  "authentication_connector": "example",
  "currency": "example"
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
