(function ($, pf, L) {
    pf.modules.map = {};
    $.extend(pf.modules.map, {

        _map: null,

        init: function () {
            this.setDom();

            this._map = this.buildMap();
            pf.viewmodel.map = this._map;

            this.setInitialView();
            L.control.scale().addTo(this._map);
            this._map.tilesSelector._selectTileLayer(true);
        },


        setDom: function () {
            pf.view.$map = $('#map');
        },


        buildMap: function () {
            return L.map('map', {
                zoomControl: false,
                zoomValueControl: true,
                maxZoom: 15
            });
        },


        setInitialView: function () {
            this._map.setView([60, 30], 6);
        }
    });
}(jQuery, pf, L));
