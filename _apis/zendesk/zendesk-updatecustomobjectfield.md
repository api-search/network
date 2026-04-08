---
aid: zendesk:zendesk-updatecustomobjectfield
name: Zendesk Patch  Api V2 Custom_objects Custom_object_key Fields Custom_object_field_key_or_id
tags:
- Custom Object Fields
humanURL: 
properties: []
description: >-
  Updates individual custom object fields. The updating rules are as follows: * Takes a `custom_object_field` object that specifies the properties to update * The `key` property cannot be updated * If updating a standard field, only the `title`, `description`, and `properties` attributes can be updated. * The `properties` parameter is comprised of four parts and can't be changed if any records exist for the object.     * `autoincrement_enabled`: A Boolean that enables and disables autonumbering...

---
