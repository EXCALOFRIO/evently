-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: localhost    Database: evently
-- ------------------------------------------------------
-- Server version	8.0.30-0ubuntu0.22.04.1

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
-- Table structure for table `discotecas`
--

DROP TABLE IF EXISTS `discotecas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discotecas` (
  `nombre` varchar(100) NOT NULL,
  `calle` varchar(100) NOT NULL,
  `numero` int DEFAULT NULL,
  `zona` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discotecas`
--

LOCK TABLES `discotecas` WRITE;
/*!40000 ALTER TABLE `discotecas` DISABLE KEYS */;
INSERT INTO `discotecas` VALUES ('B12','C. de Joaquín Costa',27,'Tetuán'),('Blackhouse','Ctra. de La Coruña',0,'MoncloaAravaca'),('Fabrik','Av. de la Industria',82,'Humanes'),('Gunilla Club','Paseo de Recoletos',16,'Salamanca'),('Independance Club','C. de Atocha',127,'Centro'),('Joy Eslava','C. del Arenal',11,'Centro'),('Kapital','Calle de Atocha',125,'Centro'),('La Riviera','Paseo Bajo de la Virgen del Puerto',0,'Moncloa-Aravaca'),('Lemon','C. de Orense',14,'Tetuán'),('Medias Puri','Pl. de Tirso de Molina',1,'Centro'),('Nazca','C. de Orense',24,'Tetuán'),('Nuit','C. de Orense',10,'Tetuán'),('Opium','Cale de Jose Abascal',56,'Castellana'),('Panda','C. de Hernani',75,'Tetuán'),('Posh Club','Calle de Orense',18,'Tetuán'),('Shoko','C. de Toledo',86,'Centro'),('Teatro Barceló','C. de Barceló',11,'Chamberi'),('Thundercart Club','C. de Campoamor',11,'Chamberi'),('Tiffanys','Av. del Dr. Arce',10,'Tetuán'),('Uñas Chung Lee','C. de Hilarión Eslava',38,'Chamberi'),('Velvet','C. de Jacometrezo',6,'Centro');
/*!40000 ALTER TABLE `discotecas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `usuario` varchar(100) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(30) NOT NULL,
  `e-mail` varchar(50) NOT NULL,
  `contrseña` varchar(255) NOT NULL,
  `edad` int NOT NULL,
  PRIMARY KEY (`usuario`),
  UNIQUE KEY `e-mail` (`e-mail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `valoraciones`
--

DROP TABLE IF EXISTS `valoraciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `valoraciones` (
  `nombre_discoteca` varchar(100) NOT NULL,
  `nota` int NOT NULL,
  `texto` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`nombre_discoteca`),
  CONSTRAINT `valoraciones_ibfk_1` FOREIGN KEY (`nombre_discoteca`) REFERENCES `discotecas` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `valoraciones`
--

LOCK TABLES `valoraciones` WRITE;
/*!40000 ALTER TABLE `valoraciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `valoraciones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-01 12:09:59
