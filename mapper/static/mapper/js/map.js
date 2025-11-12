var map = L.map('map').setView([-33.9249, 18.4241], 12);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

L.icon({
    iconUrl: '/static/mapper/img/icons/bus-stop.svg',
    iconSize: [32, 32]  // still define size for consistency
});

