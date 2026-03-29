---
aid: amazon-web-services:amazon-web-services-amazonwebservicessubmitjob
name: Submitjob
tags:
- API
humanURL: 
properties: []
description: >-
  Submits an Batch job from a job definition. Parameters that are specified during SubmitJob override parameters defined in the job definition. vCPU and memory requirements that are specified in the resourceRequirements objects in the job definition are the exception. They can't be overridden this way using the memory and vcpus parameters. Rather, you must specify updates to job definition parameters in a resourceRequirements object that's included in the containerOverrides parameter.  Job queu...

---
