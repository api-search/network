---
description: ''
layout: schema
name: Occupation
properties_list:
- description: Employer Name. <BR/>This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: employerName
  type: string
- description: Department of client. <BR/>This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: department
  type: string
- description: Employee ID of client. <BR/>This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: employeeId
  type: string
- description: Joining date of current job. <BR/>This field is required if configured as **Business Mandatory**<font color='red'>* </font>. <br/> Format - It is expressed in ISO 8601 - `YYYY-MM-DD`
  name: joiningDate
  type: string
- description: Duration (in years) of employment with current employer. <BR/>This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: employmentDuration
  type: integer
- description: Annual income of client. <BR/>This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: netAnnualIncome
  type: integer
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-occupation-schema.json
slug: mastercard-card-issuance-occupation
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Occupation
---
