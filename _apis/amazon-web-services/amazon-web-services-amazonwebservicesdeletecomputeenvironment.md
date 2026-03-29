---
aid: amazon-web-services:amazon-web-services-amazonwebservicesdeletecomputeenvironment
name: Deletecomputeenvironment
tags:
- API
humanURL: 
properties: []
description: >-
  Deletes an Batch compute environment. Before you can delete a compute environment, you must set its state to DISABLED with the UpdateComputeEnvironment API operation and disassociate it from any job queues with the UpdateJobQueue API operation. Compute environments that use Fargate resources must terminate all active jobs on that compute environment before deleting the compute environment. If this isn't done, the compute environment enters an invalid state.

---
