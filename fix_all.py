import pathlib, glob

nav = """<script>
var M={home:'index.html',messages:'messages.html',msg:'messages.html',watch:'watch.html',market:'market.html',shop:'market.html',food:'food.html',tickets:'ticket.html',ticket:'ticket.html',suppliers:'suppliers.html'};
document.addEventListener('click',function(e){
 var t=e.target.closest('a,button,div,span');
 if(!t) return;
 var txt=t.textContent.trim().toLowerCase();
 for(var k in M){ if(txt===k){ e.preventDefault(); e.stopPropagation(); location.href=M[k]; return; } }
},true);
window.alert=function(m){ if(String(m).includes('coming soon')) return; };
</script>"""

phone = """<script>
document.addEventListener('click',function(e){
 var b=e.target.closest('button');
 if(!b) return;
 if(!b.textContent.includes('LOG IN')) return;
 var ins=document.querySelectorAll('input');
 var ph=null;
 for(var i=0;i<ins.length;i++){ if((ins[i].placeholder||'').toLowerCase().includes('phone')) ph=ins[i]; }
 if(!ph) ph=ins[1];
 var v=(ph?ph.value:'').replace(/[^0-9]/g,'');
 var pre=v.slice(0,3);
 var ok=['075','076','077','078','079','091','095','096','097','098','060'].includes(pre) && v.length==10;
 if(!ok){ e.preventDefault(); e.stopPropagation(); alert('Fake number blocked! Use real Zambian number. MTN: 076,077,096 Airtel: 097,078,079,075 Zamtel: 095,091'); }
},true);
</script>"""

for f in glob.glob('*.html'):
    p = pathlib.Path(f)
    t = p.read_text()
    changed = False
    if 'var M=' not in t:
        t = t.replace('</body>', nav + '</body>')
        changed = True
    if f == 'login.html' and 'Fake number blocked' not in t:
        t = t.replace('</body>', phone + '</body>')
        changed = True
    if changed:
        p.write_text(t)
        print('Fixed', f)
print('DONE - ALL FIXED')
