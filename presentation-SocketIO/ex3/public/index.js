const sio = io();

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