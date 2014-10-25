


$( document ).ready(function () {

    //var myAppId = "325c8c21-351f-4602-8476-31e4cd404d77";
    var myAppId = '6d639b4d-7e4d-4c34-a7d2-f410d119d193';
    // var myTokenId = "1c7OjkcXxT4KGoDJ9XSe-lMTcu3h8Rkb";
    var myTokenId = 'L90dUBR0cmr4BsvemQUPCGn-Q8kzMiZC'
    //var myDeviceId = "e8f026ba-0d87-499b-98eb-03a6597e6084";
    //var myDeviceId = '84f15d76-0e80-45a9-8514-835fba2dc4f7';
    var myDeviceId = '8efc3cd7-e870-495c-9537-6815982889c5';
    var myDeviceId = 'ba370b21-2205-4e32-890f-842e8604cbd2';


    var relayr = RELAYR.init({
      appId: myAppId
    });


    console.log("inited")
    relayr.devices().getDeviceData({
      token: myTokenId,
      deviceId: myDeviceId,
      incomingData: function(data){
        console.log("data from device", data)
        $(".value").text(data + " degrees")
      }
    });
});
