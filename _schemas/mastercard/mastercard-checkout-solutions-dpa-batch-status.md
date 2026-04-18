---
description: The DpaBatchStatus response contains information related to the status of a submitted Digital Payment Application (DPA) batch.
layout: schema
name: DpaBatchStatus
properties_list:
- description: This field allows the Integrator to assign an internal reference to a batch request so that it can be used for internal tracking purposes.
  name: requestId
  type: string
- description: A unique identifier associated with the submitted Digital Payment Application (DPA) batch. The Batch ID can be used to retrieve the status of the batch by calling GET DPA status endpoint.
  name: batchId
  type: string
- description: 'Describes the outcome of the submitted Digital Payment Application (DPA) batch. Possible outcomes include: * COMPLETED_SUCCESSFULLY - Batch was completed successfully and all DPAs included in the batc'
  name: batchStatus
  type: string
- description: Start time of batch request
  name: batchStartTime
  type: string
- description: End time of batch request
  name: batchEndTime
  type: string
- description: Provides additional information when batchStatus yields a FAILED status.
  name: errorMessage
  type: string
- description: 'An array of status objects that describes the outcome of each Digital Payment Application (DPA) item in a batch request. Note: DPA item order may differ from original submission."'
  name: items
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-checkout-solutions-dpa-batch-status-schema.json
slug: mastercard-checkout-solutions-dpa-batch-status
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: DpaBatchStatus
---
