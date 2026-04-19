---
description: Schema representing an Amazon Transcribe transcription job resource.
layout: schema
name: Amazon Transcribe Transcription Job
properties_list:
- description: The name of the transcription job.
  name: TranscriptionJobName
  type: string
- description: The status of the transcription job.
  name: TranscriptionJobStatus
  type: string
- description: The language code for the input audio.
  name: LanguageCode
  type: string
- description: The sample rate of the input audio in Hz.
  name: MediaSampleRateHertz
  type: integer
- description: The format of the input media file.
  name: MediaFormat
  type: string
- description: The location of the input media file.
  name: Media
  type: object
- description: The location of the transcription output.
  name: Transcript
  type: object
- description: Optional settings for the transcription job.
  name: Settings
  type: object
- description: A timestamp indicating when the job was created.
  name: CreationTime
  type: string
- description: A timestamp indicating when the job started processing.
  name: StartTime
  type: string
- description: A timestamp indicating when the job was completed.
  name: CompletionTime
  type: string
- description: The reason the job failed, if applicable.
  name: FailureReason
  type: string
- description: A list of tags associated with the transcription job.
  name: Tags
  type: array
provider_name: Amazon Transcribe
provider_slug: amazon-transcribe
schema_file: json-schema/amazon-transcribe-job-schema.json
slug: amazon-transcribe-job
tags:
- Audio Processing
- AWS
- Machine Learning
- Speech Recognition
- Speech-To-Text
- Transcription
title: Amazon Transcribe Transcription Job
---
