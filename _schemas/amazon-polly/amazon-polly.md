---
description: Schema defining the structure of Amazon Polly speech synthesis resources, including voice configurations, lexicons, and synthesis task parameters for converting text to lifelike speech.
layout: schema
name: Amazon Polly Speech Synthesis Definition
properties_list:
- description: Specifies the engine for Amazon Polly to use when processing input text.
  name: Engine
  type: string
- description: The language identification tag for the voice.
  name: LanguageCode
  type: string
- description: List of one or more pronunciation lexicon names to apply during synthesis.
  name: LexiconNames
  type: array
- description: The format in which the returned output will be encoded.
  name: OutputFormat
  type: string
- description: The audio frequency specified in Hz.
  name: SampleRate
  type: string
- description: The type of speech marks returned for the input text.
  name: SpeechMarkTypes
  type: array
- description: The input text to synthesize.
  name: Text
  type: string
- description: Specifies whether the input text is plain text or SSML.
  name: TextType
  type: string
- description: The voice ID to use for the synthesis.
  name: VoiceId
  type: string
provider_name: Amazon Polly
provider_slug: amazon-polly
schema_file: json-schema/amazon-polly-schema.json
slug: amazon-polly
tags:
- AI
- AWS
- Machine Learning
- Speech Synthesis
- Text-To-Speech
- TTS
- Voice
- SSML
- Neural Engine
- Generative AI
title: Amazon Polly Speech Synthesis Definition
---
