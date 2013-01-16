<?php

//get post parameter
const LOG_PATH = 'log/';
$param_name = isset($_POST['name']) ? $_POST['name'] : null;
$param_date = isset($_POST['date']) ? $_POST['date'] : null;

//prepare all member's log
if ($param_name == 'all') {
    $name_list = glob(LOG_PATH . '*', GLOB_ONLYDIR);
    foreach ($name_list as $key => $name) {
        $data = $date = $time = array();
        $name = substr($name, strlen(LOG_PATH));
        $file = fopen(LOG_PATH . $name . '/' . $param_date . '.csv', 'r');
        while(!feof($file)) {
             $data[] = fgets($file);
        }
        array_pop($data);
        foreach ($data as $k => $item) {
            $res = explode(' ', $item);
            $date[] = isset($res[0]) ? str_replace('-', '/', substr($res[0], 5)) : null;
            $time[] = isset($res[1]) ? (float)$res[1] : null;
        }
        $series[$key]['name'] = $name;
        $series[$key]['data'] = $time;
    }
//prepare specific member's log
} else {
    try {
        $file = fopen(LOG_PATH . $param_name . '/' . $param_date . '.csv', 'r');
    } catch (Exception $e) {
        var_dump($e);
        echo $e->getMessage();
        exit();
    }
    while(!feof($file)) {
        $data[] = fgets($file);
    }
    array_pop($data);
    foreach ($data as $key => $item) {
        $res = explode(' ', $item);
        $date[] = isset($res[0]) ? str_replace('-', '/', substr($res[0], 5)) : null;
        $time[] = isset($res[1]) ? (float)$res[1] : null;
    }
    $series[0]['name'] = $param_name;
    $series[0]['data'] = $time;
}

//encode to json
$categories = json_encode($date);
$series = json_encode($series);

//output graph
print<<<EOF
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Highcharts Example</title>

<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
<script type="text/javascript">
$(function () {
    var chart;
    $(document).ready(function() {
        chart = new Highcharts.Chart({
            chart: {
                renderTo: 'container',
                type: 'line',
                marginRight: 130,
                marginBottom: 25
            },
            title: {
                text: '退社の記録',
                x: -20 //center
            },
            subtitle: {
                text: 'Source: 帰らせくん',
                x: -20
            },
            xAxis: {
                categories: $categories,
            },
            yAxis: {
                title: {
                    text: '時刻'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                formatter: function() {
                        return '<b>'+ this.series.name +'</b><br/>'+
                        this.x +': '+ this.y;
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -10,
                y: 100,
                borderWidth: 0
            },
            series: $series,
        });
    });
    
});
</script>
</head>
<body>
<script src="http://code.highcharts.com/highcharts.js"></script>
<script src="http://code.highcharts.com/modules/exporting.js"></script>

<form action="makeGraph.php" method="POST">
  <select name="name">
    <option value="all">all
    <option value="amuro">amuro
    <option value="taro">taro
  </select>
  <select name="date">
    <option value="201212">2012/12
  </select>
  <input type="submit">
</form>

<div id="container" style="min-width: 400px; height: 400px; margin: 0 auto"></div>

</body>
</html>
EOF;
