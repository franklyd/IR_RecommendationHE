<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"  import="java.sql.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Recommendation Page</title>

<link rel="stylesheet" type="text/css" href="styles.css" />
<script type="text/javascript">
    function validate()
{
 var error="";
 var name = document.getElementById( "name_of_user" );
 if( name.value == "" )
 {
  error = " You Have To Write Your Name. ";
  document.getElementById( "error_para" ).innerHTML = error;
  return false;
 }
}
    function validateForm() {
        var x = document.forms["myForm"]["username"].value;
        if (x == "") {
            alert("Name must be filled out");
            return false;
        }
    }
    </script>

</head>

<body>
<img  class="logo" src="img/TU_Delft_logo_RGB.png" width="110" height="75">
<div id="page" align="center" >
  <p><strong>My Recommendation Page</strong></p>
  <p>&nbsp;</p>
  <p>&nbsp; </p>
  <form id="searchForm" name="myForm" method="POST" action="enter.jsp" onsubmit="return validateForm()">
	  <fieldset>
        
           	<input id="s" type="text" name="username" />
            
          
           <button type="submit" value="Login"  name="login" style="color:black;">Login</button>

    </fieldset>
  </form>
  <%
    try{
    
        String username = request.getParameter("username");   
        //String password = request.getParameter("password");
        Class.forName("com.mysql.jdbc.Driver");  // MySQL database connection
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/logon?" + "user=root&password=root");    
        PreparedStatement pst = conn.prepareStatement("SELECT * FROM username where FirstName=?");
        pst.setString(1, username);
        //pst.setString(2, password);
        ResultSet rs = pst.executeQuery();                        
        if(rs.next())   
        {
           out.println("Valid login credentials"); 
        	String redirectURL = "search.jsp?user="+username+"&id="+rs.getString(1);
        	response.sendRedirect(redirectURL);
        }
        else
           out.println("Invalid login credentials");            
   }
   catch(Exception e){       
       out.println("Something went wrong !! Please try again" + e.toString());       
   }      
%>
    <div id="resultsDiv"></div>
    &nbsp;  &nbsp;  &nbsp;  &nbsp;<p></p>
    <div class="footer">&copy;A Tu Delft initiative</div>
</div>           

<body>

</body>
</html>