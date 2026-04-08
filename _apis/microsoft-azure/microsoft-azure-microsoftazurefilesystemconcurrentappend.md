---
aid: microsoft-azure:microsoft-azure-microsoftazurefilesystemconcurrentappend
name: Microsoft Azure Post Webhdfsext Path
tags:
- FileSystem
humanURL: 
properties: []
description: >-
  Appends to the specified file, optionally first creating the file if it does not yet exist. This method supports multiple concurrent appends to the file. NOTE: The target must not contain data added by Create or normal (serial) Append. ConcurrentAppend and Append cannot be used interchangeably; once a target file has been modified using either of these append options, the other append option cannot be used on the target file. ConcurrentAppend does not guarantee order and can result in duplica...

---
