/**
 * Created by xer01 on 11/24/2015.
 */


$(document).ready(function () {


    var osChartConfig = {
        "type": "serial",
        "categoryField": "status",
        "rotate": true,
        "startDuration": 1,
        "categoryAxis": {
            "gridPosition": "status"
        },
        "trendLines": [],
        "graphs": [
            {
                "balloonText": "[[title]]  :[[value]]",
                "fillAlphas": 1,
                "id": "AmGraph-1",
                "title": "Total",
                "type": "column",
                "valueField": "total"
            }
        ],
        "guides": [],
        "valueAxes": [
            {
                "id": "ValueAxis-1",
                "title": ""
            }
        ],
        "allLabels": [],
        "balloon": {},
        "legend": {
            "useGraphSettings": true
        },
        "titles": [
            {
                "id": "Title-1",
                "size": 15,
                "text": "Ordenes por Status"
            }
        ]
    };

    $.get('/produccion/statsProduccion').done(function (data) {

      //  console.log(JSON.stringify(data));

        $.each(data,function(key, value){


           switch (value.status){
               case '1':
                   value.status = 'Cancelado';
                   break;
                case '2':
                   value.status = 'Iniciado';
                   break;
                case '3':
                   value.status = 'Sin Terminar';
                   break;
                case '4':
                   value.status = 'Terminada';
                   break;

           }
        });

        osChartConfig.dataProvider = data;

        var chart = AmCharts.makeChart('chartOrdenes', osChartConfig);

    }).fail(function (err) {
        console.log(err)
    });




});
