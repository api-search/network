---
consumed_apis:
- lookout-for-vision
description: Workflow capability for manufacturing and quality teams to build, train, and deploy computer vision models for automated visual quality inspection using Amazon Lookout for Vision.
layout: capability
name: Amazon Lookout for Vision - Visual Inspection Workflow
operations:
- description: Create a visual inspection project
  method: POST
  name: create-project
  path: /v1/projects
- description: List all inspection projects
  method: GET
  name: list-projects
  path: /v1/projects
- description: Train a new inspection model
  method: POST
  name: train-model
  path: /v1/projects/{id}/models
- description: List trained models
  method: GET
  name: list-models
  path: /v1/projects/{id}/models
- description: Detect visual anomalies in an image
  method: POST
  name: detect-anomalies
  path: /v1/projects/{id}/models/{modelVersion}/detect
personas: []
provider_name: Amazon Lookout for Vision
provider_slug: amazon-lookout-for-vision
search_terms:
- list inspection projects
- workflow for building and deploying computer vision models for quality inspection
- detect anomalies
- running anomaly detection on product images
- machine learning
- get model status
- train a new inspection model
- create inspection project
- visual inspection
- manufacturing
- training and lifecycle management of computer vision models
- list inspection models
- train inspection model
- list trained models
- visual inspection models
- list projects
- create a new visual quality inspection project
- run anomaly detection on images
- managing training and test datasets
- start a trained model to enable real-time inspection
- list all trained inspection models in a project
- runs inspection models on product images to detect defects in real time
- Quality Inspector
- train a computer vision model for defect detection
- train model
- check the training status and performance metrics of an inspection model
- computer vision
- aws
- builds and trains computer vision models for automated defect detection
- inspect image
- amazon
- list all inspection projects
- inspection projects
- stop inspection model
- stop a running model to reduce costs when not actively inspecting
- create a visual inspection project
- run anomaly detection on a product image to identify defects
- Manufacturing Engineer
- detect visual anomalies in an image
- list models
- start inspection model
- create project
- quality inspection
- anomaly detection
- list all visual inspection projects
slug: visual-inspection-workflow
tags:
- Amazon
- Computer Vision
- Machine Learning
- Manufacturing
- Quality Inspection
- Visual Inspection
tools:
- description: Create a new visual quality inspection project
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: create-inspection-project
- description: List all visual inspection projects
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: list-inspection-projects
- description: Train a computer vision model for defect detection
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: train-inspection-model
- description: Start a trained model to enable real-time inspection
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: start-inspection-model
- description: Run anomaly detection on a product image to identify defects
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: inspect-image
- description: Check the training status and performance metrics of an inspection model
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: get-model-status
- description: Stop a running model to reduce costs when not actively inspecting
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: stop-inspection-model
- description: List all trained inspection models in a project
  hints:
    destructive: false
    idempotent: true
    readOnly: true
  name: list-inspection-models
---
