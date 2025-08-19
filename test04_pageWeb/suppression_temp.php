<!DOCTYPE html>
<html>
	<!-- Exemple de page php-->
    <head>
        <title>Suppression d'une capture</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <?php 
		echo 'Suppression d\'une capture : ' .htmlspecialchars($_POST['id_supp']);
		?>
		<p>
				
		<?php
			
			
		try
		{					
			//A COMPLETER ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			//Se connecter à la base de données
			$bdd = new PDO(___________________________________________________________);		
			//A MODIFIER SUR LE NOM DE LA TABLE EST DIFFERENTs +++++++++++++++++++++++++++++++++++
			$nb  = $bdd->query("DELETE FROM mesures_device1 WHERE ID='".$_POST['id_supp']."'");
		}
		catch (Exception $e)
		{
			echo 'ID n\'ont valide';
			die('Erreur : ' . $e->getMessage());
		}
		
				
		?>
		</p>
		
		<p>		
		<li > <a href="visualisation_temp.php">Visualisation mesures</a> </li >
		</p>
		
		<a href="../page2.html">
		
    </body>
</html>