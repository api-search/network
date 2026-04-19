---
description: Schema for the manifest.json file required by Chrome browser extensions using Manifest V3. The manifest defines extension metadata, permissions, background service workers, content scripts, UI elements, and API access. Manifest V3 is the current standard for Chrome extensions, replacing Manifest V2 with improved security, performance, and privacy. See https://developer.chrome.com/docs/extensions/reference/manifest for the complete reference.
layout: schema
name: Chrome Extension Manifest (Manifest V3)
properties_list:
- description: Manifest file format version. Must be 3 for Manifest V3 extensions. Manifest V2 is deprecated and will be removed from Chrome.
  name: manifest_version
  type: integer
- description: Name of the extension displayed in the Chrome Web Store, browser toolbar, and chrome://extensions. Maximum 45 characters.
  name: name
  type: string
- description: Extension version string. One to four dot-separated integers (e.g., 1.0.0.0). Each integer must be between 0 and 65535. Used for auto-update version comparison.
  name: version
  type: string
- description: Plain text description of the extension. Maximum 132 characters. Displayed in the Chrome Web Store and chrome://extensions.
  name: description
  type: string
- description: Default locale for internationalization (e.g., en). Required if the extension uses the _locales directory. Specifies the subdirectory of _locales that contains the default strings.
  name: default_locale
  type: string
- description: Extension icons at various sizes. Used in the Chrome Web Store, toolbar, extension management page, and other contexts. Recommended sizes are 16, 32, 48, and 128 pixels. PNG format recommended; SVG is
  name: icons
  type: object
- description: Configures the extension's toolbar icon behavior and appearance. Replaces browser_action and page_action from Manifest V2. Controls the icon, tooltip, badge, and popup displayed when the user clicks t
  name: action
  type: object
- description: Specifies the extension's background service worker. In Manifest V3, background pages are replaced by service workers that run on-demand and are terminated when idle, improving performance and resourc
  name: background
  type: object
- description: Scripts and CSS that are injected into web pages matching specified URL patterns. Content scripts run in an isolated world with access to the page DOM but a separate JavaScript namespace. They can com
  name: content_scripts
  type: array
- description: 'API permissions the extension requires. These are granted at install time and displayed to the user as permission warnings. Common permissions: activeTab, alarms, bookmarks, contextMenus, cookies, deb'
  name: permissions
  type: array
- description: API permissions that can be requested at runtime using chrome.permissions.request(). Users can grant or deny these after installation, providing a more gradual permission model.
  name: optional_permissions
  type: array
- description: URL match patterns granting the extension access to specific hosts. Separated from permissions in MV3 for better granularity. Users can choose to grant these on specific sites rather than all at once.
  name: host_permissions
  type: array
- description: Host permission patterns that can be requested at runtime using chrome.permissions.request().
  name: optional_host_permissions
  type: array
- description: Content Security Policy overrides for extension pages. MV3 restricts CSP more strictly than MV2 and does not allow remotely hosted code.
  name: content_security_policy
  type: object
- description: Resources within the extension that can be accessed by web pages or other extensions. In MV3, access is restricted by specifying which origins or extensions can access each resource set.
  name: web_accessible_resources
  type: array
- description: Path to the extension's options page HTML file. Opens in a new tab. Use options_ui instead for an embedded options experience.
  name: options_page
  type: string
- description: Configuration for the extension's embedded options page, displayed within chrome://extensions.
  name: options_ui
  type: object
- description: Configuration for the extension's side panel, displayed in Chrome's sidebar alongside the current page. Requires the sidePanel permission.
  name: side_panel
  type: object
- description: Path to an HTML page that adds functionality to Chrome DevTools. The page can use chrome.devtools.* APIs to create panels, interact with the inspected window, and access network information.
  name: devtools_page
  type: string
- description: Overrides for Chrome's built-in pages. Only one page can be overridden per extension.
  name: chrome_url_overrides
  type: object
- description: Registers a keyword for the Chrome address bar (omnibox). When the user types the keyword and presses Tab, the extension receives omnibox input and can provide suggestions.
  name: omnibox
  type: object
- description: Keyboard shortcuts for extension actions. Each command has a unique name and an optional default keyboard shortcut. The _execute_action command triggers the extension's action (toolbar icon click).
  name: commands
  type: object
- description: Configuration for the Declarative Net Request API, which enables blocking or modifying network requests using declarative rules without intercepting request content. Replaces the blocking webRequest A
  name: declarative_net_request
  type: object
- description: Specifies which web pages and other extensions can connect to this extension using chrome.runtime.connect() and chrome.runtime.sendMessage().
  name: externally_connectable
  type: object
- description: Configuration for the chrome.storage.managed API, which allows enterprise administrators to set extension configuration via policy.
  name: storage
  type: object
- description: Configuration for the chrome.identity API OAuth2 flow. Enables the extension to obtain OAuth tokens for Google APIs or other services.
  name: oauth2
  type: object
- description: Public key for the extension, used to ensure a consistent extension ID during development. This is the base64-encoded value from the .pem file generated when the extension is first packed.
  name: key
  type: string
- description: 'Minimum Chrome browser version required to install the extension. If the user''s Chrome version is older, the extension will not be installable. Format: major.minor.build.patch (e.g., 120.0.0.0).'
  name: minimum_chrome_version
  type: string
- description: 'How the extension behaves in incognito mode. spanning (default): a single instance handles both normal and incognito. split: separate instances for normal and incognito. not_allowed: extension is disa'
  name: incognito
  type: string
- description: Short name for the extension, used where space is limited. Maximum 12 characters. Falls back to name if not specified.
  name: short_name
  type: string
- description: Human-readable version string for display purposes (e.g., '1.0 beta'). Not used for update comparison.
  name: version_name
  type: string
- description: The extension author information.
  name: author
  type: object
- description: URL to the extension's homepage or documentation site.
  name: homepage_url
  type: string
- description: URL to the extension's update manifest XML file. Used for self-hosted extensions that update outside the Chrome Web Store.
  name: update_url
  type: string
- description: Declares shared modules that other extensions can import.
  name: export
  type: object
- description: Shared modules to import from other extensions.
  name: import
  type: array
- description: Defines pages that run in a sandboxed environment with a relaxed CSP. Sandboxed pages cannot use Chrome extension APIs but can use eval() and other normally restricted features.
  name: sandbox
  type: object
- description: Whether the extension works offline. If true, the extension appears in the list of offline-enabled apps.
  name: offline_enabled
  type: boolean
- description: Cross-Origin Embedder Policy for extension pages.
  name: cross_origin_embedder_policy
  type: object
- description: Cross-Origin Opener Policy for extension pages.
  name: cross_origin_opener_policy
  type: object
- description: Configuration for text-to-speech engine extensions. Registers the extension as a TTS engine that can synthesize speech.
  name: tts_engine
  type: object
provider_name: Google Chrome
provider_slug: google-chrome
schema_file: json-schema/google-chrome-extension-manifest-schema.json
slug: google-chrome-extension-manifest
tags:
- Browser
- Chrome Extensions
- Developer Tools
- Web Platform
title: Chrome Extension Manifest (Manifest V3)
---
