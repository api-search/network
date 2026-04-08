---
aid: vtex:vtex-productsearch
name: VTex Search for Products
tags:
- Search
humanURL: 
properties: []
description: >-
  Retrieves general information about the products related to the term searched.  This is the main search used by the store. The user can type anything to be searched.    For example, if they search for a "decanter", this is the URL: `https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pub/products/search/decanter`.   Note that maybe the response can be HTTP 200 or 206, 206 means that it's a partial content response.  If it is a 206 take a look at the Headers, will be an en...

---
