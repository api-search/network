---
aid: storyblok:storyblok-transformimagewithfilters
name: Transform image with resize and filter chain
tags:
- Image Transformation
humanURL: 
properties: []
description: >-
  Returns the image after applying a resize operation and one or more filters. Filters are chained using colons in the filter_chain path segment. Supported filter functions include format(webp|jpeg|png|avif), quality(0-100), fill(color_hex), blur(amount), grayscale(), focal(x:y), rotate(degrees), brightness(amount), and crop(top_left_x, top_left_y, bottom_right_x, bottom_right_y). Multiple filters are separated by colons, for example filters:format(webp):quality(80).

---
