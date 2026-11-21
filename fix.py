t=open('home.html').read()
# 1. Replace the broken focus function with a popup opener
t=t.replace("function focusPost(){document.getElementById('txt').focus();window.scrollTo(0,300);}", "function focusPost(){document.getElementById('postModal').style.display='flex';document.getElementById('modalTxt').focus();}")
# 2. Add popup before </body> if not there
if 'postModal' not in t:
    modal='<div id="postModal" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:99;align-items:flex-start;justify-content:center;padding-top:60px"><div style="background:#fff;width:92%;max-width:500px;border-radius:16px;padding:16px"><h3 style="margin-bottom:10px">Create Post</h3><textarea id="modalTxt" placeholder="What\'s on your mind?" style="width:100%;height:120px;border:1px solid #ddd;border-radius:12px;padding:12px;font-size:16px;outline:none"></textarea><div style="display:flex;gap:10px;margin-top:12px"><button onclick="postFromModal()" style="flex:1;background:#00a88f;color:#fff;border:0;padding:13px;border-radius:20px;font-weight:800;font-size:16px">Post</button><button onclick="document.getElementById(\'postModal\').style.display=\'none\'" style="flex:1;background:#eee;border:0;padding:13px;border-radius:20px;font-weight:800">Cancel</button></div></div></div><script>function postFromModal(){var v=document.getElementById("modalTxt").value.trim();if(!v){alert("Type something first");return;}var p=[];try{p=JSON.parse(localStorage.getItem("zentrix_posts")||"[]")}catch(e){p=[]}p.unshift({text:v});localStorage.setItem("zentrix_posts",JSON.stringify(p));document.getElementById("modalTxt").value="";document.getElementById("postModal").style.display="none";render();window.scrollTo(0,400);}</script>'
    t=t.replace('</body>', modal+'</body>')
    open('home.html','w').write(t)
    print('post fixed')
else:
    print('already fixed')
