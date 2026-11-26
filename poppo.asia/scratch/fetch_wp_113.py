import urllib.request
import json

url = 'https://poppo.asia/wp-json/wp/v2/pages/113'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    data = json.loads(resp.read().decode('utf-8', errors='ignore'))

content = data.get('content', {}).get('rendered', '')
print("WP rendered content length:", len(content))
with open('wp_page_113_content.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved to wp_page_113_content.html")
