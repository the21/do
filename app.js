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

    relayr.login({
        success: function(token) {
            console.log("login ok", token);

            relayr.devices().getAllDevices(function(devices) {
                console.log("getAllDevices", devices);
                
                relayr.devices().getDeviceData({
                    deviceId: "e148cfb0-9399-47bd-b9da-bda1a7ee04fc",
                    // token: "L90dUBR0cmr4BsvemQUPCGn-Q8kzMiZC",
                    incomingData: function(data) {
                        console.log("getDeviceData", data);
                    }
                });
            });


        }
    });
}