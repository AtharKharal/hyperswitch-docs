# Merchant Connector - Update

**Endpoint:** `POST /account/{account_id}/connectors/{merchant_connector_id}`

To update an existing Merchant Connector account. Helpful in enabling/disabling different payment methods and other settings for the connector

**Operation ID:** `Update a Merchant Connector`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/account/{account_id}/connectors/{merchant_connector_id}&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `connector_type` | string | YES |  |
| `connector_label` | string | NO | This is an unique label you can generate and pass in order to identify this connector account on your Hyperswitch dashboard and reports. Eg: if your profile label is `default`, connector label can be `stripe_default` |
| `connector_account_details` | string | NO |  |
| `payment_methods_enabled` | array | NO | An object containing the details about the payment methods that need to be enabled under this merchant connector account |
| `connector_webhook_details` | string | NO |  |
| `metadata` | object | NO | Metadata is useful for storing additional, unstructured information on an object. |
| `test_mode` | boolean | NO | A boolean value to indicate if the connector is in Test mode. By default, its value is false. |
| `disabled` | boolean | NO | A boolean value to indicate if the connector is disabled. By default, its value is false. |
| `frm_configs` | array | NO | Contains the frm configs for the merchant connector |
| `pm_auth_config` | object | NO | pm_auth_config will relate MCA records to their respective chosen auth services, based on payment_method and pmt |
| `status` | string | YES |  |
| `additional_merchant_data` | string | NO |  |
| `connector_wallets_details` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/account/{{account_id}}/connectors/{{merchant_connector_id}}" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "connector_type": "example",
  "connector_label": "example",
  "connector_account_details": "example",
  "payment_methods_enabled": "example",
  "connector_webhook_details": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/account/{account_id}/connectors/{merchant_connector_id}"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "connector_type": "example",
  "connector_label": "example",
  "connector_account_details": "example",
  "payment_methods_enabled": "example",
  "connector_webhook_details": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/account/{account_id}/connectors/{merchant_connector_id}";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "connector_type": "example",
  "connector_label": "example",
  "connector_account_details": "example",
  "payment_methods_enabled": "example",
  "connector_webhook_details": "example"
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
