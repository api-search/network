---
description: <p>The attributes for the instance types for a mixed instances policy. Amazon EC2 Auto Scaling uses your specified requirements to identify instance types. Then, it uses your On-Demand and Spot allocation strategies to launch instances from these instance types.</p> <p>When you specify multiple attributes, you get instance types that satisfy all of the specified attributes. If you specify multiple values for an attribute, you get instance types that satisfy any of the specified values.</p> <p>To limit the list of instance types from which Amazon EC2 Auto Scaling can identify matching instance types, you can use one of the following parameters, but not both in the same request:</p> <ul> <li> <p> <code>AllowedInstanceTypes</code> - The instance types to include in the list. All other instance types are ignored, even if they match your specified attributes.</p> </li> <li> <p> <code>ExcludedInstanceTypes</code> - The instance types to exclude from the list, even if they match your
  specified attributes.</p> </li> </ul> <note> <p>You must specify <code>VCpuCount</code> and <code>MemoryMiB</code>. All other attributes are optional. Any unspecified optional attribute is set to its default.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-instance-type-requirements.html">Creating an Auto Scaling group using attribute-based instance type selection</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. For help determining which instance types match your attributes before you apply them to your Auto Scaling group, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-get-instance-types-from-instance-requirements">Preview instance types with specified attributes</a> in the <i>Amazon EC2 User Guide for Linux Instances</i>.</p>
layout: schema
name: InstanceRequirements
properties_list:
- description: ''
  name: VCpuCount
  type: object
- description: ''
  name: MemoryMiB
  type: object
- description: ''
  name: CpuManufacturers
  type: object
- description: ''
  name: MemoryGiBPerVCpu
  type: object
- description: ''
  name: ExcludedInstanceTypes
  type: object
- description: ''
  name: InstanceGenerations
  type: object
- description: ''
  name: SpotMaxPricePercentageOverLowestPrice
  type: object
- description: ''
  name: OnDemandMaxPricePercentageOverLowestPrice
  type: object
- description: ''
  name: BareMetal
  type: object
- description: ''
  name: BurstablePerformance
  type: object
- description: ''
  name: RequireHibernateSupport
  type: object
- description: ''
  name: NetworkInterfaceCount
  type: object
- description: ''
  name: LocalStorage
  type: object
- description: ''
  name: LocalStorageTypes
  type: object
- description: ''
  name: TotalLocalStorageGB
  type: object
- description: ''
  name: BaselineEbsBandwidthMbps
  type: object
- description: ''
  name: AcceleratorTypes
  type: object
- description: ''
  name: AcceleratorCount
  type: object
- description: ''
  name: AcceleratorManufacturers
  type: object
- description: ''
  name: AcceleratorNames
  type: object
- description: ''
  name: AcceleratorTotalMemoryMiB
  type: object
- description: ''
  name: NetworkBandwidthGbps
  type: object
- description: ''
  name: AllowedInstanceTypes
  type: object
provider_name: Amazon EC2 Auto Scaling
provider_slug: amazon-ec2-auto-scaling
schema_file: json-schema/ec2-auto-scaling-instance-requirements-schema.json
slug: ec2-auto-scaling-instance-requirements
tags:
- Amazon Web Services
- Auto Scaling
- AWS
- Compute
- EC2
- High Availability
- Scaling
title: InstanceRequirements
---
