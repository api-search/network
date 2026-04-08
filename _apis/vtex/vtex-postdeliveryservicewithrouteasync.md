---
aid: vtex:vtex-postdeliveryservicewithrouteasync
name: VTex Post Delivery Service With Route Scheduling
tags:
- Delivery Services
humanURL: 
properties: []
description: >-
  This endpoint creates a delivery service in your Tracking system. It allows the user to configure the Route Scheduling services with the Delivery Person and Route date already defined.   ### Request body example  ```json [ 	{ 		"deliveryServiceRoute": { 			"deliveryServiceDate": "2020-09-28", 			"displacementType": "Caminhão", 			"carrier": { 				"username": "empresa-joao.silva" 			}, 			"vehicle": { 				"registrationPlate": "XPT-0123" 			}, 			"addressStart": { 				"addressS...

---
