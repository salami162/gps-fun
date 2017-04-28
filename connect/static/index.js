// config mapbox gl access token
mapboxgl.accessToken = "pk.eyJ1IjoidGVrbm9sb2ciLCJhIjoiSThJdmhyRSJ9.zq2xC8EwFXLPixOdVza98A";


var map = new mapboxgl.Map({
    container: "map", // container id
    style: "mapbox://styles/mapbox/streets-v9", //stylesheet location
    center: [-122.4351, 37.7612], // starting position, center of SF
    zoom: 12 // starting zoom
});

var animateHandler;

function drawPointsLayer(mapSourceId, paintProperties) {
    map.addSource(mapSourceId, {
        "type": "geojson",
        "data": {
            "type": "FeatureCollection",
            "features": []
        }
    });

    map.addLayer({
        "id": mapSourceId,
        "type": "circle",
        "paint": paintProperties,
        "source": mapSourceId
    });
}

function renderPoints(sourceUrl, mapSourceId) {
    $.ajax ({
        url: sourceUrl, // <--- returns valid json if accessed in the browser
        type: "GET",
        dataType: "json",
        cache: false,
        contentType: "application/json",
        success: function(respData) {
            map.getSource(mapSourceId).setData(respData);
            console.log(sourceUrl + ": success");

        },
        error: function(respData) {
            alert(mapSourceId + ": Somthing is wrong, please check your console!");
            clearTimeout();
            console.log(respData);
        }
    });
}

function renderTrainedPoints() {

    renderPoints("http://localhost:5000/v1/trained", "trained_points");

    // Request the next frame of the animation.
    animateHandler = setTimeout(function() {
        requestAnimationFrame(renderTrainedPoints);
    }, 1500);
}

// on map load, add "raw_points" and "trained_points" layers.
map.on("load", function () {
    drawPointsLayer("raw_points", {
        "circle-radius": 8,
        "circle-color": "#007cbf"
    });

    drawPointsLayer("trained_points", {
        "circle-radius": 8,
        "circle-color": "#FF0000"
    });

    renderPoints("http://localhost:5000/v1/raw", "raw_points");
});


// add toggles
var toggleableLayerIds = ["start"];

for (var i = 0; i < toggleableLayerIds.length; i++) {
    var id = toggleableLayerIds[i];

    var link = document.createElement("a");
    link.href = "#";
    link.textContent = id;

    link.onclick = function (e) {
        var currentState = this.textContent;
        e.preventDefault();
        e.stopPropagation();

        if (currentState === "start") {
            this.className = "active";
            this.textContent = "stop";
            // Start the animation.
            animateHandler = setTimeout(function () { renderTrainedPoints(); }, 1500);
        } else {
            this.className = "";
            this.textContent = "start";
            // Stop the animation.
            clearTimeout(animateHandler);
        }
    };

    var layers = document.getElementById("menu");
    layers.appendChild(link);
}


