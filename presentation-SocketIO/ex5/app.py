import socketio
import random
#user session, serwer będzie pamiętał user name dla każdej sesji, autentykacja
sio = socketio.Server() 
app = socketio.WSGIApp(sio,static_files={
    '/': './public/'
})
client_count = 0
a_count = 0
b_count = 0

#przykład callback w drugą stronę - tutaj server wywołuje event i oczekuje odpowiedzi
#zadziała niezależnie od connect event
#raczej rzadko występuje

#drugi sposób
def cb(data):
    print('this came from client: ',data)

def task(sid):
    sio.sleep(3)
    print('bg task')
    #sio.emit('mult',{'nums': [5,9]},callback=cb)
    #my coś chcemy od klienta
    result = sio.call('mult',{'nums': [5,9]},to=sid)
    print(result)


@sio.event
def connect(sid, environ): #args
    global client_count
    global a_count
    global b_count

    username = environ.get('HTTP_X_USERNAME') #zgodnie z konewncją wszyskie klucze mają tutaj HTTP_
    print('username: ',username)
    if not username:
        return False
    #pokaż z loginem i bez

    with sio.session(sid) as session: #sesja jest słownikiem, możemy dodawać wartości które mają być pamięane dla danego klient
                                    #dla każdej sesji tworzony jest osobny słownik
        session['username']=username

    #informujemy wszystkich użytkowników że nowy user się połączył
    sio.emit('user_joined', username)

    client_count+=1
    print(sid,'connected')
    sio.start_background_task(task, sid)
    #broadcast do wszystkich
    sio.emit('client_count',client_count)
    #przypisanie do pokoju
    if random.random() > 0.5:
        sio.enter_room(sid,'a')
        a_count+=1
        sio.emit('room_count',a_count,to='a') #wysłanie eventu do wszystkich klientów którzy są w danym pokoju
    else:
        sio.enter_room(sid,'b')
        b_count+=1
        sio.emit('room_count',b_count,to='b') #wysłanie eventu do wszystkich klientów którzy są w danym pokoju



@sio.event
def disconnect(sid):
    global client_count
    global a_count
    global b_count
    client_count-=1
    print(sid,'disconnect')
    #broadcast
    sio.emit('client_count',client_count)
    if 'a' in sio.rooms(sid): #zwraca wszystkie pokoje w których jest klient
        a_count-=1
        sio.emit('room_count',a_count,to='a')
    else:
        b_count-=1
        sio.emit('room_count',b_count,to='b')
    
    with sio.session(sid) as session: 
        sio.emit('user_left', session['username'])

#callbacks - gdy klient wyśle jakiś request i oczekuje że server zwróci mu coś
#klient chce od nast
@sio.event
def sum(sid,data):
    result = data['numbers'][0]+data['numbers'][1]
    print(sid," this is what was send by server and received from client: ",result)
    return result #callback
    pass
