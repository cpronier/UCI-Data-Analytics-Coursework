function markerSize(feature) {
  return Math.sqrt(Math.abs(feature.properties.mag)) * 7;
}

var colors = ["#6eb329", "#cfd16f", "#eede9f", "#eddb93", "#d96d0f", "#eb1313"]
function fillColor(feature) {
  var mag = feature.properties.mag;
  if (mag <= 1) {
    return colors[0]
  }
  else if (mag <= 2) {
    return colors[1]
  }
  else if (mag <= 3) {
    return colors[2]
  }
  else if (mag <= 4) {
    return colors[3]
  }
  else if (mag <= 5) {
    return colors[4]
  }
  else {
    return colors[5]
  }
}

var attribution = "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>";

var satelliteMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: attribution,
  maxZoom: 18,
  id: "mapbox.satellite",
  accessToken: API_KEY
});

var lightMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: attribution,
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
});

var outdoorsMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: attribution,
  maxZoom: 18,
  id: "mapbox.outdoors",
  accessToken: API_KEY
});

var baseMaps = {
  "Satellite": satelliteMap,
  "Grayscale": lightMap,
  "Outdoors": outdoorsMap
};

var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

var platesPath = "GeoJSON/PB2002_boundaries.json";

d3.json(queryUrl, function(data) {
    d3.json(platesPath, function(platesData) {
  
    var earthquakes = L.geoJSON(data, {

        pointToLayer: function (feature, latlng) {
          var geojsonMarkerOptions = {
            radius: 5,
            stroke: false,
            radius: markerSize(feature),
            fillColor: fillColor(feature),
            weight: 5,
            opacity: .5,
            fillOpacity: .5
          };
          return L.circleMarker(latlng, geojsonMarkerOptions);
        },
      });

    var platesStyle = {
        "color": "white",
        "weight": 1,
        "opacity": 1,
        fillOpacity: 0,
      };
      var plates = L.geoJSON(platesData, {
        style: platesStyle
      });
  
      var map = L.map("map", {
        center: [37.09, -95.71],
        zoom: 3,
        layers: [satelliteMap, plates, earthquakes]
      });
  
      L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
      }).addTo(map);
  
      var legend = L.control({ position: "bottomright" });
      legend.onAdd = function() {
        var div = L.DomUtil.create("div", "info legend");
        var limits = ["0-1", "1-2", "2-3", "3-4", "4-5", "5+"];
        var labelsColor = [];
        var labelsText = [];
        var labelsColorHtml =  "<ul>" + labelsColor.join("") + "</ul>";
        var labelsTextHtml = `<div id="labels-text">${labelsText.join("<br>")}</div>`;
  
        return div;
      };
    })
  })