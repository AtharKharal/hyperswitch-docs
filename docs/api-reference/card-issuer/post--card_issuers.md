# Card Issuer - Create

**Endpoint:** `POST /card_issuers`

Creates a new card issuer entry

**Operation ID:** `Create Card Issuer`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/card_issuers&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `issuer_name` | string | YES | The name of the card issuer to add |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/card_issuers" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "issuer_name": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/card_issuers"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "issuer_name": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/card_issuers";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "issuer_name": "example"
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
