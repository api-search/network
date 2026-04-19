---
api_count: 5
apis:
- description: REST API for managing vaults, keys, secrets, and certificates in Azure Key Vault.
  name: Azure Key Vault API
  slug: ''
- description: API for performing cryptographic operations and managing keys, secrets, and certificates within a specific Key Vault instance.
  name: Azure Key Vault Data Plane API
  slug: ''
- description: 'REST API for creating, importing, updating, and performing cryptographic operations with keys in Azure Key Vault. Supports RSA, EC, and symmetric key types with operations including encrypt, decrypt, '
  name: Azure Key Vault Keys API
  slug: ''
- description: REST API for securely storing and managing secrets such as passwords, connection strings, and API keys in Azure Key Vault.
  name: Azure Key Vault Secrets API
  slug: ''
- description: REST API for creating, importing, managing, and renewing certificates in Azure Key Vault.
  name: Azure Key Vault Certificates API
  slug: ''
capabilities:
- description: Unified workflow for managing cryptographic keys, secrets, and certificates with encryption, signing, and certificate lifecycle operations. Used by security engineers and DevOps teams.
  name: Azure Key Vault Secrets and Keys
  slug: secrets-and-keys
common:
- title: ''
  type: StatusPage
  url: https://status.azure.com/
- title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- title: ''
  type: ChangeLog
  url: https://docs.microsoft.com/en-us/azure/key-vault/general/whats-new
- title: ''
  type: Portal
  url: https://portal.azure.com/
- title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/key-vault/
- title: ''
  type: SpectralRules
  url: rules/azure-key-vault-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/azure-key-vault-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/secrets-and-keys.yaml
created: '2024'
description: Azure Key Vault is a cloud service for securely storing and accessing secrets, keys, and certificates. It helps safeguard cryptographic keys and secrets used by cloud applications and services.
features:
- description: Create, import, and manage cryptographic keys with support for RSA, EC, and symmetric key types.
  name: Key Management
- description: Securely store and control access to passwords, connection strings, API keys, and other secrets.
  name: Secrets Management
- description: Automate certificate creation, renewal, and management with certificate authority integration.
  name: Certificate Lifecycle
- description: Perform encrypt, decrypt, sign, verify, wrap, and unwrap operations using managed keys.
  name: Cryptographic Operations
- description: Use hardware security modules for FIPS 140-2 Level 2 validated key protection.
  name: HSM-Backed Keys
- description: Recover accidentally deleted vaults, keys, secrets, and certificates with configurable retention.
  name: Soft Delete and Purge Protection
image: https://azure.microsoft.com/svghandler/key-vault/
integrations:
- description: Reference Key Vault secrets and certificates directly from App Service configuration.
  name: Azure App Service
- description: Mount Key Vault secrets as volumes in AKS pods using the Secrets Store CSI Driver.
  name: Azure Kubernetes Service
- description: Use Key Vault secrets in CI/CD pipelines for secure deployment automation.
  name: Azure DevOps
- description: Encrypt Azure VM disks using customer-managed keys stored in Key Vault.
  name: Azure Disk Encryption
- description: Enable Transparent Data Encryption with customer-managed keys from Key Vault.
  name: Azure SQL Database
jsonld:
- class_count: 0
  name: Azure Key Vault Context
  property_count: 57
  slug: azure-key-vault-context
- class_count: 0
  name: Azure Key Vault Data Plane Context
  property_count: 0
  slug: azure-key-vault-data-plane-context
layout: provider
modified: '2026-04-18'
name: Azure Key Vault
rules:
- name: Azure Key Vault API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: azure-key-vault-spectral-rules
skills: []
slug: azure-key-vault
solutions: []
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
url: https://azure.microsoft.com/en-us/services/key-vault/
use_cases:
- description: Centralize and secure application secrets with audited access and automatic rotation.
  name: Application Secret Management
- description: Encrypt data at rest and in transit using customer-managed keys stored in Key Vault.
  name: Data Encryption
- description: Automate TLS certificate provisioning and renewal for web applications and services.
  name: TLS Certificate Management
- description: Sign code, documents, and artifacts using keys stored securely in Key Vault.
  name: Code and Document Signing
---
