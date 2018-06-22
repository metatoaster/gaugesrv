var $ = require('jquery');
var Gauge = require('gaugeJS').Gauge;


$.fn.gaugesrv = function() {
    this.each(function() {
        var $this = $(this),
            data = $this.data();

        if (data.gauge) {
            delete data.gauge;
        }
        if (data.gaugesrvOpts !== false) {
            data.gauge = new Gauge(this).setOptions(data.gaugesrvOpts);
            data.gauge.minValue = data.gaugeMin || data.gauge.minValue;
            data.gauge.maxValue = data.gaugeMax || data.gauge.maxValue;
            data.gauge.set(data.gaugeValue || 0);
        }
    });
    return this;
};


var main = function() {
    $('canvas[data-gaugesrv-opts]').each(function(idx) {
        $(this).gaugesrv();
    });
};


exports.main = main;

window.document.addEventListener('DOMContentLoaded', main);
