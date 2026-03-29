---
aid: atlassian:atlassian-atlassianlistopenbranches
name: List Open Branches
tags:
- Refs
humanURL: 
properties: []
description: >-
  Returns a list of all open branches within the specified repository.<br>Results will be in the order the source control manager returns them.<br><br>Branches support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering)<br>that can be used to search for specific branches. For instance, to find<br>all branches that have "stab" in their name:<br><br>```<br>curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches -G --data-urlencode 'q=name ~ "stab"'<br>```<br><br...

---
