---
api_count: 30
apis:
- description: Adyen sends notifications through webhooks to inform your system about incoming and outgoing transfers in your platform. You can use these webhooks to build your implementation. For example, you can u
  name: Adyen Accounting Notifications API
  slug: adyen-accounting-notifications-api
- description: 'This API is used for the classic integration. The Account API provides endpoints for managing account-related entities on your platform. These related entities include account holders, accounts, bank '
  name: Adyen Account API
  slug: adyen-account-api
- description: Adyen sends webhooks to inform your system about events related to cardholder authentication.
  name: Adyen Authentication Webhooks API
  slug: adyen-authentication-webhooks-api
- description: The Balance Control API lets you transfer funds between merchant accounts that belong to the same legal entity and are under the same company account.
  name: Adyen Balance Control API
  slug: adyen-balance-control-api
- description: The BIN Lookup API provides endpoints for retrieving information, such as cost estimates, and 3D Secure supported version based on a given BIN.
  name: Adyen BinLookup API
  slug: adyen-binlookup-api
- description: The Checkout API provides a powerful, PCI-compliant way to accept payments online. It supports a broad range of payment methods, including cards, wallets, and local payment methods, with built-in 3D S
  name: Adyen Checkout API
  slug: adyen-checkout-api
- description: The Configuration API enables you to create a platform where you can onboard your users as account holders and create balance accounts, cards, and business accounts.
  name: Adyen Configuration API
  slug: adyen-configuration-api
- description: 'Adyen sends webhooks to inform your system about events that occur in your platform. These events include, for example, when an account holders capabilities are updated, or when a sweep configuration '
  name: Adyen Configuration Webhooks API
  slug: adyen-configuration-webhooks-api
- description: 'Adyen Data Protection API provides a way for you to process Subject Erasure Requests as mandated in GDPR. Use our API to submit a request to delete shopper''s data, including payment details and other '
  name: Adyen Data Protection API
  slug: adyen-data-protection-api
- description: You can use the Disputes API to automate the dispute handling process so that you can respond to disputes and chargebacks as soon as they are initiated. The Disputes API lets you retrieve defense reas
  name: Adyen Disputes API
  slug: adyen-disputes-api
- description: The Fund API provides endpoints for managing the funds in the accounts on your platform. These management operations include, for example, the transfer of funds from one account to another, the payout
  name: Adyen Funds API
  slug: adyen-funds-api
- description: The Hosted Onboarding API provides endpoints for managing the hosted onboarding experience for account holders, allowing you to collect verification details through Adyen's hosted pages.
  name: Adyen Hosted Onboarding API
  slug: adyen-hosted-onboarding-api
- description: The Legal Entity Management API enables you to manage legal entities that contain information required for verification.
  name: Adyen Legal Entity API
  slug: adyen-legal-entity-api
- description: Configure and manage your Adyen company and merchant accounts, stores, and payment terminals.
  name: Adyen Management API
  slug: adyen-management-api
- description: Adyen uses webhooks to inform your system about events that happen with your Adyen company and merchant accounts, stores, payment terminals, and payment methods when using Management API.
  name: Adyen Management Webhooks API
  slug: adyen-management-webhooks-api
- description: The Notification Configuration API is used for the classic integration to configure notification subscriptions, endpoints, and settings.
  name: Adyen Notification Configuration API
  slug: adyen-notification-configuration-api
- description: Adyen sends notifications through webhooks to inform your system about events that occur in the balance platform. These events include, for example, a card user making a payment, or a merchant startin
  name: Adyen Notification Webhooks API
  slug: adyen-notification-webhooks-api
- description: The Notification API sends notifications to the endpoints specified in a given subscription. Subscriptions are managed through the Notification Configuration API.
  name: Adyen Notifications API
  slug: adyen-notifications-api
- description: A set of API endpoints that allow you to initiate, settle, and modify payments on the Adyen payments platform. You can use the API to accept card payments (including One-Click and 3D Secure), bank tra
  name: Adyen Payments API
  slug: adyen-payments-api
- description: A set of API endpoints that allow you to store payout details, confirm, or decline a payout. For more information, refer to Online payouts.
  name: Adyen Payouts API
  slug: adyen-payouts-api
- description: This API provides endpoints for managing your point-of-sale (POS) payment terminals. You can use the API to obtain information about a specific terminal, retrieve overviews of your terminals and store
  name: Adyen POS Terminal API
  slug: adyen-pos-terminal-api
- description: The Recurring APIs allow you to manage and remove your tokens or saved payment details. Tokens should be created with validation during a payment request.
  name: Adyen Recurring API
  slug: adyen-recurring-api
- description: Adyen sends webhooks to inform your system that reports were generated and are ready to be downloaded. You can download reports programmatically by making an HTTP GET request.
  name: Adyen Report Webhooks API
  slug: adyen-report-webhooks-api
- description: A set of API endpoints to manage stored value products.
  name: Adyen Stored Value API
  slug: adyen-stored-value-api
- description: The Adyen Terminal API lets you make payments, issue refunds, collect shopper information, and perform other shopper-terminal interactions using a payment terminal supplied by Adyen.
  name: Adyen Terminal API
  slug: adyen-terminal-api
- description: The Test Cards API provides endpoints for generating custom test card numbers. For more information, refer to Custom test cards documentation.
  name: Adyen Test Cards API
  slug: adyen-test-cards-api
- description: Adyen sends webhooks to inform your system about incoming and outgoing transfers in your platform. You can use these webhooks to build your implementation. For example, you can use this information to
  name: Adyen Transaction Webhooks API
  slug: adyen-transaction-webhooks-api
- description: Adyen sends webhooks to inform your system about incoming and outgoing transfers in your platform. You can use these webhooks to build your implementation. For example, you can use this information to
  name: Adyen Transfer Webhooks API
  slug: adyen-transfer-webhooks-api
- description: 'This API provides endpoints that you can use to transfer funds, whether when paying out to a transfer instrument, sending funds to third parties for users with business bank accounts, or to request a '
  name: Adyen Transfers API
  slug: adyen-transfers-api
- description: We use webhooks to send you updates about payment status updates, newly available reports, and other events that you can subscribe to.
  name: Adyen Webhooks API
  slug: adyen-webhooks-api
capabilities:
- description: 'Unified capability for building financial products on Adyen''s balance platform. Combines the Configuration API for account holder and card management with the Transfers API for fund movement. Used by '
  name: Adyen Balance Platform
  slug: balance-platform
- description: Unified capability for managing Adyen merchant accounts, stores, payment terminals, and dispute resolution. Combines Management API and Disputes API to give operations teams and platform administrator
  name: Adyen Merchant Account Management
  slug: merchant-account-management
- description: Unified capability for accepting and managing online payments. Combines the Checkout API and Payments API to provide merchants and developers with a complete payment acceptance workflow including sess
  name: Adyen Online Payment Processing
  slug: online-payment-processing
common:
- title: ''
  type: TermsOfService
  url: https://www.adyen.com/legal/terms-and-conditions
- title: ''
  type: PrivacyPolicy
  url: https://www.adyen.com/policies-and-disclaimer/privacy-policy
- title: ''
  type: Authentication
  url: https://docs.adyen.com/development-resources/api-credentials
- title: ''
  type: Pricing
  url: https://www.adyen.com/pricing
- title: ''
  type: Documentation
  url: https://docs.adyen.com/
- title: ''
  type: GettingStarted
  url: https://docs.adyen.com/get-started-with-adyen/
- title: ''
  type: Blog
  url: https://www.adyen.com/knowledge-hub
- title: ''
  type: Login
  url: https://authn-live.adyen.com/authn/ui/login
- title: ''
  type: Sandbox
  url: https://ca-test.adyen.com
- title: ''
  type: Support
  url: https://help.adyen.com/en_US
- title: ''
  type: Contact
  url: https://help.adyen.com/en_US/contact
- title: ''
  type: Webinars
  url: https://help.adyen.com/en_US/academy/webinars
- title: ''
  type: StatusPage
  url: https://status.adyen.com
- title: ''
  type: ReleaseNotes
  url: https://docs.adyen.com/development-resources/release-notes
- title: ''
  type: GitHubOrganization
  url: https://github.com/Adyen
- title: ''
  type: GitHubRepository
  url: https://github.com/Adyen/adyen-openapi
- title: ''
  type: Newsletter
  url: https://www.adyen.com/newsletter
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/adyen
- title: Web SDK
  type: SDK
  url: https://github.com/Adyen/adyen-web
- title: iOS SDK
  type: SDK
  url: https://github.com/Adyen/adyen-ios
- title: Android SDK
  type: SDK
  url: https://github.com/Adyen/adyen-android
- title: React Native SDK
  type: SDK
  url: https://github.com/Adyen/adyen-react-native
- title: Flutter SDK
  type: SDK
  url: https://github.com/Adyen/adyen-flutter
- title: PHP SDK
  type: SDK
  url: https://github.com/Adyen/adyen-php-api-library
- title: Java SDK
  type: SDK
  url: https://github.com/Adyen/adyen-java-api-library
- title: Node.js SDK
  type: SDK
  url: https://github.com/Adyen/adyen-node-api-library
- title: .NET SDK
  type: SDK
  url: https://github.com/Adyen/adyen-dotnet-api-library
- title: Go SDK
  type: SDK
  url: https://github.com/Adyen/adyen-go-api-library
- title: Python SDK
  type: SDK
  url: https://github.com/Adyen/adyen-python-api-library
- title: Ruby SDK
  type: SDK
  url: https://github.com/Adyen/adyen-ruby-api-library
- title: Apex SDK
  type: SDK
  url: https://github.com/Adyen/adyen-apex-api-library
- title: MCP Server
  type: Tools
  url: https://github.com/Adyen/adyen-mcp
- title: Postman Collection
  type: Tools
  url: https://github.com/Adyen/adyen-postman
- title: ''
  type: SpectralRules
  url: rules/adyen-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/adyen-vocabulary.yaml
- title: Online Payment Processing
  type: NaftikoCapability
  url: capabilities/online-payment-processing.yaml
- title: Merchant Account Management
  type: NaftikoCapability
  url: capabilities/merchant-account-management.yaml
- title: Balance Platform
  type: NaftikoCapability
  url: capabilities/balance-platform.yaml
created: '2023-11-13'
description: Adyen is a global payment company that provides businesses with a single platform to accept payments from customers worldwide. Their technology enables companies to accept a wide range of payment methods, including credit cards, digital wallets, and local payment methods, in multiple currencies and countries. Adyen also offers services such as fraud prevention, data analytics, and optimization tools to help businesses streamline their payment processes and improve their overall performance.
features:
- description: Accept 150+ payment methods including cards, digital wallets, bank transfers, and local payment methods in 200+ countries and territories.
  name: Global Payment Methods
- description: Built-in 3D Secure 2 authentication for card payments, supporting native, redirect, and frictionless flows for improved conversion.
  name: 3D Secure 2
- description: RevenueProtect, a machine learning-based risk management system that screens transactions for fraud in real time.
  name: Fraud Prevention
- description: Secure storage of payment details as tokens for recurring payments, subscriptions, and one-click checkout experiences.
  name: Tokenization
- description: Real-time event-driven notifications delivered via webhooks for payment status updates, reports, and platform events.
  name: Webhooks and Notifications
- description: Comprehensive reporting tools including settlement reports, payment accounting, and data analytics for business insights.
  name: Reporting and Analytics
- description: Full support for marketplace and platform business models with split payments, sub-merchant onboarding, and automated payouts.
  name: Marketplace and Platform Support
- description: Physical and virtual card issuance capabilities with network token support and 3D Secure enrollment for issued cards.
  name: Issuing
- description: Business financing through dynamic grants for eligible merchants based on processing history.
  name: Capital
- description: AI-powered Model Context Protocol server for natural language integration with Adyen APIs.
  name: MCP Server
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Pre-built plugin for Adobe Commerce and Magento e-commerce platforms with full payment method support.
  name: Adobe Commerce (Magento)
- description: Integration with Salesforce Commerce Cloud for seamless payment processing in SFCC storefronts.
  name: Salesforce Commerce Cloud
- description: Native plugin for Shopware e-commerce platform supporting all Adyen payment methods.
  name: Shopware
- description: Integration with SAP Commerce Cloud for enterprise e-commerce payment processing.
  name: SAP Commerce Cloud
- description: Partner integration with Shopify for accepting Adyen payments through Shopify stores.
  name: Shopify
- description: Integration with Oracle NetSuite ERP for payment processing and reconciliation.
  name: NetSuite
- description: Plugin for PrestaShop e-commerce platform enabling Adyen payment acceptance.
  name: PrestaShop
- description: Integration with CommerceTools headless commerce platform for flexible payment experiences.
  name: CommerceTools
jsonld:
- class_count: 40
  name: Adyen Accounting Notifications Context
  property_count: 91
  slug: adyen-accounting-notifications-context
- class_count: 2
  name: Adyen Accounts Account Context
  property_count: 9
  slug: adyen-accounts-account-context
- class_count: 1
  name: Adyen Accounts Account Event Context
  property_count: 3
  slug: adyen-accounts-account-event-context
- class_count: 3
  name: Adyen Accounts Account Holder Context
  property_count: 19
  slug: adyen-accounts-account-holder-context
- class_count: 1
  name: Adyen Accounts Account Payout Context
  property_count: 6
  slug: adyen-accounts-account-payout-context
- class_count: 1
  name: Adyen Accounts Account Processing Context
  property_count: 5
  slug: adyen-accounts-account-processing-context
- class_count: 1
  name: Adyen Accounts Amount Context
  property_count: 2
  slug: adyen-accounts-amount-context
- class_count: 1
  name: Adyen Accounts Bank Account Context
  property_count: 26
  slug: adyen-accounts-bank-account-context
- class_count: 1
  name: Adyen Accounts Business Details Context
  property_count: 10
  slug: adyen-accounts-business-details-context
- class_count: 4
  name: Adyen Accounts Close Account Context
  property_count: 7
  slug: adyen-accounts-close-account-context
- class_count: 1
  name: Adyen Accounts Close Stores Context
  property_count: 2
  slug: adyen-accounts-close-stores-context
- class_count: 5
  name: Adyen Accounts Create Account Context
  property_count: 20
  slug: adyen-accounts-create-account-context
- class_count: 1
  name: Adyen Accounts Delete Bank Context
  property_count: 2
  slug: adyen-accounts-delete-bank-context
- class_count: 1
  name: Adyen Accounts Delete Legal Context
  property_count: 2
  slug: adyen-accounts-delete-legal-context
- class_count: 1
  name: Adyen Accounts Delete Payout Context
  property_count: 2
  slug: adyen-accounts-delete-payout-context
- class_count: 1
  name: Adyen Accounts Delete Shareholder Context
  property_count: 2
  slug: adyen-accounts-delete-shareholder-context
- class_count: 1
  name: Adyen Accounts Delete Signatories Context
  property_count: 2
  slug: adyen-accounts-delete-signatories-context
- class_count: 2
  name: Adyen Accounts Document Detail Context
  property_count: 8
  slug: adyen-accounts-document-detail-context
- class_count: 1
  name: Adyen Accounts Error Field Context
  property_count: 3
  slug: adyen-accounts-error-field-context
- class_count: 1
  name: Adyen Accounts Field Type Context
  property_count: 3
  slug: adyen-accounts-field-type-context
- class_count: 1
  name: Adyen Accounts Generic Response Context
  property_count: 3
  slug: adyen-accounts-generic-response-context
- class_count: 4
  name: Adyen Accounts Get Account Context
  property_count: 15
  slug: adyen-accounts-get-account-context
- class_count: 2
  name: Adyen Accounts Get Tax Context
  property_count: 8
  slug: adyen-accounts-get-tax-context
- class_count: 2
  name: Adyen Accounts Get Uploaded Context
  property_count: 7
  slug: adyen-accounts-get-uploaded-context
- class_count: 2
  name: Adyen Accounts Individual Details Context
  property_count: 1
  slug: adyen-accounts-individual-details-context
- class_count: 3
  name: Adyen Accounts Kyc Check Context
  property_count: 7
  slug: adyen-accounts-kyc-check-context
- class_count: 2
  name: Adyen Accounts Kyc Legal Context
  property_count: 3
  slug: adyen-accounts-kyc-legal-context
- class_count: 1
  name: Adyen Accounts Kyc Payout Context
  property_count: 2
  slug: adyen-accounts-kyc-payout-context
- class_count: 1
  name: Adyen Accounts Kyc Shareholder Context
  property_count: 4
  slug: adyen-accounts-kyc-shareholder-context
- class_count: 1
  name: Adyen Accounts Kyc Signatory Context
  property_count: 2
  slug: adyen-accounts-kyc-signatory-context
- class_count: 1
  name: Adyen Accounts Kyc Ultimate Context
  property_count: 2
  slug: adyen-accounts-kyc-ultimate-context
- class_count: 1
  name: Adyen Accounts Kyc Verification Context
  property_count: 7
  slug: adyen-accounts-kyc-verification-context
- class_count: 5
  name: Adyen Accounts Legal Arrangement Context
  property_count: 18
  slug: adyen-accounts-legal-arrangement-context
- class_count: 1
  name: Adyen Accounts Migrated Accounts Context
  property_count: 2
  slug: adyen-accounts-migrated-accounts-context
- class_count: 1
  name: Adyen Accounts Migrated Shareholders Context
  property_count: 2
  slug: adyen-accounts-migrated-shareholders-context
- class_count: 1
  name: Adyen Accounts Migrated Stores Context
  property_count: 4
  slug: adyen-accounts-migrated-stores-context
- class_count: 1
  name: Adyen Accounts Migration Data Context
  property_count: 7
  slug: adyen-accounts-migration-data-context
- class_count: 1
  name: Adyen Accounts Payout Method Context
  property_count: 5
  slug: adyen-accounts-payout-method-context
- class_count: 1
  name: Adyen Accounts Payout Schedule Context
  property_count: 2
  slug: adyen-accounts-payout-schedule-context
- class_count: 1
  name: Adyen Accounts Perform Verification Context
  property_count: 3
  slug: adyen-accounts-perform-verification-context
- class_count: 1
  name: Adyen Accounts Personal Document Context
  property_count: 5
  slug: adyen-accounts-personal-document-context
- class_count: 3
  name: Adyen Accounts Shareholder Contact Context
  property_count: 9
  slug: adyen-accounts-shareholder-contact-context
- class_count: 3
  name: Adyen Accounts Signatory Contact Context
  property_count: 8
  slug: adyen-accounts-signatory-contact-context
- class_count: 1
  name: Adyen Accounts Store Detail Context
  property_count: 15
  slug: adyen-accounts-store-detail-context
- class_count: 2
  name: Adyen Accounts Suspend Account Context
  property_count: 5
  slug: adyen-accounts-suspend-account-context
- class_count: 2
  name: Adyen Accounts Ultimate Parent Context
  property_count: 8
  slug: adyen-accounts-ultimate-parent-context
- class_count: 2
  name: Adyen Accounts Un Suspend Context
  property_count: 5
  slug: adyen-accounts-un-suspend-context
- class_count: 6
  name: Adyen Accounts Update Account Context
  property_count: 20
  slug: adyen-accounts-update-account-context
- class_count: 1
  name: Adyen Accounts Update Payout Context
  property_count: 3
  slug: adyen-accounts-update-payout-context
- class_count: 1
  name: Adyen Accounts Upload Document Context
  property_count: 2
  slug: adyen-accounts-upload-document-context
- class_count: 1
  name: Adyen Accounts Vias Address Context
  property_count: 6
  slug: adyen-accounts-vias-address-context
- class_count: 1
  name: Adyen Accounts Vias Name Context
  property_count: 4
  slug: adyen-accounts-vias-name-context
- class_count: 1
  name: Adyen Accounts Vias Personal Context
  property_count: 3
  slug: adyen-accounts-vias-personal-context
- class_count: 1
  name: Adyen Accounts Vias Phone Context
  property_count: 3
  slug: adyen-accounts-vias-phone-context
- class_count: 8
  name: Adyen Authentication Webhooks Context
  property_count: 36
  slug: adyen-authentication-webhooks-context
- class_count: 1
  name: Adyen Balance Control Amount Context
  property_count: 2
  slug: adyen-balance-control-amount-context
- class_count: 3
  name: Adyen Balance Control Balance Context
  property_count: 8
  slug: adyen-balance-control-balance-context
- class_count: 1
  name: Adyen Binlookup Amount Context
  property_count: 2
  slug: adyen-binlookup-amount-context
- class_count: 1
  name: Adyen Binlookup Bin Detail Context
  property_count: 1
  slug: adyen-binlookup-bin-detail-context
- class_count: 1
  name: Adyen Binlookup Card Bin Context
  property_count: 11
  slug: adyen-binlookup-card-bin-context
- class_count: 3
  name: Adyen Binlookup Cost Estimate Context
  property_count: 18
  slug: adyen-binlookup-cost-estimate-context
- class_count: 1
  name: Adyen Binlookup Ds Public Context
  property_count: 5
  slug: adyen-binlookup-ds-public-context
- class_count: 1
  name: Adyen Binlookup Merchant Details Context
  property_count: 3
  slug: adyen-binlookup-merchant-details-context
- class_count: 1
  name: Adyen Binlookup Recurring Context
  property_count: 5
  slug: adyen-binlookup-recurring-context
- class_count: 2
  name: Adyen Binlookup Three Ds Context
  property_count: 11
  slug: adyen-binlookup-three-ds-context
- class_count: 1
  name: Adyen Binlookup Three Ds2 Context
  property_count: 6
  slug: adyen-binlookup-three-ds2-context
- class_count: 1
  name: Adyen Checkout Account Info Context
  property_count: 19
  slug: adyen-checkout-account-info-context
- class_count: 1
  name: Adyen Checkout Acct Info Context
  property_count: 16
  slug: adyen-checkout-acct-info-context
- class_count: 1
  name: Adyen Checkout Ach Details Context
  property_count: 10
  slug: adyen-checkout-ach-details-context
- class_count: 14
  name: Adyen Checkout Additional Data Context
  property_count: 187
  slug: adyen-checkout-additional-data-context
- class_count: 1
  name: Adyen Checkout Additional Data3 Context
  property_count: 6
  slug: adyen-checkout-additional-data3-context
- class_count: 1
  name: Adyen Checkout Address Context
  property_count: 6
  slug: adyen-checkout-address-context
- class_count: 1
  name: Adyen Checkout Afterpay Details Context
  property_count: 7
  slug: adyen-checkout-afterpay-details-context
- class_count: 1
  name: Adyen Checkout Amazon Pay Context
  property_count: 4
  slug: adyen-checkout-amazon-pay-context
- class_count: 1
  name: Adyen Checkout Amount Context
  property_count: 2
  slug: adyen-checkout-amount-context
- class_count: 1
  name: Adyen Checkout Android Pay Context
  property_count: 2
  slug: adyen-checkout-android-pay-context
- class_count: 4
  name: Adyen Checkout Apple Pay Context
  property_count: 10
  slug: adyen-checkout-apple-pay-context
- class_count: 1
  name: Adyen Checkout Application Info Context
  property_count: 6
  slug: adyen-checkout-application-info-context
- class_count: 1
  name: Adyen Checkout Authentication Data Context
  property_count: 3
  slug: adyen-checkout-authentication-data-context
- class_count: 1
  name: Adyen Checkout Avs Context
  property_count: 2
  slug: adyen-checkout-avs-context
- class_count: 1
  name: Adyen Checkout Bacs Direct Context
  property_count: 7
  slug: adyen-checkout-bacs-direct-context
- class_count: 2
  name: Adyen Checkout Balance Check Context
  property_count: 50
  slug: adyen-checkout-balance-check-context
- class_count: 1
  name: Adyen Checkout Bank Account Context
  property_count: 9
  slug: adyen-checkout-bank-account-context
- class_count: 1
  name: Adyen Checkout Bill Desk Context
  property_count: 3
  slug: adyen-checkout-bill-desk-context
- class_count: 1
  name: Adyen Checkout Billing Address Context
  property_count: 6
  slug: adyen-checkout-billing-address-context
- class_count: 1
  name: Adyen Checkout Blik Details Context
  property_count: 5
  slug: adyen-checkout-blik-details-context
- class_count: 1
  name: Adyen Checkout Browser Info Context
  property_count: 9
  slug: adyen-checkout-browser-info-context
- class_count: 2
  name: Adyen Checkout Cancel Order Context
  property_count: 4
  slug: adyen-checkout-cancel-order-context
- class_count: 1
  name: Adyen Checkout Card Brand Context
  property_count: 2
  slug: adyen-checkout-card-brand-context
- class_count: 1
  name: Adyen Checkout Card Context
  property_count: 8
  slug: adyen-checkout-card-context
- class_count: 3
  name: Adyen Checkout Card Details Context
  property_count: 24
  slug: adyen-checkout-card-details-context
- class_count: 1
  name: Adyen Checkout Card Donations Context
  property_count: 19
  slug: adyen-checkout-card-donations-context
- class_count: 1
  name: Adyen Checkout Cellulant Details Context
  property_count: 3
  slug: adyen-checkout-cellulant-details-context
- class_count: 2
  name: Adyen Checkout Checkout Await Context
  property_count: 3
  slug: adyen-checkout-checkout-await-context
- class_count: 2
  name: Adyen Checkout Checkout Delegated Context
  property_count: 5
  slug: adyen-checkout-checkout-delegated-context
- class_count: 2
  name: Adyen Checkout Checkout Native Context
  property_count: 5
  slug: adyen-checkout-checkout-native-context
- class_count: 1
  name: Adyen Checkout Checkout Order Context
  property_count: 6
  slug: adyen-checkout-checkout-order-context
- class_count: 2
  name: Adyen Checkout Checkout Qr Context
  property_count: 5
  slug: adyen-checkout-checkout-qr-context
- class_count: 2
  name: Adyen Checkout Checkout Redirect Context
  property_count: 4
  slug: adyen-checkout-checkout-redirect-context
- class_count: 2
  name: Adyen Checkout Checkout Sdk Context
  property_count: 4
  slug: adyen-checkout-checkout-sdk-context
- class_count: 1
  name: Adyen Checkout Checkout Session Context
  property_count: 3
  slug: adyen-checkout-checkout-session-context
- class_count: 2
  name: Adyen Checkout Checkout Three Context
  property_count: 6
  slug: adyen-checkout-checkout-three-context
- class_count: 2
  name: Adyen Checkout Checkout Voucher Context
  property_count: 20
  slug: adyen-checkout-checkout-voucher-context
- class_count: 3
  name: Adyen Checkout Common Field Context
  property_count: 0
  slug: adyen-checkout-common-field-context
- class_count: 2
  name: Adyen Checkout Company Context
  property_count: 5
  slug: adyen-checkout-company-context
- class_count: 1
  name: Adyen Checkout Configuration Context
  property_count: 4
  slug: adyen-checkout-configuration-context
- class_count: 3
  name: Adyen Checkout Create Checkout Context
  property_count: 61
  slug: adyen-checkout-create-checkout-context
- class_count: 2
  name: Adyen Checkout Create Order Context
  property_count: 11
  slug: adyen-checkout-create-order-context
- class_count: 1
  name: Adyen Checkout Delivery Address Context
  property_count: 8
  slug: adyen-checkout-delivery-address-context
- class_count: 1
  name: Adyen Checkout Details Request Context
  property_count: 1
  slug: adyen-checkout-details-request-context
- class_count: 1
  name: Adyen Checkout Device Render Context
  property_count: 2
  slug: adyen-checkout-device-render-context
- class_count: 1
  name: Adyen Checkout Doku Details Context
  property_count: 5
  slug: adyen-checkout-doku-details-context
- class_count: 2
  name: Adyen Checkout Donation Payment Context
  property_count: 44
  slug: adyen-checkout-donation-payment-context
- class_count: 1
  name: Adyen Checkout Dotpay Details Context
  property_count: 3
  slug: adyen-checkout-dotpay-details-context
- class_count: 1
  name: Adyen Checkout Dragonpay Details Context
  property_count: 4
  slug: adyen-checkout-dragonpay-details-context
- class_count: 1
  name: Adyen Checkout Econtext Voucher Context
  property_count: 6
  slug: adyen-checkout-econtext-voucher-context
- class_count: 1
  name: Adyen Checkout Encrypted Order Context
  property_count: 2
  slug: adyen-checkout-encrypted-order-context
- class_count: 3
  name: Adyen Checkout External Platform Context
  property_count: 1
  slug: adyen-checkout-external-platform-context
- class_count: 1
  name: Adyen Checkout Forex Quote Context
  property_count: 12
  slug: adyen-checkout-forex-quote-context
- class_count: 2
  name: Adyen Checkout Fraud Check Context
  property_count: 2
  slug: adyen-checkout-fraud-check-context
- class_count: 1
  name: Adyen Checkout Fraud Result Context
  property_count: 2
  slug: adyen-checkout-fraud-result-context
- class_count: 1
  name: Adyen Checkout Fund Origin Context
  property_count: 5
  slug: adyen-checkout-fund-origin-context
- class_count: 1
  name: Adyen Checkout Fund Recipient Context
  property_count: 10
  slug: adyen-checkout-fund-recipient-context
- class_count: 1
  name: Adyen Checkout Generic Issuer Context
  property_count: 5
  slug: adyen-checkout-generic-issuer-context
- class_count: 1
  name: Adyen Checkout Giropay Details Context
  property_count: 4
  slug: adyen-checkout-giropay-details-context
- class_count: 2
  name: Adyen Checkout Google Pay Context
  property_count: 7
  slug: adyen-checkout-google-pay-context
- class_count: 1
  name: Adyen Checkout Ideal Details Context
  property_count: 5
  slug: adyen-checkout-ideal-details-context
- class_count: 1
  name: Adyen Checkout Ideal Donations Context
  property_count: 5
  slug: adyen-checkout-ideal-donations-context
- class_count: 1
  name: Adyen Checkout Input Detail Context
  property_count: 9
  slug: adyen-checkout-input-detail-context
- class_count: 1
  name: Adyen Checkout Installment Option Context
  property_count: 4
  slug: adyen-checkout-installment-option-context
- class_count: 1
  name: Adyen Checkout Installments Context
  property_count: 2
  slug: adyen-checkout-installments-context
- class_count: 1
  name: Adyen Checkout Installments Number Context
  property_count: 1
  slug: adyen-checkout-installments-number-context
- class_count: 2
  name: Adyen Checkout Item Context
  property_count: 1
  slug: adyen-checkout-item-context
- class_count: 1
  name: Adyen Checkout Klarna Details Context
  property_count: 8
  slug: adyen-checkout-klarna-details-context
- class_count: 2
  name: Adyen Checkout Line Item Context
  property_count: 16
  slug: adyen-checkout-line-item-context
- class_count: 1
  name: Adyen Checkout List Stored Context
  property_count: 3
  slug: adyen-checkout-list-stored-context
- class_count: 1
  name: Adyen Checkout Mandate Context
  property_count: 8
  slug: adyen-checkout-mandate-context
- class_count: 1
  name: Adyen Checkout Masterpass Details Context
  property_count: 4
  slug: adyen-checkout-masterpass-details-context
- class_count: 1
  name: Adyen Checkout Mbway Details Context
  property_count: 4
  slug: adyen-checkout-mbway-details-context
- class_count: 1
  name: Adyen Checkout Merchant Device Context
  property_count: 3
  slug: adyen-checkout-merchant-device-context
- class_count: 1
  name: Adyen Checkout Merchant Risk Context
  property_count: 14
  slug: adyen-checkout-merchant-risk-context
- class_count: 1
  name: Adyen Checkout Mobile Pay Context
  property_count: 2
  slug: adyen-checkout-mobile-pay-context
- class_count: 1
  name: Adyen Checkout Mol Pay Context
  property_count: 3
  slug: adyen-checkout-mol-pay-context
- class_count: 1
  name: Adyen Checkout Name Context
  property_count: 2
  slug: adyen-checkout-name-context
- class_count: 1
  name: Adyen Checkout Open Invoice Context
  property_count: 7
  slug: adyen-checkout-open-invoice-context
- class_count: 1
  name: Adyen Checkout Pay Pal Context
  property_count: 9
  slug: adyen-checkout-pay-pal-context
- class_count: 1
  name: Adyen Checkout Pay U Context
  property_count: 6
  slug: adyen-checkout-pay-u-context
- class_count: 2
  name: Adyen Checkout Pay With Context
  property_count: 6
  slug: adyen-checkout-pay-with-context
- class_count: 2
  name: Adyen Checkout Payment Amount Context
  property_count: 10
  slug: adyen-checkout-payment-amount-context
- class_count: 2
  name: Adyen Checkout Payment Cancel Context
  property_count: 6
  slug: adyen-checkout-payment-cancel-context
- class_count: 2
  name: Adyen Checkout Payment Capture Context
  property_count: 11
  slug: adyen-checkout-payment-capture-context
- class_count: 1
  name: Adyen Checkout Payment Completion Context
  property_count: 18
  slug: adyen-checkout-payment-completion-context
- class_count: 3
  name: Adyen Checkout Payment Details Context
  property_count: 21
  slug: adyen-checkout-payment-details-context
- class_count: 4
  name: Adyen Checkout Payment Link Context
  property_count: 40
  slug: adyen-checkout-payment-link-context
- class_count: 4
  name: Adyen Checkout Payment Method Context
  property_count: 11
  slug: adyen-checkout-payment-method-context
- class_count: 2
  name: Adyen Checkout Payment Methods Context
  property_count: 14
  slug: adyen-checkout-payment-methods-context
- class_count: 2
  name: Adyen Checkout Payment Refund Context
  property_count: 11
  slug: adyen-checkout-payment-refund-context
- class_count: 1
  name: Adyen Checkout Payment Request Context
  property_count: 67
  slug: adyen-checkout-payment-request-context
- class_count: 1
  name: Adyen Checkout Payment Response Context
  property_count: 15
  slug: adyen-checkout-payment-response-context
- class_count: 2
  name: Adyen Checkout Payment Reversal Context
  property_count: 6
  slug: adyen-checkout-payment-reversal-context
- class_count: 2
  name: Adyen Checkout Payment Setup Context
  property_count: 58
  slug: adyen-checkout-payment-setup-context
- class_count: 2
  name: Adyen Checkout Payment Verification Context
  property_count: 11
  slug: adyen-checkout-payment-verification-context
- class_count: 1
  name: Adyen Checkout Phone Context
  property_count: 2
  slug: adyen-checkout-phone-context
- class_count: 1
  name: Adyen Checkout Platform Chargeback Context
  property_count: 3
  slug: adyen-checkout-platform-chargeback-context
- class_count: 1
  name: Adyen Checkout Ratepay Details Context
  property_count: 7
  slug: adyen-checkout-ratepay-details-context
- class_count: 1
  name: Adyen Checkout Recurring Context
  property_count: 5
  slug: adyen-checkout-recurring-context
- class_count: 2
  name: Adyen Checkout Recurring Detail Context
  property_count: 10
  slug: adyen-checkout-recurring-detail-context
- class_count: 9
  name: Adyen Checkout Response Additional Context
  property_count: 99
  slug: adyen-checkout-response-additional-context
- class_count: 1
  name: Adyen Checkout Response Payment Context
  property_count: 2
  slug: adyen-checkout-response-payment-context
- class_count: 1
  name: Adyen Checkout Risk Data Context
  property_count: 4
  slug: adyen-checkout-risk-data-context
- class_count: 1
  name: Adyen Checkout Samsung Pay Context
  property_count: 6
  slug: adyen-checkout-samsung-pay-context
- class_count: 1
  name: Adyen Checkout Sdk Ephem Context
  property_count: 4
  slug: adyen-checkout-sdk-ephem-context
- class_count: 1
  name: Adyen Checkout Sepa Direct Context
  property_count: 6
  slug: adyen-checkout-sepa-direct-context
- class_count: 1
  name: Adyen Checkout Service Context
  property_count: 4
  slug: adyen-checkout-service-context
- class_count: 1
  name: Adyen Checkout Session Result Context
  property_count: 2
  slug: adyen-checkout-session-result-context
- class_count: 1
  name: Adyen Checkout Shopper Input Context
  property_count: 3
  slug: adyen-checkout-shopper-input-context
- class_count: 1
  name: Adyen Checkout Shopper Interaction Context
  property_count: 3
  slug: adyen-checkout-shopper-interaction-context
- class_count: 1
  name: Adyen Checkout Split Amount Context
  property_count: 2
  slug: adyen-checkout-split-amount-context
- class_count: 2
  name: Adyen Checkout Split Context
  property_count: 4
  slug: adyen-checkout-split-context
- class_count: 2
  name: Adyen Checkout Standalone Payment Context
  property_count: 6
  slug: adyen-checkout-standalone-payment-context
- class_count: 1
  name: Adyen Checkout Stored Details Context
  property_count: 3
  slug: adyen-checkout-stored-details-context
- class_count: 4
  name: Adyen Checkout Stored Payment Context
  property_count: 23
  slug: adyen-checkout-stored-payment-context
- class_count: 1
  name: Adyen Checkout Sub Input Context
  property_count: 6
  slug: adyen-checkout-sub-input-context
- class_count: 3
  name: Adyen Checkout Sub Merchant Context
  property_count: 6
  slug: adyen-checkout-sub-merchant-context
- class_count: 1
  name: Adyen Checkout Three D Context
  property_count: 12
  slug: adyen-checkout-three-d-context
- class_count: 3
  name: Adyen Checkout Three Ds Context
  property_count: 11
  slug: adyen-checkout-three-ds-context
- class_count: 4
  name: Adyen Checkout Three Ds2 Context
  property_count: 60
  slug: adyen-checkout-three-ds2-context
- class_count: 1
  name: Adyen Checkout Update Payment Context
  property_count: 1
  slug: adyen-checkout-update-payment-context
- class_count: 1
  name: Adyen Checkout Upi Collect Context
  property_count: 7
  slug: adyen-checkout-upi-collect-context
- class_count: 1
  name: Adyen Checkout Upi Intent Context
  property_count: 5
  slug: adyen-checkout-upi-intent-context
- class_count: 1
  name: Adyen Checkout Utility Request Context
  property_count: 1
  slug: adyen-checkout-utility-request-context
- class_count: 1
  name: Adyen Checkout Utility Response Context
  property_count: 1
  slug: adyen-checkout-utility-response-context
- class_count: 1
  name: Adyen Checkout Vipps Details Context
  property_count: 5
  slug: adyen-checkout-vipps-details-context
- class_count: 1
  name: Adyen Checkout Visa Checkout Context
  property_count: 4
  slug: adyen-checkout-visa-checkout-context
- class_count: 2
  name: Adyen Checkout We Chat Context
  property_count: 4
  slug: adyen-checkout-we-chat-context
- class_count: 1
  name: Adyen Checkout Zip Details Context
  property_count: 5
  slug: adyen-checkout-zip-details-context
- class_count: 5
  name: Adyen Configuration Account Holder Context
  property_count: 22
  slug: adyen-configuration-account-holder-context
- class_count: 1
  name: Adyen Configuration Account Supporting Context
  property_count: 7
  slug: adyen-configuration-account-supporting-context
- class_count: 1
  name: Adyen Configuration Active Network Context
  property_count: 2
  slug: adyen-configuration-active-network-context
- class_count: 1
  name: Adyen Configuration Additional Bank Context
  property_count: 2
  slug: adyen-configuration-additional-bank-context
- class_count: 1
  name: Adyen Configuration Address Context
  property_count: 6
  slug: adyen-configuration-address-context
- class_count: 2
  name: Adyen Configuration Address Requirement Context
  property_count: 2
  slug: adyen-configuration-address-requirement-context
- class_count: 1
  name: Adyen Configuration Amount Context
  property_count: 2
  slug: adyen-configuration-amount-context
- class_count: 2
  name: Adyen Configuration Amount Min Context
  property_count: 3
  slug: adyen-configuration-amount-min-context
- class_count: 1
  name: Adyen Configuration Au Local Context
  property_count: 3
  slug: adyen-configuration-au-local-context
- class_count: 2
  name: Adyen Configuration Authentication Context
  property_count: 2
  slug: adyen-configuration-authentication-context
- class_count: 5
  name: Adyen Configuration Balance Account Context
  property_count: 10
  slug: adyen-configuration-balance-account-context
- class_count: 1
  name: Adyen Configuration Balance Context
  property_count: 5
  slug: adyen-configuration-balance-context
- class_count: 2
  name: Adyen Configuration Balance Platform Context
  property_count: 2
  slug: adyen-configuration-balance-platform-context
- class_count: 1
  name: Adyen Configuration Balance Sweep Context
  property_count: 3
  slug: adyen-configuration-balance-sweep-context
- class_count: 5
  name: Adyen Configuration Bank Account Context
  property_count: 4
  slug: adyen-configuration-bank-account-context
- class_count: 1
  name: Adyen Configuration Bank Identification Context
  property_count: 3
  slug: adyen-configuration-bank-identification-context
- class_count: 1
  name: Adyen Configuration Br Local Context
  property_count: 4
  slug: adyen-configuration-br-local-context
- class_count: 1
  name: Adyen Configuration Brand Variants Context
  property_count: 2
  slug: adyen-configuration-brand-variants-context
- class_count: 2
  name: Adyen Configuration Bulk Address Context
  property_count: 8
  slug: adyen-configuration-bulk-address-context
- class_count: 1
  name: Adyen Configuration Ca Local Context
  property_count: 5
  slug: adyen-configuration-ca-local-context
- class_count: 3
  name: Adyen Configuration Capability Problem Context
  property_count: 6
  slug: adyen-configuration-capability-problem-context
- class_count: 1
  name: Adyen Configuration Capability Settings Context
  property_count: 5
  slug: adyen-configuration-capability-settings-context
- class_count: 1
  name: Adyen Configuration Capital Balance Context
  property_count: 4
  slug: adyen-configuration-capital-balance-context
- class_count: 1
  name: Adyen Configuration Capital Grant Context
  property_count: 4
  slug: adyen-configuration-capital-grant-context
- class_count: 1
  name: Adyen Configuration Card Configuration Context
  property_count: 14
  slug: adyen-configuration-card-configuration-context
- class_count: 1
  name: Adyen Configuration Card Context
  property_count: 13
  slug: adyen-configuration-card-context
- class_count: 1
  name: Adyen Configuration Card Info Context
  property_count: 8
  slug: adyen-configuration-card-info-context
- class_count: 3
  name: Adyen Configuration Card Order Context
  property_count: 17
  slug: adyen-configuration-card-order-context
- class_count: 2
  name: Adyen Configuration Contact Details Context
  property_count: 3
  slug: adyen-configuration-contact-details-context
- class_count: 1
  name: Adyen Configuration Counterparty Bank Context
  property_count: 2
  slug: adyen-configuration-counterparty-bank-context
- class_count: 1
  name: Adyen Configuration Counterparty Context
  property_count: 2
  slug: adyen-configuration-counterparty-context
- class_count: 1
  name: Adyen Configuration Countries Restriction Context
  property_count: 2
  slug: adyen-configuration-countries-restriction-context
- class_count: 2
  name: Adyen Configuration Create Sweep Context
  property_count: 11
  slug: adyen-configuration-create-sweep-context
- class_count: 1
  name: Adyen Configuration Cz Local Context
  property_count: 3
  slug: adyen-configuration-cz-local-context
- class_count: 1
  name: Adyen Configuration Day Of Context
  property_count: 2
  slug: adyen-configuration-day-of-context
- class_count: 1
  name: Adyen Configuration Delivery Address Context
  property_count: 7
  slug: adyen-configuration-delivery-address-context
- class_count: 3
  name: Adyen Configuration Delivery Contact Context
  property_count: 4
  slug: adyen-configuration-delivery-contact-context
- class_count: 1
  name: Adyen Configuration Device Info Context
  property_count: 11
  slug: adyen-configuration-device-info-context
- class_count: 1
  name: Adyen Configuration Different Currencies Context
  property_count: 2
  slug: adyen-configuration-different-currencies-context
- class_count: 1
  name: Adyen Configuration Dk Local Context
  property_count: 3
  slug: adyen-configuration-dk-local-context
- class_count: 1
  name: Adyen Configuration Duration Context
  property_count: 2
  slug: adyen-configuration-duration-context
- class_count: 1
  name: Adyen Configuration Entry Modes Context
  property_count: 2
  slug: adyen-configuration-entry-modes-context
- class_count: 1
  name: Adyen Configuration Expiry Context
  property_count: 2
  slug: adyen-configuration-expiry-context
- class_count: 1
  name: Adyen Configuration Fee Context
  property_count: 1
  slug: adyen-configuration-fee-context
- class_count: 1
  name: Adyen Configuration Get Network Context
  property_count: 1
  slug: adyen-configuration-get-network-context
- class_count: 1
  name: Adyen Configuration Get Tax Context
  property_count: 2
  slug: adyen-configuration-get-tax-context
- class_count: 1
  name: Adyen Configuration Grant Limit Context
  property_count: 1
  slug: adyen-configuration-grant-limit-context
- class_count: 1
  name: Adyen Configuration Grant Offer Context
  property_count: 8
  slug: adyen-configuration-grant-offer-context
- class_count: 1
  name: Adyen Configuration Grant Offers Context
  property_count: 1
  slug: adyen-configuration-grant-offers-context
- class_count: 1
  name: Adyen Configuration Hk Local Context
  property_count: 3
  slug: adyen-configuration-hk-local-context
- class_count: 1
  name: Adyen Configuration Hu Local Context
  property_count: 2
  slug: adyen-configuration-hu-local-context
- class_count: 1
  name: Adyen Configuration Iban Account Context
  property_count: 2
  slug: adyen-configuration-iban-account-context
- class_count: 1
  name: Adyen Configuration International Transaction Context
  property_count: 2
  slug: adyen-configuration-international-transaction-context
- class_count: 2
  name: Adyen Configuration Invalid Field Context
  property_count: 2
  slug: adyen-configuration-invalid-field-context
- class_count: 1
  name: Adyen Configuration Json Object Context
  property_count: 0
  slug: adyen-configuration-json-object-context
- class_count: 1
  name: Adyen Configuration List Network Context
  property_count: 1
  slug: adyen-configuration-list-network-context
- class_count: 1
  name: Adyen Configuration Matching Transactions Context
  property_count: 2
  slug: adyen-configuration-matching-transactions-context
- class_count: 1
  name: Adyen Configuration Mccs Restriction Context
  property_count: 2
  slug: adyen-configuration-mccs-restriction-context
- class_count: 1
  name: Adyen Configuration Merchant Acquirer Context
  property_count: 2
  slug: adyen-configuration-merchant-acquirer-context
- class_count: 1
  name: Adyen Configuration Merchant Names Context
  property_count: 2
  slug: adyen-configuration-merchant-names-context
- class_count: 1
  name: Adyen Configuration Merchants Restriction Context
  property_count: 2
  slug: adyen-configuration-merchants-restriction-context
- class_count: 1
  name: Adyen Configuration Name Context
  property_count: 2
  slug: adyen-configuration-name-context
- class_count: 1
  name: Adyen Configuration Network Token Context
  property_count: 8
  slug: adyen-configuration-network-token-context
- class_count: 1
  name: Adyen Configuration No Local Context
  property_count: 2
  slug: adyen-configuration-no-local-context
- class_count: 1
  name: Adyen Configuration Number And Context
  property_count: 4
  slug: adyen-configuration-number-and-context
- class_count: 1
  name: Adyen Configuration Nz Local Context
  property_count: 2
  slug: adyen-configuration-nz-local-context
- class_count: 1
  name: Adyen Configuration Paginated Account Context
  property_count: 3
  slug: adyen-configuration-paginated-account-context
- class_count: 1
  name: Adyen Configuration Paginated Balance Context
  property_count: 3
  slug: adyen-configuration-paginated-balance-context
- class_count: 2
  name: Adyen Configuration Paginated Get Context
  property_count: 4
  slug: adyen-configuration-paginated-get-context
- class_count: 1
  name: Adyen Configuration Paginated Payment Context
  property_count: 3
  slug: adyen-configuration-paginated-payment-context
- class_count: 8
  name: Adyen Configuration Payment Instrument Context
  property_count: 19
  slug: adyen-configuration-payment-instrument-context
- class_count: 1
  name: Adyen Configuration Phone Context
  property_count: 2
  slug: adyen-configuration-phone-context
- class_count: 1
  name: Adyen Configuration Phone Number Context
  property_count: 3
  slug: adyen-configuration-phone-number-context
- class_count: 2
  name: Adyen Configuration Pin Change Context
  property_count: 5
  slug: adyen-configuration-pin-change-context
- class_count: 1
  name: Adyen Configuration Pl Local Context
  property_count: 2
  slug: adyen-configuration-pl-local-context
- class_count: 1
  name: Adyen Configuration Platform Payment Context
  property_count: 2
  slug: adyen-configuration-platform-payment-context
- class_count: 1
  name: Adyen Configuration Processing Types Context
  property_count: 2
  slug: adyen-configuration-processing-types-context
- class_count: 1
  name: Adyen Configuration Public Key Context
  property_count: 2
  slug: adyen-configuration-public-key-context
- class_count: 1
  name: Adyen Configuration Remediating Action Context
  property_count: 2
  slug: adyen-configuration-remediating-action-context
- class_count: 1
  name: Adyen Configuration Repayment Context
  property_count: 3
  slug: adyen-configuration-repayment-context
- class_count: 1
  name: Adyen Configuration Repayment Term Context
  property_count: 2
  slug: adyen-configuration-repayment-term-context
- class_count: 1
  name: Adyen Configuration Rest Service Context
  property_count: 9
  slug: adyen-configuration-rest-service-context
- class_count: 2
  name: Adyen Configuration Reveal Pin Context
  property_count: 4
  slug: adyen-configuration-reveal-pin-context
- class_count: 1
  name: Adyen Configuration Same Amount Context
  property_count: 2
  slug: adyen-configuration-same-amount-context
- class_count: 1
  name: Adyen Configuration Same Counterparty Context
  property_count: 2
  slug: adyen-configuration-same-counterparty-context
- class_count: 1
  name: Adyen Configuration Se Local Context
  property_count: 3
  slug: adyen-configuration-se-local-context
- class_count: 1
  name: Adyen Configuration Sg Local Context
  property_count: 3
  slug: adyen-configuration-sg-local-context
- class_count: 1
  name: Adyen Configuration String Match Context
  property_count: 2
  slug: adyen-configuration-string-match-context
- class_count: 2
  name: Adyen Configuration Sweep Configuration Context
  property_count: 12
  slug: adyen-configuration-sweep-configuration-context
- class_count: 1
  name: Adyen Configuration Sweep Counterparty Context
  property_count: 3
  slug: adyen-configuration-sweep-counterparty-context
- class_count: 1
  name: Adyen Configuration Sweep Schedule Context
  property_count: 2
  slug: adyen-configuration-sweep-schedule-context
- class_count: 1
  name: Adyen Configuration Threshold Repayment Context
  property_count: 1
  slug: adyen-configuration-threshold-repayment-context
- class_count: 2
  name: Adyen Configuration Time Of Context
  property_count: 4
  slug: adyen-configuration-time-of-context
- class_count: 1
  name: Adyen Configuration Total Amount Context
  property_count: 2
  slug: adyen-configuration-total-amount-context
- class_count: 7
  name: Adyen Configuration Transaction Rule Context
  property_count: 36
  slug: adyen-configuration-transaction-rule-context
- class_count: 1
  name: Adyen Configuration Transaction Rules Context
  property_count: 1
  slug: adyen-configuration-transaction-rules-context
- class_count: 3
  name: Adyen Configuration Transfer Route Context
  property_count: 10
  slug: adyen-configuration-transfer-route-context
- class_count: 1
  name: Adyen Configuration Uk Local Context
  property_count: 3
  slug: adyen-configuration-uk-local-context
- class_count: 1
  name: Adyen Configuration Update Network Context
  property_count: 1
  slug: adyen-configuration-update-network-context
- class_count: 2
  name: Adyen Configuration Update Payment Context
  property_count: 11
  slug: adyen-configuration-update-payment-context
- class_count: 2
  name: Adyen Configuration Update Sweep Context
  property_count: 12
  slug: adyen-configuration-update-sweep-context
- class_count: 1
  name: Adyen Configuration Us Local Context
  property_count: 4
  slug: adyen-configuration-us-local-context
- class_count: 1
  name: Adyen Configuration Verification Deadline Context
  property_count: 3
  slug: adyen-configuration-verification-deadline-context
- class_count: 2
  name: Adyen Configuration Verification Error Context
  property_count: 6
  slug: adyen-configuration-verification-error-context
- class_count: 50
  name: Adyen Configuration Webhooks Context
  property_count: 135
  slug: adyen-configuration-webhooks-context
- class_count: 2
  name: Adyen Data Protection Subject Context
  property_count: 4
  slug: adyen-data-protection-subject-context
- class_count: 2
  name: Adyen Disputes Accept Dispute Context
  property_count: 3
  slug: adyen-disputes-accept-dispute-context
- class_count: 2
  name: Adyen Disputes Defend Dispute Context
  property_count: 4
  slug: adyen-disputes-defend-dispute-context
- class_count: 2
  name: Adyen Disputes Defense Document Context
  property_count: 5
  slug: adyen-disputes-defense-document-context
- class_count: 1
  name: Adyen Disputes Defense Reason Context
  property_count: 3
  slug: adyen-disputes-defense-reason-context
- class_count: 2
  name: Adyen Disputes Defense Reasons Context
  property_count: 4
  slug: adyen-disputes-defense-reasons-context
- class_count: 2
  name: Adyen Disputes Delete Defense Context
  property_count: 4
  slug: adyen-disputes-delete-defense-context
- class_count: 1
  name: Adyen Disputes Dispute Service Context
  property_count: 2
  slug: adyen-disputes-dispute-service-context
- class_count: 2
  name: Adyen Disputes Supply Defense Context
  property_count: 4
  slug: adyen-disputes-supply-defense-context
- class_count: 1
  name: Adyen Funds Account Detail Context
  property_count: 2
  slug: adyen-funds-account-detail-context
- class_count: 4
  name: Adyen Funds Account Holder Context
  property_count: 9
  slug: adyen-funds-account-holder-context
- class_count: 1
  name: Adyen Funds Account Transaction Context
  property_count: 3
  slug: adyen-funds-account-transaction-context
- class_count: 1
  name: Adyen Funds Amount Context
  property_count: 2
  slug: adyen-funds-amount-context
- class_count: 1
  name: Adyen Funds Bank Account Context
  property_count: 26
  slug: adyen-funds-bank-account-context
- class_count: 3
  name: Adyen Funds Debit Account Context
  property_count: 9
  slug: adyen-funds-debit-account-context
- class_count: 1
  name: Adyen Funds Detail Balance Context
  property_count: 3
  slug: adyen-funds-detail-balance-context
- class_count: 1
  name: Adyen Funds Error Field Context
  property_count: 3
  slug: adyen-funds-error-field-context
- class_count: 1
  name: Adyen Funds Field Type Context
  property_count: 3
  slug: adyen-funds-field-type-context
- class_count: 3
  name: Adyen Funds Payout Account Context
  property_count: 10
  slug: adyen-funds-payout-account-context
- class_count: 2
  name: Adyen Funds Refund Funds Context
  property_count: 7
  slug: adyen-funds-refund-funds-context
- class_count: 2
  name: Adyen Funds Refund Not Context
  property_count: 5
  slug: adyen-funds-refund-not-context
- class_count: 2
  name: Adyen Funds Setup Beneficiary Context
  property_count: 6
  slug: adyen-funds-setup-beneficiary-context
- class_count: 1
  name: Adyen Funds Split Amount Context
  property_count: 2
  slug: adyen-funds-split-amount-context
- class_count: 2
  name: Adyen Funds Split Context
  property_count: 4
  slug: adyen-funds-split-context
- class_count: 2
  name: Adyen Funds Transaction Context
  property_count: 15
  slug: adyen-funds-transaction-context
- class_count: 1
  name: Adyen Funds Transaction List Context
  property_count: 2
  slug: adyen-funds-transaction-list-context
- class_count: 2
  name: Adyen Funds Transfer Funds Context
  property_count: 8
  slug: adyen-funds-transfer-funds-context
- class_count: 1
  name: Adyen Hosted Onboarding Collect Context
  property_count: 6
  slug: adyen-hosted-onboarding-collect-context
- class_count: 1
  name: Adyen Hosted Onboarding Error Context
  property_count: 3
  slug: adyen-hosted-onboarding-error-context
- class_count: 1
  name: Adyen Hosted Onboarding Field Context
  property_count: 3
  slug: adyen-hosted-onboarding-field-context
- class_count: 4
  name: Adyen Hosted Onboarding Get Context
  property_count: 12
  slug: adyen-hosted-onboarding-get-context
- class_count: 1
  name: Adyen Hosted Onboarding Show Context
  property_count: 9
  slug: adyen-hosted-onboarding-show-context
- class_count: 2
  name: Adyen Legal Entity Accept Terms Of Service Context
  property_count: 6
  slug: adyen-legal-entity-accept-terms-of-service-context
- class_count: 1
  name: Adyen Legal Entity Additional Context
  property_count: 2
  slug: adyen-legal-entity-additional-context
- class_count: 1
  name: Adyen Legal Entity Address Context
  property_count: 6
  slug: adyen-legal-entity-address-context
- class_count: 1
  name: Adyen Legal Entity Amount Context
  property_count: 2
  slug: adyen-legal-entity-amount-context
- class_count: 1
  name: Adyen Legal Entity Attachment Context
  property_count: 5
  slug: adyen-legal-entity-attachment-context
- class_count: 1
  name: Adyen Legal Entity Au Context
  property_count: 3
  slug: adyen-legal-entity-au-context
- class_count: 1
  name: Adyen Legal Entity Bank Context
  property_count: 5
  slug: adyen-legal-entity-bank-context
- class_count: 1
  name: Adyen Legal Entity Birth Context
  property_count: 1
  slug: adyen-legal-entity-birth-context
- class_count: 4
  name: Adyen Legal Entity Business Context
  property_count: 11
  slug: adyen-legal-entity-business-context
- class_count: 1
  name: Adyen Legal Entity Ca Context
  property_count: 5
  slug: adyen-legal-entity-ca-context
- class_count: 1
  name: Adyen Legal Entity Calculate Terms Of Service Context
  property_count: 1
  slug: adyen-legal-entity-calculate-terms-of-service-context
- class_count: 4
  name: Adyen Legal Entity Capability Context
  property_count: 11
  slug: adyen-legal-entity-capability-context
- class_count: 1
  name: Adyen Legal Entity Cz Context
  property_count: 3
  slug: adyen-legal-entity-cz-context
- class_count: 1
  name: Adyen Legal Entity Data Context
  property_count: 1
  slug: adyen-legal-entity-data-context
- class_count: 1
  name: Adyen Legal Entity Dk Context
  property_count: 3
  slug: adyen-legal-entity-dk-context
- class_count: 4
  name: Adyen Legal Entity Document Context
  property_count: 16
  slug: adyen-legal-entity-document-context
- class_count: 1
  name: Adyen Legal Entity Entity Context
  property_count: 1
  slug: adyen-legal-entity-entity-context
- class_count: 2
  name: Adyen Legal Entity Generate Context
  property_count: 4
  slug: adyen-legal-entity-generate-context
- class_count: 2
  name: Adyen Legal Entity Get Context
  property_count: 5
  slug: adyen-legal-entity-get-context
- class_count: 3
  name: Adyen Legal Entity Get Terms Of Service Context
  property_count: 6
  slug: adyen-legal-entity-get-terms-of-service-context
- class_count: 1
  name: Adyen Legal Entity Hk Context
  property_count: 3
  slug: adyen-legal-entity-hk-context
- class_count: 1
  name: Adyen Legal Entity Hu Context
  property_count: 2
  slug: adyen-legal-entity-hu-context
- class_count: 1
  name: Adyen Legal Entity Iban Context
  property_count: 2
  slug: adyen-legal-entity-iban-context
- class_count: 1
  name: Adyen Legal Entity Identification Context
  property_count: 7
  slug: adyen-legal-entity-identification-context
- class_count: 3
  name: Adyen Legal Entity Individual Context
  property_count: 7
  slug: adyen-legal-entity-individual-context
- class_count: 6
  name: Adyen Legal Entity Legal Context
  property_count: 28
  slug: adyen-legal-entity-legal-context
- class_count: 1
  name: Adyen Legal Entity Name Context
  property_count: 3
  slug: adyen-legal-entity-name-context
- class_count: 1
  name: Adyen Legal Entity No Context
  property_count: 2
  slug: adyen-legal-entity-no-context
- class_count: 1
  name: Adyen Legal Entity Number Context
  property_count: 4
  slug: adyen-legal-entity-number-context
- class_count: 1
  name: Adyen Legal Entity Nz Context
  property_count: 2
  slug: adyen-legal-entity-nz-context
- class_count: 6
  name: Adyen Legal Entity Onboarding Context
  property_count: 11
  slug: adyen-legal-entity-onboarding-context
- class_count: 3
  name: Adyen Legal Entity Organization Context
  property_count: 14
  slug: adyen-legal-entity-organization-context
- class_count: 1
  name: Adyen Legal Entity Owner Context
  property_count: 2
  slug: adyen-legal-entity-owner-context
- class_count: 3
  name: Adyen Legal Entity Pci Context
  property_count: 6
  slug: adyen-legal-entity-pci-context
- class_count: 1
  name: Adyen Legal Entity Phone Context
  property_count: 2
  slug: adyen-legal-entity-phone-context
- class_count: 1
  name: Adyen Legal Entity Pl Context
  property_count: 2
  slug: adyen-legal-entity-pl-context
- class_count: 1
  name: Adyen Legal Entity Remediating Context
  property_count: 2
  slug: adyen-legal-entity-remediating-context
- class_count: 1
  name: Adyen Legal Entity Se Context
  property_count: 3
  slug: adyen-legal-entity-se-context
- class_count: 1
  name: Adyen Legal Entity Sg Context
  property_count: 3
  slug: adyen-legal-entity-sg-context
- class_count: 3
  name: Adyen Legal Entity Sole Context
  property_count: 9
  slug: adyen-legal-entity-sole-context
- class_count: 2
  name: Adyen Legal Entity Source Context
  property_count: 3
  slug: adyen-legal-entity-source-context
- class_count: 1
  name: Adyen Legal Entity Stock Context
  property_count: 3
  slug: adyen-legal-entity-stock-context
- class_count: 1
  name: Adyen Legal Entity Supporting Context
  property_count: 4
  slug: adyen-legal-entity-supporting-context
- class_count: 2
  name: Adyen Legal Entity Tax Context
  property_count: 6
  slug: adyen-legal-entity-tax-context
- class_count: 1
  name: Adyen Legal Entity Terms Of Service Context
  property_count: 5
  slug: adyen-legal-entity-terms-of-service-context
- class_count: 3
  name: Adyen Legal Entity Transfer Context
  property_count: 10
  slug: adyen-legal-entity-transfer-context
- class_count: 3
  name: Adyen Legal Entity Trust Context
  property_count: 11
  slug: adyen-legal-entity-trust-context
- class_count: 1
  name: Adyen Legal Entity Uk Context
  property_count: 3
  slug: adyen-legal-entity-uk-context
- class_count: 2
  name: Adyen Legal Entity Undefined Context
  property_count: 1
  slug: adyen-legal-entity-undefined-context
- class_count: 3
  name: Adyen Legal Entity Unincorporated Context
  property_count: 10
  slug: adyen-legal-entity-unincorporated-context
- class_count: 1
  name: Adyen Legal Entity Us Context
  property_count: 4
  slug: adyen-legal-entity-us-context
- class_count: 4
  name: Adyen Legal Entity Verification Context
  property_count: 9
  slug: adyen-legal-entity-verification-context
- class_count: 2
  name: Adyen Legal Entity Web Context
  property_count: 3
  slug: adyen-legal-entity-web-context
- class_count: 1
  name: Adyen Management Additional Commission Context
  property_count: 3
  slug: adyen-management-additional-commission-context
- class_count: 2
  name: Adyen Management Additional Settings Context
  property_count: 3
  slug: adyen-management-additional-settings-context
- class_count: 1
  name: Adyen Management Address Context
  property_count: 7
  slug: adyen-management-address-context
- class_count: 1
  name: Adyen Management Afterpay Touch Context
  property_count: 1
  slug: adyen-management-afterpay-touch-context
- class_count: 1
  name: Adyen Management Allowed Origin Context
  property_count: 3
  slug: adyen-management-allowed-origin-context
- class_count: 1
  name: Adyen Management Allowed Origins Context
  property_count: 1
  slug: adyen-management-allowed-origins-context
- class_count: 1
  name: Adyen Management Amount Context
  property_count: 2
  slug: adyen-management-amount-context
- class_count: 2
  name: Adyen Management Android App Context
  property_count: 7
  slug: adyen-management-android-app-context
- class_count: 1
  name: Adyen Management Android Apps Context
  property_count: 1
  slug: adyen-management-android-apps-context
- class_count: 3
  name: Adyen Management Android Certificate Context
  property_count: 5
  slug: adyen-management-android-certificate-context
- class_count: 1
  name: Adyen Management Android Certificates Context
  property_count: 1
  slug: adyen-management-android-certificates-context
- class_count: 3
  name: Adyen Management Api Context
  property_count: 13
  slug: adyen-management-api-context
- class_count: 1
  name: Adyen Management Apple Pay Context
  property_count: 1
  slug: adyen-management-apple-pay-context
- class_count: 1
  name: Adyen Management Bcmc Info Context
  property_count: 2
  slug: adyen-management-bcmc-info-context
- class_count: 1
  name: Adyen Management Billing Entities Context
  property_count: 1
  slug: adyen-management-billing-entities-context
- class_count: 3
  name: Adyen Management Billing Entity Context
  property_count: 3
  slug: adyen-management-billing-entity-context
- class_count: 1
  name: Adyen Management Cardholder Receipt Context
  property_count: 1
  slug: adyen-management-cardholder-receipt-context
- class_count: 1
  name: Adyen Management Cartes Bancaires Context
  property_count: 2
  slug: adyen-management-cartes-bancaires-context
- class_count: 1
  name: Adyen Management Clearpay Info Context
  property_count: 1
  slug: adyen-management-clearpay-info-context
- class_count: 1
  name: Adyen Management Commission Context
  property_count: 2
  slug: adyen-management-commission-context
- class_count: 2
  name: Adyen Management Company Api Context
  property_count: 9
  slug: adyen-management-company-api-context
- class_count: 3
  name: Adyen Management Company Context
  property_count: 5
  slug: adyen-management-company-context
- class_count: 1
  name: Adyen Management Company Links Context
  property_count: 4
  slug: adyen-management-company-links-context
- class_count: 3
  name: Adyen Management Company User Context
  property_count: 9
  slug: adyen-management-company-user-context
- class_count: 1
  name: Adyen Management Configuration Context
  property_count: 4
  slug: adyen-management-configuration-context
- class_count: 1
  name: Adyen Management Connectivity Context
  property_count: 1
  slug: adyen-management-connectivity-context
- class_count: 2
  name: Adyen Management Contact Context
  property_count: 4
  slug: adyen-management-contact-context
- class_count: 1
  name: Adyen Management Create Allowed Context
  property_count: 3
  slug: adyen-management-create-allowed-context
- class_count: 2
  name: Adyen Management Create Api Context
  property_count: 10
  slug: adyen-management-create-api-context
- class_count: 3
  name: Adyen Management Create Company Api Context
  property_count: 11
  slug: adyen-management-create-company-api-context
- class_count: 7
  name: Adyen Management Create Company Context
  property_count: 21
  slug: adyen-management-create-company-context
- class_count: 2
  name: Adyen Management Create Merchant Api Context
  property_count: 2
  slug: adyen-management-create-merchant-api-context
- class_count: 8
  name: Adyen Management Create Merchant Context
  property_count: 22
  slug: adyen-management-create-merchant-context
- class_count: 3
  name: Adyen Management Create User Context
  property_count: 8
  slug: adyen-management-create-user-context
- class_count: 1
  name: Adyen Management Currency Context
  property_count: 3
  slug: adyen-management-currency-context
- class_count: 1
  name: Adyen Management Custom Notification Context
  property_count: 7
  slug: adyen-management-custom-notification-context
- class_count: 2
  name: Adyen Management Data Center Context
  property_count: 1
  slug: adyen-management-data-center-context
- class_count: 1
  name: Adyen Management Event Url Context
  property_count: 2
  slug: adyen-management-event-url-context
- class_count: 1
  name: Adyen Management External Terminal Context
  property_count: 8
  slug: adyen-management-external-terminal-context
- class_count: 2
  name: Adyen Management File Context
  property_count: 1
  slug: adyen-management-file-context
- class_count: 1
  name: Adyen Management Generate Api Context
  property_count: 1
  slug: adyen-management-generate-api-context
- class_count: 1
  name: Adyen Management Generate Client Context
  property_count: 1
  slug: adyen-management-generate-client-context
- class_count: 1
  name: Adyen Management Generate Hmac Context
  property_count: 1
  slug: adyen-management-generate-hmac-context
- class_count: 1
  name: Adyen Management Generic Pm Context
  property_count: 1
  slug: adyen-management-generic-pm-context
- class_count: 1
  name: Adyen Management Giro Pay Context
  property_count: 1
  slug: adyen-management-giro-pay-context
- class_count: 1
  name: Adyen Management Google Pay Context
  property_count: 2
  slug: adyen-management-google-pay-context
- class_count: 1
  name: Adyen Management Gratuity Context
  property_count: 4
  slug: adyen-management-gratuity-context
- class_count: 1
  name: Adyen Management Hardware Context
  property_count: 3
  slug: adyen-management-hardware-context
- class_count: 2
  name: Adyen Management Id Name Context
  property_count: 1
  slug: adyen-management-id-name-context
- class_count: 2
  name: Adyen Management Install Android Context
  property_count: 3
  slug: adyen-management-install-android-context
- class_count: 2
  name: Adyen Management Invalid Field Context
  property_count: 2
  slug: adyen-management-invalid-field-context
- class_count: 1
  name: Adyen Management Json Object Context
  property_count: 0
  slug: adyen-management-json-object-context
- class_count: 3
  name: Adyen Management Key Context
  property_count: 1
  slug: adyen-management-key-context
- class_count: 1
  name: Adyen Management Klarna Info Context
  property_count: 4
  slug: adyen-management-klarna-info-context
- class_count: 1
  name: Adyen Management Links Context
  property_count: 1
  slug: adyen-management-links-context
- class_count: 1
  name: Adyen Management Links Element Context
  property_count: 1
  slug: adyen-management-links-element-context
- class_count: 1
  name: Adyen Management List Company Api Context
  property_count: 4
  slug: adyen-management-list-company-api-context
- class_count: 2
  name: Adyen Management List Company Context
  property_count: 4
  slug: adyen-management-list-company-context
- class_count: 1
  name: Adyen Management List External Context
  property_count: 1
  slug: adyen-management-list-external-context
- class_count: 1
  name: Adyen Management List Merchant Api Context
  property_count: 4
  slug: adyen-management-list-merchant-api-context
- class_count: 2
  name: Adyen Management List Merchant Context
  property_count: 4
  slug: adyen-management-list-merchant-context
- class_count: 1
  name: Adyen Management List Stores Context
  property_count: 4
  slug: adyen-management-list-stores-context
- class_count: 1
  name: Adyen Management List Terminals Context
  property_count: 4
  slug: adyen-management-list-terminals-context
- class_count: 1
  name: Adyen Management List Webhooks Context
  property_count: 5
  slug: adyen-management-list-webhooks-context
- class_count: 1
  name: Adyen Management Localization Context
  property_count: 3
  slug: adyen-management-localization-context
- class_count: 1
  name: Adyen Management Logo Context
  property_count: 1
  slug: adyen-management-logo-context
- class_count: 2
  name: Adyen Management Me Api Context
  property_count: 10
  slug: adyen-management-me-api-context
- class_count: 1
  name: Adyen Management Meal Voucher Context
  property_count: 3
  slug: adyen-management-meal-voucher-context
- class_count: 3
  name: Adyen Management Merchant Context
  property_count: 12
  slug: adyen-management-merchant-context
- class_count: 1
  name: Adyen Management Merchant Links Context
  property_count: 4
  slug: adyen-management-merchant-links-context
- class_count: 1
  name: Adyen Management Minor Units Context
  property_count: 2
  slug: adyen-management-minor-units-context
- class_count: 1
  name: Adyen Management Name Context
  property_count: 2
  slug: adyen-management-name-context
- class_count: 1
  name: Adyen Management Name2 Context
  property_count: 2
  slug: adyen-management-name2-context
- class_count: 1
  name: Adyen Management Nexo Context
  property_count: 5
  slug: adyen-management-nexo-context
- class_count: 1
  name: Adyen Management Notification Context
  property_count: 5
  slug: adyen-management-notification-context
- class_count: 1
  name: Adyen Management Notification Url Context
  property_count: 2
  slug: adyen-management-notification-url-context
- class_count: 1
  name: Adyen Management Offline Processing Context
  property_count: 2
  slug: adyen-management-offline-processing-context
- class_count: 1
  name: Adyen Management Opi Context
  property_count: 3
  slug: adyen-management-opi-context
- class_count: 2
  name: Adyen Management Order Item Context
  property_count: 3
  slug: adyen-management-order-item-context
- class_count: 1
  name: Adyen Management Pagination Links Context
  property_count: 5
  slug: adyen-management-pagination-links-context
- class_count: 1
  name: Adyen Management Passcodes Context
  property_count: 4
  slug: adyen-management-passcodes-context
- class_count: 1
  name: Adyen Management Pay At Context
  property_count: 3
  slug: adyen-management-pay-at-context
- class_count: 1
  name: Adyen Management Pay Pal Context
  property_count: 3
  slug: adyen-management-pay-pal-context
- class_count: 1
  name: Adyen Management Payment Context
  property_count: 2
  slug: adyen-management-payment-context
- class_count: 3
  name: Adyen Management Payment Method Context
  property_count: 42
  slug: adyen-management-payment-method-context
- class_count: 3
  name: Adyen Management Payout Settings Context
  property_count: 8
  slug: adyen-management-payout-settings-context
- class_count: 2
  name: Adyen Management Profile Context
  property_count: 17
  slug: adyen-management-profile-context
- class_count: 1
  name: Adyen Management Receipt Options Context
  property_count: 3
  slug: adyen-management-receipt-options-context
- class_count: 1
  name: Adyen Management Receipt Printing Context
  property_count: 16
  slug: adyen-management-receipt-printing-context
- class_count: 1
  name: Adyen Management Referenced Context
  property_count: 1
  slug: adyen-management-referenced-context
- class_count: 1
  name: Adyen Management Refunds Context
  property_count: 1
  slug: adyen-management-refunds-context
- class_count: 1
  name: Adyen Management Release Update Context
  property_count: 2
  slug: adyen-management-release-update-context
- class_count: 1
  name: Adyen Management Request Activation Context
  property_count: 2
  slug: adyen-management-request-activation-context
- class_count: 1
  name: Adyen Management Rest Service Context
  property_count: 9
  slug: adyen-management-rest-service-context
- class_count: 2
  name: Adyen Management Schedule Terminal Context
  property_count: 8
  slug: adyen-management-schedule-terminal-context
- class_count: 1
  name: Adyen Management Settings Context
  property_count: 3
  slug: adyen-management-settings-context
- class_count: 2
  name: Adyen Management Shipping Location Context
  property_count: 3
  slug: adyen-management-shipping-location-context
- class_count: 1
  name: Adyen Management Shipping Locations Context
  property_count: 1
  slug: adyen-management-shipping-locations-context
- class_count: 1
  name: Adyen Management Signature Context
  property_count: 4
  slug: adyen-management-signature-context
- class_count: 1
  name: Adyen Management Sofort Info Context
  property_count: 2
  slug: adyen-management-sofort-info-context
- class_count: 5
  name: Adyen Management Split Configuration Context
  property_count: 25
  slug: adyen-management-split-configuration-context
- class_count: 1
  name: Adyen Management Standalone Context
  property_count: 2
  slug: adyen-management-standalone-context
- class_count: 2
  name: Adyen Management Store Context
  property_count: 11
  slug: adyen-management-store-context
- class_count: 3
  name: Adyen Management Store Creation Context
  property_count: 8
  slug: adyen-management-store-creation-context
- class_count: 1
  name: Adyen Management Store Location Context
  property_count: 7
  slug: adyen-management-store-location-context
- class_count: 1
  name: Adyen Management Store Split Context
  property_count: 2
  slug: adyen-management-store-split-context
- class_count: 1
  name: Adyen Management Surcharge Context
  property_count: 2
  slug: adyen-management-surcharge-context
- class_count: 1
  name: Adyen Management Swish Info Context
  property_count: 1
  slug: adyen-management-swish-info-context
- class_count: 1
  name: Adyen Management Tap To Context
  property_count: 1
  slug: adyen-management-tap-to-context
- class_count: 1
  name: Adyen Management Terminal Action Context
  property_count: 2
  slug: adyen-management-terminal-action-context
- class_count: 1
  name: Adyen Management Terminal Assignment Context
  property_count: 5
  slug: adyen-management-terminal-assignment-context
- class_count: 5
  name: Adyen Management Terminal Connectivity Context
  property_count: 10
  slug: adyen-management-terminal-connectivity-context
- class_count: 1
  name: Adyen Management Terminal Context
  property_count: 8
  slug: adyen-management-terminal-context
- class_count: 1
  name: Adyen Management Terminal Models Context
  property_count: 1
  slug: adyen-management-terminal-models-context
- class_count: 2
  name: Adyen Management Terminal Order Context
  property_count: 12
  slug: adyen-management-terminal-order-context
- class_count: 1
  name: Adyen Management Terminal Orders Context
  property_count: 1
  slug: adyen-management-terminal-orders-context
- class_count: 4
  name: Adyen Management Terminal Product Context
  property_count: 5
  slug: adyen-management-terminal-product-context
- class_count: 1
  name: Adyen Management Terminal Products Context
  property_count: 1
  slug: adyen-management-terminal-products-context
- class_count: 2
  name: Adyen Management Terminal Reassignment Context
  property_count: 4
  slug: adyen-management-terminal-reassignment-context
- class_count: 1
  name: Adyen Management Terminal Settings Context
  property_count: 20
  slug: adyen-management-terminal-settings-context
- class_count: 1
  name: Adyen Management Test Company Context
  property_count: 3
  slug: adyen-management-test-company-context
- class_count: 1
  name: Adyen Management Test Output Context
  property_count: 6
  slug: adyen-management-test-output-context
- class_count: 2
  name: Adyen Management Test Webhook Context
  property_count: 3
  slug: adyen-management-test-webhook-context
- class_count: 1
  name: Adyen Management Timeouts Context
  property_count: 1
  slug: adyen-management-timeouts-context
- class_count: 1
  name: Adyen Management Transaction Description Context
  property_count: 2
  slug: adyen-management-transaction-description-context
- class_count: 1
  name: Adyen Management Twint Info Context
  property_count: 1
  slug: adyen-management-twint-info-context
- class_count: 2
  name: Adyen Management Uninstall Android Context
  property_count: 3
  slug: adyen-management-uninstall-android-context
- class_count: 1
  name: Adyen Management Updatable Address Context
  property_count: 6
  slug: adyen-management-updatable-address-context
- class_count: 2
  name: Adyen Management Update Company Api Context
  property_count: 4
  slug: adyen-management-update-company-api-context
- class_count: 6
  name: Adyen Management Update Company Context
  property_count: 17
  slug: adyen-management-update-company-context
- class_count: 2
  name: Adyen Management Update Merchant Api Context
  property_count: 3
  slug: adyen-management-update-merchant-api-context
- class_count: 6
  name: Adyen Management Update Merchant Context
  property_count: 14
  slug: adyen-management-update-merchant-context
- class_count: 1
  name: Adyen Management Update Payment Context
  property_count: 18
  slug: adyen-management-update-payment-context
- class_count: 1
  name: Adyen Management Update Payout Context
  property_count: 1
  slug: adyen-management-update-payout-context
- class_count: 4
  name: Adyen Management Update Split Context
  property_count: 19
  slug: adyen-management-update-split-context
- class_count: 2
  name: Adyen Management Update Store Context
  property_count: 6
  slug: adyen-management-update-store-context
- class_count: 1
  name: Adyen Management Upload Android Context
  property_count: 1
  slug: adyen-management-upload-android-context
- class_count: 2
  name: Adyen Management Url Context
  property_count: 3
  slug: adyen-management-url-context
- class_count: 3
  name: Adyen Management User Context
  property_count: 8
  slug: adyen-management-user-context
- class_count: 1
  name: Adyen Management Vipps Info Context
  property_count: 2
  slug: adyen-management-vipps-info-context
- class_count: 3
  name: Adyen Management Webhook Context
  property_count: 20
  slug: adyen-management-webhook-context
- class_count: 1
  name: Adyen Management Webhook Links Context
  property_count: 5
  slug: adyen-management-webhook-links-context
- class_count: 17
  name: Adyen Management Webhooks Context
  property_count: 30
  slug: adyen-management-webhooks-context
- class_count: 1
  name: Adyen Management Wifi Profiles Context
  property_count: 2
  slug: adyen-management-wifi-profiles-context
- class_count: 1
  name: Adyen Notification Configurations Create Context
  property_count: 1
  slug: adyen-notification-configurations-create-context
- class_count: 1
  name: Adyen Notification Configurations Delete Context
  property_count: 1
  slug: adyen-notification-configurations-delete-context
- class_count: 1
  name: Adyen Notification Configurations Empty Context
  property_count: 0
  slug: adyen-notification-configurations-empty-context
- class_count: 1
  name: Adyen Notification Configurations Error Context
  property_count: 3
  slug: adyen-notification-configurations-error-context
- class_count: 1
  name: Adyen Notification Configurations Exchange Context
  property_count: 2
  slug: adyen-notification-configurations-exchange-context
- class_count: 1
  name: Adyen Notification Configurations Field Context
  property_count: 3
  slug: adyen-notification-configurations-field-context
- class_count: 1
  name: Adyen Notification Configurations Generic Context
  property_count: 3
  slug: adyen-notification-configurations-generic-context
- class_count: 3
  name: Adyen Notification Configurations Get Context
  property_count: 6
  slug: adyen-notification-configurations-get-context
- class_count: 3
  name: Adyen Notification Configurations Notification Context
  property_count: 11
  slug: adyen-notification-configurations-notification-context
- class_count: 2
  name: Adyen Notification Configurations Test Context
  property_count: 8
  slug: adyen-notification-configurations-test-context
- class_count: 1
  name: Adyen Notification Configurations Update Context
  property_count: 1
  slug: adyen-notification-configurations-update-context
- class_count: 68
  name: Adyen Notification Webhooks Context
  property_count: 150
  slug: adyen-notification-webhooks-context
- class_count: 86
  name: Adyen Notifications Context
  property_count: 209
  slug: adyen-notifications-context
- class_count: 1
  name: Adyen Payments Account Info Context
  property_count: 19
  slug: adyen-payments-account-info-context
- class_count: 1
  name: Adyen Payments Acct Info Context
  property_count: 16
  slug: adyen-payments-acct-info-context
- class_count: 15
  name: Adyen Payments Additional Data Context
  property_count: 188
  slug: adyen-payments-additional-data-context
- class_count: 1
  name: Adyen Payments Additional Data3 Context
  property_count: 6
  slug: adyen-payments-additional-data3-context
- class_count: 1
  name: Adyen Payments Address Context
  property_count: 6
  slug: adyen-payments-address-context
- class_count: 1
  name: Adyen Payments Adjust Authorisation Context
  property_count: 11
  slug: adyen-payments-adjust-authorisation-context
- class_count: 1
  name: Adyen Payments Amount Context
  property_count: 2
  slug: adyen-payments-amount-context
- class_count: 1
  name: Adyen Payments Application Info Context
  property_count: 6
  slug: adyen-payments-application-info-context
- class_count: 2
  name: Adyen Payments Authentication Result Context
  property_count: 4
  slug: adyen-payments-authentication-result-context
- class_count: 1
  name: Adyen Payments Bank Account Context
  property_count: 9
  slug: adyen-payments-bank-account-context
- class_count: 1
  name: Adyen Payments Browser Info Context
  property_count: 9
  slug: adyen-payments-browser-info-context
- class_count: 1
  name: Adyen Payments Cancel Or Context
  property_count: 9
  slug: adyen-payments-cancel-or-context
- class_count: 1
  name: Adyen Payments Cancel Request Context
  property_count: 10
  slug: adyen-payments-cancel-request-context
- class_count: 1
  name: Adyen Payments Capture Request Context
  property_count: 11
  slug: adyen-payments-capture-request-context
- class_count: 1
  name: Adyen Payments Card Context
  property_count: 8
  slug: adyen-payments-card-context
- class_count: 3
  name: Adyen Payments Common Field Context
  property_count: 0
  slug: adyen-payments-common-field-context
- class_count: 1
  name: Adyen Payments Device Render Context
  property_count: 2
  slug: adyen-payments-device-render-context
- class_count: 1
  name: Adyen Payments Donation Request Context
  property_count: 6
  slug: adyen-payments-donation-request-context
- class_count: 3
  name: Adyen Payments External Platform Context
  property_count: 1
  slug: adyen-payments-external-platform-context
- class_count: 1
  name: Adyen Payments Forex Quote Context
  property_count: 12
  slug: adyen-payments-forex-quote-context
- class_count: 3
  name: Adyen Payments Fraud Check Context
  property_count: 2
  slug: adyen-payments-fraud-check-context
- class_count: 1
  name: Adyen Payments Fraud Result Context
  property_count: 2
  slug: adyen-payments-fraud-result-context
- class_count: 1
  name: Adyen Payments Fund Destination Context
  property_count: 9
  slug: adyen-payments-fund-destination-context
- class_count: 1
  name: Adyen Payments Fund Source Context
  property_count: 6
  slug: adyen-payments-fund-source-context
- class_count: 1
  name: Adyen Payments Installments Context
  property_count: 2
  slug: adyen-payments-installments-context
- class_count: 1
  name: Adyen Payments Mandate Context
  property_count: 8
  slug: adyen-payments-mandate-context
- class_count: 1
  name: Adyen Payments Merchant Device Context
  property_count: 3
  slug: adyen-payments-merchant-device-context
- class_count: 1
  name: Adyen Payments Merchant Risk Context
  property_count: 14
  slug: adyen-payments-merchant-risk-context
- class_count: 1
  name: Adyen Payments Modification Result Context
  property_count: 3
  slug: adyen-payments-modification-result-context
- class_count: 1
  name: Adyen Payments Name Context
  property_count: 2
  slug: adyen-payments-name-context
- class_count: 1
  name: Adyen Payments Payment Request Context
  property_count: 53
  slug: adyen-payments-payment-request-context
- class_count: 1
  name: Adyen Payments Payment Request3D Context
  property_count: 45
  slug: adyen-payments-payment-request3d-context
- class_count: 1
  name: Adyen Payments Payment Request3Ds2 Context
  property_count: 45
  slug: adyen-payments-payment-request3ds2-context
- class_count: 1
  name: Adyen Payments Payment Result Context
  property_count: 11
  slug: adyen-payments-payment-result-context
- class_count: 1
  name: Adyen Payments Phone Context
  property_count: 2
  slug: adyen-payments-phone-context
- class_count: 1
  name: Adyen Payments Platform Chargeback Context
  property_count: 3
  slug: adyen-payments-platform-chargeback-context
- class_count: 1
  name: Adyen Payments Recurring Context
  property_count: 5
  slug: adyen-payments-recurring-context
- class_count: 1
  name: Adyen Payments Refund Request Context
  property_count: 11
  slug: adyen-payments-refund-request-context
- class_count: 9
  name: Adyen Payments Response Additional Context
  property_count: 99
  slug: adyen-payments-response-additional-context
- class_count: 1
  name: Adyen Payments Sdk Ephem Context
  property_count: 4
  slug: adyen-payments-sdk-ephem-context
- class_count: 1
  name: Adyen Payments Shopper Interaction Context
  property_count: 3
  slug: adyen-payments-shopper-interaction-context
- class_count: 1
  name: Adyen Payments Split Amount Context
  property_count: 2
  slug: adyen-payments-split-amount-context
- class_count: 2
  name: Adyen Payments Split Context
  property_count: 4
  slug: adyen-payments-split-context
- class_count: 2
  name: Adyen Payments Sub Merchant Context
  property_count: 4
  slug: adyen-payments-sub-merchant-context
- class_count: 1
  name: Adyen Payments Technical Cancel Context
  property_count: 10
  slug: adyen-payments-technical-cancel-context
- class_count: 1
  name: Adyen Payments Three D Context
  property_count: 12
  slug: adyen-payments-three-d-context
- class_count: 2
  name: Adyen Payments Three Ds Context
  property_count: 7
  slug: adyen-payments-three-ds-context
- class_count: 1
  name: Adyen Payments Three Ds1 Context
  property_count: 6
  slug: adyen-payments-three-ds1-context
- class_count: 4
  name: Adyen Payments Three Ds2 Context
  property_count: 53
  slug: adyen-payments-three-ds2-context
- class_count: 1
  name: Adyen Payments Void Pending Context
  property_count: 11
  slug: adyen-payments-void-pending-context
- class_count: 1
  name: Adyen Payouts Address Context
  property_count: 6
  slug: adyen-payouts-address-context
- class_count: 1
  name: Adyen Payouts Amount Context
  property_count: 2
  slug: adyen-payouts-amount-context
- class_count: 1
  name: Adyen Payouts Bank Account Context
  property_count: 9
  slug: adyen-payouts-bank-account-context
- class_count: 1
  name: Adyen Payouts Card Context
  property_count: 8
  slug: adyen-payouts-card-context
- class_count: 3
  name: Adyen Payouts Fraud Check Context
  property_count: 2
  slug: adyen-payouts-fraud-check-context
- class_count: 1
  name: Adyen Payouts Fraud Result Context
  property_count: 2
  slug: adyen-payouts-fraud-result-context
- class_count: 1
  name: Adyen Payouts Fund Source Context
  property_count: 6
  slug: adyen-payouts-fund-source-context
- class_count: 1
  name: Adyen Payouts Modify Request Context
  property_count: 3
  slug: adyen-payouts-modify-request-context
- class_count: 1
  name: Adyen Payouts Modify Response Context
  property_count: 3
  slug: adyen-payouts-modify-response-context
- class_count: 1
  name: Adyen Payouts Name Context
  property_count: 2
  slug: adyen-payouts-name-context
- class_count: 1
  name: Adyen Payouts Payout Request Context
  property_count: 14
  slug: adyen-payouts-payout-request-context
- class_count: 1
  name: Adyen Payouts Payout Response Context
  property_count: 11
  slug: adyen-payouts-payout-response-context
- class_count: 1
  name: Adyen Payouts Recurring Context
  property_count: 5
  slug: adyen-payouts-recurring-context
- class_count: 9
  name: Adyen Payouts Response Additional Context
  property_count: 99
  slug: adyen-payouts-response-additional-context
- class_count: 4
  name: Adyen Payouts Store Detail Context
  property_count: 23
  slug: adyen-payouts-store-detail-context
- class_count: 1
  name: Adyen Payouts Submit Request Context
  property_count: 15
  slug: adyen-payouts-submit-request-context
- class_count: 1
  name: Adyen Payouts Submit Response Context
  property_count: 4
  slug: adyen-payouts-submit-response-context
- class_count: 1
  name: Adyen Pos Terminal Address Context
  property_count: 6
  slug: adyen-pos-terminal-address-context
- class_count: 2
  name: Adyen Pos Terminal Assign Context
  property_count: 6
  slug: adyen-pos-terminal-assign-context
- class_count: 2
  name: Adyen Pos Terminal Find Context
  property_count: 5
  slug: adyen-pos-terminal-find-context
- class_count: 6
  name: Adyen Pos Terminal Get Context
  property_count: 28
  slug: adyen-pos-terminal-get-context
- class_count: 1
  name: Adyen Pos Terminal Merchant Context
  property_count: 4
  slug: adyen-pos-terminal-merchant-context
- class_count: 2
  name: Adyen Pos Terminal Store Context
  property_count: 5
  slug: adyen-pos-terminal-store-context
- class_count: 1
  name: Adyen Recurring Address Context
  property_count: 6
  slug: adyen-recurring-address-context
- class_count: 1
  name: Adyen Recurring Amount Context
  property_count: 2
  slug: adyen-recurring-amount-context
- class_count: 1
  name: Adyen Recurring Bank Account Context
  property_count: 9
  slug: adyen-recurring-bank-account-context
- class_count: 1
  name: Adyen Recurring Card Context
  property_count: 8
  slug: adyen-recurring-card-context
- class_count: 2
  name: Adyen Recurring Create Permit Context
  property_count: 6
  slug: adyen-recurring-create-permit-context
- class_count: 2
  name: Adyen Recurring Disable Permit Context
  property_count: 4
  slug: adyen-recurring-disable-permit-context
- class_count: 1
  name: Adyen Recurring Disable Request Context
  property_count: 4
  slug: adyen-recurring-disable-request-context
- class_count: 1
  name: Adyen Recurring Disable Result Context
  property_count: 1
  slug: adyen-recurring-disable-result-context
- class_count: 1
  name: Adyen Recurring Name Context
  property_count: 2
  slug: adyen-recurring-name-context
- class_count: 2
  name: Adyen Recurring Notify Shopper Context
  property_count: 13
  slug: adyen-recurring-notify-shopper-context
- class_count: 1
  name: Adyen Recurring Permit Context
  property_count: 5
  slug: adyen-recurring-permit-context
- class_count: 1
  name: Adyen Recurring Permit Restriction Context
  property_count: 3
  slug: adyen-recurring-permit-restriction-context
- class_count: 1
  name: Adyen Recurring Permit Result Context
  property_count: 2
  slug: adyen-recurring-permit-result-context
- class_count: 1
  name: Adyen Recurring Recurring Context
  property_count: 5
  slug: adyen-recurring-recurring-context
- class_count: 3
  name: Adyen Recurring Recurring Detail Context
  property_count: 16
  slug: adyen-recurring-recurring-detail-context
- class_count: 2
  name: Adyen Recurring Recurring Details Context
  property_count: 6
  slug: adyen-recurring-recurring-details-context
- class_count: 2
  name: Adyen Recurring Schedule Account Context
  property_count: 8
  slug: adyen-recurring-schedule-account-context
- class_count: 1
  name: Adyen Recurring Token Details Context
  property_count: 2
  slug: adyen-recurring-token-details-context
- class_count: 6
  name: Adyen Report Webhooks Context
  property_count: 13
  slug: adyen-report-webhooks-context
- class_count: 1
  name: Adyen Stored Value Amount Context
  property_count: 2
  slug: adyen-stored-value-amount-context
- class_count: 12
  name: Adyen Stored Value Stored Context
  property_count: 20
  slug: adyen-stored-value-stored-context
- class_count: 1
  name: Adyen Terminal Abort Request Context
  property_count: 3
  slug: adyen-terminal-abort-request-context
- class_count: 1
  name: Adyen Terminal Account Type Context
  property_count: 0
  slug: adyen-terminal-account-type-context
- class_count: 1
  name: Adyen Terminal Admin Request Context
  property_count: 1
  slug: adyen-terminal-admin-request-context
- class_count: 1
  name: Adyen Terminal Admin Response Context
  property_count: 1
  slug: adyen-terminal-admin-response-context
- class_count: 1
  name: Adyen Terminal Alignment Context
  property_count: 0
  slug: adyen-terminal-alignment-context
- class_count: 1
  name: Adyen Terminal Allowed Product Context
  property_count: 4
  slug: adyen-terminal-allowed-product-context
- class_count: 1
  name: Adyen Terminal Amounts Req Context
  property_count: 8
  slug: adyen-terminal-amounts-req-context
- class_count: 1
  name: Adyen Terminal Amounts Resp Context
  property_count: 6
  slug: adyen-terminal-amounts-resp-context
- class_count: 1
  name: Adyen Terminal Area Size Context
  property_count: 2
  slug: adyen-terminal-area-size-context
- class_count: 1
  name: Adyen Terminal Authentication Method Context
  property_count: 0
  slug: adyen-terminal-authentication-method-context
- class_count: 2
  name: Adyen Terminal Balance Inquiry Context
  property_count: 6
  slug: adyen-terminal-balance-inquiry-context
- class_count: 1
  name: Adyen Terminal Barcode Type Context
  property_count: 0
  slug: adyen-terminal-barcode-type-context
- class_count: 1
  name: Adyen Terminal Captured Signature Context
  property_count: 2
  slug: adyen-terminal-captured-signature-context
- class_count: 3
  name: Adyen Terminal Card Acquisition Context
  property_count: 15
  slug: adyen-terminal-card-acquisition-context
- class_count: 1
  name: Adyen Terminal Card Data Context
  property_count: 11
  slug: adyen-terminal-card-data-context
- class_count: 1
  name: Adyen Terminal Card Holder Context
  property_count: 3
  slug: adyen-terminal-card-holder-context
- class_count: 2
  name: Adyen Terminal Card Reader Context
  property_count: 8
  slug: adyen-terminal-card-reader-context
- class_count: 1
  name: Adyen Terminal Cash Handling Context
  property_count: 3
  slug: adyen-terminal-cash-handling-context
- class_count: 1
  name: Adyen Terminal Character Height Context
  property_count: 0
  slug: adyen-terminal-character-height-context
- class_count: 1
  name: Adyen Terminal Character Style Context
  property_count: 0
  slug: adyen-terminal-character-style-context
- class_count: 1
  name: Adyen Terminal Character Width Context
  property_count: 0
  slug: adyen-terminal-character-width-context
- class_count: 1
  name: Adyen Terminal Check Data Context
  property_count: 7
  slug: adyen-terminal-check-data-context
- class_count: 1
  name: Adyen Terminal Coins Or Context
  property_count: 2
  slug: adyen-terminal-coins-or-context
- class_count: 1
  name: Adyen Terminal Color Context
  property_count: 0
  slug: adyen-terminal-color-context
- class_count: 1
  name: Adyen Terminal Converted Amount Context
  property_count: 2
  slug: adyen-terminal-converted-amount-context
- class_count: 1
  name: Adyen Terminal Currency Conversion Context
  property_count: 6
  slug: adyen-terminal-currency-conversion-context
- class_count: 2
  name: Adyen Terminal Customer Order Context
  property_count: 10
  slug: adyen-terminal-customer-order-context
- class_count: 1
  name: Adyen Terminal Device Context
  property_count: 0
  slug: adyen-terminal-device-context
- class_count: 1
  name: Adyen Terminal Diagnosis Request Context
  property_count: 3
  slug: adyen-terminal-diagnosis-request-context
- class_count: 1
  name: Adyen Terminal Diagnosis Response Context
  property_count: 4
  slug: adyen-terminal-diagnosis-response-context
- class_count: 1
  name: Adyen Terminal Display Output Context
  property_count: 7
  slug: adyen-terminal-display-output-context
- class_count: 1
  name: Adyen Terminal Display Request Context
  property_count: 1
  slug: adyen-terminal-display-request-context
- class_count: 1
  name: Adyen Terminal Display Response Context
  property_count: 1
  slug: adyen-terminal-display-response-context
- class_count: 1
  name: Adyen Terminal Document Qualifier Context
  property_count: 0
  slug: adyen-terminal-document-qualifier-context
- class_count: 2
  name: Adyen Terminal Enable Service Context
  property_count: 4
  slug: adyen-terminal-enable-service-context
- class_count: 1
  name: Adyen Terminal Entry Mode Context
  property_count: 0
  slug: adyen-terminal-entry-mode-context
- class_count: 1
  name: Adyen Terminal Error Condition Context
  property_count: 0
  slug: adyen-terminal-error-condition-context
- class_count: 1
  name: Adyen Terminal Event Notification Context
  property_count: 7
  slug: adyen-terminal-event-notification-context
- class_count: 1
  name: Adyen Terminal Event To Context
  property_count: 0
  slug: adyen-terminal-event-to-context
- class_count: 1
  name: Adyen Terminal Force Entry Context
  property_count: 0
  slug: adyen-terminal-force-entry-context
- class_count: 1
  name: Adyen Terminal Generic Profile Context
  property_count: 0
  slug: adyen-terminal-generic-profile-context
- class_count: 1
  name: Adyen Terminal Geographic Coordinates Context
  property_count: 2
  slug: adyen-terminal-geographic-coordinates-context
- class_count: 1
  name: Adyen Terminal Geolocation Context
  property_count: 2
  slug: adyen-terminal-geolocation-context
- class_count: 2
  name: Adyen Terminal Get Totals Context
  property_count: 5
  slug: adyen-terminal-get-totals-context
- class_count: 1
  name: Adyen Terminal Global Status Context
  property_count: 0
  slug: adyen-terminal-global-status-context
- class_count: 1
  name: Adyen Terminal Host Status Context
  property_count: 2
  slug: adyen-terminal-host-status-context
- class_count: 1
  name: Adyen Terminal Icc Reset Context
  property_count: 2
  slug: adyen-terminal-icc-reset-context
- class_count: 1
  name: Adyen Terminal Identification Support Context
  property_count: 0
  slug: adyen-terminal-identification-support-context
- class_count: 1
  name: Adyen Terminal Identification Type Context
  property_count: 0
  slug: adyen-terminal-identification-type-context
- class_count: 1
  name: Adyen Terminal Info Qualify Context
  property_count: 0
  slug: adyen-terminal-info-qualify-context
- class_count: 1
  name: Adyen Terminal Input Command Context
  property_count: 0
  slug: adyen-terminal-input-command-context
- class_count: 1
  name: Adyen Terminal Input Context
  property_count: 7
  slug: adyen-terminal-input-context
- class_count: 1
  name: Adyen Terminal Input Data Context
  property_count: 21
  slug: adyen-terminal-input-data-context
- class_count: 1
  name: Adyen Terminal Input Request Context
  property_count: 2
  slug: adyen-terminal-input-request-context
- class_count: 1
  name: Adyen Terminal Input Response Context
  property_count: 2
  slug: adyen-terminal-input-response-context
- class_count: 1
  name: Adyen Terminal Input Result Context
  property_count: 4
  slug: adyen-terminal-input-result-context
- class_count: 1
  name: Adyen Terminal Input Update Context
  property_count: 7
  slug: adyen-terminal-input-update-context
- class_count: 1
  name: Adyen Terminal Instalment Context
  property_count: 10
  slug: adyen-terminal-instalment-context
- class_count: 1
  name: Adyen Terminal Instalment Type Context
  property_count: 0
  slug: adyen-terminal-instalment-type-context
- class_count: 1
  name: Adyen Terminal Login Request Context
  property_count: 10
  slug: adyen-terminal-login-request-context
- class_count: 1
  name: Adyen Terminal Login Response Context
  property_count: 4
  slug: adyen-terminal-login-response-context
- class_count: 1
  name: Adyen Terminal Logout Request Context
  property_count: 1
  slug: adyen-terminal-logout-request-context
- class_count: 1
  name: Adyen Terminal Logout Response Context
  property_count: 1
  slug: adyen-terminal-logout-response-context
- class_count: 4
  name: Adyen Terminal Loyalty Account Context
  property_count: 9
  slug: adyen-terminal-loyalty-account-context
- class_count: 1
  name: Adyen Terminal Loyalty Acquirer Context
  property_count: 4
  slug: adyen-terminal-loyalty-acquirer-context
- class_count: 1
  name: Adyen Terminal Loyalty Amount Context
  property_count: 3
  slug: adyen-terminal-loyalty-amount-context
- class_count: 1
  name: Adyen Terminal Loyalty Data Context
  property_count: 3
  slug: adyen-terminal-loyalty-data-context
- class_count: 1
  name: Adyen Terminal Loyalty Handling Context
  property_count: 0
  slug: adyen-terminal-loyalty-handling-context
- class_count: 1
  name: Adyen Terminal Loyalty Request Context
  property_count: 3
  slug: adyen-terminal-loyalty-request-context
- class_count: 1
  name: Adyen Terminal Loyalty Response Context
  property_count: 5
  slug: adyen-terminal-loyalty-response-context
- class_count: 1
  name: Adyen Terminal Loyalty Result Context
  property_count: 5
  slug: adyen-terminal-loyalty-result-context
- class_count: 1
  name: Adyen Terminal Loyalty Totals Context
  property_count: 3
  slug: adyen-terminal-loyalty-totals-context
- class_count: 2
  name: Adyen Terminal Loyalty Transaction Context
  property_count: 5
  slug: adyen-terminal-loyalty-transaction-context
- class_count: 1
  name: Adyen Terminal Loyalty Unit Context
  property_count: 0
  slug: adyen-terminal-loyalty-unit-context
- class_count: 2
  name: Adyen Terminal Menu Entry Context
  property_count: 5
  slug: adyen-terminal-menu-entry-context
- class_count: 1
  name: Adyen Terminal Message Category Context
  property_count: 0
  slug: adyen-terminal-message-category-context
- class_count: 1
  name: Adyen Terminal Message Class Context
  property_count: 0
  slug: adyen-terminal-message-class-context
- class_count: 1
  name: Adyen Terminal Message Header Context
  property_count: 8
  slug: adyen-terminal-message-header-context
- class_count: 1
  name: Adyen Terminal Message Reference Context
  property_count: 5
  slug: adyen-terminal-message-reference-context
- class_count: 1
  name: Adyen Terminal Message Type Context
  property_count: 0
  slug: adyen-terminal-message-type-context
- class_count: 1
  name: Adyen Terminal Mobile Data Context
  property_count: 6
  slug: adyen-terminal-mobile-data-context
- class_count: 1
  name: Adyen Terminal Original Poi Context
  property_count: 9
  slug: adyen-terminal-original-poi-context
- class_count: 1
  name: Adyen Terminal Output Barcode Context
  property_count: 2
  slug: adyen-terminal-output-barcode-context
- class_count: 1
  name: Adyen Terminal Output Content Context
  property_count: 5
  slug: adyen-terminal-output-content-context
- class_count: 1
  name: Adyen Terminal Output Format Context
  property_count: 0
  slug: adyen-terminal-output-format-context
- class_count: 1
  name: Adyen Terminal Output Result Context
  property_count: 3
  slug: adyen-terminal-output-result-context
- class_count: 1
  name: Adyen Terminal Output Text Context
  property_count: 11
  slug: adyen-terminal-output-text-context
- class_count: 2
  name: Adyen Terminal Payment Account Context
  property_count: 6
  slug: adyen-terminal-payment-account-context
- class_count: 1
  name: Adyen Terminal Payment Acquirer Context
  property_count: 6
  slug: adyen-terminal-payment-acquirer-context
- class_count: 1
  name: Adyen Terminal Payment Data Context
  property_count: 7
  slug: adyen-terminal-payment-data-context
- class_count: 2
  name: Adyen Terminal Payment Instrument Context
  property_count: 5
  slug: adyen-terminal-payment-instrument-context
- class_count: 1
  name: Adyen Terminal Payment Receipt Context
  property_count: 4
  slug: adyen-terminal-payment-receipt-context
- class_count: 1
  name: Adyen Terminal Payment Request Context
  property_count: 4
  slug: adyen-terminal-payment-request-context
- class_count: 1
  name: Adyen Terminal Payment Response Context
  property_count: 7
  slug: adyen-terminal-payment-response-context
- class_count: 1
  name: Adyen Terminal Payment Result Context
  property_count: 13
  slug: adyen-terminal-payment-result-context
- class_count: 1
  name: Adyen Terminal Payment Token Context
  property_count: 3
  slug: adyen-terminal-payment-token-context
- class_count: 1
  name: Adyen Terminal Payment Totals Context
  property_count: 3
  slug: adyen-terminal-payment-totals-context
- class_count: 1
  name: Adyen Terminal Payment Transaction Context
  property_count: 4
  slug: adyen-terminal-payment-transaction-context
- class_count: 1
  name: Adyen Terminal Payment Type Context
  property_count: 0
  slug: adyen-terminal-payment-type-context
- class_count: 1
  name: Adyen Terminal Performed Transaction Context
  property_count: 6
  slug: adyen-terminal-performed-transaction-context
- class_count: 1
  name: Adyen Terminal Period Unit Context
  property_count: 0
  slug: adyen-terminal-period-unit-context
- class_count: 1
  name: Adyen Terminal Pin Format Context
  property_count: 0
  slug: adyen-terminal-pin-format-context
- class_count: 1
  name: Adyen Terminal Pin Request Context
  property_count: 0
  slug: adyen-terminal-pin-request-context
- class_count: 1
  name: Adyen Terminal Poi Capabilities Context
  property_count: 0
  slug: adyen-terminal-poi-capabilities-context
- class_count: 1
  name: Adyen Terminal Poi Data Context
  property_count: 2
  slug: adyen-terminal-poi-data-context
- class_count: 1
  name: Adyen Terminal Poi Profile Context
  property_count: 2
  slug: adyen-terminal-poi-profile-context
- class_count: 1
  name: Adyen Terminal Poi Software Context
  property_count: 4
  slug: adyen-terminal-poi-software-context
- class_count: 1
  name: Adyen Terminal Poi Status Context
  property_count: 8
  slug: adyen-terminal-poi-status-context
- class_count: 1
  name: Adyen Terminal Poi System Context
  property_count: 4
  slug: adyen-terminal-poi-system-context
- class_count: 1
  name: Adyen Terminal Poi Terminal Context
  property_count: 4
  slug: adyen-terminal-poi-terminal-context
- class_count: 1
  name: Adyen Terminal Point Context
  property_count: 2
  slug: adyen-terminal-point-context
- class_count: 1
  name: Adyen Terminal Predefined Content Context
  property_count: 2
  slug: adyen-terminal-predefined-content-context
- class_count: 1
  name: Adyen Terminal Print Output Context
  property_count: 5
  slug: adyen-terminal-print-output-context
- class_count: 1
  name: Adyen Terminal Print Request Context
  property_count: 1
  slug: adyen-terminal-print-request-context
- class_count: 1
  name: Adyen Terminal Print Response Context
  property_count: 2
  slug: adyen-terminal-print-response-context
- class_count: 1
  name: Adyen Terminal Printer Status Context
  property_count: 0
  slug: adyen-terminal-printer-status-context
- class_count: 1
  name: Adyen Terminal Rebates Context
  property_count: 3
  slug: adyen-terminal-rebates-context
- class_count: 1
  name: Adyen Terminal Reconciliation Request Context
  property_count: 3
  slug: adyen-terminal-reconciliation-request-context
- class_count: 1
  name: Adyen Terminal Reconciliation Response Context
  property_count: 4
  slug: adyen-terminal-reconciliation-response-context
- class_count: 1
  name: Adyen Terminal Reconciliation Type Context
  property_count: 0
  slug: adyen-terminal-reconciliation-type-context
- class_count: 1
  name: Adyen Terminal Repeated Message Context
  property_count: 2
  slug: adyen-terminal-repeated-message-context
- class_count: 1
  name: Adyen Terminal Repeated Response Context
  property_count: 6
  slug: adyen-terminal-repeated-response-context
- class_count: 1
  name: Adyen Terminal Response Context
  property_count: 3
  slug: adyen-terminal-response-context
- class_count: 1
  name: Adyen Terminal Response Mode Context
  property_count: 0
  slug: adyen-terminal-response-mode-context
- class_count: 1
  name: Adyen Terminal Result Context
  property_count: 0
  slug: adyen-terminal-result-context
- class_count: 1
  name: Adyen Terminal Reversal Reason Context
  property_count: 0
  slug: adyen-terminal-reversal-reason-context
- class_count: 1
  name: Adyen Terminal Reversal Request Context
  property_count: 5
  slug: adyen-terminal-reversal-request-context
- class_count: 1
  name: Adyen Terminal Reversal Response Context
  property_count: 6
  slug: adyen-terminal-reversal-response-context
- class_count: 1
  name: Adyen Terminal Sale Capabilities Context
  property_count: 0
  slug: adyen-terminal-sale-capabilities-context
- class_count: 1
  name: Adyen Terminal Sale Data Context
  property_count: 12
  slug: adyen-terminal-sale-data-context
- class_count: 2
  name: Adyen Terminal Sale Item Context
  property_count: 12
  slug: adyen-terminal-sale-item-context
- class_count: 1
  name: Adyen Terminal Sale Software Context
  property_count: 4
  slug: adyen-terminal-sale-software-context
- class_count: 1
  name: Adyen Terminal Sale Terminal Context
  property_count: 1
  slug: adyen-terminal-sale-terminal-context
- class_count: 1
  name: Adyen Terminal Sale To Context
  property_count: 1
  slug: adyen-terminal-sale-to-context
- class_count: 1
  name: Adyen Terminal Security Trailer Context
  property_count: 5
  slug: adyen-terminal-security-trailer-context
- class_count: 1
  name: Adyen Terminal Sensitive Card Context
  property_count: 4
  slug: adyen-terminal-sensitive-card-context
- class_count: 1
  name: Adyen Terminal Sensitive Mobile Context
  property_count: 3
  slug: adyen-terminal-sensitive-mobile-context
- class_count: 1
  name: Adyen Terminal Service Context
  property_count: 0
  slug: adyen-terminal-service-context
- class_count: 1
  name: Adyen Terminal Services Enabled Context
  property_count: 0
  slug: adyen-terminal-services-enabled-context
- class_count: 1
  name: Adyen Terminal Sound Action Context
  property_count: 0
  slug: adyen-terminal-sound-action-context
- class_count: 1
  name: Adyen Terminal Sound Content Context
  property_count: 4
  slug: adyen-terminal-sound-content-context
- class_count: 1
  name: Adyen Terminal Sound Format Context
  property_count: 0
  slug: adyen-terminal-sound-format-context
- class_count: 8
  name: Adyen Terminal Stored Value Context
  property_count: 18
  slug: adyen-terminal-stored-value-context
- class_count: 1
  name: Adyen Terminal Terminal Environment Context
  property_count: 0
  slug: adyen-terminal-terminal-environment-context
- class_count: 1
  name: Adyen Terminal Token Requested Context
  property_count: 0
  slug: adyen-terminal-token-requested-context
- class_count: 1
  name: Adyen Terminal Total Details Context
  property_count: 0
  slug: adyen-terminal-total-details-context
- class_count: 1
  name: Adyen Terminal Total Filter Context
  property_count: 5
  slug: adyen-terminal-total-filter-context
- class_count: 1
  name: Adyen Terminal Track Data Context
  property_count: 3
  slug: adyen-terminal-track-data-context
- class_count: 1
  name: Adyen Terminal Track Format Context
  property_count: 0
  slug: adyen-terminal-track-format-context
- class_count: 1
  name: Adyen Terminal Transaction Action Context
  property_count: 0
  slug: adyen-terminal-transaction-action-context
- class_count: 1
  name: Adyen Terminal Transaction Conditions Context
  property_count: 9
  slug: adyen-terminal-transaction-conditions-context
- class_count: 1
  name: Adyen Terminal Transaction Id Context
  property_count: 2
  slug: adyen-terminal-transaction-id-context
- class_count: 2
  name: Adyen Terminal Transaction Status Context
  property_count: 5
  slug: adyen-terminal-transaction-status-context
- class_count: 1
  name: Adyen Terminal Transaction Totals Context
  property_count: 14
  slug: adyen-terminal-transaction-totals-context
- class_count: 1
  name: Adyen Terminal Transaction Type Context
  property_count: 0
  slug: adyen-terminal-transaction-type-context
- class_count: 1
  name: Adyen Terminal Type Code Context
  property_count: 0
  slug: adyen-terminal-type-code-context
- class_count: 1
  name: Adyen Terminal Unit Of Context
  property_count: 0
  slug: adyen-terminal-unit-of-context
- class_count: 1
  name: Adyen Terminal Utm Coordinates Context
  property_count: 3
  slug: adyen-terminal-utm-coordinates-context
- class_count: 1
  name: Adyen Test Cards Avs Context
  property_count: 2
  slug: adyen-test-cards-avs-context
- class_count: 2
  name: Adyen Test Cards Create Context
  property_count: 4
  slug: adyen-test-cards-create-context
- class_count: 2
  name: Adyen Test Cards Test Context
  property_count: 14
  slug: adyen-test-cards-test-context
- class_count: 8
  name: Adyen Transaction Webhooks Context
  property_count: 17
  slug: adyen-transaction-webhooks-context
- class_count: 49
  name: Adyen Transfer Webhooks Context
  property_count: 101
  slug: adyen-transfer-webhooks-context
- class_count: 1
  name: Adyen Transfers Additional Bank Context
  property_count: 2
  slug: adyen-transfers-additional-bank-context
- class_count: 1
  name: Adyen Transfers Address Context
  property_count: 6
  slug: adyen-transfers-address-context
- class_count: 1
  name: Adyen Transfers Amount Context
  property_count: 2
  slug: adyen-transfers-amount-context
- class_count: 1
  name: Adyen Transfers Au Local Context
  property_count: 3
  slug: adyen-transfers-au-local-context
- class_count: 1
  name: Adyen Transfers Bank Account Context
  property_count: 2
  slug: adyen-transfers-bank-account-context
- class_count: 1
  name: Adyen Transfers Bank Category Context
  property_count: 2
  slug: adyen-transfers-bank-category-context
- class_count: 1
  name: Adyen Transfers Br Local Context
  property_count: 4
  slug: adyen-transfers-br-local-context
- class_count: 1
  name: Adyen Transfers Ca Local Context
  property_count: 5
  slug: adyen-transfers-ca-local-context
- class_count: 1
  name: Adyen Transfers Capital Balance Context
  property_count: 4
  slug: adyen-transfers-capital-balance-context
- class_count: 2
  name: Adyen Transfers Capital Grant Context
  property_count: 9
  slug: adyen-transfers-capital-grant-context
- class_count: 1
  name: Adyen Transfers Capital Grants Context
  property_count: 1
  slug: adyen-transfers-capital-grants-context
- class_count: 1
  name: Adyen Transfers Counterparty Context
  property_count: 3
  slug: adyen-transfers-counterparty-context
- class_count: 1
  name: Adyen Transfers Counterparty Info Context
  property_count: 3
  slug: adyen-transfers-counterparty-info-context
- class_count: 1
  name: Adyen Transfers Counterparty V3 Context
  property_count: 4
  slug: adyen-transfers-counterparty-v3-context
- class_count: 1
  name: Adyen Transfers Cz Local Context
  property_count: 3
  slug: adyen-transfers-cz-local-context
- class_count: 1
  name: Adyen Transfers Dk Local Context
  property_count: 3
  slug: adyen-transfers-dk-local-context
- class_count: 1
  name: Adyen Transfers Fee Context
  property_count: 1
  slug: adyen-transfers-fee-context
- class_count: 1
  name: Adyen Transfers Hk Local Context
  property_count: 3
  slug: adyen-transfers-hk-local-context
- class_count: 1
  name: Adyen Transfers Hu Local Context
  property_count: 2
  slug: adyen-transfers-hu-local-context
- class_count: 1
  name: Adyen Transfers Iban Account Context
  property_count: 2
  slug: adyen-transfers-iban-account-context
- class_count: 1
  name: Adyen Transfers Internal Category Context
  property_count: 3
  slug: adyen-transfers-internal-category-context
- class_count: 2
  name: Adyen Transfers Invalid Field Context
  property_count: 2
  slug: adyen-transfers-invalid-field-context
- class_count: 1
  name: Adyen Transfers Issued Card Context
  property_count: 8
  slug: adyen-transfers-issued-card-context
- class_count: 1
  name: Adyen Transfers Json Object Context
  property_count: 0
  slug: adyen-transfers-json-object-context
- class_count: 1
  name: Adyen Transfers Link Context
  property_count: 1
  slug: adyen-transfers-link-context
- class_count: 1
  name: Adyen Transfers Links Context
  property_count: 2
  slug: adyen-transfers-links-context
- class_count: 1
  name: Adyen Transfers Merchant Data Context
  property_count: 5
  slug: adyen-transfers-merchant-data-context
- class_count: 2
  name: Adyen Transfers Name Location Context
  property_count: 5
  slug: adyen-transfers-name-location-context
- class_count: 1
  name: Adyen Transfers No Local Context
  property_count: 2
  slug: adyen-transfers-no-local-context
- class_count: 1
  name: Adyen Transfers Number And Context
  property_count: 4
  slug: adyen-transfers-number-and-context
- class_count: 1
  name: Adyen Transfers Nz Local Context
  property_count: 2
  slug: adyen-transfers-nz-local-context
- class_count: 1
  name: Adyen Transfers Party Identification Context
  property_count: 7
  slug: adyen-transfers-party-identification-context
- class_count: 2
  name: Adyen Transfers Payment Instrument Context
  property_count: 3
  slug: adyen-transfers-payment-instrument-context
- class_count: 1
  name: Adyen Transfers Pl Local Context
  property_count: 2
  slug: adyen-transfers-pl-local-context
- class_count: 1
  name: Adyen Transfers Platform Payment Context
  property_count: 6
  slug: adyen-transfers-platform-payment-context
- class_count: 1
  name: Adyen Transfers Relayed Authorisation Context
  property_count: 2
  slug: adyen-transfers-relayed-authorisation-context
- class_count: 1
  name: Adyen Transfers Repayment Context
  property_count: 3
  slug: adyen-transfers-repayment-context
- class_count: 1
  name: Adyen Transfers Repayment Term Context
  property_count: 2
  slug: adyen-transfers-repayment-term-context
- class_count: 2
  name: Adyen Transfers Resource Reference Context
  property_count: 2
  slug: adyen-transfers-resource-reference-context
- class_count: 1
  name: Adyen Transfers Rest Service Context
  property_count: 9
  slug: adyen-transfers-rest-service-context
- class_count: 2
  name: Adyen Transfers Return Transfer Context
  property_count: 5
  slug: adyen-transfers-return-transfer-context
- class_count: 1
  name: Adyen Transfers Se Local Context
  property_count: 3
  slug: adyen-transfers-se-local-context
- class_count: 1
  name: Adyen Transfers Sg Local Context
  property_count: 3
  slug: adyen-transfers-sg-local-context
- class_count: 1
  name: Adyen Transfers Threshold Repayment Context
  property_count: 1
  slug: adyen-transfers-threshold-repayment-context
- class_count: 1
  name: Adyen Transfers Transaction Context
  property_count: 10
  slug: adyen-transfers-transaction-context
- class_count: 1
  name: Adyen Transfers Transaction Search Context
  property_count: 2
  slug: adyen-transfers-transaction-search-context
- class_count: 2
  name: Adyen Transfers Transfer Context
  property_count: 14
  slug: adyen-transfers-transfer-context
- class_count: 1
  name: Adyen Transfers Transfer Data Context
  property_count: 2
  slug: adyen-transfers-transfer-data-context
- class_count: 2
  name: Adyen Transfers Transfer Info Context
  property_count: 9
  slug: adyen-transfers-transfer-info-context
- class_count: 1
  name: Adyen Transfers Transfer Notification Context
  property_count: 2
  slug: adyen-transfers-transfer-notification-context
- class_count: 1
  name: Adyen Transfers Uk Local Context
  property_count: 3
  slug: adyen-transfers-uk-local-context
- class_count: 1
  name: Adyen Transfers Ultimate Party Context
  property_count: 7
  slug: adyen-transfers-ultimate-party-context
- class_count: 1
  name: Adyen Transfers Us Local Context
  property_count: 4
  slug: adyen-transfers-us-local-context
- class_count: 27
  name: Adyen Webhooks Context
  property_count: 171
  slug: adyen-webhooks-context
layout: provider
modified: '2026-04-19'
name: Adyen
rules:
- name: Adyen API Rules
  rule_count: 32
  severity_counts:
    error: 12
    hint: 0
    info: 6
    warn: 14
  slug: adyen-spectral-rules
skills: []
slug: adyen
solutions: []
tags:
- Payments
- Financial Services
- Fintech
url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/apis.yml
use_cases:
- description: Accept payments on web and mobile with Drop-in or Components, supporting all major payment methods and currencies.
  name: Online Checkout
- description: Process in-person payments using Adyen's Terminal API and supported payment terminals with tap, dip, and swipe capabilities.
  name: Point-of-Sale Payments
- description: Manage recurring payments and subscriptions using stored payment methods and tokenization.
  name: Subscription and Recurring Billing
- description: Onboard sub-merchants, split payments, and manage payouts to sellers and service providers on marketplace platforms.
  name: Marketplace and Platform Payouts
- description: Offer BNPL options including Affirm, Afterpay, and Klarna to shoppers at checkout to increase conversion.
  name: Buy Now Pay Later
- description: Issue and manage gift cards and stored value products with balance inquiry, load, and redemption capabilities.
  name: Gift Cards and Stored Value
- description: Automate dispute handling processes to respond to chargebacks with defense documents and evidence.
  name: Dispute and Chargeback Management
- description: Process subject erasure requests to comply with GDPR right-to-be-forgotten requirements for shopper data.
  name: GDPR Data Erasure
---
