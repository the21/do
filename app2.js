window.onload = function() {
if(document.getElementById("canvas"))
{

    var randomScalingFactor = function(){ return 34+Math.round(Math.random()*3)};

    var barChartData = {
        labels : ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        datasets : [
            {
                fillColor : "rgba(220,220,220,0.5)",
                strokeColor : "rgba(220,220,220,0.8)",
                highlightFill: "rgba(220,220,220,0.75)",
                highlightStroke: "rgba(220,220,220,1)",
                data : [randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]
            },
        ]

    }
    var ctx = document.getElementById("canvas").getContext("2d");
        window.myBar = new Chart(ctx).Bar(barChartData, {
            responsive : true
        });
}





    var R_APP_ID = "6d639b4d-7e4d-4c34-a7d2-f410d119d193"
    var R_OAUTH_S = "4_EL2H.lsyznY0jOIcaYWOk7Dp4A4ag."
    var R_TOKEN = "L90dUBR0cmr4BsvemQUPCGn-Q8kzMiZC"
    var R_REDIRECT = "http://localhost:8080";
    var LIGHT = "ba370b21-2205-4e32-890f-842e8604cbd2"
    var TEMP = "199209ec-ff32-472c-b904-cc0d527a30ab"
    var SOUND = "077cbc8c-eece-4b6e-9bd6-fcb74ce13a27"
    console.log("here we are");


    var relayr = RELAYR.init({
        appId: R_APP_ID,
        redirectUri: R_REDIRECT
    });

    

    relayr.devices().getDeviceData({
                    deviceId: TEMP,
                    token: R_TOKEN,
                    incomingData: function(data) {
                        console.log("getDeviceData", data);
                        var val = data.temp;
                        var max = 43;
                        var pr = 100*val/max;
                        
                        var alertv = 37;
                        if($("#temp"))
                        {
                        // var pralert = 100*alert/max;
                        $("#temp").css("width", pr+"%");
                        // $("#temp-alert").css("width", pralert+"%");
                        // $("#temp").text(val);

                        if (val > alertv)
                        {
                          alert("Temperature is too high, please call a doctor");
                        }
                        }
                        // var clr = data.clr;
                    //     var color = $( ".colored" ).css( "background-color", "rgb("+0+","+clr.g+","+clr.b+")" );
                    }
                });
}