import pathlib, glob, shutil

# 1. Make index.html = home.html (so opening / goes straight to Home)
if pathlib.Path('home.html').exists():
    shutil.copy('home.html', 'index.html')
    print('index.html now = Home - NO LOGIN')

# 2. Remove any code that sends you back to login
for f in glob.glob('*.html'):
    p = pathlib.Path(f)
    t = p.read_text()
    # If home checks "please login first" - remove it
    t = t.replace("if(!user){alert('Please login first');return;}", "if(!user){user={name:'Guest',phone:'',pic:''};}")
    t = t.replace("if(!user){alert('Please login first.');return;}", "if(!user){user={name:'Guest',phone:'',pic:''};}")
    t = t.replace("location.href='login.html'", "location.href='index.html'")
    t = t.replace('location.href="login.html"', 'location.href="index.html"')
    t = t.replace("location.href = 'login.html'", "location.href = 'index.html'")
    p.write_text(t)
    print('Cleaned', f)

# 3. Delete login files
for f in ['login.html', 'login_backup.html']:
    try:
        pathlib.Path(f).unlink()
        print('Deleted', f)
    except:
        print('No', f)

print('DONE - LOGIN REMOVED')
