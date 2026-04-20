# Payments API

The Payments API is the central component of Hyperswitch, allowing you to create, manage, and track payment transactions across multiple processors.

## Payment Lifecycle

A typical payment follows these states:
1.  **Created**: A payment intent is created.
2.  **Requires Action**: Customer needs to authenticate (e.g., 3DS).
3.  **Processing**: The payment is being authorized by the gateway.
4.  **Succeeded**: Payment was successful.
5.  **Failed**: Payment was declined or an error occurred.

---

## Primary Endpoints

<div class="endpoint-card">
  <span class="method-badge method-post">POST</span> <code>/payments</code>
  <h3>[Create a Payment](post--payments)</h3>
  <p>Initiate a new payment transaction. This returns a <code>client_secret</code> for frontend integration.</p>
  <a href="https://sandbox.hyperswitch.io/playground?endpoint=/payments&method=POST" class="playground-badge" target="_blank">Try in Playground</a>
</div>

<div class="endpoint-card">
  <span class="method-badge method-get">GET</span> <code>/payments/{payment_id}</code>
  <h3>[Retrieve a Payment](get--payments-payment_id)</h3>
  <p>Get the current status and details of a specific payment.</p>
</div>

<div class="endpoint-card">
  <span class="method-badge method-post">POST</span> <code>/payments/{payment_id}/confirm</code>
  <h3>[Confirm a Payment](post--payments-payment_id-confirm)</h3>
  <p>Finalize a payment that requires manual confirmation or has pending actions.</p>
</div>

<div class="endpoint-card">
  <span class="method-badge method-post">POST</span> <code>/payments/{payment_id}/capture</code>
  <h3>[Capture a Payment](post--payments-payment_id-capture)</h3>
  <p>Capture funds for a previously authorized payment (Auth-Capture flow).</p>
</div>

---

## 🛠️ Management & Optimization

### [Update a Payment](post--payments-payment_id)
Modify payment details such as amount, metadata, or customer info.

### [Cancel a Payment](post--payments-payment_id-cancel)
Void an authorized payment or cancel a pending intent.

### [List Payments](get--payments-list)
Retrieve a list of payments with filtering and pagination.

---

## 🛡️ Advanced Features

- [Incremental Authorization](post--payments-payment_id-incremental_authorization) — Increase the authorized amount on a confirmed payment.
- [Extended Authorization](post--payments-payment_id-extend_authorization) — Extend the validity period of an authorization.
- [External 3DS Authentication](post--payments-payment_id-3ds-authentication) — Integrate with third-party 3DS providers.
- [Session Tokens](post--payments-session_tokens) — Generate tokens for mobile SDKs.

---

## Playground
Try the Payments API live in the [Hyperswitch Playground](https://sandbox.hyperswitch.io/playground?category=payments).
