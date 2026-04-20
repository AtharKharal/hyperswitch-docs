# Authentication - Enable Authn Methods Token

**Endpoint:** `POST /authentication/{authentication_id}/enabled_authn_methods_token`

Enable authn methods token for an authentication.


**Operation ID:** `Enable Authentication Authn Methods Token`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/authentication/{authentication_id}/enabled_authn_methods_token&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `client_secret` | string | YES | Client Secret for the authentication |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/authentication/{{authentication_id}}/enabled_authn_methods_token" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "client_secret": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/authentication/{authentication_id}/enabled_authn_methods_token"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "client_secret": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/authentication/{authentication_id}/enabled_authn_methods_token";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "client_secret": "example"
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
