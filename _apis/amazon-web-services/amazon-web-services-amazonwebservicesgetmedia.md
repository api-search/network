---
aid: amazon-web-services:amazon-web-services-amazonwebservicesgetmedia
name: Getmedia
tags:
- API
humanURL: 
properties: []
description: >-
  Use this API to retrieve media content from a Kinesis video stream. In the request, you identify the stream name or stream Amazon Resource Name (ARN), and the starting chunk. Kinesis Video Streams then returns a stream of chunks in order by fragment number.  You must first call the GetDataEndpoint API to get an endpoint. Then send the GetMedia requests to this endpoint using the --endpoint-url parameter.   When you put media data (fragments) on a stream, Kinesis Video Streams stores each inco...

---
