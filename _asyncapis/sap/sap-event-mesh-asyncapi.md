---
channels:
- description: Event emitted when a new business partner is created in SAP S/4HANA.
  name: sap/s4/beh/businesspartner/v1/BusinessPartner/Created/v1
  operation: publish
  operation_id: onBusinessPartnerCreated
  summary: Business Partner Created
- description: Event emitted when an existing business partner is modified in SAP S/4HANA.
  name: sap/s4/beh/businesspartner/v1/BusinessPartner/Changed/v1
  operation: publish
  operation_id: onBusinessPartnerChanged
  summary: Business Partner Changed
- description: Event emitted when a new sales order is created in SAP S/4HANA.
  name: sap/s4/beh/salesorder/v1/SalesOrder/Created/v1
  operation: publish
  operation_id: onSalesOrderCreated
  summary: Sales Order Created
- description: Event emitted when a sales order is modified in SAP S/4HANA.
  name: sap/s4/beh/salesorder/v1/SalesOrder/Changed/v1
  operation: publish
  operation_id: onSalesOrderChanged
  summary: Sales Order Changed
- description: Event emitted when a new purchase order is created in SAP S/4HANA.
  name: sap/s4/beh/purchaseorder/v1/PurchaseOrder/Created/v1
  operation: publish
  operation_id: onPurchaseOrderCreated
  summary: Purchase Order Created
- description: Event emitted when a material document (goods receipt, goods issue) is posted in SAP S/4HANA.
  name: sap/s4/beh/materialDocument/v1/MaterialDocument/Created/v1
  operation: publish
  operation_id: onMaterialDocumentCreated
  summary: Material Document Created
description: Event-driven messaging API for SAP Business Technology Platform supporting AMQP, MQTT, and REST protocols. Enables publish/subscribe patterns for business events across SAP and third-party applications.
layout: asyncapi
messages:
- description: ''
  name: BusinessPartnerCreated
  summary: ''
  title: Business Partner Created Event
- description: ''
  name: BusinessPartnerChanged
  summary: ''
  title: Business Partner Changed Event
- description: ''
  name: SalesOrderCreated
  summary: ''
  title: Sales Order Created Event
- description: ''
  name: SalesOrderChanged
  summary: ''
  title: Sales Order Changed Event
- description: ''
  name: PurchaseOrderCreated
  summary: ''
  title: Purchase Order Created Event
- description: ''
  name: MaterialDocumentCreated
  summary: ''
  title: Material Document Created Event
name: SAP Event Mesh Events
provider_name: SAP
provider_slug: sap
servers:
- description: SAP Event Mesh REST API endpoint
  name: restServer
  protocol: https
  url: https://enterprise-messaging-pubsub.cfapps.{region}.hana.ondemand.com
- description: SAP Event Mesh MQTT endpoint
  name: mqttServer
  protocol: mqtts
  url: mqtts://enterprise-messaging-messaging-mqtts.cfapps.{region}.hana.ondemand.com:443
- description: SAP Event Mesh AMQP endpoint
  name: amqpServer
  protocol: amqps
  url: amqps://enterprise-messaging-messaging-amqps.cfapps.{region}.hana.ondemand.com:443
slug: sap-event-mesh-asyncapi
spec_file: asyncapi/sap-event-mesh-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/sap/refs/heads/main/asyncapi/sap-event-mesh-asyncapi.yml
tags:
- AI
- BTP
- Business Applications
- Cloud
- Data Management
- Enterprise
- ERP
- Integration
- AsyncAPI
- Webhooks
- Events
version: '1.0'
---
