-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: mydiscord
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(255) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=519 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (340,'test2','he'),(341,'salutsalut','hee'),(342,'salutsalut','salut'),(343,'salutsalut','ca va'),(344,'salutsalut','ouii'),(345,'salutsalut',''),(346,'salutsalut','et toiu'),(347,'salutsalut','jee'),(348,'salutsalut','cc'),(349,'salutsalut','c'),(350,'salutsalut','sais pas'),(351,'cesar@cesar.com','hh'),(352,'test2','he'),(353,'test2','de'),(354,'test2','he'),(355,'test2','ca va'),(356,'test2','caa'),(357,'salutsalut','he'),(358,'test2','ca'),(359,'test2','he'),(360,'test2','ca'),(361,'test2','ca'),(362,'salutsalut','he'),(363,'test2','sa'),(364,'test2','salut'),(365,'test2','test'),(366,'test2','test'),(367,'test2','a'),(368,'test2','sa'),(369,'test2','sa'),(370,'test2','ca'),(371,'salutsalut','he'),(372,'test2','de'),(373,'test2','de'),(374,'test2','ca'),(375,'test2','va'),(376,'salutsalut','sa'),(377,'salutsalut','ca'),(378,'salutsalut','va'),(379,'salutsalut','oué et toi'),(380,'cesar@cesar.com','heee'),(381,'cesar@cesar.com','ca va'),(382,'test2','ho'),(383,'test2','ca va'),(384,'salutsalut','te'),(385,'salutsalut','te'),(386,'salutsalut','e'),(387,'salutsalut','what'),(388,'salutsalut','test'),(389,'test2','he'),(390,'salutsalut','he'),(391,'salutsalut','q'),(392,'salutsalut','ca va '),(393,'test2','test'),(394,'test2','ho'),(395,'salutsalut','cava'),(396,'test2','ca'),(397,'salutsalut','va'),(398,'salutsalut','te'),(399,'salutsalut','fr'),(400,'salutsalut','oo'),(401,'test2','saaa'),(402,'test2','saaaaa'),(403,'salutsalut','deee'),(404,'test2','de'),(405,'test2','dee'),(406,'test2','oa'),(407,'test2','saa'),(408,'test2','olé'),(409,'salutsalut','heee'),(410,'salutsalut','shit'),(411,'test2','sa'),(412,'salutsalut','he'),(413,'salutsalut','a'),(414,'salutsalut','c'),(415,'salutsalut','bon'),(416,'cesar@cesar.com','he'),(417,'test2','de'),(418,'test2','de'),(419,'test2','de'),(420,'test2','de'),(421,'test2','de'),(422,'test2','saa'),(423,'test2','he'),(424,'test2','ca'),(425,'test2','ca'),(426,'salutsalut','sa'),(427,'test2','sa'),(428,'salutsalut','ca'),(429,'test2','sa'),(430,'salutsalut','salut'),(431,'salutsalut','de'),(432,'salutsalut','de'),(433,'test2','de'),(434,'test2','sa'),(435,'test2','sa'),(436,'test2','ca'),(437,'test2','ca'),(438,'test2','aa'),(439,'salutsalut','sa'),(440,'test2','de'),(441,'test2','de'),(442,'salutsalut','sa'),(443,'test2','salut melvin l\'enfant'),(444,'test2','ca va'),(445,'test2','test'),(446,'salutsalut','ca'),(447,'salutsalut','va'),(448,'salutsalut','salut comment tu vas'),(449,'salutsalut','bien et toi'),(450,'test2','dada'),(451,'test2','da'),(452,'test2','dede'),(453,'test2','de'),(454,'test2','dedada'),(455,'test2','dada'),(456,'test2','dede'),(457,'test2','dedeada'),(458,'test2','dededece'),(459,'salutsalut','dede'),(460,'salutsalut','dead'),(461,'test2','dada'),(462,'test2','dede'),(463,'salutsalut','dede'),(464,'salutsalut','deada'),(465,'test2','dede'),(466,'test2','dead'),(467,'test2','dada'),(468,'test2','dada'),(469,'test2','da'),(470,'test2','deda'),(471,'test2','dea'),(472,'salutsalut','deada'),(473,'test2','dedea'),(474,'test2','deadae'),(475,'test2','ddead'),(476,'test2','dada'),(477,'test2','deada'),(478,'cesar@cesar.com','dede'),(479,'test2','sa'),(480,'test2','dada'),(481,'salutsalut','salut'),(482,'test2','cocucou'),(483,'salutsalut','xsxs'),(484,'test2','cdcd'),(485,'test2','sa'),(486,'test2','sa'),(487,'test2','ca'),(488,'test2','va'),(489,'test2','de'),(490,'test2','de'),(491,'test2','de'),(492,'test2','dza'),(493,'test2','daz'),(494,'test2','dada'),(495,'test2','dea'),(496,'test2','dead'),(497,'test2','deacd'),(498,'salutsalut','salut'),(499,'test2','test2'),(500,'salutsalut','test'),(501,'test2','test'),(502,'test2','test'),(503,'salutsalut','test'),(504,'test2','saa'),(505,'salutsalut','sa'),(506,'test2','da'),(507,'salutsalut','de'),(508,'test2','dede'),(509,'test2','test'),(510,'test2','test2'),(511,'salutsalut','test'),(512,'test2','dede'),(513,'salutsalut','dede'),(514,'test2','cava'),(515,'test2','cava'),(516,'test2','cacaerde'),(517,'salutsalut','dedada'),(518,'salutsalut','deada');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'test','test','',''),(2,'test','test','',''),(3,'erere','derder','',''),(4,'erere','derder','',''),(5,'','','test2','test2'),(6,'test3','test3','',''),(7,'test4','test4','',''),(8,'cez','cez','',''),(9,'Jean','Charles','',''),(10,'avc','vede','c',''),(11,'seara','ezar','sas',''),(12,'saa','saaaa','',''),(13,'','','',''),(14,'','','',''),(15,'ca','va','',''),(16,'ca','va','',''),(17,'salutsalut','salutsalut','dedec',''),(18,'salutsalut2','salutsalut2','salutsalut','salutsalut'),(19,'edede','dzzd','',''),(20,'edede','dzzdearda','caada','deardaerde'),(21,'ededezadea','dzzdeardazed','caada','deardaerde'),(22,'daze','dazed','daz',''),(23,'dazedear','dazeddaer','daz',''),(24,'dazedearazder','dazeddaerdazer','dazaerda','zeadrazer'),(25,'dazedearazderdazer','dazeddaerdazeradzerd','dazaerda','zeadrazer'),(26,'cesar','cesar','cesar@cesar.com','cesar');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-21 15:13:01
