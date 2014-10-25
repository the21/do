window.onload = function() {
    var R_APP_ID = "6d639b4d-7e4d-4c34-a7d2-f410d119d193"
    var R_OAUTH_S = "4_EL2H.lsyznY0jOIcaYWOk7Dp4A4ag."
    var R_TOKEN = "L90dUBR0cmr4BsvemQUPCGn-Q8kzMiZC"
    var R_REDIRECT = "http://localhost:8080";
    console.log("here we are");

    var relayr = RELAYR.init({
        appId: R_APP_ID,
        redirectUri: R_REDIRECT
    });

    relayr.devices().getDeviceData({
                    deviceId: "ba370b21-2205-4e32-890f-842e8604cbd2",
                    token: R_TOKEN,
                    incomingData: function(data) {
                        console.log("getDeviceData", data);
                        var clr = data.clr;
                        var color = $( ".colored" ).css( "background-color", "rgb("+0+","+clr.g+","+clr.b+")" );
                    }
                });
    
    // relayr.login({
    //     success: function(token) {
    //         console.log("login ok", token);

    //         relayr.devices().getAllDevices(function(devices) {
    //             console.log("getAllDevices", devices);
                
                
    //         });


    //     }
    // });
}