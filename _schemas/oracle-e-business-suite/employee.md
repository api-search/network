---
description: Schema representing an employee record in Oracle E-Business Suite Human Resources Management System (HRMS). Maps to PER_ALL_PEOPLE_F, PER_ALL_ASSIGNMENTS_F, PER_ADDRESSES, and PER_PHONES tables. Uses date-track versioning where records have effective start and end dates.
layout: schema
name: Oracle EBS Employee
properties_list:
- description: Unique person identifier (PER_ALL_PEOPLE_F.PERSON_ID)
  name: personId
  type: integer
- description: Employee number (PER_ALL_PEOPLE_F.EMPLOYEE_NUMBER)
  name: employeeNumber
  type: string
- description: Person type identifier (PER_PERSON_TYPES.PERSON_TYPE_ID)
  name: personTypeId
  type: integer
- description: Title (Mr., Mrs., Ms., Dr., etc.)
  name: title
  type:
  - string
  - 'null'
- description: First name
  name: firstName
  type: string
- description: Middle name(s)
  name: middleNames
  type:
  - string
  - 'null'
- description: Last name
  name: lastName
  type: string
- description: Name suffix (Jr., Sr., III, etc.)
  name: suffix
  type:
  - string
  - 'null'
- description: 'Full name (system-derived: LastName, Title FirstName MiddleNames Suffix)'
  name: fullName
  type: string
- description: Preferred/known-as name
  name: knownAs
  type:
  - string
  - 'null'
- description: Previous last name (maiden name)
  name: previousLastName
  type:
  - string
  - 'null'
- description: Email address
  name: emailAddress
  type:
  - string
  - 'null'
- description: Gender
  name: sex
  type: string
- description: Date of birth
  name: dateOfBirth
  type:
  - string
  - 'null'
- description: National identifier (Social Security Number, National Insurance Number, etc.)
  name: nationalIdentifier
  type:
  - string
  - 'null'
- description: Nationality lookup code
  name: nationality
  type:
  - string
  - 'null'
- description: Marital status lookup code
  name: maritalStatus
  type:
  - string
  - 'null'
- description: Registered disabled status
  name: registeredDisabledFlag
  type:
  - string
  - 'null'
- description: Date-track effective start date
  name: effectiveStartDate
  type: string
- description: Date-track effective end date (31-DEC-4712 for current records)
  name: effectiveEndDate
  type: string
- description: Original hire date (PER_PERIODS_OF_SERVICE.DATE_START)
  name: hireDate
  type: string
- description: Original date of hire (may differ from hire date for rehires)
  name: originalDateOfHire
  type:
  - string
  - 'null'
- description: Adjusted service date
  name: adjustedServiceDate
  type:
  - string
  - 'null'
- description: Actual termination date
  name: terminationDate
  type:
  - string
  - 'null'
- description: Whether the person is currently an active employee
  name: currentEmployeeFlag
  type: string
- description: Business group identifier (HR_ALL_ORGANIZATION_UNITS.ORGANIZATION_ID)
  name: businessGroupId
  type: integer
- description: Primary employee assignment
  name: assignment
  type: object
- description: All employee assignments (including secondary)
  name: assignments
  type: array
- description: Employee addresses
  name: addresses
  type: array
- description: Employee phone numbers
  name: phones
  type: array
- description: Current period of service
  name: periodOfService
  type: object
- description: User who created the record
  name: createdBy
  type: integer
- description: Record creation date
  name: creationDate
  type: string
- description: User who last updated the record
  name: lastUpdatedBy
  type: integer
- description: Record last update date
  name: lastUpdateDate
  type: string
- description: Object version number for optimistic locking
  name: objectVersionNumber
  type: integer
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/employee.json
slug: employee
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: Oracle EBS Employee
---
