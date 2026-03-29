---
aid: fluentd:fluentd-posteventwithformat
name: Post a log event with explicit format
tags:
- Events
humanURL: 
properties: []
description: >-
  Posts a single log event to Fluentd with both a tag and an explicit format specifier in the path. The format segment can be 'json' or 'msgpack' and overrides Content-Type-based format detection. This is useful for clients that cannot set Content-Type headers correctly.

---
