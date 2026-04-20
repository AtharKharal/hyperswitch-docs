# Authentication - Sync

**Endpoint:** `POST /authentication/{authentication_id}/sync`

Sync an authentication for accessing our APIs from your servers.


**Operation ID:** `Sync an Authentication`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/authentication/{authentication_id}/sync&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `client_secret` | string | YES | The client secret for this authentication. |
| `payment_method_details` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/authentication/{{authentication_id}}/sync" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "client_secret": "example",
  "payment_method_details": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/authentication/{authentication_id}/sync"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "client_secret": "example",
  "payment_method_details": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/authentication/{authentication_id}/sync";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "client_secret": "example",
  "payment_method_details": "example"
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
