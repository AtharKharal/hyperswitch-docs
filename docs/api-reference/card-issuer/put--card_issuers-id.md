# Card Issuer - Update

**Endpoint:** `PUT /card_issuers/{id}`

Updates an existing card issuer entry

**Operation ID:** `Update Card Issuer`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/card_issuers/{id}&method=PUT" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `issuer_name` | string | YES | The new name for the card issuer |

## Code Examples

=== "cURL"

```bash
curl -X PUT "https://sandbox.hyperswitch.io/card_issuers/{{id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "issuer_name": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/card_issuers/{id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "issuer_name": "example"
}
response = requests.put(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/card_issuers/{id}";
const options = {
  method: "PUT",
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
