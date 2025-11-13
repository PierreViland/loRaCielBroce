<?php
  $valid_username = '______________';
  $valid_password = '______________';
  if (!isset($_SERVER['PHP_AUTH_USER']) || !isset($_SERVER['PHP_AUTH_PW'])
      || $_SERVER['PHP_AUTH_USER'] !== $valid_username
      || $_SERVER['PHP_AUTH_PW'] !== $valid_password) {
  
      header('WWW-Authenticate: Basic realm="Accès restreint"');
      header('HTTP/1.0 401 Unauthorized');
      echo 'Authentification requise.';
      exit;
 }

?>

<!DOCTYPE html>
<html>
    <head>
        <title>Visualisation température device 1</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Visualisation température device 1</h1>
    
        <!-- Formulaire Gestion suppression A FAIRE -->
        


        <?php    
        try {
            // 🔹 Connexion à la base
            $bdd = new PDO(
                'mysql:host=mysql;dbname=_________;charset=utf8',
                '_____',     // utilisateur
                '______'      // mot de passe
            );    

            // 🔹 Requête : récupérer toutes les mesures du device 1
            $rep = $bdd->query("_______________________________");

            // 🔹 Affichage des résultats
            while ($reponse_bdd = $rep->fetch()) {
                ?>    
                <h3><?php echo "Mesure N° " . $reponse_bdd['id_mesure']; ?></h3>
    
                <i><?php echo " Température min : " . $reponse_bdd['temp_min']; ?></i><br/>
                <i><?php echo " Température max : " . $reponse_bdd['temp_max']; ?></i><br/><br/>
                <i><?php echo " ID gateway : " . $reponse_bdd['id_gateway']; ?></i><br/>
                <i><?php echo " ID Device : " . $reponse_bdd['id_device']; ?></i><br/><br/>
                <i><?php echo " RSSI : " . $reponse_bdd['RSSI']; ?></i><br/><br/>
                <div><?php echo " Date : " . $reponse_bdd['timep']; ?></div>
                <hr/>
                <?php
            }
            $rep->closeCursor();    
        }
        catch (Exception $e) {
            echo 'Erreur de connexion ou d\'exécution SQL';
            die('Détail : ' . $e->getMessage());
        }    
        ?>
    </body>
</html>


