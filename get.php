<?
$w = $_GET["w"];
$w = utf8_encode($w);
$m = $_GET["m"];
$descriptorspec = array(
	           0 => array("pipe", "r"),  
		              1 => array("pipe", "w"), 
			                 2 => array("file", "./error-output.txt", "a") 
					          );
$process = proc_open('python sanagram.py', $descriptorspec, $pipes);

if (is_resource($process)) {
	    fwrite($pipes[0], "catalan_$m ".$w);
	        fclose($pipes[0]);

	        echo stream_get_contents($pipes[1]);
		    fclose($pipes[1]);
		    $return_value = proc_close($process);
}

?>

