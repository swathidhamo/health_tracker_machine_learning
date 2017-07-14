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

      if(isset($_POST["entry"])){
        if(isset($_POST["time"])){
          $time = $_POST["time"];
        }
        if(isset($_POST["score_1"])){
          $score_1 = $_POST["score_1"];
        }
        if(isset($_POST["type"])){
          $type = $_POST["type"];       
        }
         if(isset($_POST["score_2"])){
          $score_2 = $_POST["score_2"];
        }
        if(isset($_POST["score_3"])){
          $score_3 = $_POST["score_3"];
        }

         $query_create = "INSERT INTO medication (name, s_one, s_two, s_three, time) VALUES (?,?,?,?,?)";

        

        $sql = mysqli_prepare($link,$query_create);
        mysqli_stmt_bind_param($sql,"siiis",$type,$score_1,$score_2,$score_3,$time);
        $result =  mysqli_stmt_execute($sql);

        
        if($result){
          echo "Created the entry";
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
      <li><a href = "#">Medication</a></li>
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
    <p>Timing: <input type = "time" name = "time"></p>
    <p> Medicine type: <select name = "type">
                  <option value = "M1">Medicine 1</option>
                  <option value = "M2">Medicine 2</option>  
                  <option value = "M3">Medicine 3</option>
                  <option value = "M4">Medicine 4</option>
                </select></p>
    
      <p>Nausea: <input type = "number" name = "score_1" max = "10" min = "0"></p>
      <p>Fever: <input type = "number" name = "score_2" max = "10" min = "0"></p>
      <p>Rashes: <input type = "number" name = "score_3" max = "10" min = "0"></p>
      <p>Others (if any): <input type = "number" name = "score_4" max = "10" min = "0"></p>

    <input type = "submit" name = "entry" value = "Record entry">  
    <input type = "submit" name = "search" value = "Search" id = "search"> 
    <input type = "submit" name = "display" value = "display" id = "display"> 


  </div>
 </form>

<?php


 
 if(isset($_POST["search"])){
      $medicine = "M1";
      $output = fopen("data.csv", "w");  
      
      $query = "SELECT s_one,s_two,s_three,time FROM medication WHERE name = '$medicine' ";  
      $result = mysqli_query($link, $query);  
      while($row = mysqli_fetch_assoc($result))  
      {      
        fputcsv($output, $row);  
      }  
     // fputcsv($output, $array);  
      echo mysqli_error($link);
      fclose($output);  
 }

 if(isset($_POST["display"])){
  $input = fopen("getData.csv","r");
  print_r(fgetcsv($input));
  fclose($input);

 }



?>
</body>
</html>