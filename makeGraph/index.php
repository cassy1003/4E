<?php

const LOG_PATH = 'log/';
const MAX_HISTORY = 5;
$log_list = glob(LOG_PATH . '*', GLOB_ONLYDIR);
//generate member list from log file name
foreach ($log_list as $name) {
    $name_list[] = substr($name, strlen(LOG_PATH));
}

//generate month list
for ($i = 0; $i < MAX_HISTORY; $i++) {
    $month_list[] = date('Ym', strtotime('-'.$i.'month'));
}

//output selectbox
print<<<EOF
<!DOCTYPE HTML>
<html>
<head>
</head>
<body>
<form action="makeGraph.php" method="POST">
  <select name="name">
    <option value="all">all
EOF;

foreach ($name_list as $name) {
    echo '<option value="' . $name . '">' . $name;
}

print<<<EOF
  </select>
  <select name="date">
EOF;

foreach ($month_list as $month) {
    echo '<option value="' . $month . '">' . $month;
}

print<<<EOF
  </select>
  <input type="submit">
</form>
</body>
</html>
EOF;
