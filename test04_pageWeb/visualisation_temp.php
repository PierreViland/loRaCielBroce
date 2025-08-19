<!DOCTYPE html>
<html>
	<!-- Exemple de page php-->
    <head>
        <title>Visulisation température device 1</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Visualisation température device 1</h1>
		
		<!-- Formulaire Gestion suppression -->
		<p>
		<form method="post" action="suppression_temp.php" >
		<p>
		Mesure à suprimer: <input type="text" name="id_supp" /input> </p> 
		</p>			
		<p> 
		<input type="submit" name="validation_suppression" value="Supprimer mesure" />
		</form>
		<p>				
		<?php		
		try
		{
//A COMPLETER ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			//Se connecter à la base de données
			$bdd = new PDO(___________________________________________________________);		

//A COMPLETER ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++			
			//Requete à une base de données. Les résultats sont récupérés sous la forme d'un tableau
			//Toute les donnees sont a recuperer
			$rep = $bdd->query(___________________________________);
			
			//Affichage des résultats
			while ($reponse_bdd = $rep->fetch())
			{	?>	
				
				<h3><?php echo "Mesure N° ".$reponse_bdd['ID']  ;
				//Si vous n'avez pas mis les mêmes noms, il faudra les changer dans les lignes ci-dessous....
				?></h3>
					
                    <i><?php echo " Température min : " . $reponse_bdd['temp_min']; ?></br></i>
					<i><?php echo " Température  max : " . $reponse_bdd['temp_max']; ?></br></br></i>
					<i><?php echo " ID gateway: " . $reponse_bdd['id_gateway']; ?></br></i>
					<i><?php echo " RSSI: " . $reponse_bdd['rssi']; ?></br></br></i>
					<div><?php echo " Date : " . $reponse_bdd['timep']; ?></div>
				
				<?php
			}
			$rep->closeCursor();					
		}
		catch (Exception $e)
		{
			echo 'Erreur';
			die('Erreur : ' . $e->getMessage());
		}	
		?>
		</p>

		
    </body>
</html>