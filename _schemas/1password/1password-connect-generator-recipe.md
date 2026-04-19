---
description: Configuration for generating a random value for a field, such as password length and character types.
layout: schema
name: GeneratorRecipe
properties_list:
- description: The length of the generated value.
  name: length
  type: integer
- description: The character sets to use when generating the value.
  name: characterSets
  type: array
- description: Characters to exclude from the generated value.
  name: excludeCharacters
  type: string
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-connect-generator-recipe-schema.json
slug: 1password-connect-generator-recipe
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: GeneratorRecipe
---
