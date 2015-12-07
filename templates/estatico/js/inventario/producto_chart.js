$(function () {
    var graficar = function (data) {
        var data2 = [];
        $.each(data, function (index, value) {
            data2.push({
                fecha: Date.parse(value.fields.fecha_creacion),
                total: value.fields.cantidad_total_almacen_despues
            });
        });

        if (data2.length < 1)
            return;

        new Morris.Line({
            // ID of the element in which to draw the chart.
            element: 'myfirstchart',
            // Chart data records -- each entry in this array corresponds to a point on
            // the chart.
            data: data2,
            // The name of the data record attribute that contains x-values.
            xkey: 'fecha',
            // A list of names of data record attributes that contain y-values.
            ykeys: ['total'],
            // Labels for the ykeys -- will be displayed when you hover over the
            // chart.
            labels: ['total']
        });
    };

    $.getJSON('/inventario/productos/' + document.producto + '/chart', graficar);

});
