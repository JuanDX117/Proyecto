let map;
let markers = [];

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 0, lng: 0 },
        zoom: 2
    });
}

document.getElementById('upload-button').addEventListener('click', () => {
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            clearMarkers();
            data.forEach(point => {
                const position = { lat: point.lat, lng: point.lon };
                const marker = new google.maps.Marker({
                    position: position,
                    map: map,
                });
                markers.push(marker);
                map.setCenter(position); 
            });
        }
    })
    .catch(error => console.error('Error:', error));
});

function clearMarkers() {
    markers.forEach(marker => marker.setMap(null));
    markers = [];
}
