function setupMap(){
	bounds = new L.LatLngBounds(new L.LatLng(42.5, -76.09), new L.LatLng(43.5, -76.20));
// Map Layer //
var map = new L.Map('content', {
  center: [43.05,-76.13],
  zoom: 13,
	minZoom: 13,
  maxBounds: bounds
});
// Add Map Layer //
 layer = L.esri.basemapLayer('DarkGray');
 map.addLayer(layer);
 layer = L.esri.basemapLayer('DarkGrayLabels');
 map.addLayer(layer);
}
function loadInitialStreetData(){
	/////////////////
	// Load JSON File with 
}
setupMap()

    //////////////////////////////////////////
    // Load JSON of CITYID+CORDS Store those in hash map CityID: Key, Value: Leaflet polylineobject
    // Load primilimerary data
    // Load rabbitMq
    //////////////////////////////////////////