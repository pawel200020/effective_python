const sio = io();

// odbijanie piłeczki
sio.on('sum_result', (data) => {
    console.log(data);
});

sio.on('connect', () => {
    console.log('connected');
    sio.emit('sum', { numbers: [2, 3] }); //arg (event name, data dla servera które chcemy wysłać(JSON))
});

sio.on('disconnect', () => {
    console.log('disconnected');
})