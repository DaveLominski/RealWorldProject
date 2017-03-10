# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.6.33)
# Database: Real-World
# Generation Time: 2017-03-10 09:53:05 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table EffectAreas
# ------------------------------------------------------------

DROP TABLE IF EXISTS `EffectAreas`;

CREATE TABLE `EffectAreas` (
  `areaId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `areaType` varchar(30) NOT NULL DEFAULT '',
  PRIMARY KEY (`areaId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `EffectAreas` WRITE;
/*!40000 ALTER TABLE `EffectAreas` DISABLE KEYS */;

INSERT INTO `EffectAreas` (`areaId`, `areaType`)
VALUES
	(1,'Local'),
	(2,'Neighbours'),
	(3,'Global');

/*!40000 ALTER TABLE `EffectAreas` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table EffectDamages
# ------------------------------------------------------------

DROP TABLE IF EXISTS `EffectDamages`;

CREATE TABLE `EffectDamages` (
  `effectId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `happiness` float NOT NULL DEFAULT '0',
  `population` float NOT NULL DEFAULT '0',
  `inequalities` float NOT NULL DEFAULT '0',
  `health` float NOT NULL DEFAULT '0',
  `income` float NOT NULL DEFAULT '0',
  `food` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`effectId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `EffectDamages` WRITE;
/*!40000 ALTER TABLE `EffectDamages` DISABLE KEYS */;

INSERT INTO `EffectDamages` (`effectId`, `happiness`, `population`, `inequalities`, `health`, `income`, `food`)
VALUES
	(1,0,0,0,0,0,0),
	(2,0,0,0,0,0,0),
	(3,-0.1,-0.05,0,0,-0.2,0.15),
	(4,0.15,0.1,0,0.05,0,-0.2),
	(5,0,0,0,0,0,0),
	(6,0,0,0,0,0,0),
	(7,0,0,0,0,0,0),
	(8,0,0,0,0,0,0),
	(9,0,0,0,0,0,0),
	(10,0,0,0,0,0,0),
	(11,0,0,0,0,0,0),
	(12,0,0,0,0,0,0),
	(13,0,0,0,0,0,0),
	(14,0,0,0,0,0,0);

/*!40000 ALTER TABLE `EffectDamages` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table QuestionResults
# ------------------------------------------------------------

DROP TABLE IF EXISTS `QuestionResults`;

CREATE TABLE `QuestionResults` (
  `questionId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `effect_one` int(11) unsigned NOT NULL DEFAULT '0',
  `effect_two` int(11) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`questionId`),
  KEY `effectOne_EffectDamages` (`effect_one`),
  KEY `effectTwo_EffectDamages` (`effect_two`),
  CONSTRAINT `effectOne_EffectDamages` FOREIGN KEY (`effect_one`) REFERENCES `EffectDamages` (`effectId`),
  CONSTRAINT `effectTwo_EffectDamages` FOREIGN KEY (`effect_two`) REFERENCES `EffectDamages` (`effectId`),
  CONSTRAINT `questionId_Questions` FOREIGN KEY (`questionId`) REFERENCES `Questions` (`questionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `QuestionResults` WRITE;
/*!40000 ALTER TABLE `QuestionResults` DISABLE KEYS */;

INSERT INTO `QuestionResults` (`questionId`, `effect_one`, `effect_two`)
VALUES
	(1,1,2),
	(2,3,4),
	(3,5,6),
	(4,7,8),
	(5,9,10),
	(6,11,12),
	(7,13,14);

/*!40000 ALTER TABLE `QuestionResults` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table Questions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Questions`;

CREATE TABLE `Questions` (
  `questionId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `question` longtext NOT NULL,
  `desicion_one` varchar(255) NOT NULL DEFAULT '',
  `desicion_two` varchar(255) NOT NULL DEFAULT '',
  `effect_area` int(11) unsigned NOT NULL,
  PRIMARY KEY (`questionId`),
  KEY `effectArea_EffectAreas` (`effect_area`),
  CONSTRAINT `effectArea_EffectAreas` FOREIGN KEY (`effect_area`) REFERENCES `EffectAreas` (`areaId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `Questions` WRITE;
/*!40000 ALTER TABLE `Questions` DISABLE KEYS */;

INSERT INTO `Questions` (`questionId`, `question`, `desicion_one`, `desicion_two`, `effect_area`)
VALUES
	(1,'District F3 has the Flu and the closest District with medical supplies is District E3, what do you do?','Give no medical supplies','Give 20% of medical supplies',1),
	(2,'In District F1, a peasant was found stealing food from the food warehouse. What would you like to do with him?','Hang the peasant','Let the peasant go',2),
	(3,'There has been a conflict between districts F1 and E2. They are arguing about your decision of unequal splitting of finances. District F1 has wealthy people and requires more money. What shall we do ?','Support District F1','Support District E2',1),
	(4,'There has been a major fire in the Military District and we are susceptible to an attack. What are your orders ?','Do not help the military.','Send the necessary resources to help.',1),
	(5,'Recently there have been Riot attacks in the capital and many citizens have been injured. What shall we do?','Bring in the military to stop the riots','Let the riots continue',1),
	(6,'Another civilization has abducted your brother and wants to make a deal with you. What is your decision?','Accept the deal','Go to war and get your brother back',1),
	(7,'The rich in poor from District E2 are stealing from rich in District F1. What do you want to do?','Support the poor','Punish the poor for theft',1);

/*!40000 ALTER TABLE `Questions` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
