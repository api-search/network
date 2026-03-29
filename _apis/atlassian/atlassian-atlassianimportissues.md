---
aid: atlassian:atlassian-atlassianimportissues
name: Import Issues
tags:
- Issue tracker
humanURL: 
properties: []
description: >-
  A POST request to this endpoint will import the zip file given by the archive parameter into the repository. All<br>existing issues will be deleted and replaced by the contents of the imported zip file.<br><br>Imports are done through a multipart/form-data POST. There is one valid and required form field, with the name<br>"archive," which needs to be a file field:<br><br>```<br>$ curl -u  -X POST -F archive=@/path/to/file.zip https://api.bitbucket.org/2.0/repositories///issues/import<br>```

---
