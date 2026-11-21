import pathlib, glob
for f in glob.glob('*.html'):
    p = pathlib.Path(f)
    t = p.read_text()
    # Remove demo posts / demo images
    t = t.replace("New watch in Kitwe! K350", "")
    t = t.replace("Mary's Kitchen", "Your Feed")
    t = t.replace("Fresh Chicken & Chips K60 today! Order now", "Your posts will appear here after you post.")
    # Make tabs real links - remove coming soon alerts
    t = t.replace("alert('Market coming soon')", "location.href='market.html'")
    t = t.replace("alert('Watch coming soon')", "location.href='watch.html'")
    t = t.replace("alert('Food coming soon')", "location.href='food.html'")
    t = t.replace("alert('Messages coming in Step 3')", "location.href='messages.html'")
    # Clear demo posts from storage on load
    if 'zentrix_posts' in t and 'CLEAR_DEMO' not in t:
        t = t.replace('</body>', "<script>/*CLEAR_DEMO*/ if(!localStorage.getItem('zentrix_cleaned')){ localStorage.setItem('zentrix_posts','[]'); localStorage.setItem('zentrix_cleaned','1'); }</script></body>")
    p.write_text(t)
    print('Fixed', f)

# Create food.html if missing
if not pathlib.Path('food.html').exists():
    txt = pathlib.Path('market.html').read_text()
    txt = txt.replace('Market','Food')
    pathlib.Path('food.html').write_text(txt)
    print('Created food.html')
print('DONE')
