<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Anagrames</title>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript">
function oncl() {
  var checked = document.getElementById("check").checked;
  var str = "";
  if (checked) str = "stripunicode";
  else str = "nostrip"
  var w = document.getElementById("w").value;
  w = w.toLowerCase();
  w = w.replace("à","&agrave;");
  w = w.replace("è","&egrave;");
  w = w.replace("ò","&ograve;");
  w = w.replace("é","&eacute;");
  w = w.replace("í","&iacute;");
  w = w.replace("ú","&uacute;");
  w = w.replace("ü","&uuml;");
  w = w.replace("ï","&iuml;");
  w = w.replace("·","&middot;");
  w = w.replace("ç","&ccedil;");
  
  $.get("get.php?w="+encodeURIComponent(w)+"&m="+str,function (response) {
	document.getElementById("resultats").innerHTML = response;
    }
  );
}
</script>
</head>
<body style="font-family:sans-serif,Arial;">
<div style="margin-left:auto;margin-right:auto;width:60%;text-align:center;">
<h2>Cercador d'anagrames</h2>
Amb exactament 612.510 paraules.<br/><br/>
<div style="padding:10px;background:lightsteelblue;border:1px solid steelblue;text-align:center;">
<input type="text" id="w">
<input type="button" onclick="oncl()" value="Aconsegueix-ne anagrames!">
<br/>
<input type="checkbox" id="check" checked>Ignora accents i diacrítics
</div>
<br/>
<div id="resultats" style="padding:10px;background:lightsteelblue;border:1px solid steelblue;text-align:center;">

</div>
<br/><br/>
<span style="color:gray;font-size:80%;">La font és un fitxer provinent d'<a href="http://www.jmoratinos.com">http://www.jmoratinos.com</a>, modificat per a Debian que es troba a <span style="font-family:monospace;">/usr/share/dict/wcatalan</span> en sistemes Debian. La llicència és la <a href="GPL.txt">GPL</a>, i els seus autors: (2001-2002) Ignasi Labastida i Juan i (2002-2006) Joan Moratinos.</span>
</div>
</body>
</html>
