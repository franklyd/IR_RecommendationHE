
<%@ page import ="java.sql.*" %>
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
           out.println("Valid login credentials");        
        else
           out.println("Invalid login credentials");            
   }
   catch(Exception e){       
       out.println("Something went wrong !! Please try again" + e.toString());       
   }      
%>