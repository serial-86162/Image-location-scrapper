function initMap(){
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat:-34.9285, lng:138.6007}, //not default centre
        zoom:10 //adjusting zoom level
});

//fetching json file
//from server and creating markers for each location
fetch('C:\Users\OKI86162\Documents\Repos\Image-location-scrapper\markers.json')
    .then(response =>response.json())
    .then(data => {
        data.forEach(marker => {
            new google.maps.Marker({
                position: {lat:marker.lat, lng:marker.lon},
                map:map,
                title:marker.title
            });
        });
    });
}

