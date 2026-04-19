---
class_count: 71
classes:
- AccessDeniedException
- Boolean
- CertificateType
- ConflictException
- CreateAliasInput
- CreateAliasOutput
- CreateKeyInput
- CreateKeyOutput
- DeleteAliasInput
- DeleteAliasOutput
- DeleteKeyInput
- DeleteKeyInputDeleteKeyInDaysInteger
- DeleteKeyOutput
- ExportKeyInput
- ExportKeyMaterial
- ExportKeyOutput
- ExportTokenId
- ExportTr31KeyBlock
- ExportTr34KeyBlock
- GetAliasInput
- GetAliasOutput
- GetKeyInput
- GetKeyOutput
- GetParametersForExportInput
- GetParametersForExportOutput
- GetParametersForImportInput
- GetParametersForImportOutput
- GetPublicKeyCertificateInput
- GetPublicKeyCertificateOutput
- HexLength16
- ImportKeyInput
- ImportKeyMaterial
- ImportKeyOutput
- ImportTokenId
- ImportTr31KeyBlock
- ImportTr34KeyBlock
- InternalServerException
- KeyArnOrKeyAliasType
- KeySummary
- KeySummaryList
- ListAliasesInput
- ListAliasesOutput
- ListKeysInput
- ListKeysOutput
- ListTagsForResourceInput
- ListTagsForResourceOutput
- PrimitiveBoolean
- ResourceNotFoundException
- RestoreKeyInput
- RestoreKeyOutput
- ServiceQuotaExceededException
- ServiceUnavailableException
- StartKeyUsageInput
- StartKeyUsageOutput
- StopKeyUsageInput
- StopKeyUsageOutput
- Tag
- TagKey
- TagResourceInput
- TagResourceOutput
- TagValue
- ThrottlingException
- Timestamp
- Tr31WrappedKeyBlock
- Tr34KeyBlockFormat
- Tr34WrappedKeyBlock
- UntagResourceInput
- UntagResourceOutput
- UpdateAliasInput
- UpdateAliasOutput
- ValidationException
context_file: json-ld/amazon-payment-cryptography-openapi-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-payment-cryptography/refs/heads/main/json-ld/amazon-payment-cryptography-openapi-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Payment Cryptography Openapi from Amazon Payment Cryptography.
layout: jsonld
name: Amazon Payment Cryptography Openapi Context
namespaces:
- prefix: payment
  uri: https://payment.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Alias
  type: string
- container: ''
  name: AliasName
  type: string
- container: ''
  name: Aliases
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: KeyAlgorithm
  type: string
- container: ''
  name: KeyArn
  type: string
- container: ''
  name: KeyAttributes
  type: string
- container: ''
  name: KeyCheckValue
  type: string
- container: ''
  name: KeyCheckValueAlgorithm
  type: string
- container: ''
  name: KeyClass
  type: string
- container: ''
  name: KeyMaterial
  type: string
- container: ''
  name: KeyMaterialType
  type: string
- container: ''
  name: KeyModesOfUse
  type: string
- container: ''
  name: KeyOrigin
  type: string
- container: ''
  name: KeyState
  type: string
- container: ''
  name: KeyUsage
  type: string
- container: ''
  name: MaxResults
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: ResourceArn
  type: string
- container: ''
  name: RootCertificatePublicKey
  type: string
- container: ''
  name: TagKeys
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: TrustedCertificatePublicKey
  type: string
- container: ''
  name: WrappedKey
  type: string
- container: ''
  name: WrappedKeyMaterialFormat
  type: string
- container: ''
  name: CertificateAuthorityPublicKeyIdentifier
  type: string
- container: ''
  name: CreateTimestamp
  type: string
- container: ''
  name: Decrypt
  type: string
- container: ''
  name: DeleteKeyInDays
  type: string
- container: ''
  name: DeletePendingTimestamp
  type: string
- container: ''
  name: DeleteTimestamp
  type: string
- container: ''
  name: DeriveKey
  type: string
- container: ''
  name: Enabled
  type: string
- container: ''
  name: Encrypt
  type: string
- container: ''
  name: ExportKeyIdentifier
  type: string
- container: ''
  name: ExportToken
  type: string
- container: ''
  name: Exportable
  type: string
- container: ''
  name: Generate
  type: string
- container: ''
  name: ImportToken
  type: string
- container: ''
  name: KeyBlockFormat
  type: string
- container: ''
  name: KeyCertificate
  type: string
- container: ''
  name: KeyCertificateChain
  type: string
- container: ''
  name: KeyIdentifier
  type: string
- container: ''
  name: Keys
  type: string
- container: ''
  name: NoRestrictions
  type: string
- container: ''
  name: ParametersValidUntilTimestamp
  type: string
- container: ''
  name: PublicKeyCertificate
  type: string
- container: ''
  name: RandomNonce
  type: string
- container: ''
  name: Sign
  type: string
- container: ''
  name: SigningKeyAlgorithm
  type: string
- container: ''
  name: SigningKeyCertificate
  type: string
- container: ''
  name: SigningKeyCertificateChain
  type: string
- container: ''
  name: Tr31KeyBlock
  type: string
- container: ''
  name: Tr34KeyBlock
  type: string
- container: ''
  name: Unwrap
  type: string
- container: ''
  name: UsageStartTimestamp
  type: string
- container: ''
  name: UsageStopTimestamp
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: Verify
  type: string
- container: ''
  name: Wrap
  type: string
- container: ''
  name: WrappedKeyBlock
  type: string
- container: ''
  name: WrappingKeyAlgorithm
  type: string
- container: ''
  name: WrappingKeyArn
  type: string
- container: ''
  name: WrappingKeyCertificate
  type: string
- container: ''
  name: WrappingKeyCertificateChain
  type: string
- container: ''
  name: WrappingKeyIdentifier
  type: string
property_count: 66
provider_name: Amazon Payment Cryptography
provider_slug: amazon-payment-cryptography
slug: amazon-payment-cryptography-openapi-context
tags:
- AWS
- Cryptography
- Financial Services
- Payment Processing
- PCI
- JSON-LD
- Linked Data
- Semantic Web
---
