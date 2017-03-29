<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Recommendation Page</title>

<link rel="stylesheet" type="text/css" href="styles.css" />

</head>

<body>
<img  class="logo" src="img/TU_Delft_logo_RGB.png" width="110" height="75">
<div id="page" align="center" >
  <p><strong>My Recommendation Page</strong></p>
  <p>&nbsp;</p>
  <p>&nbsp; </p>
  <form id="loginForm" method="POST">
	  <fieldset>
        
           	<input id="s" type="text" name="input" />
            
            <input type="submit" value="login" id="login" name="login" />
            
    <?php 
 
/* $ID = $_POST['user']; $Password = $_POST['pass']; 

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
		 header("Location:http://localhost/search.php?user=".$row['FirstName']."&id=".$row['UserID']);
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
</div>
</body>
</html>