const sio = io({
    transportOptions: {
        polling: {
            extraHeaders: {
                'X-Username': window.location.hash.substring(1)
            }
        }
    } //dodanie custom headera
    //uwaga socket io nie wspiera tego, najpierw jest stawiane poly connection a potem dopiero websocket bo jego protokoły nie pozwalają na extra headers
});

sio.on('connect_error', (e) => {
    console.log(e.message)
})

//my chcemy coś od servera
sio.on('connect', () => {
    console.log('connected');
    sio.emit('sum', { numbers: [2, 3] }, (result) => {
        console.log(result);
    }); //jeśli sio ma 3 argument to chce uzyskać response od servera
});

//server coś chce od nas
sio.on('mult', (data, cb) => {
    const result = data.nums[0] * data.nums[1];
    console.log(result);
    cb(result);
})

sio.on('disconnect', () => {
    console.log('disconnected');
})

//broadcast function
sio.on('client_count', (count) => {
    console.log(count + " connected clients")
})

//room function
sio.on('room_count', (count) => {
    console.log(count + " connected clients in room")
})

sio.on('user_joined', (username) => {
    console.log(username + " has joined to the server")
})


sio.on('user_left', (username) => {
    console.log(username + " has left the server")
})