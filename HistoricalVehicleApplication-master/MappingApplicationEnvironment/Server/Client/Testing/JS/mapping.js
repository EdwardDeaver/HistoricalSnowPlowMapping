var jsonCords;

var myMapCords = new Map();
function setupMap(){
  	bounds = new L.LatLngBounds(new L.LatLng(42.5, -76.09), new L.LatLng(43.5, -76.20));
    // Map Layer //
    map = new L.Map('content', {
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
///////////////////////////////////////////////////////////////////////////////////////////////////
// NOTE: SYNCHRONOUS REQUESTS ARE BEING DEPRECATED
//       SOMEONE WILL NEED TO CREATE an ASYNC VERSION OF THIS
////////////////////////////////////////////////////////////////////////////////////////////////////
    $.ajax({ 
    url: "Data/Cords.json", 
    dataType: 'json', 
    async: false, 
    success: function(json){ 
        jsonCords = json;
        buildMapBlocks(jsonCords);
    } 
});
}

function buildMapBlocks(jsonFile){
  console.log(jsonFile);
  for(i = 0; i< jsonFile.length; i++ ){
    createPolyLine(jsonFile[i].CITYST_ID,jsonFile[i].CORD);

  }
}
function createPolyLine(ID, Cordinates){
  var POLYLINE = new L.Polyline(Cordinates, {
        color: 'red',
        weight: 3,
        opacity: 0.5,
        smoothFactor: 1
    }).bindPopup(String(ID));
    myMapCords.set(ID,POLYLINE);
    POLYLINE.addTo(map);
    return POLYLINE;
}
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function testMapColoring(){
  var iterator1 = myMapCords.keys();
  var iterator2 = myMapCords.keys();

  console.log(iterator1);

    for(i = 0; i<myMapCords.size; i++){
      await sleep(50);
      polygon = myMapCords.get(iterator1.next().value)
      
        polygon.setStyle({
        color: 'white'});   
        //  color: "#"+String(2351+i)});
      
      
      if(i>999 && i<1999){
        polygon.setStyle({
        color: 'yellow'});   
        //  color: "#"+String(2351+i)});
        }
      
      if(i>1999 && i<1999){
        polygon.setStyle({
        color: 'blue'});   
//  color: "#"+String(2351+i)});
        
      }
            if(i>2999 && i<3999){
        polygon.setStyle({
        color: 'green'});   
//  color: "#"+String(2351+i)});
        
      }
                  if(i>3999 && i<4999){
        polygon.setStyle({
        color: 'purple'});   
//  color: "#"+String(2351+i)});
        
      }
                  if(i>4999 && i<5999){
        polygon.setStyle({
        color: 'pink'});   
//  color: "#"+String(2351+i)});
        
      }
    }
}

setupMap()
loadInitialStreetData()
console.log(jsonCords);
console.log("Map Value Key 70");
console.log(myMapCords.get(70));
testMapColoring()
    //////////////////////////////////////////
    // Load JSON of CITYID+CORDS Store those in hash map CityID: Key, Value: Leaflet polylineobject
    // Load primilimerary data
    // Load rabbitMq
    //////////////////////////////////////////