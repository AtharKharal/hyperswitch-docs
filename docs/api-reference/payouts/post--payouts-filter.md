# Payouts - List available filters

**Endpoint:** `POST /payouts/filter`



**Operation ID:** `List available payout filters`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payouts/filter&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `start_time` | string | YES | The start time to filter payments list or to get list of filters. To get list of filters start time is needed to be passed |
| `end_time` | string | NO | The end time to filter payments list or to get list of filters. If not passed the default time is now |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payouts/filter" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "start_time": "example",
  "end_time": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payouts/filter"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "start_time": "example",
  "end_time": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payouts/filter";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "start_time": "example",
  "end_time": "example"
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
