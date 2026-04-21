---
consumed_apis:
- rekognition
description: Unified computer vision workflows combining image analysis, facial recognition, content moderation, and identity verification capabilities for developers and security teams.
layout: capability
name: Amazon Rekognition Computer Vision Workflows
operations:
- description: Detect objects, scenes, and concepts in an image
  method: POST
  name: detect-labels
  path: /v1/analyze/labels
- description: Detect faces and analyze facial attributes
  method: POST
  name: detect-faces
  path: /v1/analyze/faces
- description: Detect and extract text from an image
  method: POST
  name: detect-text
  path: /v1/analyze/text
- description: Detect unsafe or explicit content in an image
  method: POST
  name: detect-inappropriate-content
  path: /v1/moderation/labels
- description: Compare a face in a source image with a target image
  method: POST
  name: compare-faces
  path: /v1/identity/compare
- description: Search for matching faces in a collection using an image
  method: POST
  name: search-by-image
  path: /v1/identity/search
- description: Create a face liveness verification session
  method: POST
  name: create-session
  path: /v1/liveness/sessions
- description: Get the results of a face liveness session
  method: GET
  name: get-results
  path: /v1/liveness/sessions/{session_id}/results
- description: Identify celebrities in an image
  method: POST
  name: recognize
  path: /v1/celebrities
- description: List all face collections
  method: GET
  name: list
  path: /v1/collections
- description: Create a new face collection
  method: POST
  name: create
  path: /v1/collections
- description: Index faces into a collection
  method: POST
  name: index
  path: /v1/collections/{collection_id}/faces
- description: Start asynchronous label detection in a video
  method: POST
  name: start
  path: /v1/videos/labels
- description: Get the results of a video label detection job
  method: GET
  name: get-results
  path: /v1/videos/labels/{job_id}
personas: []
provider_name: Amazon Rekognition
provider_slug: amazon-rekognition
search_terms:
- facial recognition
- search for matching faces in a collection using an image
- compare a face in a source image with faces in a target image for identity verification
- unified computer vision, identity verification, and content moderation workflows
- detect text in image
- security teams using facial recognition and liveness detection for identity verification and fraud prevention.
- compare faces for identity verification
- create session
- start asynchronous detection of labels in a video stored in amazon s3
- developers building apps with computer vision features such as image search, face login, and text extraction.
- create face collection
- create
- identify celebrities in an image and return names and reference urls
- get the results of a video label detection job
- get results
- detect inappropriate content
- identify celebrities in an image
- compare faces
- image analysis
- aws
- recognize
- celebrity recognition in images
- face liveness verification for fraud prevention
- create a new face collection
- retrieve face liveness session results
- asynchronous analysis of stored and streaming video
- recognize celebrities
- detect faces
- list all face collections in the aws account
- Application Developer
- Security Engineer
- content moderation
- search faces by image
- trust and safety teams moderating user-generated content for inappropriate or explicit imagery.
- synchronous analysis of images for labels, faces, text, and moderation
- index faces in collection
- face liveness
- detect labels
- detect and extract printed and handwritten text from an image
- detect faces and analyze facial attributes
- start asynchronous label detection in a video
- create liveness session
- identity verification
- get the confidence score and status from a face liveness verification session
- start
- list all face collections
- detect and extract text from an image
- detect image labels
- detect custom labels in an image using a trained amazon rekognition custom labels model
- detect faces in an image and return facial attributes including age range, emotions, and smile
- custom labels
- celebrity recognition
- detect objects, scenes, and concepts in an image
- list
- content moderation for inappropriate imagery
- search a face collection for faces matching a provided image
- start video label detection
- detect labels and objects in images
- search by image
- asynchronous label detection in stored videos
- text detection
- moderate image content
- face comparison, collection search, and liveness detection for user identity
- amazon rekognition
- machine learning
- get the results of an asynchronous video label detection job
- manage faces in a collection
- detect and analyze facial attributes
- detect objects, scenes, and concepts in an image using amazon rekognition
- detect explicit, inappropriate, or violent content in an image for content moderation
- index
- index faces from an image into a face collection for future searching
- detect text
- Content Moderator
- search face collections for matching identities
- object detection
- get the results of a face liveness session
- get liveness results
- create a face liveness verification session to confirm a user is physically present
- extract text from images
- computer vision
- create a new face collection for storing and indexing face data
- create a face liveness verification session
- compare a face in a source image with a target image
- detect custom labels
- list face collections
- index faces into a collection
- detect unsafe or explicit content in an image
- video analysis
- manage face collections
- get video label detection results
- deep learning
slug: computer-vision-workflows
tags:
- Amazon Rekognition
- Computer Vision
- Identity Verification
- Content Moderation
- Facial Recognition
tools:
- description: Detect objects, scenes, and concepts in an image using Amazon Rekognition
  hints:
    openWorld: true
    readOnly: true
  name: detect-image-labels
- description: Detect faces in an image and return facial attributes including age range, emotions, and smile
  hints:
    openWorld: true
    readOnly: true
  name: detect-faces
- description: Compare a face in a source image with faces in a target image for identity verification
  hints:
    openWorld: true
    readOnly: true
  name: compare-faces
- description: Detect and extract printed and handwritten text from an image
  hints:
    openWorld: true
    readOnly: true
  name: detect-text-in-image
- description: Detect explicit, inappropriate, or violent content in an image for content moderation
  hints:
    openWorld: true
    readOnly: true
  name: moderate-image-content
- description: Identify celebrities in an image and return names and reference URLs
  hints:
    openWorld: true
    readOnly: true
  name: recognize-celebrities
- description: Detect custom labels in an image using a trained Amazon Rekognition Custom Labels model
  hints:
    openWorld: true
    readOnly: true
  name: detect-custom-labels
- description: Create a new face collection for storing and indexing face data
  hints:
    openWorld: false
    readOnly: false
  name: create-face-collection
- description: List all face collections in the AWS account
  hints:
    openWorld: false
    readOnly: true
  name: list-face-collections
- description: Index faces from an image into a face collection for future searching
  hints:
    openWorld: false
    readOnly: false
  name: index-faces-in-collection
- description: Search a face collection for faces matching a provided image
  hints:
    openWorld: false
    readOnly: true
  name: search-faces-by-image
- description: Create a face liveness verification session to confirm a user is physically present
  hints:
    openWorld: false
    readOnly: false
  name: create-liveness-session
- description: Get the confidence score and status from a face liveness verification session
  hints:
    openWorld: false
    readOnly: true
  name: get-liveness-results
- description: Start asynchronous detection of labels in a video stored in Amazon S3
  hints:
    openWorld: false
    readOnly: false
  name: start-video-label-detection
- description: Get the results of an asynchronous video label detection job
  hints:
    openWorld: false
    readOnly: true
  name: get-video-label-detection-results
---
