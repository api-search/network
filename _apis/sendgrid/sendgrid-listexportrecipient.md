---
aid: sendgrid:sendgrid-listexportrecipient
name: Get All Existing Exports
tags:
- Recipients
humanURL: 
properties: []
description: >-
  **Use this endpoint to retrieve details of all current exported jobs**.  It will return an array of objects, each of which records an export job in flight or recently completed.   Each object's `export_type` field will tell you which kind of export it is and its `status` field will indicate what stage of processing it has reached. Exports which are `ready` will be accompanied by a `urls` field which lists the URLs of the export's downloadable files — there will be more than one if you specifi...

---
