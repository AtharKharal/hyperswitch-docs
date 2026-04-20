# Routing - Rule Evaluate

**Endpoint:** `POST /routing/rule/evaluate`

Evaluate routing rules

**Operation ID:** `Evaluate routing rules (alternative)`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/routing/rule/evaluate&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `created_by` | string | YES | Identifier of the user/system triggering routing evaluation.

Example:
```json
"created_by": "some_id"
``` |
| `payment_id` | string | NO | Payment ID for debugging and tracing routing decisions.

Example:
```json
"payment_id": "pay_abc123"
``` |
| `parameters` | object | YES | Dynamic parameters used during routing evaluation.

Each key represents a routing attribute.

Example fields:

- `payment_method`
- `payment_method_type`
- `amount`
- `currency`
- `authentication_type`
- `card_bin`
- `capture_method`
- `business_country`
- `billing_country`
- `business_label`
- `setup_future_usage`
- `card_network`
- `payment_type`
- `mandate_type`
- `mandate_acceptance_type`
- `metadata`

Example:
```json
{
"payment_method": { "type": "enum_variant", "value": "card" },
"amount": { "type": "number", "value": 10 },
"currency": { "type": "str_value", "value": "INR" },
"authentication_type": { "type": "enum_variant", "value": "three_ds" },
"card_bin": { "type": "str_value", "value": "424242" },
"business_country": { "type": "str_value", "value": "IN" },
"setup_future_usage": { "type": "enum_variant", "value": "off_session" },
"card_network": { "type": "enum_variant", "value": "visa" },
"metadata": {
"type": "metadata_variant",
"value": { "key": "key1", "value": "value1" }
}
}
```

For the complete superset of supported routing keys,
refer to `routing_configs.keys` in:
https://github.com/juspay/decision-engine/blob/main/config/development.toml |
| `fallback_output` | array | YES | Fallback connectors used if routing rule evaluation fails.

These connectors will be returned if no rule matches.

Example:
```json
[
{
"gateway_name": "stripe",
"gateway_id": "mca_123"
}
]
``` |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/routing/rule/evaluate" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "created_by": "example",
  "payment_id": "example",
  "parameters": "example",
  "fallback_output": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/routing/rule/evaluate"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "created_by": "example",
  "payment_id": "example",
  "parameters": "example",
  "fallback_output": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/routing/rule/evaluate";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "created_by": "example",
  "payment_id": "example",
  "parameters": "example",
  "fallback_output": "example"
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
