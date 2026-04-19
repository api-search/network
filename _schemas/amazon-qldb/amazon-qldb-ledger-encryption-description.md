---
description: <p>Information about the encryption of data at rest in an Amazon QLDB ledger. This includes the current status, the key in Key Management Service (KMS), and when the key became inaccessible (in the case of an error).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/qldb/latest/developerguide/encryption-at-rest.html">Encryption at rest</a> in the <i>Amazon QLDB Developer Guide</i>.</p>
layout: schema
name: LedgerEncryptionDescription
properties_list:
- description: ''
  name: KmsKeyArn
  type: object
- description: ''
  name: EncryptionStatus
  type: object
- description: ''
  name: InaccessibleKmsKeyDateTime
  type: object
provider_name: Amazon QLDB
provider_slug: amazon-qldb
schema_file: json-schema/amazon-qldb-ledger-encryption-description-schema.json
slug: amazon-qldb-ledger-encryption-description
tags:
- AWS
- Blockchain
- Database
- Ledger
title: LedgerEncryptionDescription
---
