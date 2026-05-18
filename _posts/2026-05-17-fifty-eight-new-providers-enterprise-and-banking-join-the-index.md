---
date: 2026-05-17
image: /assets/images/blog/network-rebuild-may-17.png
layout: post
tags:
- Network Update
- Providers
- APIs
- Catalog Refresh
- Enterprise
- Banking
title: Fifty-Eight New Providers — Enterprise and Banking Move Into the Index
---

Today's network rebuild was substantial. Across the upstream `api-evangelist` provider mirror, **58 new providers** and **185 new APIs** landed in the catalog, while **2,638 existing provider profiles** picked up content refreshes from the same upstream pull. The running totals across the network are now **4,411 providers**, **16,219 APIs**, **2,263 capabilities**, **42,419 schemas**, **3,640 JSON-LD documents**, and **1,348 Spectral rulesets**.

The new providers cluster cleanly into four themes worth calling out — enterprise/brand, banking and finance, cloud and developer infrastructure, and a structural addition: the api-evangelist meta-collection repos themselves.

## Enterprise and Brand

The largest single category in this refresh is enterprise. Major industrial, consumer, and brand companies that had no profile in the index now have one — covering manufacturing, food and beverage, transportation, energy, and media.

- **[Airbus](https://providers.apis.io/providers/airbus/)** — Aerospace manufacturer.
- **[Bosch](https://providers.apis.io/providers/bosch/)** — Industrial and consumer electronics, IoT.
- **[Sony](https://providers.apis.io/providers/sony/)** — Consumer electronics, media, gaming.
- **[Philips](https://providers.apis.io/providers/philips/)** — Healthcare and consumer electronics.
- **[Rolls-Royce](https://providers.apis.io/providers/rolls-royce/)** — Aerospace and power systems.
- **[Lenovo](https://providers.apis.io/providers/lenovo/)** — Computing hardware.
- **[L'Oréal](https://providers.apis.io/providers/loreal/)** — Beauty and personal care.
- **[Heineken](https://providers.apis.io/providers/heineken/)** — Beverage manufacturer.
- **[Burger King](https://providers.apis.io/providers/burger-king/)**, **[Chick-fil-A](https://providers.apis.io/providers/chickfila/)**, **[Circle K](https://providers.apis.io/providers/circlek/)** — Quick-service restaurants and convenience retail.
- **[Deliveroo](https://providers.apis.io/providers/deliveroo/)** — Food delivery platform.
- **[Bunge](https://providers.apis.io/providers/bunge/)** — Agribusiness.
- **[Carnival Corporation](https://providers.apis.io/providers/carnival-corporation/)** — Cruise operator.
- **[Hapag-Lloyd](https://providers.apis.io/providers/hapag-lloyd/)** — Container shipping.
- **[Canadian National Railway](https://providers.apis.io/providers/canadian-national-railway/)** — Rail transport.
- **[T-Mobile](https://providers.apis.io/providers/t-mobile/)** — Wireless carrier.
- **[Travelport](https://providers.apis.io/providers/travelport/)** — Travel distribution.
- **[Major League Baseball](https://providers.apis.io/providers/major-league-baseball/)** — Sports league.
- **[Blizzard Entertainment](https://providers.apis.io/providers/blizzard-entertainment/)** — Game publisher.
- **[SAS](https://providers.apis.io/providers/sas/)** — Analytics platform.
- **[CMC Materials](https://providers.apis.io/providers/cmc-materials/)** — Specialty chemicals.
- **[Eventbrite](https://providers.apis.io/providers/eventbrite/)** — Event ticketing.

This is the kind of breadth that the catalog has been working toward — the API economy is no longer a tech-sector story, and the index needs to reflect that. Each of these providers has a meaningful API footprint, often spread across developer portals that were not previously indexed in a unified, machine-readable form.

## Banking and Finance

Six major global banks landed in this rebuild — a long-overdue cluster, given how much of the open-banking and PSD2 landscape runs through these institutions.

- **[HSBC](https://providers.apis.io/providers/hsbc/)** — Global banking and financial services.
- **[UBS](https://providers.apis.io/providers/ubs/)** — Swiss multinational investment bank.
- **[ING](https://providers.apis.io/providers/ing/)** — Dutch multinational bank.
- **[ABN AMRO](https://providers.apis.io/providers/abn-amro/)** — Dutch bank.
- **[Rabobank](https://providers.apis.io/providers/rabobank/)** — Dutch cooperative banking.
- **[Commonwealth Bank](https://providers.apis.io/providers/commonwealth-bank/)** — Major Australian bank.
- **[TransUnion](https://providers.apis.io/providers/transunion/)** — Credit reporting.
- **[Zurich Insurance](https://providers.apis.io/providers/zurich-insurance/)** — Global insurance.

The European bank cluster is notable. Open Banking and PSD2 obligations have produced documented developer surfaces at most of these institutions, and pulling them into the index makes those surfaces searchable alongside the rest of the financial sector. The combination with **TransUnion** and **Zurich Insurance** rounds out the financial-services slice.

## Cloud and Developer Infrastructure

A smaller but structurally important cluster — cloud platforms, packaging standards, and developer tooling.

- **[Cloud Foundry](https://providers.apis.io/providers/cloud-foundry/)** — Open-source application platform.
- **[Cloud Native Buildpacks](https://providers.apis.io/providers/cloud-native-buildpacks/)** — Container image build standard.
- **[Cloudsmith](https://providers.apis.io/providers/cloudsmith/)** — Software supply chain platform.
- **[CloudFront](https://providers.apis.io/providers/cloudfront/)** — CDN service.
- **[CloudKit](https://providers.apis.io/providers/cloudkit/)** — Apple cloud framework.
- **[Cloudwell Opal](https://providers.apis.io/providers/cloudwell-opal/)** — Cloud operations tooling.
- **[Collibra](https://providers.apis.io/providers/collibra/)** — Data governance platform.
- **[Tamr](https://providers.apis.io/providers/tamr/)** — Master data management.
- **[Gusto](https://providers.apis.io/providers/gusto/)** — Payroll and HR platform.

## Healthcare and Public Data

- **[Roche](https://providers.apis.io/providers/roche/)** — Pharmaceutical and diagnostics.
- **[Kaiser Permanente](https://providers.apis.io/providers/kaiser-permanente/)** — Integrated health system.
- **[UPMC](https://providers.apis.io/providers/upmc/)** — Health system and insurer.
- **[Clinical Trials Gov](https://providers.apis.io/providers/clinical-trials-gov/)** — Public clinical-trial registry.
- **[EcoVadis](https://providers.apis.io/providers/ecovadis/)** — Sustainability ratings.
- **[Clearview AI](https://providers.apis.io/providers/clearview-ai/)** — Facial recognition (controversial; profiled for catalog completeness).

## A Structural Addition: The api-evangelist Meta Repos

Twelve internal `api-evangelist-*` collection repos are now being profiled alongside provider repos. These represent the catalog's own underlying primitives — APIs, bases, blueprints, contracts, lifecycles, organizations, policies, rules, tools, utilities — each as a first-class provider entry that points at the canonical metadata source.

- [api-evangelist-apis](https://providers.apis.io/providers/api-evangelist-apis/), [api-evangelist-bases](https://providers.apis.io/providers/api-evangelist-bases/), [api-evangelist-blueprints](https://providers.apis.io/providers/api-evangelist-blueprints/), [api-evangelist-contracts](https://providers.apis.io/providers/api-evangelist-contracts/), [api-evangelist-lifecycles](https://providers.apis.io/providers/api-evangelist-lifecycles/), [api-evangelist-organizations](https://providers.apis.io/providers/api-evangelist-organizations/), [api-evangelist-policies](https://providers.apis.io/providers/api-evangelist-policies/), [api-evangelist-rules](https://providers.apis.io/providers/api-evangelist-rules/), [api-evangelist-tools](https://providers.apis.io/providers/api-evangelist-tools/), [api-evangelist-utilities](https://providers.apis.io/providers/api-evangelist-utilities/)

This is the self-describing layer of the catalog made first-class. Treating these meta-collections as providers (rather than implicit infrastructure) means they can be linked to, searched against, and reasoned about with the same primitives as every other entry.

## The Quiet Story: 2,638 Existing Profiles Refreshed

The new providers are the visible part of this rebuild. The larger story underneath: **2,638 existing provider profiles were updated** by the same upstream pull. Most providers in the catalog don't change in a given week, but when the upstream `api-evangelist` repos do get touched — new APIs added, descriptions refined, links updated, OpenAPI specs swapped — those changes propagate through every rebuild. Today's pull triggered an unusually broad refresh, with content updates landing across roughly 60% of the catalog. The plan, rate-limit, and FinOps profiles followed — picking up four new entries each, in line with the small subset of providers that ship those metadata files.

## What This Means for the Index

Three patterns are worth tracking from this refresh:

1. **The catalog is expanding outside the tech sector.** Aerospace, banking, retail, healthcare, shipping — each picked up meaningful representation today. The API economy is no longer a software-vendor story, and the index reflects that more fully now.
2. **European open banking is becoming searchable.** The cluster of Dutch and Swiss banks landing together is a direct consequence of PSD2 and Open Banking regulations producing documented developer surfaces. Indexing them turns those obligations into searchable, machine-readable infrastructure.
3. **The catalog's own primitives are now first-class.** The api-evangelist meta-collections being profiled as providers means the catalog can describe itself in the same shape it describes everyone else.

Every new provider in this rebuild is now live across the network — at [providers.apis.io](https://providers.apis.io), [apis.apis.io](https://apis.apis.io), [capabilities.apis.io](https://capabilities.apis.io), [schemas.apis.io](https://schemas.apis.io), and the rest of the subdomain set. The federated [api-catalog](https://apis.apis.io/.well-known/api-catalog) feed picked up all 185 new APIs in the same rebuild.

If you ship an API and we should be indexing it, the upstream lives at [api-evangelist](https://github.com/api-evangelist) — open a PR with an `apis.yml` and the next rebuild picks it up.
