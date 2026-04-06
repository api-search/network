# Generates static tag and provider listing pages from the _apis collection.
# Only runs when Jekyll is invoked with custom plugin support (e.g., local
# `bundle exec jekyll build`). On GitHub Pages this is ignored, and the
# query-string fallback pages at /tag/ and /provider/ handle the same routes.

module Jekyll
  class TagPage < Page
    def initialize(site, base, tag, apis)
      @site = site
      @base = base
      @dir  = File.join('tag', Jekyll::Utils.slugify(tag))
      @name = 'index.html'

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'tag-listing.html') rescue nil
      self.data ||= {}
      self.data['layout']           = 'default'
      self.data['title']            = "APIs tagged \"#{tag}\""
      self.data['meta_title']       = "APIs tagged \"#{tag}\" | APIs.io"
      self.data['meta_description'] = "Browse #{apis.size} APIs tagged with \"#{tag}\" on APIs.io."
      self.data['tag']              = tag
      self.data['apis']             = apis
      self.content = render_listing(tag, apis)
    end

    def render_listing(tag, apis)
      out = String.new
      out << %Q(<nav aria-label="breadcrumb"><ol class="breadcrumb" style="font-size:0.9rem;">)
      out << %Q(<li class="breadcrumb-item"><a href="/">Home</a></li>)
      out << %Q(<li class="breadcrumb-item"><a href="/tags/">Tags</a></li>)
      out << %Q(<li class="breadcrumb-item active">#{tag}</li></ol></nav>)
      out << %Q(<h1 style="font-size:1.75rem;">APIs tagged &ldquo;#{tag}&rdquo;</h1>)
      out << %Q(<p style="color:#666;">#{apis.size} APIs</p>)
      out << %Q(<div class="list-group">)
      apis.each do |api|
        name = api.data['name'] || ''
        desc = (api.data['description'] || '').to_s.gsub(/<[^>]+>/, '').strip[0, 200]
        out << %Q(<div class="list-group-item" style="border-left:3px solid #0d6efd;">)
        out << %Q(<h6 style="margin-bottom:0.25rem;"><a href="#{api.url}" style="text-decoration:none;">#{name}</a></h6>)
        out << %Q(<p style="font-size:0.85rem;color:#666;margin:0;">#{desc}</p>) unless desc.empty?
        out << %Q(</div>)
      end
      out << %Q(</div>)
      out
    end
  end

  class ProviderPage < Page
    def initialize(site, base, provider, apis)
      @site = site
      @base = base
      @dir  = File.join('provider', Jekyll::Utils.slugify(provider))
      @name = 'index.html'

      self.process(@name)
      self.data ||= {}
      self.data['layout']           = 'default'
      self.data['title']            = "#{provider} APIs"
      self.data['meta_title']       = "#{provider} APIs | APIs.io"
      self.data['meta_description'] = "Browse #{apis.size} APIs from #{provider} on APIs.io."
      self.data['provider']         = provider
      self.data['apis']             = apis
      self.content = render_listing(provider, apis)
    end

    def render_listing(provider, apis)
      out = String.new
      out << %Q(<nav aria-label="breadcrumb"><ol class="breadcrumb" style="font-size:0.9rem;">)
      out << %Q(<li class="breadcrumb-item"><a href="/">Home</a></li>)
      out << %Q(<li class="breadcrumb-item active">#{provider}</li></ol></nav>)
      out << %Q(<h1 style="font-size:1.75rem;">APIs from #{provider}</h1>)
      out << %Q(<p style="color:#666;">#{apis.size} APIs</p>)
      out << %Q(<div class="list-group">)
      apis.each do |api|
        name = api.data['name'] || ''
        desc = (api.data['description'] || '').to_s.gsub(/<[^>]+>/, '').strip[0, 200]
        out << %Q(<div class="list-group-item" style="border-left:3px solid #0d6efd;">)
        out << %Q(<h6 style="margin-bottom:0.25rem;"><a href="#{api.url}" style="text-decoration:none;">#{name}</a></h6>)
        out << %Q(<p style="font-size:0.85rem;color:#666;margin:0;">#{desc}</p>) unless desc.empty?
        out << %Q(</div>)
      end
      out << %Q(</div>)
      out
    end
  end

  class StaticListingsGenerator < Generator
    safe true
    priority :low

    def generate(site)
      apis_collection = site.collections['apis']
      return unless apis_collection

      tag_map = Hash.new { |h, k| h[k] = [] }
      provider_map = Hash.new { |h, k| h[k] = [] }

      apis_collection.docs.each do |api|
        (api.data['tags'] || []).each do |tag|
          next if tag.nil? || tag.to_s.strip.empty?
          tag_map[tag.to_s] << api
        end
        aid = api.data['aid'].to_s
        if aid.include?(':')
          provider = aid.split(':').first
          provider_map[provider] << api unless provider.nil? || provider.empty?
        end
      end

      # Pre-compute sibling lists on each api doc so layouts don't have
      # to do an O(N) scan per page render.
      provider_map.each do |provider, apis|
        api_summaries = apis.map { |a| { 'name' => a.data['name'], 'url' => a.url } }
        apis.each do |api|
          api.data['provider']        = provider
          api.data['provider_count']  = apis.size
          api.data['siblings']        = api_summaries.reject { |s| s['url'] == api.url }
        end
      end

      tag_map.each do |tag, apis|
        site.pages << TagPage.new(site, site.source, tag, apis)
      end
      provider_map.each do |provider, apis|
        site.pages << ProviderPage.new(site, site.source, provider, apis)
      end
    end
  end
end
