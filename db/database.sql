-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: data
-- ------------------------------------------------------
-- Server version	5.7.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS data;
USE data;

--
-- Table structure for table `tv_show`
--

DROP TABLE IF EXISTS `tv_show`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tv_show` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `show_name` varchar(255) NOT NULL,
  `score` float(2,1) DEFAULT NULL,
  `release_date` year(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tv_show`
--

LOCK TABLES `tv_show` WRITE;
/*!40000 ALTER TABLE `tv_show` DISABLE KEYS */;
INSERT INTO `tv_show` VALUES (1,'The Filthy Frank Show',9.7,2011),(2,'Game of Thrones',9.5,2011),(3,'Breaking Bad',9.5,2008),(4,'Rick and Morty',9.3,2013),(5,'The Wire',9.3,2002),(6,'Cosmos A Spacetime Odyssey',9.3,2014),(7,'Cosmos',9.3,1980),(8,'Sherlock',9.2,2010),(9,'The Sopranos',9.2,1999),(10,'Avatar The Last Airbender',9.2,2003),(11,'Jogos Sagrados',9.1,2018),(12,'True Detective',9.0,2014),(13,'Fargo',9.0,2014),(14,'Last Week Tonight with John Oliver',9.0,2014),(15,'The Twilight Zone',9.0,1959),(16,'Firefly',9.0,2002),(17,'Stranger Things',8.9,2016),(18,'Friends',8.9,1994),(19,'Westworld',8.9,2016),(20,'House of Cards',8.9,2013),(21,'Narcos',8.9,2015),(22,'Seinfeld',8.9,1989),(23,'Arrested Development',8.9,2003),(24,'Cobra Kai',8.9,2018),(25,'Gravity Falls',8.9,2012),(26,'Batman The Animated Series',8.9,1992),(27,'It\'s Always Sunny in Philadelphia',8.8,2005),(28,'The Office',8.8,2005),(29,'This Is Us',8.8,2016),(30,'House',8.8,2004),(31,'Twin Peaks',8.8,1990),(32,'Rome',8.8,2005),(33,'Freaks and Geeks',8.8,1999),(34,'Nathan for You',8.8,2013),(35,'Shameless',8.7,2011),(36,'Better Call Saul',8.7,2015),(37,'The Marvelous Mrs Maisel',8.7,2017),(38,'The Crown',8.7,2016),(39,'Daredevil',8.7,2015),(40,'South Park',8.7,1997),(41,'Dexter',8.7,2006),(42,'The Punisher',8.7,2017),(43,'The X Files',8.7,1993),(44,'The Simpsons',8.7,1989),(45,'Archer',8.7,2009),(46,'The West Wing',8.7,1999),(47,'Friday Night Lights',8.7,2006),(48,'Curb Your Enthusiasm',8.7,2000),(49,'Deadwood',8.7,2004),(50,'Battlestar Galactica',8.7,2004);
/*!40000 ALTER TABLE `tv_show` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-26  1:59:29
