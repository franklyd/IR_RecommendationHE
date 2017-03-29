<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Recommendation Page</title>

<link rel="stylesheet" type="text/css" href="styles.css" />

</head>

<body>
<img  class="logo" src="img/TU_Delft_logo_RGB.png" width="110" height="75">
<form id="loginname">
	<p id="paragraph">
	<?php
    echo "Welcome to our Recommendation Site,".$_GET['user']."(".$_GET['id'].")";
	?>
	</p>
</form>
<div id="page" align="center"><strong>My Recommendation Page</strong>
  <form id="searchForm" method="post">
	  <fieldset>
        
           	<input id="s" type="text" />
            
            <input type="submit" value="Search" id="submitButton" />
            
            <div id="searchInContainer">
                <input type="radio" name="check" value="site" id="searchSite" checked />
                <label for="searchSite" id="siteNameLabel">Recommendation</label>
                
                <input type="radio" name="check" value="web" id="searchWeb" />
                <label for="searchWeb">Explanation</label>
			</div>
                        

    </fieldset>
  </form>

    <div id="resultsDiv"></div>
</div>

</body>
</html>
