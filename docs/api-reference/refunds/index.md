# Refunds API

The Refunds API allows you to process full and partial refunds for successful payments, manage refund metadata, and track refund status across different payment processors.

---

## Primary Endpoints

### [Create a Refund](post--refunds)
`POST /refunds`
Initiate a full or partial refund for a specific payment.

### [Retrieve a Refund](get--refunds-refund_id)
`GET /refunds/{refund_id}`
Get the details and current status of a specific refund.

### [Update a Refund](post--refunds-refund_id)
`POST /refunds/{refund_id}`
Update the metadata or other non-financial details of a refund.

### [List Refunds](post--refunds-list)
`POST /refunds/list`
Search and list refunds with advanced filtering and pagination.

---

## 🛠️ Key Concepts

- **Full Refund**: Automatically refunds the entire amount of the original payment.
- **Partial Refund**: Refund a specific portion of the payment. Multiple partial refunds can be issued until the original amount is reached.
- **Refund Status**: Common statuses include `succeeded`, `pending`, `failed`, and `cancelled`.

---

## Playground
Try the Refunds API live in the [Hyperswitch Playground](https://sandbox.hyperswitch.io/playground?category=refunds).
