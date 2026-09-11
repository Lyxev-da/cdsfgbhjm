from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Browser Sandbox</title>
  <style>
    :root { color-scheme: dark; }
    * { box-sizing: border-box; }
    body, html { margin: 0; height: 100%; font-family: -apple-system, system-ui, sans-serif;
      background: #0f1115; color: #e6e6e6; }
    #bar {
      display: flex; gap: 8px; padding: 10px; background: #161a22; border-bottom: 1px solid #2a2f3a;
      position: sticky; top: 0; z-index: 10;
    }
    #url { flex: 1; padding: 9px 12px; border-radius: 8px; border: 1px solid #2a2f3a;
      background: #0f1115; color: #e6e6e6; font-size: 14px; outline: none; }
    #url:focus { border-color: #4b8bff; }
    button { padding: 9px 16px; border-radius: 8px; border: none; cursor: pointer;
      background: #4b8bff; color: #fff; font-size: 14px; font-weight: 600; }
    button:hover { background: #3a78f0; }
    iframe { width: 100%; height: calc(100vh - 60px); border: none; background: #fff; }
    #note { text-align: center; padding: 30px 16px; color: #7a8294; font-size: 13px; line-height: 1.6; }
  </style>
</head>
<body>
  <form id="bar" onsubmit="go(); return false;">
    <input id="url" type="text" placeholder="Enter a URL (e.g. https://example.com)"
      value="{{ url }}" autocomplete="off">
    <button type="submit">Go</button>
  </form>
  <iframe id="frame" src="{{ src }}" title="Sandboxed browser"></iframe>
  <div id="note" style="display:none">Some sites block embedding via headers and won't load here.</div>
  <script>
    function go() {
      let u = document.getElementById('url').value.trim();
      if (!u) return;
      if (!/^https?:\\/\\//.test(u)) u = 'https://' + u;
      document.getElementById('frame').src = u;
    }
    const f = document.getElementById('frame');
    f.addEventListener('load', function () {
      try { f.contentWindow.location.href; } catch (e) {
        document.getElementById('note').style.display = 'block';
      }
    });
  </script>
</body>
</html>
"""

@app.get("/")
def index():
    url = request.args.get("url", "https://3kh0.github.io").strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return render_template_string(PAGE, url=url, src=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
