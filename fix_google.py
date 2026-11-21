import pathlib
p = pathlib.Path('login.html')
t = p.read_text()

google_html = """
<div style="display:flex;flex-direction:column;gap:12px;margin-bottom:18px">
<button id="googleBtn" style="background:#fff;color:#111;border:1px solid #ddd;padding:14px;border-radius:12px;font-weight:700;font-size:16px;cursor:pointer">Continue with Google</button>
<button id="appleBtn" style="background:#000;color:#fff;border:1px solid #000;padding:14px;border-radius:12px;font-weight:700;font-size:16px;cursor:pointer">Continue with Apple</button>
<div style="text-align:center;color:#888;font-size:13px">or continue with phone</div>
</div>
<script>
document.getElementById('googleBtn').onclick = function(){
  var name = prompt('Google Demo Login\\nEnter your Google name:');
  if(!name) return;
  localStorage.setItem('zentrix_user', name);
  localStorage.setItem('zentrix_login', 'google');
  alert('Welcome back, ' + name + '! Google login successful.');
  location.href = 'index.html';
};
document.getElementById('appleBtn').onclick = function(){
  var name = prompt('Apple Demo Login\\nEnter your Apple name:');
  if(!name) return;
  localStorage.setItem('zentrix_user', name);
  localStorage.setItem('zentrix_login', 'apple');
  alert('Welcome back, ' + name + '! Apple login successful.');
  location.href = 'index.html';
};
</script>
"""

if 'googleBtn' not in t:
    # Put buttons right before LOG IN button, or at top of form
    if 'LOG IN TO ZENTRIX' in t:
        t = t.replace('LOG IN TO ZENTRIX', google_html + 'LOG IN TO ZENTRIX')
    else:
        t = t.replace('</body>', google_html + '</body>')
    p.write_text(t)
    print('GOOGLE + APPLE ADDED')
else:
    print('ALREADY ADDED')
