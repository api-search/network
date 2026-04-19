---
class_count: 16
classes:
- GetSpeechSynthesisTaskOutput
- SynthesisTask
- StartSpeechSynthesisTaskInput
- SynthesizeSpeechOutput
- Voice
- LexiconAttributes
- LexiconDescription
- StartSpeechSynthesisTaskOutput
- SynthesizeSpeechInput
- ListLexiconsOutput
- GetLexiconOutput
- Lexicon
- Amazon Polly Speech Synthesis Definition
- PutLexiconInput
- ListSpeechSynthesisTasksOutput
- DescribeVoicesOutput
context_file: json-ld/amazon-polly-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-polly/refs/heads/main/json-ld/amazon-polly-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Polly from Amazon Polly.
layout: jsonld
name: Amazon Polly Context
namespaces:
- prefix: polly
  uri: https://polly.amazonaws.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Engine
  type: string
- container: ''
  name: LanguageCode
  type: string
- container: ''
  name: LexiconNames
  type: string
- container: ''
  name: OutputFormat
  type: string
- container: ''
  name: OutputS3BucketName
  type: string
- container: ''
  name: OutputS3KeyPrefix
  type: string
- container: ''
  name: SampleRate
  type: string
- container: ''
  name: SnsTopicArn
  type: string
- container: ''
  name: SpeechMarkTypes
  type: string
- container: ''
  name: Text
  type: string
- container: ''
  name: TextType
  type: string
- container: ''
  name: VoiceId
  type: string
- container: ''
  name: AudioStream
  type: string
- container: ''
  name: Gender
  type: string
- container: ''
  name: Id
  type: string
- container: ''
  name: LanguageName
  type: string
- container: ''
  name: Name
  type: string
- container: ''
  name: AdditionalLanguageCodes
  type: string
- container: ''
  name: SupportedEngines
  type: string
- container: ''
  name: Alphabet
  type: string
- container: ''
  name: LastModified
  type: string
- container: ''
  name: LexiconArn
  type: string
- container: ''
  name: LexemesCount
  type: string
- container: ''
  name: Size
  type: string
- container: ''
  name: Attributes
  type: string
- container: ''
  name: TaskId
  type: string
- container: ''
  name: TaskStatus
  type: string
- container: ''
  name: TaskStatusReason
  type: string
- container: ''
  name: OutputUri
  type: string
- container: ''
  name: CreationTime
  type: string
- container: ''
  name: RequestCharacters
  type: string
- container: ''
  name: Lexicons
  type: string
- container: ''
  name: NextToken
  type: string
- container: ''
  name: Content
  type: string
- container: ''
  name: SynthesisTasks
  type: string
- container: ''
  name: Voices
  type: string
property_count: 36
provider_name: Amazon Polly
provider_slug: amazon-polly
slug: amazon-polly-context
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
- JSON-LD
- Linked Data
- Semantic Web
---
