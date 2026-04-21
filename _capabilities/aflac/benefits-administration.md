---
consumed_apis:
- aflac-enterprise-connect
description: Unified workflow capability for Aflac supplemental insurance benefits administration covering enrollment, claims, eligibility, and policy management. Used by HR platform engineers and benefits administrators.
layout: capability
name: Aflac Benefits Administration
operations:
- description: List benefit enrollments.
  method: GET
  name: list-enrollments
  path: /v1/enrollments
- description: Create a new enrollment.
  method: POST
  name: create-enrollment
  path: /v1/enrollments
- description: Retrieve an enrollment.
  method: GET
  name: get-enrollment
  path: /v1/enrollments/{enrollment_id}
- description: List claims.
  method: GET
  name: list-claims
  path: /v1/claims
- description: Submit a claim.
  method: POST
  name: submit-claim
  path: /v1/claims
- description: Verify employee eligibility.
  method: POST
  name: verify-eligibility
  path: /v1/eligibility/verify
personas:
- description: Backend developer integrating Aflac supplemental insurance enrollment into an HR or benefits administration platform.
  id: hr-platform-engineer
  name: HR Platform Engineer
- description: HR or benefits team member managing employee enrollment, claims, and eligibility for supplemental insurance.
  id: benefits-administrator
  name: Benefits Administrator
provider_name: aflac
provider_slug: aflac
search_terms:
- submit an aflac supplemental insurance claim for a qualifying event.
- list claims
- verify employee eligibility.
- hr platform engineer
- get enrollment
- claim submission and tracking for qualifying health events.
- list aflac supplemental insurance claims.
- hr or benefits team member managing employee enrollment, claims, and eligibility for supplemental insurance.
- benefit enrollment management.
- aflac
- verify an employee's eligibility for an aflac supplemental insurance product.
- list claims.
- claims
- list enrollments
- claims management.
- insurance
- create a new enrollment.
- enroll an employee in an aflac supplemental insurance product.
- real-time eligibility verification for supplemental insurance products.
- enrollment
- create enrollment
- benefits
- benefits administrator
- retrieve a specific aflac enrollment record.
- employee enrollment in supplemental insurance products.
- retrieve an enrollment.
- backend developer integrating aflac supplemental insurance enrollment into an hr or benefits administration platform.
- list benefit enrollments.
- specific enrollment operations.
- submit a claim.
- verify eligibility
- full supplemental insurance benefits lifecycle from enrollment through claims and eligibility verification.
- active supplemental insurance policy tracking.
- list aflac supplemental insurance benefit enrollments for a group or employee.
- submit claim
- eligibility verification.
slug: benefits-administration
tags:
- Aflac
- Benefits
- Insurance
- Enrollment
- Claims
tools:
- description: List Aflac supplemental insurance benefit enrollments for a group or employee.
  hints:
    destructive: false
    readOnly: true
  name: list-enrollments
- description: Enroll an employee in an Aflac supplemental insurance product.
  hints:
    destructive: false
    readOnly: false
  name: create-enrollment
- description: Retrieve a specific Aflac enrollment record.
  hints:
    destructive: false
    readOnly: true
  name: get-enrollment
- description: List Aflac supplemental insurance claims.
  hints:
    destructive: false
    readOnly: true
  name: list-claims
- description: Submit an Aflac supplemental insurance claim for a qualifying event.
  hints:
    destructive: false
    readOnly: false
  name: submit-claim
- description: Verify an employee's eligibility for an Aflac supplemental insurance product.
  hints:
    destructive: false
    readOnly: true
  name: verify-eligibility
---
