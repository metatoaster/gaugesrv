'use strict';

var gaugesrv = require('gaugesrv/lib');
var $ = require('jquery');

window.mocha.setup('bdd');


describe('gaugesrv testcases', function() {

    beforeEach(function() {
        this.clock = sinon.useFakeTimers();
    });

    afterEach(function() {
        this.clock.restore();
        document.body.innerHTML = "";
    });

    it('test gaugesrv main', function() {
        document.body.innerHTML = (
            '<canvas id=\'test\' data-gaugesrv-opts=\'{' +
            '    "staticLabels": {' +
            '        "font": "10px sans-serif",' +
            '        "labels": [1, 2, 5, 10],' +
            '        "color": "#000000"' +
            '    },' +
            '    "limitMax": true' +
            '}\' data-gauge-max=\'10\' data-gauge-value=\'2\'></canvas>'
        );

        gaugesrv.main();
        var gaugedata = $('canvas#test').data('gauge');
        expect(gaugedata.value).to.equal(2);
        expect(gaugedata.options.staticLabels.labels.length).to.equal(4);

    });

});
