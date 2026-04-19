---
api_count: 5
apis:
- description: GitHub Issues API enables teams to create, manage, and track user stories and acceptance criteria as structured issue records with labels, milestones, and custom fields. Commonly used to attach accept
  name: GitHub Issues API
  slug: github-issues-api
- description: Jira REST API provides access to issues, user stories, epics, and acceptance criteria stored in custom fields. Teams use Jira to define, link, and track acceptance criteria against development work it
  name: Jira Issues API
  slug: jira-issues-api
- description: Azure DevOps Work Items REST API enables management of user stories, acceptance criteria, and test cases in Azure Boards. Acceptance criteria are stored as a rich text field on Product Backlog Items a
  name: Azure DevOps Work Items API
  slug: azure-devops-work-items-api
- description: Linear GraphQL API provides access to issues, projects, and cycles used by engineering teams to track features and acceptance criteria. Linear supports structured issue descriptions with Markdown, ena
  name: Linear API
  slug: linear-api
- description: TestRail REST API provides access to test cases, test runs, test plans, and results. Teams use TestRail to formally document acceptance criteria as test cases with preconditions, expected results, and
  name: TestRail API
  slug: testrail-api
capabilities:
- description: ''
  name: Requirements Management
  slug: requirements-management
common:
- title: ''
  type: Website
  url: https://www.agilealliance.org/glossary/acceptance-criteria/
- title: ''
  type: GettingStarted
  url: https://www.mountaingoatsoftware.com/blog/clarifying-the-relationship-between-definition-of-done-and-conditions-of-satisfaction
- title: ''
  type: SpectralRules
  url: rules/acceptance-criteria-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/requirements-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/acceptance-criteria-vocabulary.yaml
- title: ''
  type: OpenAPI
  url: openapi/acceptance-criteria-management.yaml
- title: ''
  type: JSONSchema
  url: json-schema/acceptance-criteria-management-user-story-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/acceptance-criteria-management-acceptance-criterion-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/acceptance-criteria-management-scenario-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/acceptance-criteria-management-test-run-schema.json
- title: ''
  type: JSONStructure
  url: json-structure/acceptance-criteria-management-user-story-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/acceptance-criteria-management-acceptance-criterion-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/acceptance-criteria-management-scenario-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/acceptance-criteria-management-test-run-structure.json
- title: ''
  type: JSON-LD
  url: json-ld/acceptance-criteria-management-context.jsonld
- title: ''
  type: Example
  url: examples/acceptance-criteria-management-user-story-example.json
- title: ''
  type: Example
  url: examples/acceptance-criteria-management-acceptance-criterion-example.json
- title: ''
  type: Example
  url: examples/acceptance-criteria-management-scenario-example.json
- title: ''
  type: Example
  url: examples/acceptance-criteria-management-test-run-example.json
created: '2025-01-01'
description: Acceptance criteria are predefined conditions that a product, feature, or user story must meet to be considered complete and acceptable by stakeholders. These criteria establish clear, testable requirements that guide development, validate when work is done, and serve as the foundation for automated testing through frameworks like Cucumber, SpecFlow, and Behave. APIs in this space support requirements management, behavior-driven development (BDD), test execution tracking, and agile project management workflows.
features:
- description: Structured Given/When/Then format for writing human-readable acceptance criteria that can be directly executed as automated tests
  name: Gherkin Syntax Support
- description: Behavior-driven development workflows connecting acceptance criteria to automated test suites via Cucumber, SpecFlow, or Behave
  name: BDD Workflow Integration
- description: Structured checklist format for breaking down complex acceptance criteria into discrete, verifiable conditions
  name: Acceptance Criteria Checklists
- description: Linking acceptance criteria to user stories, epics, test cases, and defects for end-to-end traceability
  name: Requirements Traceability
- description: Executing acceptance criteria as automated test suites that verify implementation correctness on each code change
  name: Automated Acceptance Testing
- description: Shared definition of acceptance criteria between product owners, developers, and QA engineers using accessible, plain-language formats
  name: Stakeholder Collaboration
- description: Incorporating acceptance criteria verification into team Definition of Done checklists and sprint completion gates
  name: Definition of Done Integration
- description: Tracking which acceptance criteria have passing automated tests and which remain untested or failing
  name: Test Coverage Reporting
image: /assets/icons/acceptance-criteria.png
integrations:
- description: Open-source BDD testing framework that executes Gherkin-formatted acceptance criteria as automated tests
  name: Cucumber
- description: BDD framework for .NET that maps Gherkin feature files to C# step definitions for automated acceptance testing
  name: SpecFlow
- description: Python BDD testing library that runs Gherkin acceptance criteria scenarios against Python application code
  name: Behave
- description: Project management platform with dedicated Acceptance Criteria field on user story issue types
  name: Jira
- description: Issue tracking with Markdown checklist support for embedding structured acceptance criteria on feature issues
  name: GitHub Issues
- description: Microsoft project management with Acceptance Criteria rich-text field on User Story and Product Backlog Item work items
  name: Azure DevOps Boards
- description: Test management platform for formalizing acceptance criteria as structured test cases with expected outcomes
  name: TestRail
- description: Modern issue tracker supporting Markdown acceptance criteria on issues with checklist rendering
  name: Linear
jsonld:
- class_count: 38
  name: Acceptance Criteria Management Context
  property_count: 5
  slug: acceptance-criteria-management-context
layout: provider
modified: '2026-04-19'
name: Acceptance Criteria
rules:
- name: Acceptance Criteria API Rules
  rule_count: 27
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 14
  slug: acceptance-criteria-spectral-rules
skills: []
slug: acceptance-criteria
solutions: []
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
url: https://raw.githubusercontent.com/api-evangelist/acceptance-criteria/refs/heads/main/apis.yml
use_cases:
- description: Define measurable, testable conditions that must be satisfied before a user story is accepted as complete
  name: User Story Validation
- description: Convert Gherkin-formatted acceptance criteria into executable test scenarios using Cucumber or SpecFlow
  name: Automated BDD Testing
- description: Use acceptance criteria as the basis for demonstrating completed work to stakeholders during sprint reviews
  name: Sprint Review Preparation
- description: Maintain automated acceptance test suites that run on every pull request to prevent regressions
  name: Regression Prevention
- description: Use acceptance criteria to define and verify API behavior contracts between producers and consumers
  name: API Contract Verification
- description: Communicate precise feature requirements from product managers to engineers using structured acceptance criteria templates
  name: Requirements Handoff
- description: Block deployments or story completion when acceptance criteria tests are failing in CI/CD pipelines
  name: Quality Gate Enforcement
---
