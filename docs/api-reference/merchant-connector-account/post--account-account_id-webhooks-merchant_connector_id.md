# Configure Connector Webhook - Register

**Endpoint:** `POST /account/{account_id}/webhooks/{merchant_connector_id}`

Setup webhook configuration for an existing Merchant at the connector.

**Operation ID:** `Register a Connector Webhook`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/account/{account_id}/webhooks/{merchant_connector_id}&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `event_type` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/account/{{account_id}}/webhooks/{{merchant_connector_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "event_type": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/account/{account_id}/webhooks/{merchant_connector_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "event_type": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/account/{account_id}/webhooks/{merchant_connector_id}";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "event_type": "example"
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
