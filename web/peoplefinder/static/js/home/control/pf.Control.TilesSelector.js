L.Control.TilesSelector = L.Control.extend({
    options: {
        position: 'topright'
    },

    _map: null,
    _isOnline: true,

    onAdd: function (map) {
        var container = L.DomUtil.create('div', 'pf-tiles-selector leaflet-bar'),
            options = this.options;

        container.innerHTML = '<div id="tilesSelector" class="btn-group" data-toggle="buttons"><label class="btn btn-default active"><input type="radio" name="options" id="option1" autocomplete="off" checked> Online</label><label class="btn btn-default"><input type="radio" name="options" id="option2" autocomplete="off"> Local</label></div>';

        this._map = map;
        this._map._tilesLayer = null;

        $(container).find('input').on('change', $.proxy(function () {
            if (this._map._tilesLayer) {
                this._map.removeLayer(this._map._tilesLayer);
            }
            this._isOnline = !this._isOnline;
            this._selectTileLayer(this._isOnline);
        }, this));

        return container;
    },

    onRemove: function (map) {
    },

    _selectTileLayer: function (isOnline) {
        if (isOnline) {
            this.addOnlineTilesLayer();
        } else {
            this.addLocalTilesLayer();
        }
    },

    addOnlineTilesLayer: function () {
        this._map._tilesLayer = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
            maxZoom: Math.min(this._map.options.maxZoom, 18)
        });
        this._map._tilesLayer.addTo(this._map);
    },

    addLocalTilesLayer: function () {
        this._map._tilesLayer = L.tileLayer(pf.settings.root_url + '/tiles/{z}/{x}/{y}.png', {
            attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
            maxZoom: Math.min(this._map.options.maxZoom, 18),
            errorTileUrl: pf.settings.root_url + '/static/styles/images/no-tiles.png'
        });
        this._map._tilesLayer.addTo(this._map);
    }
});

L.Map.mergeOptions({
    tilesSelector: true
});

L.Map.addInitHook(function () {
    if (this.options.tilesSelector) {
        this.tilesSelector = new L.Control.TilesSelector();
        this.addControl(this.tilesSelector);
    }
});
