# Generates static tag listing pages from all collections.

module Jekyll
  class TagPage < Page
    def initialize(site, base, tag, items)
      @site = site
      @base = base
      @dir  = File.join('tag', Jekyll::Utils.slugify(tag))
      @name = 'index.html'

      self.process(@name)
      self.data ||= {}
      self.data['layout']           = 'default'
      self.data['title']            = "Tagged \"#{tag}\""
      self.data['meta_title']       = "Tagged \"#{tag}\" | APIs.io"
      self.data['meta_description'] = "Browse #{items.size} items tagged with \"#{tag}\" on APIs.io."
      self.data['tag']              = tag
      self.data['items']            = items
      self.content = render_listing(tag, items)
    end

    def render_listing(tag, items)
      out = String.new
      out << %Q(<nav aria-label="breadcrumb"><ol class="breadcrumb" style="font-size:0.9rem;">)
      out << %Q(<li class="breadcrumb-item"><a href="/">Home</a></li>)
      out << %Q(<li class="breadcrumb-item active">#{tag}</li></ol></nav>)
      out << %Q(<h1 style="font-size:1.75rem;">Tagged &ldquo;#{tag}&rdquo;</h1>)
      out << %Q(<p style="color:#666;">#{items.size} results</p>)
      out << %Q(<div class="list-group">)
      items.each do |item|
        name = item.data['name'] || item.data['title'] || ''
        desc = (item.data['description'] || '').to_s.gsub(/<[^>]+>/, '').strip[0, 200]
        item_type = item.collection&.label || 'item'
        type_color = case item_type
                     when 'providers' then '#6f42c1'
                     when 'apis' then '#0d6efd'
                     when 'capabilities' then '#198754'
                     when 'schemas' then '#dc3545'
                     else '#6c757d'
                     end
        type_label = item_type.chomp('s').capitalize
        out << %Q(<div class="list-group-item" style="border-left:3px solid #{type_color};">)
        out << %Q(<h6 style="margin-bottom:0.25rem;"><a href="#{item.url}" style="text-decoration:none;">#{name}</a>)
        out << %Q( <span class="badge" style="background:#{type_color};font-size:0.65rem;vertical-align:middle;">#{type_label}</span>)
        out << %Q(</h6>)
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
      tag_map = Hash.new { |h, k| h[k] = [] }

      ['providers', 'apis', 'capabilities', 'schemas'].each do |coll_name|
        coll = site.collections[coll_name]
        next unless coll
        coll.docs.each do |doc|
          (doc.data['tags'] || []).each do |tag|
            next if tag.nil? || tag.to_s.strip.empty?
            tag_map[tag.to_s] << doc
          end
        end
      end

      tag_map.each do |tag, items|
        site.pages << TagPage.new(site, site.source, tag, items)
      end
    end
  end
end
