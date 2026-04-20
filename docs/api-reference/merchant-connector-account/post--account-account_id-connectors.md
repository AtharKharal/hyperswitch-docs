# Merchant Connector - Create

**Endpoint:** `POST /account/{account_id}/connectors`

Creates a new Merchant Connector for the merchant account. The connector could be a payment processor/facilitator/acquirer or a provider of specialized services like Fraud/Accounting etc.

**Operation ID:** `Create a Merchant Connector`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/account/{account_id}/connectors&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `connector_type` | string | YES |  |
| `connector_name` | string | YES |  |
| `connector_label` | string | NO | This is an unique label you can generate and pass in order to identify this connector account on your Hyperswitch dashboard and reports. Eg: if your profile label is `default`, connector label can be `stripe_default` |
| `profile_id` | string | NO | Identifier for the profile, if not provided default will be chosen from merchant account |
| `connector_account_details` | string | NO |  |
| `payment_methods_enabled` | array | NO | An object containing the details about the payment methods that need to be enabled under this merchant connector account |
| `connector_webhook_details` | string | NO |  |
| `metadata` | object | NO | Metadata is useful for storing additional, unstructured information on an object. |
| `test_mode` | boolean | NO | A boolean value to indicate if the connector is in Test mode. By default, its value is false. |
| `disabled` | boolean | NO | A boolean value to indicate if the connector is disabled. By default, its value is false. |
| `frm_configs` | array | NO | Contains the frm configs for the merchant connector |
| `business_country` | string | NO |  |
| `business_label` | string | NO | The business label to which the connector account is attached. To be deprecated soon. Use the 'profile_id' instead |
| `business_sub_label` | string | NO | The business sublabel to which the connector account is attached. To be deprecated soon. Use the 'profile_id' instead |
| `merchant_connector_id` | string | NO | Unique ID of the connector |
| `pm_auth_config` | object | NO |  |
| `status` | string | NO |  |
| `additional_merchant_data` | string | NO |  |
| `connector_wallets_details` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/account/{{account_id}}/connectors" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "connector_type": "example",
  "connector_name": "example",
  "connector_label": "example",
  "profile_id": "example",
  "connector_account_details": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/account/{account_id}/connectors"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "connector_type": "example",
  "connector_name": "example",
  "connector_label": "example",
  "profile_id": "example",
  "connector_account_details": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/account/{account_id}/connectors";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "connector_type": "example",
  "connector_name": "example",
  "connector_label": "example",
  "profile_id": "example",
  "connector_account_details": "example"
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
