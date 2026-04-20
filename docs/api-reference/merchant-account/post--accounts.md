# Merchant Account - Create

**Endpoint:** `POST /accounts`

Create a new account for a *merchant* and the *merchant* could be a seller or retailer or client who likes to receive and send payments.

**Operation ID:** `Create a Merchant Account`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/accounts&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `merchant_id` | string | YES | The identifier for the Merchant Account |
| `merchant_name` | string | NO | Name of the Merchant Account |
| `merchant_details` | string | NO |  |
| `return_url` | string | NO | The URL to redirect after the completion of the operation |
| `webhook_details` | string | NO |  |
| `payout_routing_algorithm` | string | NO |  |
| `sub_merchants_enabled` | boolean | NO | A boolean value to indicate if the merchant is a sub-merchant under a master or a parent merchant. By default, its value is false. |
| `parent_merchant_id` | string | NO | Refers to the Parent Merchant ID if the merchant being created is a sub-merchant |
| `enable_payment_response_hash` | boolean | NO | A boolean value to indicate if payment response hash needs to be enabled |
| `payment_response_hash_key` | string | NO | Refers to the hash key used for calculating the signature for webhooks and redirect response. If the value is not provided, a value is automatically generated. |
| `redirect_to_merchant_with_http_post` | boolean | NO | A boolean value to indicate if redirect to merchant with http post needs to be enabled. |
| `metadata` | object | NO | Metadata is useful for storing additional, unstructured information on an object |
| `publishable_key` | string | NO | API key that will be used for client side API access. A publishable key has to be always paired with a `client_secret`.
A `client_secret` can be obtained by creating a payment with `confirm` set to false |
| `locker_id` | string | NO | An identifier for the vault used to store payment method information. |
| `primary_business_details` | string | NO |  |
| `frm_routing_algorithm` | object | NO | The frm routing algorithm to be used for routing payments to desired FRM's |
| `organization_id` | string | NO | The id of the organization to which the merchant belongs to, if not passed an organization is created |
| `pm_collect_link_config` | string | NO |  |
| `product_type` | string | NO |  |
| `merchant_account_type` | string | NO |  |
| `network_tokenization_credentials` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/accounts" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "merchant_id": "example",
  "merchant_name": "example",
  "merchant_details": "example",
  "return_url": "example",
  "webhook_details": "example"
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/accounts"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "merchant_id": "example",
  "merchant_name": "example",
  "merchant_details": "example",
  "return_url": "example",
  "webhook_details": "example"
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/accounts";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "merchant_id": "example",
  "merchant_name": "example",
  "merchant_details": "example",
  "return_url": "example",
  "webhook_details": "example"
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
