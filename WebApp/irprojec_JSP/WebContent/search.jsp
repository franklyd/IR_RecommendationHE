<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Recommendation Page</title>

<link rel="stylesheet" type="text/css" href="styles.css" />

</head>

<body>
<img  class="logo" src="img/TU_Delft_logo_RGB.png" width="110" height="75">
<form id="loginname">
	<p id="paragraph">
	Welcome to your Recommendation Page
    <%= request.getParameter("user") %>
    (
    <%= request.getParameter("id") %>
    )
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