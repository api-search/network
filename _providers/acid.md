---
api_count: 5
apis:
- description: PostgreSQL provides full ACID compliance through its transaction management system including BEGIN, COMMIT, ROLLBACK, SAVEPOINT, and isolation level controls (READ COMMITTED, REPEATABLE READ, SERIALIZ
  name: PostgreSQL Transaction API
  slug: ''
- description: CockroachDB is a distributed SQL database providing serializable ACID transactions across multiple nodes and regions. It uses the Raft consensus algorithm and supports the PostgreSQL wire protocol. Co
  name: CockroachDB Distributed SQL API
  slug: ''
- description: Google Spanner is a globally distributed, externally consistent database providing ACID transactions at global scale using TrueTime clock synchronization (GPS receivers and atomic clocks). The Cloud S
  name: Google Spanner API
  slug: ''
- description: Amazon Aurora provides ACID-compliant transactions for both MySQL-compatible and PostgreSQL-compatible editions. Aurora's distributed storage layer provides durability across 3 availability zones with
  name: Amazon Aurora Transactions API
  slug: ''
- description: Atomikos provides ACID transaction management middleware for distributed microservices, supporting XA transactions across REST services using the Try-Confirm/Cancel (TCC) pattern. It enables ACID guar
  name: Atomikos Transaction API
  slug: ''
common:
- title: ACID Wikipedia Reference
  type: Website
  url: https://en.wikipedia.org/wiki/ACID
- title: CockroachDB Open Source Repository
  type: GitHubRepository
  url: https://github.com/cockroachdb/cockroach
- title: ACID JSON-LD Context
  type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/acid/refs/heads/main/json-ld/acid-context.jsonld
- title: ACID Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/acid/refs/heads/main/vocabulary/acid-vocabulary.yaml
created: '2025-01-01'
description: ACID (Atomicity, Consistency, Isolation, Durability) is a set of properties that guarantee database transactions are processed reliably even in the face of errors, power failures, or system crashes. These four properties ensure that data remains accurate and consistent, making ACID compliance a fundamental requirement for relational databases, distributed systems, and financial APIs.
features:
- description: 'Transactions are all-or-nothing: either all operations in a transaction succeed and are committed, or none are applied and the database is rolled back to its prior state.'
  name: Atomicity
- description: A transaction brings the database from one valid, consistent state to another, enforcing all defined constraints, triggers, and cascades. No transaction can leave data in an invalid state.
  name: Consistency
- description: Concurrent transactions execute as if they were serialized, preventing interference. Isolation levels (READ COMMITTED, REPEATABLE READ, SERIALIZABLE) control the degree of visibility between concurrent transactions.
  name: Isolation
- description: Once a transaction is committed, it remains committed even in the event of system crashes, power failures, or other errors, typically achieved through write-ahead logging (WAL) and replication.
  name: Durability
- description: Modern distributed databases extend ACID guarantees across multiple nodes, regions, and data centers using consensus algorithms (Raft, Paxos) and synchronized clocks (TrueTime).
  name: Distributed ACID
- description: Design patterns for ACID-like guarantees in REST APIs include Two-Phase Commit (2PC), Try-Confirm/Cancel (TCC), and Saga patterns for managing distributed transactions across microservices.
  name: REST API Transaction Patterns
image: /assets/icons/acid.png
integrations:
- description: The most widely deployed open-source RDBMS with full ACID compliance via MVCC and configurable transaction isolation levels.
  name: PostgreSQL
- description: Popular open-source databases providing ACID compliance through the InnoDB storage engine with row-level locking and MVCC.
  name: MySQL / MariaDB
- description: MongoDB added multi-document ACID transactions in version 4.0, extending its document model with ACID guarantees across documents and collections.
  name: MongoDB Multi-Document Transactions
- description: Kafka's transactional API (since 0.11) enables exactly-once semantics with atomic writes to multiple partitions, providing ACID-like guarantees for stream processing pipelines.
  name: Apache Kafka Transactions
- description: The Saga pattern decomposes long-running transactions into a series of local transactions with compensating actions for distributed consistency without 2PC overhead.
  name: Saga Pattern / Orchestration
jsonld:
- class_count: 2
  name: Acid Context
  property_count: 22
  slug: acid-context
layout: provider
modified: '2026-04-19'
name: ACID
skills: []
slug: acid
solutions: []
tags:
- ACID
- Database
- Transactions
- Atomicity
- Consistency
- Isolation
- Durability
- Distributed Systems
url: https://raw.githubusercontent.com/api-evangelist/acid/refs/heads/main/apis.yml
use_cases:
- description: Banking and payment systems require ACID compliance to ensure monetary transfers are atomic — debits and credits always balance — and durable across system failures.
  name: Financial Transactions
- description: E-commerce and supply chain systems use ACID transactions to prevent overselling by ensuring inventory decrements and order creation are atomic.
  name: Inventory Management
- description: Microservices architectures use Saga and TCC patterns to achieve eventual consistency with compensating transactions when full ACID across services is not feasible.
  name: Distributed Microservices Coordination
- description: Global applications use databases like Google Spanner and CockroachDB to maintain ACID consistency across geographic regions without sacrificing availability.
  name: Multi-Region Database Replication
- description: REST APIs use database transactions to implement idempotency keys, ensuring duplicate requests produce the same result without double processing.
  name: Idempotent API Design
---
