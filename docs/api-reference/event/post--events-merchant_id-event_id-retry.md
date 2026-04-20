# Events - Manual Retry

**Endpoint:** `POST /events/{merchant_id}/{event_id}/retry`

Manually retry the delivery of the specified Event.

**Operation ID:** `Manually retry the delivery of an Event`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/events/{merchant_id}/{event_id}/retry&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/events/{{merchant_id}}/{{event_id}}/retry" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY"
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/events/{merchant_id}/{event_id}/retry"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
response = requests.post(url, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/events/{merchant_id}/{event_id}/retry";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"id":"obj_xyz","status":"success"}
```

---

*Last updated: 2026-04-19*
