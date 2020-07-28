-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cricketfantasy
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `match1`
--

DROP TABLE IF EXISTS `match1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match1` (
  `player_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `scored` tinyint(3) unsigned NOT NULL,
  `faced` tinyint(3) unsigned NOT NULL,
  `fours` tinyint(3) unsigned NOT NULL,
  `sixes` tinyint(3) unsigned NOT NULL,
  `bowled` tinyint(3) unsigned NOT NULL,
  `maiden` tinyint(3) unsigned NOT NULL,
  `runs_given` tinyint(3) unsigned NOT NULL,
  `wkts` tinyint(3) unsigned NOT NULL,
  `catches` tinyint(3) unsigned NOT NULL,
  `stumping` tinyint(3) unsigned NOT NULL,
  `runout` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`player_id`),
  CONSTRAINT `player_id_1` FOREIGN KEY (`player_id`) REFERENCES `stats` (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match1`
--

LOCK TABLES `match1` WRITE;
/*!40000 ALTER TABLE `match1` DISABLE KEYS */;
INSERT INTO `match1` VALUES (1,91,97,8,2,0,0,0,0,0,0,1),(2,75,62,10,4,30,1,45,2,0,1,0),(3,49,75,4,0,0,0,0,0,1,0,0),(4,32,35,4,0,0,0,0,0,0,0,0),(5,56,45,3,1,0,0,0,0,1,1,0),(6,8,4,2,0,48,2,35,1,0,0,0),(7,42,36,3,3,30,0,25,0,1,0,0),(8,18,10,1,1,60,3,50,2,1,0,1),(9,65,60,7,0,0,0,0,0,0,0,1),(10,0,0,0,0,24,1,8,4,0,0,0),(11,2,5,0,0,24,2,37,2,0,0,1),(12,0,0,0,0,18,1,10,3,0,0,0),(13,15,12,2,0,12,0,6,1,0,0,0),(14,60,47,5,2,0,0,0,0,1,0,0),(15,29,42,3,0,0,0,0,0,2,0,1),(16,42,32,2,1,0,0,0,0,2,0,0),(17,20,20,2,0,24,1,13,2,1,0,0),(18,51,60,7,1,6,0,15,0,0,0,1),(19,46,52,6,1,0,0,0,0,2,0,0),(20,12,15,1,0,12,1,21,2,0,0,0);
/*!40000 ALTER TABLE `match1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `match2`
--

DROP TABLE IF EXISTS `match2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match2` (
  `player_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `scored` tinyint(3) unsigned NOT NULL,
  `faced` tinyint(3) unsigned NOT NULL,
  `fours` tinyint(3) unsigned NOT NULL,
  `sixes` tinyint(3) unsigned NOT NULL,
  `bowled` tinyint(3) unsigned NOT NULL,
  `maiden` tinyint(3) unsigned NOT NULL,
  `runs_given` tinyint(3) unsigned NOT NULL,
  `wkts` tinyint(3) unsigned NOT NULL,
  `catches` tinyint(3) unsigned NOT NULL,
  `stumping` tinyint(3) unsigned NOT NULL,
  `runout` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match2`
--

LOCK TABLES `match2` WRITE;
/*!40000 ALTER TABLE `match2` DISABLE KEYS */;
INSERT INTO `match2` VALUES (1,121,102,14,4,0,0,0,0,2,0,0),(2,75,62,10,4,18,1,21,2,0,0,0),(3,49,75,4,0,0,0,0,0,1,0,0),(4,32,35,4,0,0,0,0,0,0,0,0),(5,67,58,7,6,0,0,0,0,0,2,0),(6,41,38,6,1,12,1,18,1,0,0,1),(7,42,36,3,3,21,0,8,3,0,0,0),(8,18,10,1,1,12,0,23,1,0,0,1),(9,32,38,4,0,0,0,0,0,0,0,1),(10,0,0,0,0,24,1,8,4,0,0,0),(11,2,5,0,0,24,2,37,2,0,0,1),(12,0,0,0,0,18,1,10,3,0,0,0),(13,1,2,0,0,12,0,6,1,0,0,0),(14,15,32,1,0,0,0,0,0,1,0,0),(15,37,56,3,0,0,0,0,0,0,1,1),(16,98,110,12,4,0,0,0,0,0,0,1),(17,54,58,8,1,12,0,5,0,1,0,0),(18,21,16,7,1,6,0,15,0,0,0,1),(19,46,52,6,1,0,0,0,0,2,0,0),(20,0,0,0,0,18,1,32,3,0,0,0);
/*!40000 ALTER TABLE `match2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `match3`
--

DROP TABLE IF EXISTS `match3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match3` (
  `player_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `scored` tinyint(3) unsigned NOT NULL,
  `faced` tinyint(3) unsigned NOT NULL,
  `fours` tinyint(3) unsigned NOT NULL,
  `sixes` tinyint(3) unsigned NOT NULL,
  `bowled` tinyint(3) unsigned NOT NULL,
  `maiden` tinyint(3) unsigned NOT NULL,
  `runs_given` tinyint(3) unsigned NOT NULL,
  `wkts` tinyint(3) unsigned NOT NULL,
  `catches` tinyint(3) unsigned NOT NULL,
  `stumping` tinyint(3) unsigned NOT NULL,
  `runout` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match3`
--

LOCK TABLES `match3` WRITE;
/*!40000 ALTER TABLE `match3` DISABLE KEYS */;
INSERT INTO `match3` VALUES (1,91,97,8,2,0,0,0,0,0,0,1),(2,75,62,10,4,30,1,45,2,0,1,0),(3,49,75,4,0,0,0,0,0,1,0,0),(4,32,35,4,0,0,0,0,0,0,0,0),(5,56,45,3,1,0,0,0,0,1,1,0),(6,8,4,2,0,48,2,35,1,0,0,0),(7,42,36,3,3,30,0,25,0,1,0,0),(8,18,10,1,1,60,3,50,2,1,0,1),(9,65,60,7,0,0,0,0,0,0,0,1),(10,0,0,0,0,24,1,8,4,0,0,0),(11,2,5,0,0,24,2,37,2,0,0,1),(12,0,0,0,0,18,1,10,3,0,0,0),(13,15,12,2,0,12,0,6,1,0,0,0),(14,60,47,5,2,0,0,0,0,1,0,0),(15,29,42,3,0,0,0,0,0,2,0,1),(16,42,32,2,1,0,0,0,0,2,0,0),(17,20,20,2,0,24,1,13,2,1,0,0),(18,51,60,7,1,6,0,15,0,0,0,1),(19,46,52,6,1,0,0,0,0,2,0,0),(20,12,15,1,0,12,1,21,2,0,0,0);
/*!40000 ALTER TABLE `match3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `match4`
--

DROP TABLE IF EXISTS `match4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match4` (
  `player_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `scored` tinyint(3) unsigned NOT NULL,
  `faced` tinyint(3) unsigned NOT NULL,
  `fours` tinyint(3) unsigned NOT NULL,
  `sixes` tinyint(3) unsigned NOT NULL,
  `bowled` tinyint(3) unsigned NOT NULL,
  `maiden` tinyint(3) unsigned NOT NULL,
  `runs_given` tinyint(3) unsigned NOT NULL,
  `wkts` tinyint(3) unsigned NOT NULL,
  `catches` tinyint(3) unsigned NOT NULL,
  `stumping` tinyint(3) unsigned NOT NULL,
  `runout` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match4`
--

LOCK TABLES `match4` WRITE;
/*!40000 ALTER TABLE `match4` DISABLE KEYS */;
INSERT INTO `match4` VALUES (1,121,102,14,4,0,0,0,0,2,0,0),(2,75,62,10,4,18,1,21,2,0,0,0),(3,49,75,4,0,0,0,0,0,1,0,0),(4,32,35,4,0,0,0,0,0,0,0,0),(5,67,58,7,6,0,0,0,0,0,2,0),(6,41,38,6,1,12,1,18,1,0,0,1),(7,42,36,3,3,21,0,8,3,0,0,0),(8,18,10,1,1,12,0,23,1,0,0,1),(9,32,38,4,0,0,0,0,0,0,0,1),(10,0,0,0,0,24,1,8,4,0,0,0),(11,2,5,0,0,24,2,37,2,0,0,1),(12,0,0,0,0,18,1,10,3,0,0,0),(13,1,2,0,0,12,0,6,1,0,0,0),(14,15,32,1,0,0,0,0,0,1,0,0),(15,37,56,3,0,0,0,0,0,0,1,1),(16,98,110,12,4,0,0,0,0,0,0,1),(17,54,58,8,1,12,0,5,0,1,0,0),(18,21,16,7,1,6,0,15,0,0,0,1),(19,46,52,6,1,0,0,0,0,2,0,0),(20,0,0,0,0,18,1,32,3,0,0,0);
/*!40000 ALTER TABLE `match4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `match5`
--

DROP TABLE IF EXISTS `match5`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match5` (
  `player_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `scored` tinyint(3) unsigned NOT NULL,
  `faced` tinyint(3) unsigned NOT NULL,
  `fours` tinyint(3) unsigned NOT NULL,
  `sixes` tinyint(3) unsigned NOT NULL,
  `bowled` tinyint(3) unsigned NOT NULL,
  `maiden` tinyint(3) unsigned NOT NULL,
  `runs_given` tinyint(3) unsigned NOT NULL,
  `wkts` tinyint(3) unsigned NOT NULL,
  `catches` tinyint(3) unsigned NOT NULL,
  `stumping` tinyint(3) unsigned NOT NULL,
  `runout` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match5`
--

LOCK TABLES `match5` WRITE;
/*!40000 ALTER TABLE `match5` DISABLE KEYS */;
INSERT INTO `match5` VALUES (1,91,97,8,2,0,0,0,0,0,0,1),(2,75,62,10,4,30,1,45,2,0,1,0),(3,49,75,4,0,0,0,0,0,1,0,0),(4,32,35,4,0,0,0,0,0,0,0,0),(5,56,45,3,1,0,0,0,0,1,1,0),(6,8,4,2,0,48,2,35,1,0,0,0),(7,42,36,3,3,30,0,25,0,1,0,0),(8,18,10,1,1,60,3,50,2,1,0,1),(9,65,60,7,0,0,0,0,0,0,0,1),(10,0,0,0,0,24,1,8,4,0,0,0),(11,2,5,0,0,24,2,37,2,0,0,1),(12,0,0,0,0,18,1,10,3,0,0,0),(13,15,12,2,0,12,0,6,1,0,0,0),(14,60,47,5,2,0,0,0,0,1,0,0),(15,29,42,3,0,0,0,0,0,2,0,1),(16,42,32,2,1,0,0,0,0,2,0,0),(17,20,20,2,0,24,1,13,2,1,0,0),(18,51,60,7,1,6,0,15,0,0,0,1),(19,46,52,6,1,0,0,0,0,2,0,0),(20,12,15,1,0,12,1,21,2,0,0,0);
/*!40000 ALTER TABLE `match5` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stats`
--

DROP TABLE IF EXISTS `stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stats` (
  `player_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `matches` smallint(5) unsigned NOT NULL,
  `runs` smallint(5) unsigned NOT NULL,
  `100s` tinyint(3) unsigned NOT NULL,
  `50s` tinyint(3) unsigned NOT NULL,
  `overs` smallint(5) unsigned NOT NULL,
  `wickets` tinyint(3) unsigned NOT NULL,
  `4wick` tinyint(3) unsigned NOT NULL,
  `5wick` tinyint(3) unsigned NOT NULL,
  `player_value` tinyint(3) unsigned NOT NULL,
  `ctg` varchar(5) NOT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stats`
--

LOCK TABLES `stats` WRITE;
/*!40000 ALTER TABLE `stats` DISABLE KEYS */;
INSERT INTO `stats` VALUES (1,'Kohli',177,5412,5,36,41,4,0,0,98,'BAT'),(2,'Yuvraj',132,2750,0,13,140,36,2,0,95,'AR'),(3,'Rahane',140,3820,2,27,1,1,0,0,93,'BAT'),(4,'Dhawan',159,4579,0,37,8,4,0,0,95,'BAT'),(5,'Dhoni',190,4432,0,23,0,157,0,0,97,'WK'),(6,'Axar',82,796,0,0,285,71,1,0,88,'AR'),(7,'Pandya',66,1068,0,3,144,42,0,0,90,'AR'),(8,'Jadeja',170,1927,0,0,415,108,3,1,92,'AR'),(9,'Kedar',79,1079,0,4,0,0,0,0,85,'BAT'),(10,'Ashwin',139,375,0,0,487,125,1,0,88,'BWL'),(11,'Umesh',296,122,0,0,413,119,2,0,91,'BWL'),(12,'Bumrah',77,35,0,0,288,82,0,0,92,'BWL'),(13,'Bhuwaneshwar',117,183,0,0,435,133,2,1,94,'BWL'),(14,'Rohit',188,4898,1,36,55,15,1,0,88,'BAT'),(15,'Kartik',182,3654,0,18,0,152,0,0,86,'WK'),(16,'Rahul',67,1977,1,16,0,0,0,0,88,'BAT'),(17,'Raina',193,5368,1,38,32,25,0,0,90,'AR'),(18,'Krunal',55,891,0,1,157,40,0,0,85,'AR'),(19,'Pant',54,1736,1,11,0,47,0,0,91,'WK'),(20,'Chahal',84,21,0,0,297,100,2,0,92,'BWL');
/*!40000 ALTER TABLE `stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teams` (
  `name` varchar(50) NOT NULL DEFAULT 'Team_NA',
  `players` varchar(300) NOT NULL,
  `team_value` smallint(6) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES ('MyTeam','Rohit,Kohli,Dhawan,Rahul,Pant,Yuvraj,Pandya,Bumrah,Ashwin,Chahal,Bhuwaneshwar',1011),('MyTeam2','Rohit,Kohli,Dhawan,Rahul,Pant,Yuvraj,Pandya,Bumrah,Ashwin,Axar,Jadeja',1005),('ShauryaG','Rohit,Kohli,Dhawan,Rahul,Pant,Yuvraj,Bumrah,Ashwin,Axar,Pandya,Jadeja',1005);
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-27  1:22:31
