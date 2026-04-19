---
api_count: 1
apis:
- description: API for managing Application Load Balancers (ALB), Network Load Balancers (NLB), and Gateway Load Balancers (GLB) with advanced routing and target group management.
  name: Elastic Load Balancing v2 API
  slug: ''
capabilities:
- description: Unified capability for managing Amazon Elastic Load Balancing resources. Combines Amazon Elastic Load Balancing APIs for Cloud Architect workflows in Network Traffic Management.
  name: Amazon Elastic Load Balancing Management
  slug: amazon-elastic-load-balancing-capability
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/elasticloadbalancing/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/elasticloadbalancing/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/ec2/home#LoadBalancers/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/elasticloadbalancing/faqs/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: Security
  url: https://aws.amazon.com/security/
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/elasticloadbalancing
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-elastic-load-balancing-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-elastic-load-balancing-capability.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/api.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-elastic-load-balancing-vocabulary.yaml
created: '2024-01-15'
description: Amazon Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions, ensuring high availability and fault tolerance for your applications.
features:
- description: HTTP/HTTPS load balancing with advanced request routing based on content
  name: Application Load Balancer
- description: Ultra-high performance TCP/UDP load balancing at OSI layer 4
  name: Network Load Balancer
- description: Distribute traffic to third-party virtual appliances for inspection
  name: Gateway Load Balancer
- description: Automatically route traffic away from unhealthy targets
  name: Health Checks
- description: Offload SSL/TLS decryption from application servers
  name: SSL/TLS Termination
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Distribute traffic across EC2 instances
  name: Amazon EC2
- description: Load balance traffic to containerized applications
  name: Amazon ECS
- description: Route HTTP requests directly to Lambda functions
  name: AWS Lambda
- description: Integrate with DNS for global traffic routing
  name: Amazon Route 53
- description: Protect applications from web exploits and bots
  name: AWS WAF
jsonld:
- class_count: 0
  name: Amazon Elastic Load Balancing Context
  property_count: 6
  slug: amazon-elastic-load-balancing-context
layout: provider
modified: '2026-04-19'
name: Amazon Elastic Load Balancing
rules:
- name: Amazon Elastic Load Balancing API Rules
  rule_count: 20
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 9
  slug: amazon-elastic-load-balancing-spectral-rules
skills: []
slug: amazon-elastic-load-balancing
solutions: []
tags:
- Amazon Web Services
- AWS
- High Availability
- Load Balancing
- Networking
- Scalability
url: https://aws.amazon.com/elasticloadbalancing/
use_cases:
- description: Distribute HTTP/HTTPS traffic across multiple web servers
  name: Web Application Load Balancing
- description: Route requests to different microservices based on URL paths or headers
  name: Microservices Routing
- description: Load balance traffic to ECS containers and Kubernetes pods
  name: Container Load Balancing
- description: Distribute global traffic across multiple AWS regions
  name: Multi-Region Traffic Management
---
