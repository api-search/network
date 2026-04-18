---
description: A member (subscriber/contact) of a Mailchimp audience/list. Represents an individual who is currently or has been previously subscribed to a list, including members who have bounced or unsubscribed.
layout: schema
name: Mailchimp List Member
properties_list:
- description: The MD5 hash of the lowercase version of the list member's email address. This serves as the unique identifier for a member within a list.
  name: id
  type: string
- description: Email address for the subscriber.
  name: email_address
  type: string
- description: An identifier for the address across all of Mailchimp.
  name: unique_email_id
  type: string
- description: A contact identifier that is agnostic of email address. As Mailchimp evolves beyond email, contacts may exist without an email address.
  name: contact_id
  type: string
- description: The contact's full name.
  name: full_name
  type: string
- description: The ID used in the Mailchimp web application.
  name: web_id
  type: integer
- description: Type of email this member asked to get ('html' or 'text').
  name: email_type
  type: string
- description: Subscriber's current status.
  name: status
  type: string
- description: A subscriber's reason for unsubscribing.
  name: unsubscribe_reason
  type: string
- description: Indicates whether a contact consents to 1:1 messaging.
  name: consents_to_one_to_one_messaging
  type: boolean
- description: A US phone number for SMS contact.
  name: sms_phone_number
  type: string
- description: The status of an SMS subscription.
  name: sms_subscription_status
  type: string
- description: The datetime when the SMS subscription was last updated.
  name: sms_subscription_last_updated
  type: string
- description: A dictionary of merge fields where the keys are the merge tags (e.g., FNAME, LNAME). Values are the corresponding merge field values.
  name: merge_fields
  type: object
- description: The key of this object's properties is the ID of the interest in question, and the value is a boolean indicating whether the member is in that interest group.
  name: interests
  type: object
- description: Open and click rates for this subscriber.
  name: stats
  type: object
- description: IP address the subscriber signed up from.
  name: ip_signup
  type: string
- description: The date and time the subscriber signed up for the list in ISO 8601 format.
  name: timestamp_signup
  type: string
- description: The IP address the subscriber used to confirm their opt-in status.
  name: ip_opt
  type: string
- description: The date and time the subscriber confirmed their opt-in status in ISO 8601 format.
  name: timestamp_opt
  type: string
- description: Star rating for this member, between 1 and 5.
  name: member_rating
  type: integer
- description: The date and time the member's info was last changed in ISO 8601 format.
  name: last_changed
  type: string
- description: If set/detected, the subscriber's language.
  name: language
  type: string
- description: VIP status for subscriber.
  name: vip
  type: boolean
- description: The list member's email client.
  name: email_client
  type: string
- description: Subscriber location information.
  name: location
  type: object
- description: The marketing permissions for the subscriber.
  name: marketing_permissions
  type: array
- description: The most recent note added about this member.
  name: last_note
  type: object
- description: The source from which the subscriber was added to this list.
  name: source
  type: string
- description: The number of tags applied to this member.
  name: tags_count
  type: integer
- description: Tags applied to the member for additional segmentation and organization.
  name: tags
  type: array
- description: The list ID that this member belongs to.
  name: list_id
  type: string
provider_name: Mailchimp
provider_slug: mailchimp
schema_file: json-schema/member.json
slug: member
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
title: Mailchimp List Member
---
