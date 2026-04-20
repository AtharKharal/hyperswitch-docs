# Authentication - Authenticate

**Endpoint:** `POST /authentication/{authentication_id}/authenticate`

Authenticate an authentication for accessing our APIs from your servers.


**Operation ID:** `Authenticate an Authentication`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/authentication/{authentication_id}/authenticate&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `client_secret` | string | YES | Client secret for the authentication |
| `sdk_information` | string | NO |  |
| `device_channel` | string | YES |  |
| `threeds_method_comp_ind` | string | YES |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/authentication/{{authentication_id}}/authenticate" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "client_secret": "example",
  "sdk_information": "example",
  "device_channel": "example",
  "threeds_method_comp_ind": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/authentication/{authentication_id}/authenticate"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "client_secret": "example",
  "sdk_information": "example",
  "device_channel": "example",
  "threeds_method_comp_ind": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/authentication/{authentication_id}/authenticate";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "client_secret": "example",
  "sdk_information": "example",
  "device_channel": "example",
  "threeds_method_comp_ind": "example"
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
