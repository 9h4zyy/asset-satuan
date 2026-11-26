import urllib.request
import re

css_urls = [
    'https://poppo.asia/wp-content/themes/astra/assets/css/minified/main.min.css?ver=4.14.0',
    'https://poppo.asia/wp-content/plugins/elementor/assets/css/frontend.min.css?ver=4.1.1',
    'https://poppo.asia/wp-content/uploads/elementor/css/post-113.css?ver=1793852762',
    'https://poppo.asia/wp-content/uploads/elementor/css/post-5.css?ver=1793742578',
    'https://poppo.asia/wp-content/uploads/elementor/css/post-3960.css?ver=1793817160'
]

for url in css_urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        css = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        print(f"=== {url.split('/')[-1]} (len {len(css)}) ===")
        # Check text-fill-color or gradient or span color
        for m in re.finditer(r'[^{}]*(?:text-fill-color|background-clip|h1\s+span|h2\s+span|entry-content)[^{}]*\{[^{}]*\}', css):
            print("  ", m.group(0)[:120])
    except Exception as e:
        print(f"Error {url}: {e}")
