# Payouts - Fulfill

**Endpoint:** `POST /payouts/{payout_id}/fulfill`



**Operation ID:** `Fulfill a Payout`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payouts/{payout_id}/fulfill&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `payout_id` | string | YES | Unique identifier for the payout. This ensures idempotency for multiple payouts
that have been done by a single merchant. This field is auto generated and is returned in the API response. |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payouts/{{payout_id}}/fulfill" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "payout_id": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payouts/{payout_id}/fulfill"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "payout_id": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payouts/{payout_id}/fulfill";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "payout_id": "example"
}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"payout_id":"pout_xyz456","status":"pending","amount":50000}
```

---

*Last updated: 2026-04-19*
