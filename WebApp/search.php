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
    echo "Welcome to your Recommendation Site,".$_GET['user']."(".$_GET['id'].")";
	?>
	</p>
</form>
<div id="page" align="center"><strong>My Recommendation Page</strong>
  <form id="searchForm" method="post">
	  <fieldset>

           

                <button  type="submit" value="Submit" onclick="doRecommend();" name="recommendation"><a href="recommendation.html"></a>Recommendation</button>&nbsp;&nbsp;&nbsp;&nbsp;
              <button type="submit" value="Submit" onclick="doExplain();" name="explanation" >Explanation</button>
                        

    </fieldset>
  </form>

    <div id="resultsDiv"></div>
</div>

</body>
</html>
