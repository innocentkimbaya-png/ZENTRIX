t=open('home.html').read()
if 'zentrix-menu' not in t:
    menu='<div class="zentrix-menu" style="background:#fff;padding:12px;border-radius:12px;margin:10px 0;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;text-align:center"><a href="watch.html" style="text-decoration:none;color:#000">▶️<br>Watch</a><a href="market.html" style="text-decoration:none;color:#000">🛍️<br>Market</a><a href="food.html" style="text-decoration:none;color:#000">🍔<br>Food</a><a href="messages.html" style="text-decoration:none;color:#000">💬<br>Messages</a><a href="suppliers.html" style="text-decoration:none;color:#000">🏭<br>Suppliers</a><a href="ticket.html" style="text-decoration:none;color:#000">🎟️<br>Ticket</a></div>'
    t=t.replace("<div id='feed'>", menu+"<div id='feed'>")
    open('home.html','w').write(t)
    print('menu added')
else:
    print('already linked')
