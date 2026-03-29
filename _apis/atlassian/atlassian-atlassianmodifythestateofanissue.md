---
aid: atlassian:atlassian-atlassianmodifythestateofanissue
name: Modify The State Of An Issue
tags:
- Issue tracker
humanURL: 
properties: []
description: >-
  Makes a change to the specified issue.<br><br>For example, to change an issue's state and assignee, create a new<br>change object that modifies these fields:<br><br>```<br>curl https://api.bitbucket.org/2.0/site/master/issues/1234/changes \<br>  -s -u evzijst -X POST -H "Content-Type: application/json" \<br>  -d '{<br>    "changes": {<br>      "assignee_account_id": {<br>        "new": "557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443"<br>      },<br>      "state": {<br>        "new": 'resolved"<b...

---
