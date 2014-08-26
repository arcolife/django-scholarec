var temp1;
$.getJSON("/raw/published/", function(items) {
    temp1 = items;
});

var temp2;
$.getJSON("/raw/keywords/", function(items) {
    temp2 = items;
});
//  var temp3;
//  $.getJSON("/details/raw/inbound/countries/", function(items) {
//  temp3 = items;
//  });
//  var temp4;
//  $.getJSON("/details/raw/outbound/countries/", function(items) {
//  temp4 = items;
//  });
//  var temp5;
//  $.getJSON("/details/raw/inbound/hangups/", function(items) {
//  temp5 = items;
//  });
//  var temp6;
//  $.getJSON("/details/raw/outbound/hangups/", function(items) {
//  temp6 = items;
//  });
//  var temp7;
//  $.getJSON("/details/raw/inbound/carrier_amount/", function(items) {
//  temp7 = items;
//  });
//  var temp8;
//  $.getJSON("/details/raw/outbound/carrier_amount/", function(items) {
//  temp8 = items;
//  });
//  var temp9;
//  $.getJSON("/details/raw/inbound/minutes/", function(items) {
//  temp9 = items;
//  });
//  var temp10;
//  $.getJSON("/details/raw/outbound/minutes/", function(items) {
//  temp10 = items;
//  });

google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);

function drawChart() {
    var data1 = google.visualization.arrayToDataTable(temp1);
    var data2 = google.visualization.arrayToDataTable(temp2);
    // var data3 = google.visualization.arrayToDataTable(temp3);
    // var data4 = google.visualization.arrayToDataTable(temp4);
    // var data5 = google.visualization.arrayToDataTable(temp5);
    // var data6 = google.visualization.arrayToDataTable(temp6);
    // var data7 = google.visualization.arrayToDataTable(temp7);
    // var data8 = google.visualization.arrayToDataTable(temp8);
    // var data9 = google.visualization.arrayToDataTable(temp9);
    // var data10 = google.visualization.arrayToDataTable(temp10);

    var options1 = {
	title: 'Research Doc Stats',
	vAxis: {title: '# of published docs',  titleTextStyle: {color: 'red'}}
    };
    var options2 = {
	title: 'Fields Count'
    };
    // var options3 = {
    // title: 'OUT (Outbound)',
    // vAxis: {title: 'Country',  titleTextStyle: {color: 'red'}}
    // };
    // var options4 = {
    // title: 'OUT (Outbound)',
    // vAxis: {title: 'Country',  titleTextStyle: {color: 'red'}}
    // };
    // var options5 = {
    // title: 'OUT (Outbound)',
    // vAxis: {title: 'Hangup Type',  titleTextStyle: {color: 'red'}}
    // };
    // var options6 = {
    // title: 'OUT (Outbound)',
    // vAxis: {title: 'Hangup Type',  titleTextStyle: {color: 'red'}}
    // };
    // var options7 = {
    // title: 'OUT (Outbound)',
    // vAxis: {title: 'Minutes',  titleTextStyle: {color: 'red'}}
    // };
    // var options8 = {
    // title: 'OUT (Outbound)',
    // vAxis: {title: 'Minutes',  titleTextStyle: {color: 'red'}}
    // };
    // var options9 = {
    // title: 'OUT (Outbound)',
    // vAxis: {title: 'Amount',  titleTextStyle: {color: 'red'}}
    // };
    // var options10 = {
    // title: 'OUT (Outbound)',
    // vAxis: {title: 'Amount',  titleTextStyle: {color: 'red'}}
    // };
    
    var chart1 = new google.visualization.ColumnChart(document.getElementById('d_chart1'));
    var chart2 = new google.visualization.ColumnChart(document.getElementById('d_chart2'));

    // var chart3 = new google.visualization.GeoChart(document.getElementById('d_chart3'));
    // var chart4 = new google.visualization.GeoChart(document.getElementById('d_chart4'));
    // var chart5 = new google.visualization.PieChart(document.getElementById('d_chart5'));
    // var chart6 = new google.visualization.PieChart(document.getElementById('d_chart6'));
    // var chart7 = new google.visualization.ColumnChart(document.getElementById('d_chart7'));
    // var chart8 = new google.visualization.ColumnChart(document.getElementById('d_chart8'));
    // var chart9 = new google.visualization.ColumnChart(document.getElementById('d_chart9'));
    // var chart10 = new google.visualization.ColumnChart(document.getElementById('d_chart10'));

    chart1.draw(data1, options1);
    chart2.draw(data2, options2);

    // chart3.draw(data3, options3);
    // chart4.draw(data4, options4);
    // chart5.draw(data5, options5);
    // chart6.draw(data6, options6);
    // chart7.draw(data7, options7);
    // chart8.draw(data8, options8);
    // chart9.draw(data9, options9);
    // chart10.draw(data10, options10);

}
