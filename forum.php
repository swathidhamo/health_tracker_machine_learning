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

      if(isset($_POST["create_group"])){
        if(isset($_POST["title"])){
          $title = $_POST["title"];
        }
        if(isset($_POST["description"])){
          $description = $_POST["description"];
        }
        if(isset($_POST["time"])){
          $time = $_POST["time"];
          if($time=='one'){
            $date = strtotime("+7 days");
          }
          else if($time=='two'){
            $date = strtotime("+90 days");
          }
          else if($time=='twelve'){
            $date = strtotime("+60 days");
          }
          else if($time=='month'){
            $date= strtotime("+30 days");
          }
          else if($time=='three'){
            $date = strtotime("+90 seconds");
          }
          else{
            $date = null;
          }          
        }
         $leader = $_SESSION["username"];
         $query_create = "INSERT INTO group_info (title,description,leader,time) VALUES (?,?,?,?)";
        

        $sql = mysqli_prepare($link,$query_create);
        mysqli_stmt_bind_param($sql,"sssi",$title,$description,$leader,$date);
        $result =  mysqli_stmt_execute($sql);
        if($result){
          echo "Created the group";
        }
        else{
          echo mysqli_error($link);
        }

      }



 








      ?>
      <style type="text/css">

      .forum_link{
        border: 2px solid black;
        padding-left: 30px;
        padding-top: 30px;
        border: 3px solid black;
        padding-bottom: 30px;
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
      <li><a href="forum.php">My forums</a></li>
      <li><a href="diet.php">My diets</a></li>
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
    <p>Group name: <input type = "text" name = "title"></p>
    <p>Description: <input type = "text" name = "description"></p>
    <p> Time limit: <select name = "time">
                  <option value = "one">week</option>
                  <option value = "three">90 seconds</option>  
                  <option value = "month">One month</option>
                  <option value = "two">90 days</option>
                  <option value = "twelve">Two months</option>
                  <option value = "none">Never</option>
                </select></p>

    <input type = "submit" name = "create_group" value = "Create Group">
    
    <p><input type = "text" name = "group_name" placeholder = "Enter the title of the group"> 
    <input type = "text" name = "member_name" placeholder = "Enter the names">
    <input type = "submit" name = "add members" value = "Add members"></p>

  </div>
</form>
 <?php
  $query_show = "SELECT * FROM group_info";
  $sql_display = mysqli_query($link,$query_show);

  if($sql_display){
    while($rows = mysqli_fetch_assoc($sql_display)){
      echo "<div class = 'forum_link' ><p>".$rows["title"]."</p><p> About the group: ".$rows["description"]."
      </p><p><a href = 'group.php?title=".$rows["title"]."'>Click here to go to the group</a></p><p> Created by, "
      .$rows["leader"]."</p></div>";

    }
  } 










 ?>
</body>
</html>