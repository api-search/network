---
aid: vtex:vtex-get-api-catalog-system-pub-facets-category-categoryid
name: VTex Get Category Facets
tags:
- Facets
humanURL: 
properties: []
description: >-
  Retrieves the names and IDs of the categories facets.  >⚠️ This endpoint returns a maximum of 50 items per response, so the difference between `_from` and `_to` should not exceed this number. The result order is descending, from the highest product ID to the lowest.  ## Response body example:  ```json [ 	[     {       "Name":"Tamanho Global",       "Id":45 		}, 		{       "Name":"Percentuals",       "Id":25 		} 	] ] ```

---
