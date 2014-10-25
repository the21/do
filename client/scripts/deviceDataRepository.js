/**
 * Created by stepa on 25.10.2014.
 */
var deviceRepository = (function () {
    var _onGetDataCallback = null;
    var _delay = null;

    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    return {
        setGetDataCallback: function (onGetDataCallback) {
            _onGetDataCallback = onGetDataCallback;
        },
        setDelay: function (delay) {
            _delay = delay;
        },

        process: function () {
            setInterval(function () {
                var currentdate = new Date();
                var datetime = currentdate.getDate() + "/"
                    + (currentdate.getMonth()+1)  + "/"
                    + currentdate.getFullYear() + " @ "
                    + currentdate.getHours() + ":"
                    + currentdate.getMinutes() + ":"
                    + currentdate.getSeconds();

                var deviceData = {
                    time: datetime,
                    data: getRandomInt(28,42)
                };
                _onGetDataCallback(deviceData);
            }, _delay);
        }
    };
})();
