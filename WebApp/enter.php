<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
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
    </script>

</head>

<body>
<img  class="logo" src="img/TU_Delft_logo_RGB.png" width="110" height="75">
<div id="page" align="center" >
  <p><strong>My Recommendation Page</strong></p>
  <p>&nbsp;</p>
  <p>&nbsp; </p>
  <form id="searchForm" method="POST">
	  <fieldset>
        
           	<input id="s" type="text" name="input" />
            
          
           <button type="submit" value="Login"  name="login" style="color:black;">Login</button>
            
    <?php 
 
/* $ID = $_POST['user']; $Password = $_POST['pass']; 
sdsdsdsd
*/ 

	session_start(); 
//starting the session for user profile page 
 if(!empty($_POST['input'])) //checking the 'user' name which is from Sign-In.html, is it empty or have some text 
 { 
	 $db = mysqli_connect('localhost','root','','mysql') or die('Error connecting to MySQL server.');
	 $input="SELECT * FROM username where FirstName = '$_POST[input]'";
	 $query = mysqli_query($db,$input); 
	 $row = mysqli_fetch_array($query) ;
	 if(!empty($row['FirstName']))
	 {
		 $_SESSION['FirstName'] = $row['FirstName']; 
		 $name=$_SESSION['FirstName'];
		 echo "SUCCESSFULLY LOGIN TO USER PROFILE PAGE...".$_SESSION['FirstName']; 
		 header("Location:http://localhost/irproject/WebApp/search.php?user=".$row['FirstName']."&id=".$row['UserID']);
	 }
	 else 
	 { 
		 echo "<p>SORRY... YOU ENTERD WRONG ID... PLEASE RETRY...</p>"; 
	 }
 }

?>

       
                        

    </fieldset>
  </form>

    <div id="resultsDiv"></div>
    &nbsp;  &nbsp;  &nbsp;  &nbsp;<p></p>
    <div class="footer">&copy;A Tu Delft initiative</div>
</div>
  
</body>
</html>