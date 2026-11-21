t=open('home.html').read()
# If not logged in, go to login page
if 'zentrix_logged_in' not in t:
    t=t.replace("if(location.search.includes('clear=1'))", "if(!localStorage.getItem('zentrix_logged_in') && !location.search.includes('clear=1')){location.href='login.html'}if(location.search.includes('clear=1'))")
    open('home.html','w').write(t)
    print('home now needs login')
else:
    print('already')
