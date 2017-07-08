<html>
<head>
	<title>Health forum</title>
	  <script src='https://www.google.com/recaptcha/api.js'></script>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
      <?php
      $link = mysqli_connect("127.0.0.1", "root", "", "app");
      session_start();
      date_default_timezone_set("Asia/Kolkata");
      $createdate= date('Y-m-d H:i:s');
      echo mysqli_error($link);
        $title = $_GET["title"];
        $username = $_SESSION["username"];

     if(!empty($_SESSION["username"])){
       if(isset($_POST["submit"])){
        
        if(isset($_POST["comment"])){
          $comment = $_POST["comment"];
        }        
         $username = $_SESSION["username"];
         
        
         $query_create = "INSERT INTO content (group_name,comment,username,timedate) VALUES (?,?,?,'$createdate')";
        

        $sql = mysqli_prepare($link,$query_create);
        mysqli_stmt_bind_param($sql,"sss",$title,$comment,$username);
        $result =  mysqli_stmt_execute($sql);
        if($result){
        }
        else{
          echo mysqli_error($link);
        }

      }

   }

 








      ?>
      <style type="text/css">

      .forum_link{
        border: 2px solid black;
        padding-left: 18px;
        padding-top: 18px;
        border: 3px solid black;
        padding-bottom: 18px;
        margin-left: 20px;
        margin-right: 700px;
        margin-bottom: 20px;
      }
      .page_header div{
      	border-bottom: 12px solid blue;
      }
      #new_group{
        padding-left: 30px;
        padding-top: 30px;
        border: 3px solid black;
        padding-bottom: 30px;
        margin-left: 20px;
        margin-right: 900px;
      }







      </style>
</head>
<body>
 
  <nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Health tracker</a>
    </div>
    <ul class="nav navbar-nav">
      <li><a href="landing.php">Home</a></li>
      <li><a href = "#">Group name: <?php echo $title ?></a></li>
    </ul>
    <ul class="nav navbar-nav navbar-right">
      <li><a href = "logout.php"><?php echo $_SESSION["username"]; ?></a></li>
      <li><a href="register.php"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
      <li><a href="login.php"><span class="glyphicon glyphicon-log-in"></span> Login</a></li>
    </ul>
  </div>
</nav>
 <form method = "POST">
 <div id = "new_group">
    
    <p>Comment: <input type = "text" name = "comment"></p>
    <input type = "submit" name = "submit" value = "Add Comment"></p>

  </div>
</form>
 <?php

  $query_show = "SELECT * FROM content WHERE group_name = '$title' ORDER BY timedate";
  $sql_display = mysqli_query($link,$query_show);

  if($sql_display){
    while($rows = mysqli_fetch_assoc($sql_display)){
      echo "<div class = 'forum_link' ><p>".$rows["comment"]."
      </p><p> Written by, "
      .$rows["username"]."</p></div>";
    }
  } 
  else{
    echo mysqli_error($link);
  }










 ?>
</body>
</html>