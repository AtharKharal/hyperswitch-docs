# Payments - Create

**Endpoint:** `POST /payments`

Creates a payment resource, which represents a customer's intent to pay.
This endpoint is the starting point for various payment flows:


**Operation ID:** `Create a Payment`

## Playground

<a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments&method=POST" class="md-button-playground" target="_blank">Try in Playground →</a>

## Try It Now

<div class="api-playground" data-endpoint="/payments" data-method="POST">
  <div class="playground-form">
    <div class="form-group">
      <label>API Key</label>
      <input type="password" name="api-key" placeholder="sk_test_..." />
    </div>
    <div class="form-group">
      <label>Amount</label>
      <input type="number" name="amount" value="1000" />
    </div>
    <div class="form-group">
      <label>Currency</label>
      <input type="text" name="currency" value="USD" />
    </div>
    <button type="button" class="execute-btn">Execute Request</button>
  </div>
  <div class="response-section" style="display:none;">
    <label>Response</label>
    <pre class="response-output"></pre>
  </div>
</div>

## Parameters

| Parameter | Type | Required | Description |
|------------|------|----------|-------------|
| `amount` | integer | YES | The primary amount for the payment, provided in the lowest denomination of the specified currency (e.g., 6540 for $65.40 USD). This field is mandatory for creating a payment. |
| `order_tax_amount` | integer | NO | Total tax amount applicable to the order, in the lowest denomination of the currency. |
| `currency` | string | YES |  |
| `amount_to_capture` | integer | NO | The amount to be captured from the user's payment method, in the lowest denomination. If not provided, and `capture_method` is `automatic`, the full payment `amount` will be captured. If `capture_method` is `manual`, this can be specified in the `/capture` call. Must be less than or equal to the authorized amount. |
| `shipping_cost` | integer | NO | The shipping cost for the payment. This is required for tax calculation in some regions. |
| `payment_id` | string | NO | Optional. A merchant-provided unique identifier for the payment, contains 30 characters long (e.g., "pay_mbabizu24mvu3mela5njyhpit4"). If provided, it ensures idempotency for the payment creation request. If omitted, Hyperswitch generates a unique ID for the payment. |
| `routing` | string | NO |  |
| `connector` | array | NO | This allows to manually select a connector with which the payment can go through. |
| `capture_method` | string | NO |  |
| `authentication_type` | string | NO |  |
| `billing` | string | NO |  |
| `confirm` | boolean | NO | If set to `true`, Hyperswitch attempts to confirm and authorize the payment immediately after creation, provided sufficient payment method details are included. If `false` or omitted (default is `false`), the payment is created with a status such as `requires_payment_method` or `requires_confirmation`, and a separate `POST /payments/{payment_id}/confirm` call is necessary to proceed with authorization. |
| `customer` | string | NO |  |
| `customer_id` | string | NO | The identifier for the customer |
| `off_session` | boolean | NO | Set to true to indicate that the customer is not in your checkout flow during this payment, and therefore is unable to authenticate. This parameter is intended for scenarios where you collect card details and charge them later. When making a recurring payment by passing a mandate_id, this parameter is mandatory |
| `description` | string | NO | An arbitrary string attached to the payment. Often useful for displaying to users or for your own internal record-keeping. |
| `return_url` | string | NO | The URL to redirect the customer to after they complete the payment process or authentication. This is crucial for flows that involve off-site redirection (e.g., 3DS, some bank redirects, wallet payments). |
| `setup_future_usage` | string | NO |  |
| `payment_method_data` | string | NO |  |
| `payment_method` | string | NO |  |
| `payment_token` | string | NO | As Hyperswitch tokenises the sensitive details about the payments method, it provides the payment_token as a reference to a stored payment method, ensuring that the sensitive details are not exposed in any manner. |
| `shipping` | string | NO |  |
| `statement_descriptor_name` | string | NO | For non-card charges, you can use this value as the complete description that appears on your customers’ statements. Must contain at least one letter, maximum 22 characters. To be deprecated soon, use billing_descriptor instead. |
| `statement_descriptor_suffix` | string | NO | Provides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor. To be deprecated soon, use billing_descriptor instead. |
| `order_details` | array | NO | Use this object to capture the details about the different products for which the payment is being made. The sum of amount across different products here should be equal to the overall payment amount |
| `mandate_data` | string | NO |  |
| `customer_acceptance` | string | NO |  |
| `mandate_id` | string | NO | A unique identifier to link the payment to a mandate. To do Recurring payments after a mandate has been created, pass the mandate_id instead of payment_method_data |
| `browser_info` | string | NO |  |
| `payment_experience` | string | NO |  |
| `payment_method_type` | string | NO |  |
| `business_country` | string | NO |  |
| `business_label` | string | NO | Business label of the merchant for this payment.
To be deprecated soon. Pass the profile_id instead |
| `merchant_connector_details` | string | NO |  |
| `allowed_payment_method_types` | array | NO | Use this parameter to restrict the Payment Method Types to show for a given PaymentIntent |
| `metadata` | object | NO | You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long. Metadata is useful for storing additional, structured information on an object. |
| `connector_metadata` | string | NO |  |
| `payment_link` | boolean | NO | Whether to generate the payment link for this payment or not (if applicable) |
| `payment_link_config` | string | NO |  |
| `payment_link_config_id` | string | NO | Custom payment link config id set at business profile, send only if business_specific_configs is configured |
| `profile_id` | string | NO | The business profile to be used for this payment, if not passed the default business profile associated with the merchant account will be used. It is mandatory in case multiple business profiles have been set up. |
| `surcharge_details` | string | NO |  |
| `payment_type` | string | NO |  |
| `request_incremental_authorization` | boolean | NO | Request an incremental authorization, i.e., increase the authorized amount on a confirmed payment before you capture it. |
| `session_expiry` | integer | NO | Will be used to expire client secret after certain amount of time to be supplied in seconds
(900) for 15 mins |
| `frm_metadata` | object | NO | Additional data related to some frm(Fraud Risk Management) connectors |
| `request_external_three_ds_authentication` | boolean | NO | Whether to perform external authentication (if applicable) |
| `three_ds_data` | string | NO |  |
| `recurring_details` | string | NO |  |
| `split_payments` | string | NO |  |
| `request_extended_authorization` | boolean | NO | Optional boolean value to extent authorization period of this payment

capture method must be manual or manual_multiple |
| `merchant_order_reference_id` | string | NO | Your unique identifier for this payment or order. This ID helps you reconcile payments on your system. If provided, it is passed to the connector if supported. |
| `skip_external_tax_calculation` | boolean | NO | Whether to calculate tax for this payment intent |
| `psd2_sca_exemption_type` | string | NO |  |
| `ctp_service_details` | string | NO |  |
| `force_3ds_challenge` | boolean | NO | Indicates if 3ds challenge is forced |
| `threeds_method_comp_ind` | string | NO |  |
| `is_iframe_redirection_enabled` | boolean | NO | Indicates if the redirection has to open in the iframe |
| `all_keys_required` | boolean | NO | If enabled, provides whole connector response |
| `payment_channel` | string | NO |  |
| `tax_status` | string | NO |  |
| `discount_amount` | integer | NO | Total amount of the discount you have applied to the order or transaction. |
| `shipping_amount_tax` | string | NO |  |
| `duty_amount` | string | NO |  |
| `order_date` | string | NO | Date the payer placed the order. |
| `enable_partial_authorization` | boolean | NO | Allow partial authorization for this payment |
| `enable_overcapture` | boolean | NO | Boolean indicating whether to enable overcapture for this payment |
| `is_stored_credential` | boolean | NO | Boolean flag indicating whether this payment method is stored and has been previously used for payments |
| `mit_category` | string | NO |  |
| `billing_descriptor` | string | NO |  |
| `tokenization` | string | NO |  |
| `partner_merchant_identifier_details` | string | NO |  |
| `installment_options` | array | NO | Installment payment options grouped by payment method. When provided, the payment is treated as an installment payment. |
| `installment_data` | string | NO |  |

## Code Examples

=== "cURL"

```bash
curl -X POST "https://sandbox.hyperswitch.io/payments" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{{
  "amount": 1000,
  "order_tax_amount": 1000,
  "currency": "example",
  "amount_to_capture": 1000,
  "shipping_cost": 1000
}}'
```

=== "Python"

```python
import requests

url = "https://sandbox.hyperswitch.io/payments"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}
payload = {
  "amount": 1000,
  "order_tax_amount": 1000,
  "currency": "example",
  "amount_to_capture": 1000,
  "shipping_cost": 1000
}
response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

=== "JavaScript"

```javascript
const axios = require("axios");
const url = "https://sandbox.hyperswitch.io/payments";
const options = {
  method: "POST",
  url: url,
  headers: {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"},
  data: {
  "amount": 1000,
  "order_tax_amount": 1000,
  "currency": "example",
  "amount_to_capture": 1000,
  "shipping_cost": 1000
}
};
axios.request(options).then(r => console.log(r.data)).catch(e => console.error(e));
```

## Response

```json
{"payment_id":"pay_abc123xyz","status":"requires_payment_method","client_secret":"pi_secret_xyz","amount":6540,"currency":"USD"}
```

---

*Last updated: 2026-04-19*
