<html>
<head>
	<title>Health forum</title>
	  <script src='https://www.google.com/recaptcha/api.js'></script>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
      <?php
       $link = mysqli_connect("127.0.0.1", "root", "", "app");
       session_start();
        $requirements = array();
        $requirements["carbs"] = 310;
        $requirements["fats"] = 70;
        $requirements["protein"] = 50;
        $requirements["fibre"] = 30;
        date_default_timezone_set("Asia/Kolkata");
        $createdate= date('Y-m-d');
   
       
      

         /*Carbohydrates 310 grams  Dietary Fibre 30 gramsProtein 50 grams Fat  70 grams Carbohydrates  310 grams  Dietary Fibre 30 grams*/
       if(!empty($_SESSION["username"])){
        echo "Welcome to the portal".$_SESSION["username"]." ";
         $username = $_SESSION["username"];
       if(isset($_POST["create"])){
        $query_create = "CREATE TABLE $username (
           id INT NOT NULL PRIMARY KEY AUTO_INCREMENT , 
           carbs INT NOT NULL ,
           fats INT NOT NULL, 
           protein INT NOT NULL,
           fibre INT NOT NULL,
           meal_time INT NOT NULL, 
           time DATE NOT NULL ,
           description TEXT NOT NULL
          
          )";
        $sql_create = mysqli_query($link,$query_create);
        if($sql_create){
          echo "Sucessfully created";
        }
        else{
          echo "You already have a plan";
          ECHO $username;
          echo mysqli_error($link);
        }

       }

        if(isset($_POST["submit"])){
          if(isset($_POST["description"])){
            $description = $_POST["description"];
          }
          if(isset($_POST["carbs"])){
            $carbs = $_POST["carbs"];
          }
          if(isset($_POST["fats"])){
            $fats = $_POST["fats"];
          }
          if(isset($_POST["protein"])){
            $protein = $_POST["protein"];
          }
          if(isset($_POST["fibre"])){
            $fibre = $_POST["fibre"];
          }
          if(isset($_POST["meal"])){
            $time = $_POST["meal"];
          }

          
          
          $query_add = "INSERT INTO $username (description,carbs, fats, protein, fibre,meal_time, time)
           VALUES (?,?,?,?,?,?,'$createdate')";
           $sql_entry = mysqli_prepare($link,$query_add);
           mysqli_stmt_bind_param($sql_entry,"siiiii",$description,$carbs,$fats,$protein,$fibre,$time);
            $result_entry = mysqli_stmt_execute($sql_entry);
            if($result_entry){
              echo "Yes";
            }
            else{
            echo mysqli_error($link);
            }


        }

        
         


            
           /* if(isset($sum["carbs"])){
            $var = ( $sum["carbs"] / constant("req_carbs"))*(100);
            echo "<div id='myProgress'><div id='myBar' style = 'width:".$var."%'>Carbohydrates</div></div>";

            $var = ( $sum["fats"] / constant("req_carbs"))*(100);
            echo "<div id='myProgress'><div id='myBar' style = 'width:".$var."%'>Fats</div></div>";
            $var = ( $sum["protein"] / constant("req_carbs"))*(100);
            echo "<div id='myProgress'><div id='myBar' style = 'width:".$var."%'>Protein</div></div>";
            $var = ( $sum["fibre"] / constant("req_carbs"))*(100);
            echo "<div id='myProgress'><div id='myBar' style = 'width:".$var."%'>Fibre</div></div>";
            }*/


          }
          else{ 
            echo mysqli_error($link);
          }

    

      ?>
      <style type="text/css">
      .diet{
        padding: 20px 20px 20px 20px;
      }
      .create{
        margin-left: 30px; 
        margin-top: 30px; 
        margin-bottom: 30px;
      }
      #table{
        border: 2px solid black;
        padding: 20px 20px 20px 20px;
        margin-right: 600px;

      }
      #myBar{
        
        height: 30px;
        background-color: #4CAF50;
        text-align: center; /* To center it horizontally (if you want) */
        line-height: 30px; /* To center it vertically */
        color: white; 
        margin left: 20px;
        margin-right: 500px;
        

      }
      #myProgress{
        border: 2px solid black;
        margin-left: 20px;
        margin-right: 500px;
      }
      #food_progress{
    
      }
      </style>
</head>
<body>
  
  <nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Health Tracker</a>
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
<div class = "diet">
  <input type = "submit" name = "create" value = "Create diet plan" class = "create">
  <div id = "table">
  <p>Description: <input type = "text" name = "description" class = "diet_input">
  <p>Carbs: <input type = "number" name = "carbs" class = "diet_input">
  <p>Fats: <input type = "number" name = "fats" class = "diet_input">
  <p>Protein: <input type = "number" name = "protein" class = "diet_input">
  <p>Fibre: <input type = "number" name = "fibre" class = "diet_input">
  <p><select name = "meal">
    <option value = "0">Breakfast</option>
    <option value = "1">Lunch</option>
    <option value = "2">Snack</option>
    <option value = "3">Dinner</option>
  </select></p>
  <p><input type = "submit" name = "submit" value = "Make entry"></p>
  </div>
</div>
  
</div>  
</form>
 <?php


 $display = "SELECT carbs, fats, protein, fibre FROM $username WHERE time = '$createdate' ";
          $query_display = mysqli_query($link,$display);
          if($query_display){
            $sum = array();
            
            while($result = mysqli_fetch_assoc($query_display)){
              
               $sum["carbs"] += $result["carbs"];
               $sum["fats"] += $result["fats"];
               $sum["protein"] += $result["protein"];
               $sum["fibre"] += $result["fibre"];
               }
               echo "<div id = 'food_progress'>";
           if(!empty($sum["carbs"])){
             foreach ($sum as $key => $value) {
               
                $var = ( ( $value / $requirements[$key])*(100) );
      
                if($var>100){

                 echo "exceeded health limit";

                }

                else{

                 echo "<p><div id='myProgress'><div id='myBar' style = 'width:".$var."%'>".$key."</div></div></p>";
                
                }

            }   
          }
           echo "</div>";
        }
         










 ?>

</body>
</html>