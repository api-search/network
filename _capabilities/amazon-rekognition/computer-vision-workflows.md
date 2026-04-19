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
- celebrity recognition
- manage faces in a collection
- recognize
- asynchronous label detection in stored videos
- detect faces in an image and return facial attributes including age range, emotions, and smile
- custom labels
- search a face collection for faces matching a provided image
- machine learning
- detect faces and analyze facial attributes
- detect text
- create a new face collection
- get results
- detect unsafe or explicit content in an image
- create a face liveness verification session to confirm a user is physically present
- Security Engineer
- video analysis
- detect inappropriate content
- list all face collections in the aws account
- facial recognition
- face liveness
- list
- create face collection
- aws
- detect and extract text from an image
- get video label detection results
- identity verification
- create a new face collection for storing and indexing face data
- detect objects, scenes, and concepts in an image
- detect labels
- security teams using facial recognition and liveness detection for identity verification and fraud prevention.
- search by image
- get the results of a video label detection job
- celebrity recognition in images
- content moderation
- identify celebrities in an image and return names and reference urls
- content moderation for inappropriate imagery
- compare faces
- object detection
- compare faces for identity verification
- get liveness results
- detect text in image
- computer vision
- detect custom labels in an image using a trained amazon rekognition custom labels model
- asynchronous analysis of stored and streaming video
- compare a face in a source image with a target image
- create session
- search faces by image
- amazon rekognition
- start asynchronous label detection in a video
- index faces from an image into a face collection for future searching
- developers building apps with computer vision features such as image search, face login, and text extraction.
- detect labels and objects in images
- list face collections
- synchronous analysis of images for labels, faces, text, and moderation
- search for matching faces in a collection using an image
- start video label detection
- face comparison, collection search, and liveness detection for user identity
- Content Moderator
- recognize celebrities
- start asynchronous detection of labels in a video stored in amazon s3
- get the confidence score and status from a face liveness verification session
- detect image labels
- face liveness verification for fraud prevention
- text detection
- detect and analyze facial attributes
- detect custom labels
- trust and safety teams moderating user-generated content for inappropriate or explicit imagery.
- start
- create liveness session
- search face collections for matching identities
- manage face collections
- image analysis
- Application Developer
- detect faces
- compare a face in a source image with faces in a target image for identity verification
- detect objects, scenes, and concepts in an image using amazon rekognition
- index faces into a collection
- create a face liveness verification session
- index faces in collection
- extract text from images
- moderate image content
- retrieve face liveness session results
- list all face collections
- unified computer vision, identity verification, and content moderation workflows
- create
- get the results of an asynchronous video label detection job
- detect and extract printed and handwritten text from an image
- get the results of a face liveness session
- index
- detect explicit, inappropriate, or violent content in an image for content moderation
- deep learning
- identify celebrities in an image
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
