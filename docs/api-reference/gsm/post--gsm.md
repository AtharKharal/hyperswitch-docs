# Gsm - Create

**Endpoint:** `POST /gsm`

Creates a GSM (Global Status Mapping) Rule. A GSM rule is used to map a connector's error message/error code combination during a particular payments flow/sub-flow to Hyperswitch's unified status/error code/error message combination. It is also used to decide the next action in the flow - retry/requeue/do_default

**Operation ID:** `Create Gsm Rule`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/gsm&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `connector` | string | YES |  |
| `flow` | string | YES | The flow in which the code and message occurred for a connector |
| `sub_flow` | string | YES | The sub_flow in which the code and message occurred  for a connector |
| `code` | string | YES | code received from the connector |
| `message` | string | YES | message received from the connector |
| `status` | string | YES | status provided by the router |
| `router_error` | string | NO | optional error provided by the router |
| `decision` | string | YES |  |
| `step_up_possible` | boolean | YES | indicates if step_up retry is possible
**Deprecated**: This field is now included as part of `feature_data` under the `Retry` variant. |
| `unified_code` | string | NO | error code unified across the connectors |
| `unified_message` | string | NO | error message unified across the connectors |
| `error_category` | string | NO |  |
| `clear_pan_possible` | boolean | YES | indicates if retry with pan is possible
**Deprecated**: This field is now included as part of `feature_data` under the `Retry` variant. |
| `feature` | string | NO |  |
| `feature_data` | string | NO |  |
| `standardised_code` | string | NO |  |
| `description` | string | NO | A detailed description of the error intended for debugging, analytics, and support teams. |
| `user_guidance_message` | string | NO | A user-friendly message that can be safely displayed to the customer.
This message provides guidance on what the user should do to
resolve the issue. |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/gsm" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "connector": "example",
  "flow": "example",
  "sub_flow": "example",
  "code": "example",
  "message": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/gsm"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "connector": "example",
  "flow": "example",
  "sub_flow": "example",
  "code": "example",
  "message": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/gsm";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "connector": "example",
  "flow": "example",
  "sub_flow": "example",
  "code": "example",
  "message": "example"
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
