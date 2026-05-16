---
date: 2026-05-16
image: /assets/images/blog/network-update.png
layout: post
tags:
- Network Update
- Providers
- APIs
- Catalog Refresh
title: Ten New Providers, Sixteen New APIs — Today's Network Rebuild
---

This morning's rebuild added **10 providers** and **16 APIs** to the APIs.io catalog. Running totals are now **4,353 providers** and **16,034 APIs**, with **2,254 capabilities** (+18), **42,423 schemas** (+66), **3,632 JSON-LD documents** (+11), and **1,338 Spectral rulesets** (+10) across the network of subdomain sites.

The ten new providers are concentrated in three themes worth calling out — public-records and open data, AI-agent-native developer surfaces, and privacy/ephemeral tooling — plus a couple of singletons that fill real gaps in the index.

## Public records and open data

- **[FastDOL](https://providers.apis.io/fastdol/)** — Federal workplace enforcement records on 2.3M US employers across 16 federal agencies (OSHA, WHD, MSHA, EPA ECHO, NLRB, FMCSA, OFLC, BLS SOII, SAM.gov, CMS, USAspending, CPSC, NHTSA, SEC, UVA Corporate Prosecution Registry) normalized into a single JSON API. Employer search and profile lookup, OSHA inspections and violations, WHD wage theft cases, severe injury reports, SEC enforcement, batch lookup, CSV upload, and async export jobs.
- **[OpenMercantil](https://providers.apis.io/openmercantil/)** — Independent Spanish company-intelligence API indexing the Boletin Oficial del Registro Mercantil (BORME) and cross-referencing 29+ public sources (CNMV, OEPM, PLACSP, BDNS, OpenSanctions, CCAA gazettes, CNMC, CENDOJ). Company search, structured reports, registry event timelines, officer records, CNAE sector navigation, daily BORME summaries, and a cross-source trust score.
- **[PostalCodes.info](https://providers.apis.io/postalcodes-info/)** — Postal-code lookup, country exports, and address validation for 123+ countries, anchored on GeoNames and national open-data feeds. ~1.83M postal records with 99.2% geocoding coverage on locality centroids, released under ODbL 1.0.
- **[DiscGolfAPI](https://providers.apis.io/discgolfapi/)** — Free, read-only public API publishing structured JSON disc-golf course records — names, locations, countries, regions, hole counts, coordinates, operational fields, confidence and verification signals — for apps, maps, directories, and AI systems. A small index, but exactly the niche-domain open-data the catalog should be picking up.

The FastDOL profile is the standout in this group. A unified JSON surface over OSHA, WHD, NLRB, EPA ECHO, SEC enforcement, NHTSA recalls, and the UVA Corporate Prosecution Registry is the kind of cross-agency aggregation that has historically required scraping or hand-rolling against a dozen separate portals.

## AI-agent-native developer surfaces

- **[BrewPage](https://providers.apis.io/brewpage/)** — Free, no-registration instant hosting for HTML pages, Markdown documents, AI-agent artifacts, files, and multi-file static sites. Also offers a namespaced key-value store and JSON document store. REST API returns short shareable links plus an owner token; ships with an MCP server (`brewpage-mcp`), a Claude Code skill (`brewdoc:publish`), and a `llms.txt` manifest. Designed end-to-end for agents.
- **[BuyWhere](https://providers.apis.io/buywhere/)** — Agent-native, MCP-native product catalog and price comparison covering 1.5M+ products across Shopee, Lazada, Carousell, FairPrice, Best Denki, Amazon, Walmart, Best Buy, and 20+ retailers. Hosted MCP HTTP endpoint plus a `@buywhere/mcp-server` STDIO package; responses are Schema.org-compatible (Product, Offer, ItemList).
- **[Memesio](https://providers.apis.io/memesio/)** — Meme creation and sharing service exposing template discovery, caption rendering, AI-driven image generation, face swap, background removal, video editing, billing, growth/analytics, and an MCP server. Contract-first surface for both human developers and autonomous agents.
- **[Frostbyte](https://providers.apis.io/frostbyte/)** — Free API platform bundling 40+ services — IP geolocation, crypto prices, screenshots, DNS, scraping, code execution, agent memory, wallets, DeFi trading, scheduling, and more — behind a unified agent gateway. Free tier of 200 credits with no signup; USDC-on-Base top-ups via x402 for higher volume. Seven distinct API entries in the catalog covering the individual services plus the unified gateway.

The shape of these four is the same in three different verticals (hosting, commerce, media): a REST API plus a first-class MCP server plus an explicit agent-friendly framing. Frostbyte's x402-on-Base payment surface is the more unusual signal — pay-per-call billing in stablecoin specifically targeted at autonomous agents is a pattern worth watching.

## Privacy, ephemeral, and social data

- **[Dead Drop](https://providers.apis.io/dead-drop/)** — Privacy-focused, ephemeral data-sharing API with zero-knowledge encryption. Open source under MIT, built on Cloudflare Workers, Hono, and D1. CRUD on text-only ephemeral shares with random unused drop-name generation, availability checks, and version history. Free tier: 10KB / 7-day lifespan; Deep tier: 4MB / 90-day lifespan.
- **[Sorsa](https://providers.apis.io/sorsa/)** — Real-time X (Twitter) data API, formerly Tweetscout. 40 REST endpoints covering user profiles, followers/following, tweets (single and batch), articles, timelines, comments, quotes, retweets, search, mentions, Twitter Spaces, and a Sorsa Score crypto-influence analytics layer. Positioned as an affordable alternative to the official X API.

## Why this matters for the index

Eight of the ten new providers ship an OpenAPI specification, and four of them (BrewPage, BuyWhere, Memesio, Frostbyte) ship an MCP server alongside the REST surface. That ratio — MCP-as-companion to REST — is the most consistent signal in this rebuild and tracks with the broader shift we have been documenting across the agent-skills and agent-frameworks roundups earlier this month. The agent surface is no longer being grafted onto APIs after the fact; it is being shipped on day one.

Every new provider is now live across the network — at [providers.apis.io](https://providers.apis.io) for the profile, [apis.apis.io](https://apis.apis.io) for the API records, [capabilities.apis.io](https://capabilities.apis.io) for the capability rollups, and [schemas.apis.io](https://schemas.apis.io) for the schema index. The federated [api-catalog](https://apis.apis.io/.well-known/api-catalog) feed picked up all 16 new APIs in the same rebuild.

If you ship an API and we should know about it, the upstream lives at [api-evangelist](https://github.com/api-evangelist) — open a PR with an `apis.yml` and the next rebuild picks it up.
