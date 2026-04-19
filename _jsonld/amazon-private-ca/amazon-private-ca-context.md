---
class_count: 59
classes:
- Extensions
- ExtendedKeyUsage
- KeyUsage
- AccessDescription
- AccessMethod
- ASN1Subject
- UpdateCertificateAuthorityRequest
- RevocationConfiguration
- ApiPassthrough
- DeleteCertificateAuthorityRequest
- GeneralName
- OtherName
- EdiPartyName
- Qualifier
- DescribeCertificateAuthorityRequest
- GetPolicyResponse
- ListPermissionsRequest
- DescribeCertificateAuthorityAuditReportResponse
- PutPolicyRequest
- DescribeCertificateAuthorityAuditReportRequest
- PolicyQualifierInfo
- CreateCertificateAuthorityRequest
- CertificateAuthorityConfiguration
- ListTagsRequest
- CsrExtensions
- IssueCertificateResponse
- GetCertificateRequest
- GetCertificateAuthorityCsrRequest
- GetCertificateAuthorityCertificateResponse
- CustomExtension
- CrlConfiguration
- GetCertificateAuthorityCsrResponse
- RestoreCertificateAuthorityRequest
- IssueCertificateRequest
- Validity
- CustomAttribute
- RevokeCertificateRequest
- GetCertificateAuthorityCertificateRequest
- Tag
- UntagCertificateAuthorityRequest
- TagCertificateAuthorityRequest
- PolicyInformation
- ImportCertificateAuthorityCertificateRequest
- CreateCertificateAuthorityAuditReportResponse
- Permission
- DeletePolicyRequest
- CreatePermissionRequest
- CreateCertificateAuthorityResponse
- GetPolicyRequest
- OcspConfiguration
- ListCertificateAuthoritiesRequest
- CreateCertificateAuthorityAuditReportRequest
- DescribeCertificateAuthorityResponse
- CertificateAuthority
- ListTagsResponse
- ListCertificateAuthoritiesResponse
- ListPermissionsResponse
- DeletePermissionRequest
- GetCertificateResponse
context_file: json-ld/amazon-private-ca-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-private-ca/refs/heads/main/json-ld/amazon-private-ca-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Private Ca from Amazon Private CA.
layout: jsonld
name: Amazon Private Ca Context
namespaces:
- prefix: pca
  uri: https://acm-pca.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: CertificatePolicies
  type: string
- container: ''
  name: SubjectAlternativeNames
  type: string
- container: ''
  name: CustomExtensions
  type: string
- container: ''
  name: AccessLocation
  type: string
- container: ''
  name: Country
  type: string
- container: ''
  name: Organization
  type: string
- container: ''
  name: OrganizationalUnit
  type: string
- container: ''
  name: DistinguishedNameQualifier
  type: string
- container: ''
  name: State
  type: string
- container: ''
  name: CommonName
  type: string
- container: ''
  name: SerialNumber
  type: string
- container: ''
  name: Locality
  type: string
- container: ''
  name: Title
  type: string
- container: ''
  name: Surname
  type: string
- container: ''
  name: GivenName
  type: string
- container: ''
  name: Initials
  type: string
- container: ''
  name: Pseudonym
  type: string
- container: ''
  name: GenerationQualifier
  type: string
- container: ''
  name: CustomAttributes
  type: string
- container: ''
  name: CertificateAuthorityArn
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: Subject
  type: string
- container: ''
  name: PermanentDeletionTimeInDays
  type: string
- container: ''
  name: Rfc822Name
  type: string
- container: ''
  name: DnsName
  type: string
- container: ''
  name: DirectoryName
  type: string
- container: ''
  name: UniformResourceIdentifier
  type: string
- container: ''
  name: IpAddress
  type: string
- container: ''
  name: RegisteredId
  type: string
- container: ''
  name: CpsUri
  type: string
- container: ''
  name: Policy
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: MaxResults
  type: string
- container: ''
  name: AuditReportStatus
  type: string
- container: ''
  name: S3BucketName
  type: string
- container: ''
  name: S3Key
  type: string
- container: ''
  name: CreatedAt
  type: string
- container: ''
  name: ResourceArn
  type: string
- container: ''
  name: AuditReportId
  type: string
- container: ''
  name: DigitalSignature
  type: string
- container: ''
  name: NonRepudiation
  type: string
- container: ''
  name: KeyEncipherment
  type: string
- container: ''
  name: DataEncipherment
  type: string
- container: ''
  name: KeyAgreement
  type: string
- container: ''
  name: KeyCertSign
  type: string
- container: ''
  name: CRLSign
  type: string
- container: ''
  name: EncipherOnly
  type: string
- container: ''
  name: DecipherOnly
  type: string
- container: ''
  name: PolicyQualifierId
  type: string
- container: ''
  name: CertificateAuthorityType
  type: string
- container: ''
  name: IdempotencyToken
  type: string
- container: ''
  name: KeyStorageSecurityStandard
  type: string
- container: ''
  name: Tags
  type: string
- container: ''
  name: UsageMode
  type: string
- container: ''
  name: KeyAlgorithm
  type: string
- container: ''
  name: SigningAlgorithm
  type: string
- container: ''
  name: CertificateArn
  type: string
- container: ''
  name: Certificate
  type: string
- container: ''
  name: CertificateChain
  type: string
- container: ''
  name: ObjectIdentifier
  type: string
- container: ''
  name: Value
  type: string
- container: ''
  name: Critical
  type: string
- container: ''
  name: SubjectInformationAccess
  type: string
- container: ''
  name: Enabled
  type: string
- container: ''
  name: ExpirationInDays
  type: string
- container: ''
  name: CustomCname
  type: string
- container: ''
  name: S3ObjectAcl
  type: string
- container: ''
  name: Csr
  type: string
- container: ''
  name: TemplateArn
  type: string
- container: ''
  name: ValidityNotBefore
  type: string
- container: ''
  name: CertificateSerial
  type: string
- container: ''
  name: RevocationReason
  type: string
- container: ''
  name: Key
  type: string
- container: ''
  name: CertPolicyId
  type: string
- container: ''
  name: PolicyQualifiers
  type: string
- container: ''
  name: Type
  type: string
- container: ''
  name: PartyName
  type: string
- container: ''
  name: NameAssigner
  type: string
- container: ''
  name: Principal
  type: string
- container: ''
  name: SourceAccount
  type: string
- container: ''
  name: Actions
  type: string
- container: ''
  name: ExtendedKeyUsageType
  type: string
- container: ''
  name: ExtendedKeyUsageObjectIdentifier
  type: string
- container: ''
  name: OcspCustomCname
  type: string
- container: ''
  name: ResourceOwner
  type: string
- container: ''
  name: TypeId
  type: string
- container: ''
  name: AuditReportResponseFormat
  type: string
- container: ''
  name: Arn
  type: string
- container: ''
  name: OwnerAccount
  type: string
- container: ''
  name: LastStateChangeAt
  type: string
- container: ''
  name: Serial
  type: string
- container: ''
  name: NotBefore
  type: string
- container: ''
  name: NotAfter
  type: string
- container: ''
  name: FailureReason
  type: string
- container: ''
  name: RestorableUntil
  type: string
- container: ''
  name: CertificateAuthorities
  type: string
- container: ''
  name: Permissions
  type: string
- container: ''
  name: CustomObjectIdentifier
  type: string
- container: ''
  name: AccessMethodType
  type: string
property_count: 99
provider_name: Amazon Private CA
provider_slug: amazon-private-ca
slug: amazon-private-ca-context
tags:
- AWS
- Certificate Authority
- Certificates
- PKI
- Security
- X.509
- TLS
- IoT
- JSON-LD
- Linked Data
- Semantic Web
---
