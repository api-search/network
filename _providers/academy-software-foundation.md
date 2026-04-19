---
api_count: 11
apis:
- description: OpenEXR is an open standard high-dynamic-range (HDR) image file format specification and reference implementation developed by Industrial Light and Magic. It is the industry standard for visual effect
  name: OpenEXR
  slug: openexr
- description: OpenVDB is an Academy Award-winning open source C++ library for efficient storage and manipulation of sparse volumetric data discretized on three-dimensional grids. It is the industry standard for vol
  name: OpenVDB
  slug: openvdb
- description: OpenColorIO (OCIO) is a complete color management solution geared towards motion picture production, enabling color transforms and image display to be handled in a consistent manner across many applic
  name: OpenColorIO
  slug: opencolorio
- description: OpenTimelineIO (OTIO) is an open source API and interchange format for editorial timeline information. It is designed to be more expressive than existing formats while still being easy to read and wri
  name: OpenTimelineIO
  slug: opentimelineio
- description: 'Open Shading Language (OSL) is a small but rich language for programmable shading in advanced renderers and other applications. It is ideal for describing materials, lights, displacement, and pattern '
  name: Open Shading Language
  slug: openshadinglanguage
- description: MaterialX is an open standard for the exchange of rich material and look-development content between applications and renderers. It provides a language for defining surface and volume shading patterns
  name: MaterialX
  slug: materialx
- description: OpenCue is an open source render management system for visual effects and animation productions. It enables studios to deploy and manage a render farm, schedule jobs, and track progress across large n
  name: OpenCue
  slug: opencue
- description: OpenImageIO (OIIO) is a library for reading, writing, and processing images in a wide variety of file formats. It is used in visual effects and animation production pipelines for texture baking, image
  name: OpenImageIO
  slug: openimagedio
- description: OpenFX is an open standard API for visual effects plug-ins used in compositing and image processing applications. It defines how host applications and image processing plug-ins communicate, enabling i
  name: OpenFX
  slug: openfx
- description: OpenAPV is an open, royalty-free video codec specification designed for professional video production and post-production workflows. It is optimized for high-quality intermediate video formats used in
  name: OpenAPV
  slug: openapv
- description: OpenPBR is an open specification and reference implementation for a physically-based shading model. It defines a standard material definition language that can be used across different renderers to ac
  name: OpenPBR
  slug: openpbr
capabilities:
- description: 'Render farm management workflow using OpenCue for monitoring and managing render jobs, layers, frames, and hosts in a VFX production pipeline. Used by render wranglers and pipeline TDs to monitor and '
  name: Academy Software Foundation Render Farm Management
  slug: render-farm-management
common:
- title: ''
  type: Website
  url: https://www.aswf.io/
- title: ''
  type: Documentation
  url: https://www.aswf.io/projects/
- title: ''
  type: GitHubOrganization
  url: https://github.com/AcademySoftwareFoundation
- title: ''
  type: Blog
  url: https://www.aswf.io/news/
- title: ''
  type: GettingStarted
  url: https://www.aswf.io/get-involved/
- title: ''
  type: TermsOfService
  url: https://www.aswf.io/terms/
- title: ''
  type: PrivacyPolicy
  url: https://www.aswf.io/privacy/
- title: ''
  type: SpectralRules
  url: rules/academy-software-foundation-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/render-farm-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/academy-software-foundation-vocabulary.yaml
created: '2026-03-16'
description: The Academy Software Foundation (ASWF) is a Linux Foundation project that supports open source software development for the motion picture, visual effects, and animation industries. ASWF hosts a portfolio of production-proven open source projects including OpenEXR, OpenVDB, OpenColorIO, OpenTimelineIO, OpenShadingLanguage, MaterialX, and more. These projects form the backbone of modern film and media production pipelines worldwide.
features:
- description: All ASWF projects are governed by open, transparent processes under the Linux Foundation umbrella
  name: Open Source Governance
- description: Projects like OpenEXR, OpenVDB, and OpenColorIO are used in major film studios worldwide
  name: Production-Proven Projects
- description: ASWF provides a neutral forum where studios, vendors, and developers collaborate on shared technology challenges
  name: Vendor-Neutral Collaboration
- description: ASWF provides shared containerized build and test infrastructure via aswf-docker for consistent CI/CD across all projects
  name: CI/CD Infrastructure
- description: Dedicated working groups address cross-project topics such as CI, color interop, and language interoperability
  name: Working Groups
- description: ASWF projects define and maintain industry standards used across the global VFX and animation pipeline
  name: Standards Development
image: /assets/icons/academy-software-foundation.png
integrations:
- description: Integrates with OpenColorIO, OpenEXR, and other ASWF standards via native plug-ins
  name: Autodesk Maya
- description: Uses OpenColorIO, OpenEXR, and OpenFX plug-ins extensively in compositing workflows
  name: The Foundry Nuke
- description: Deep integration with OpenVDB, OpenColorIO, and OpenEXR for VFX and simulation workflows
  name: SideFX Houdini
- description: Uses OpenEXR, OpenColorIO, OpenShadingLanguage, and OpenVDB for rendering and compositing
  name: Blender
- description: Works alongside ASWF standards as part of the broader VFX open source ecosystem
  name: Pixar USD
- description: Uses MaterialX and OpenColorIO for material interchange and color management
  name: NVIDIA Omniverse
jsonld:
- class_count: 5
  name: Academy Software Foundation Opencue Context
  property_count: 22
  slug: academy-software-foundation-opencue-context
layout: provider
modified: '2026-04-19'
name: Academy Software Foundation
rules:
- name: Academy Software Foundation API Rules
  rule_count: 21
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 5
  slug: academy-software-foundation-spectral-rules
skills: []
slug: academy-software-foundation
solutions: []
tags:
- Animation
- Color Management
- Film
- Linux Foundation
- Open Source
- Rendering
- Standards
- Visual Effects
- VFX
url: https://raw.githubusercontent.com/api-evangelist/academy-software-foundation/refs/heads/main/apis.yml
use_cases:
- description: OpenEXR, OpenVDB, OpenColorIO, and OSL form the core of visual effects production pipelines at major studios
  name: VFX Production Pipeline
- description: OpenCue enables studios to build and operate large-scale distributed render farms for animation and VFX
  name: Render Farm Management
- description: OpenColorIO provides consistent color transforms across all DCC tools in a studio pipeline
  name: Color Pipeline Standardization
- description: OpenTimelineIO enables timeline data exchange between editing applications like Avid, Premiere, and DaVinci Resolve
  name: Editorial Interchange
- description: MaterialX and OpenPBR enable look development assets to be transferred between different render engines
  name: Material Interchange
- description: OpenEXR provides a universal HDR image format for compositing, rendering output, and archiving
  name: Image Format Standardization
---
