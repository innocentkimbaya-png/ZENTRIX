t=open('home.html').read()
# 1. Remove fake people - make others empty
t=t.replace("var others=[{n:'Chanda M.'", "var others=[]; // var others_old=[{n:'Chanda M.'")
# 2. On load, if ?clear=1, wipe the test 'Photo' post from this phone
t=t.replace("render();", "if(location.search.includes('clear=1')){localStorage.removeItem('zentrix_posts');localStorage.removeItem('zentrix_pic');}render();")
open('home.html','w').write(t)
print('fake posts removed')
