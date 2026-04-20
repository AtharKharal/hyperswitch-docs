# Customers API

The Customers API allows you to create and manage customer profiles. Storing customer information enables faster checkouts and better tracking of payment history.

---

## Primary Endpoints

### [Create a Customer](post--customers)
`POST /customers`
Create a new customer profile to store contact information and metadata.

### [Retrieve a Customer](get--customers-customer_id)
`GET /customers/{customer_id}`
Get the details of a specific customer, including their metadata and status.

### [Update a Customer](post--customers-customer_id)
`POST /customers/{customer_id}`
Modify existing customer information.

### [Delete a Customer](delete--customers-customer_id)
`DELETE /customers/{customer_id}`
Permanently remove a customer profile.

---

## 🛠️ Key Concepts

- **Customer ID**: A unique identifier (e.g., `cus_abc123`) used to link payments and payment methods to a specific user.
- **Metadata**: Key-value pairs that can be used to store additional information like loyalty tiers or internal user IDs.
- **Repeat Payments**: By passing a `customer_id` during payment creation, you can leverage saved payment methods for a "one-click" checkout experience.

---

## Playground
Try the Customers API live in the [Hyperswitch Playground](https://sandbox.hyperswitch.io/playground?category=customers).
