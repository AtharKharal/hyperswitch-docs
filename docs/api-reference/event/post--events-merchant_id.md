# Events - List

**Endpoint:** `POST /events/{merchant_id}`

List all Events associated with a Merchant Account or Profile.

**Operation ID:** `List all Events associated with a Merchant Account or Profile`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/events/{merchant_id}&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `created_after` | string | NO | Filter events created after the specified time. |
| `created_before` | string | NO | Filter events created before the specified time. |
| `limit` | integer | NO | Include at most the specified number of events. |
| `offset` | integer | NO | Include events after the specified offset. |
| `object_id` | string | NO | Filter all events associated with the specified object identifier (Payment Intent ID,
Refund ID, etc.) |
| `event_id` | string | NO | Filter all events associated with the specified Event_id |
| `profile_id` | string | NO | Filter all events associated with the specified business profile ID. |
| `event_classes` | array | NO | Filter events by their class. |
| `event_types` | array | NO | Filter events by their type. |
| `is_delivered` | boolean | NO | Filter all events by `is_overall_delivery_successful` field of the event. |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/events/{{merchant_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "created_after": "example",
  "created_before": "example",
  "limit": 1000,
  "offset": 1000,
  "object_id": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/events/{merchant_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "created_after": "example",
  "created_before": "example",
  "limit": 1000,
  "offset": 1000,
  "object_id": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/events/{merchant_id}";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "created_after": "example",
  "created_before": "example",
  "limit": 1000,
  "offset": 1000,
  "object_id": "example"
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
