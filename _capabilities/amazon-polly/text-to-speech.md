---
consumed_apis:
- amazon-polly
description: Workflow capability for converting text to lifelike speech using Amazon Polly. Combines speech synthesis, voice discovery, and lexicon management for developers building voice-enabled applications.
layout: capability
name: Amazon Polly Text-to-Speech
operations:
- description: Convert text to speech audio
  method: POST
  name: synthesize-speech
  path: /v1/speech
- description: List available voices by language and engine
  method: GET
  name: list-voices
  path: /v1/voices
- description: List pronunciation lexicons
  method: GET
  name: list-lexicons
  path: /v1/lexicons
- description: Create or update a pronunciation lexicon
  method: PUT
  name: create-lexicon
  path: /v1/lexicons
- description: Start an asynchronous speech synthesis task
  method: POST
  name: start-task
  path: /v1/tasks
- description: List synthesis tasks
  method: GET
  name: list-tasks
  path: /v1/tasks
personas: []
provider_name: Amazon Polly
provider_slug: amazon-polly
search_terms:
- start an asynchronous speech synthesis task
- synthesize speech
- list available voices by language and engine
- Application Developer
- list custom pronunciation lexicons for controlling how words are spoken
- machine learning
- start an asynchronous synthesis task for long text with s3 output
- ai
- create or update a pronunciation lexicon
- start task
- list tasks
- tts
- get the content of a pronunciation lexicon
- builds voice-enabled applications using polly speech synthesis
- text-to-speech
- speech synthesis from text
- voice
- speech synthesis
- convert text to speech audio
- list pronunciation lexicons
- get lexicon
- ssml
- start synthesis task
- available synthesis voices
- voice applications
- create lexicon
- list available amazon polly voices filterable by language and engine type
- aws
- creates audio content from written text using polly
- amazon
- list voices
- Content Creator
- convert text to lifelike speech audio using amazon polly
- list and monitor asynchronous speech synthesis tasks
- multi-channel text-to-speech synthesis workflow
- custom pronunciation lexicons
- generative ai
- list lexicons
- asynchronous synthesis tasks
- list synthesis tasks
- create or update a custom pronunciation lexicon
- neural engine
slug: text-to-speech
tags:
- Amazon
- AWS
- Text-To-Speech
- Speech Synthesis
- AI
- Voice Applications
- Machine Learning
tools:
- description: Convert text to lifelike speech audio using Amazon Polly
  hints:
    destructive: false
    readOnly: false
  name: synthesize-speech
- description: List available Amazon Polly voices filterable by language and engine type
  hints:
    openWorld: true
    readOnly: true
  name: list-voices
- description: List custom pronunciation lexicons for controlling how words are spoken
  hints:
    openWorld: true
    readOnly: true
  name: list-lexicons
- description: Get the content of a pronunciation lexicon
  hints:
    openWorld: false
    readOnly: true
  name: get-lexicon
- description: Create or update a custom pronunciation lexicon
  hints:
    destructive: false
    readOnly: false
  name: create-lexicon
- description: Start an asynchronous synthesis task for long text with S3 output
  hints:
    destructive: false
    readOnly: false
  name: start-synthesis-task
- description: List and monitor asynchronous speech synthesis tasks
  hints:
    openWorld: true
    readOnly: true
  name: list-synthesis-tasks
---
