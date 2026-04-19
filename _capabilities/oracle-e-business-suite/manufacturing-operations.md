---
consumed_apis:
- oracle-manufacturing
- oracle-supply-chain
description: Manufacturing execution combining BOMs, routings, discrete jobs, WIP operations, and inventory management. Used by production managers and shop floor supervisors for manufacturing lifecycle.
layout: capability
name: Oracle EBS Manufacturing Operations
operations:
- description: List BOMs.
  method: GET
  name: get-bills-of-material
  path: /v1/bills-of-material
- description: List discrete jobs.
  method: GET
  name: get-discrete-jobs
  path: /v1/discrete-jobs
- description: List inventory items.
  method: GET
  name: get-inventory-items
  path: /v1/inventory-items
- description: List on-hand quantities.
  method: GET
  name: get-onhand-quantities
  path: /v1/onhand-quantities
personas: []
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
search_terms:
- on-hand quantity management.
- mfg issue material
- mfg create discrete job
- retrieve bills of material.
- business applications
- e-business suite
- inv get onhand quantities
- get bom by id.
- inv get deliveries
- get onhand quantities
- create a discrete job.
- retrieve wip operations.
- mfg get bills of material
- list on-hand quantities.
- oracle
- retrieve deliveries.
- enterprise
- erp
- mfg get bill of material by id
- inv get sales orders
- mfg get wip operations
- get discrete job by id.
- mfg get discrete job by id
- bom management.
- list discrete jobs.
- retrieve routings.
- inv get inventory items
- supply chain
- list boms.
- inventory item management.
- production
- mfg get routings
- get discrete jobs
- retrieve sales orders.
- get bills of material
- manufacturing
- get inventory items
- mfg get discrete jobs
- issue material to a job.
- complete an assembly.
- retrieve on-hand quantities.
- list inventory items.
- mfg complete assembly
- retrieve discrete jobs.
- retrieve inventory items.
- discrete job management.
slug: manufacturing-operations
tags:
- Oracle
- Manufacturing
- Supply Chain
- Production
tools:
- description: Retrieve bills of material.
  hints:
    openWorld: true
    readOnly: true
  name: mfg-get-bills-of-material
- description: Get BOM by ID.
  hints:
    readOnly: true
  name: mfg-get-bill-of-material-by-id
- description: Retrieve routings.
  hints:
    readOnly: true
  name: mfg-get-routings
- description: Retrieve discrete jobs.
  hints:
    readOnly: true
  name: mfg-get-discrete-jobs
- description: Create a discrete job.
  hints:
    readOnly: false
  name: mfg-create-discrete-job
- description: Get discrete job by ID.
  hints:
    readOnly: true
  name: mfg-get-discrete-job-by-id
- description: Retrieve WIP operations.
  hints:
    readOnly: true
  name: mfg-get-wip-operations
- description: Complete an assembly.
  hints:
    readOnly: false
  name: mfg-complete-assembly
- description: Issue material to a job.
  hints:
    readOnly: false
  name: mfg-issue-material
- description: Retrieve inventory items.
  hints:
    readOnly: true
  name: inv-get-inventory-items
- description: Retrieve on-hand quantities.
  hints:
    readOnly: true
  name: inv-get-onhand-quantities
- description: Retrieve sales orders.
  hints:
    readOnly: true
  name: inv-get-sales-orders
- description: Retrieve deliveries.
  hints:
    readOnly: true
  name: inv-get-deliveries
---
