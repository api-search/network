---
consumed_apis:
- dynamodb
description: Unified capability for managing DynamoDB tables, items, queries, and transactions for application developers and data engineers.
layout: capability
name: Amazon DynamoDB NoSQL Database Operations
operations:
- description: Amazon DynamoDB Create a DynamoDB Table
  method: POST
  name: createTable
  path: /v1/resource
- description: Amazon DynamoDB Describe a DynamoDB Table
  method: POST
  name: describeTable
  path: /v1/#DescribeTable
- description: Amazon DynamoDB List DynamoDB Tables
  method: POST
  name: listTables
  path: /v1/#ListTables
- description: Amazon DynamoDB Update a DynamoDB Table
  method: POST
  name: updateTable
  path: /v1/#UpdateTable
- description: Amazon DynamoDB Delete a DynamoDB Table
  method: POST
  name: deleteTable
  path: /v1/#DeleteTable
- description: Amazon DynamoDB Put an Item Into a Table
  method: POST
  name: putItem
  path: /v1/#PutItem
- description: Amazon DynamoDB Get an Item from a Table
  method: POST
  name: getItem
  path: /v1/#GetItem
- description: Amazon DynamoDB Update an Item in a Table
  method: POST
  name: updateItem
  path: /v1/#UpdateItem
- description: Amazon DynamoDB Delete an Item from a Table
  method: POST
  name: deleteItem
  path: /v1/#DeleteItem
- description: Amazon DynamoDB Query Items in a Table or Index
  method: POST
  name: query
  path: /v1/#Query
personas: []
provider_name: Amazon DynamoDB
provider_slug: amazon-dynamodb
search_terms:
- nosql database operations business domain for amazon dynamodb.
- list tables
- updateItem
- query
- update table
- engineers managing amazon dynamodb resources on aws.
- amazon dynamodb put an item into a table
- deleteTable
- describeTable
- amazon dynamodb delete a dynamodb table
- document store
- amazon dynamodb delete an item from a table
- amazon dynamodb create a dynamodb table
- serverless
- workflow capability for nosql database operations.
- deleteItem
- update item
- amazon dynamodb query items in a table or index
- amazon dynamodb
- putItem
- amazon dynamodb describe a dynamodb table
- put item
- delete item
- amazon dynamodb get an item from a table
- amazon dynamodb update an item in a table
- amazon dynamodb list dynamodb tables
- create table
- aws
- getItem
- createTable
- database
- amazon dynamodb update a dynamodb table
- describe table
- updateTable
- nosql
- delete table
- get item
- listTables
- key-value
slug: dynamodb-management
tags:
- Amazon DynamoDB
- AWS
- Database
- NoSQL
tools:
- description: Amazon DynamoDB Create a DynamoDB Table
  hints:
    destructive: false
    readOnly: false
  name: create-table
- description: Amazon DynamoDB Describe a DynamoDB Table
  hints:
    destructive: false
    readOnly: false
  name: describe-table
- description: Amazon DynamoDB List DynamoDB Tables
  hints:
    destructive: false
    readOnly: false
  name: list-tables
- description: Amazon DynamoDB Update a DynamoDB Table
  hints:
    destructive: false
    readOnly: false
  name: update-table
- description: Amazon DynamoDB Delete a DynamoDB Table
  hints:
    destructive: false
    readOnly: false
  name: delete-table
- description: Amazon DynamoDB Put an Item Into a Table
  hints:
    destructive: false
    readOnly: false
  name: put-item
- description: Amazon DynamoDB Get an Item from a Table
  hints:
    destructive: false
    readOnly: false
  name: get-item
- description: Amazon DynamoDB Update an Item in a Table
  hints:
    destructive: false
    readOnly: false
  name: update-item
- description: Amazon DynamoDB Delete an Item from a Table
  hints:
    destructive: false
    readOnly: false
  name: delete-item
- description: Amazon DynamoDB Query Items in a Table or Index
  hints:
    destructive: false
    readOnly: false
  name: query
---
