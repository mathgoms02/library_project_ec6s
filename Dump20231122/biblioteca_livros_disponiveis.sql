-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: biblioteca
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `livros_disponiveis`
--

DROP TABLE IF EXISTS `livros_disponiveis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `livros_disponiveis` (
  `idLivro` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(500) DEFAULT NULL,
  `autor` varchar(500) DEFAULT NULL,
  `ano` varchar(4) DEFAULT NULL,
  `genero` varchar(100) DEFAULT NULL,
  `preco` float DEFAULT NULL,
  PRIMARY KEY (`idLivro`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `livros_disponiveis`
--

LOCK TABLES `livros_disponiveis` WRITE;
/*!40000 ALTER TABLE `livros_disponiveis` DISABLE KEYS */;
INSERT INTO `livros_disponiveis` VALUES (1,'Fahrenheit 451','Ray Bradbury','1953','Ficção',53.99),(2,'Dentro da Baleia e outros ensaios','George Orwell','1984','Drama',25.99),(3,'O Segredo das Estrelas','Lucas Silva','2019','Ficção Científica',19.99),(4,'Caminho para a Sabedoria','Maria Pereira','2017','Autoajuda',24.99),(5,'Amor em Paris','Carlos Almeida','2020','Romance',14.99),(6,'O Mistério da Mansão Sombria','Ana Santos','2018','Mistério',29.99),(7,'A Jornada do Herói','Pedro Martins','2021','Fantasia',16.99),(8,'Viagem ao Centro da Terra','Júlia Ferreira','2015','Aventura',22.99),(9,'Cidades Invisíveis','Luís Rodrigues','2016','Ficção',17.99),(10,'A Vida de Leonardo da Vinci','Mariana Ribeiro','2014','Biografia',12.99),(11,'O Poder do Hábito','Gustavo Oliveira','2022','Não-ficção',27.99),(12,'O Enigma do Tempo','Beatriz Silva','2019','Ficção Científica',19.99),(13,'A Arte da Guerra','Rafael Costa','2017','Autoajuda',24.99),(14,'Paixão Proibida','Isabel Pereira','2020','Romance',14.99),(15,'O Caso da Herança Perdida','Miguel Santos','2018','Mistério',29.99),(16,'A Busca pelo Santo Graal','Cláudia Almeida','2021','Fantasia',16.99),(17,'A Ilha Misteriosa','Ricardo Ferreira','2016','Aventura',22.99),(18,'O Labirinto dos Espíritos','Sofia Rodrigues','2014','Mistério',17.99),(19,'A História da Arte','João Ribeiro','2015','História',12.99),(20,'Steve Jobs: A Biografia','Ana Silva','2023','Biografia',27.99),(21,'O Poder da Mente','Gustavo Oliveira','2019','Autoajuda',19.99),(22,'O Último Homem na Terra','Laura Santos','2017','Ficção Científica',24.99),(23,'Amor e Destino','Carlos Pereira','2020','Romance',14.99),(24,'Assassinato no Expresso do Oriente','Miguel Almeida','2018','Mistério',29.99),(25,'A Profecia do Dragão','Sara Ferreira','2021','Fantasia',16.99),(26,'A Volta ao Mundo em 80 Dias','Daniel Ribeiro','2016','Aventura',22.99),(27,'O Código Da Vinci','Marta Rodrigues','2014','Mistério',17.99),(28,'O Livro dos Cinco Anéis','Filipe Almeida','2015','Filosofia',12.99),(29,'Madame Curie: Uma Vida','Eduarda Silva','2022','Biografia',27.99),(30,'O Poder do Pensamento Positivo','Rui Martins','2019','Autoajuda',19.99),(31,'20000 Léguas Submarinas','Inês Pereira','2017','Aventura',24.99),(32,'A Cidade das Sombras','Mário Ribeiro','2020','Ficção',14.99),(33,'Harry Potter e a Pedra Filosofal','J.K. Rowling','1997','Fantasia',29.99),(34,'Harry Potter e a Câmara Secreta','J.K. Rowling','1998','Fantasia',29.99),(35,'Harry Potter e o Prisioneiro de Azkaban','J.K. Rowling','1999','Fantasia',29.99),(36,'Harry Potter e o Cálice de Fogo','J.K. Rowling','2000','Fantasia',29.99),(37,'Harry Potter e a Ordem da Fênix','J.K. Rowling','2003','Fantasia',29.99),(38,'Harry Potter e o Enigma do Príncipe','J.K. Rowling','2005','Fantasia',29.99),(39,'Harry Potter e as Relíquias da Morte','J.K. Rowling','2007','Fantasia',29.99),(40,'Animais Fantásticos e Onde Habitam','Newt Scamander','2001','Fantasia',24.99),(41,'Quadribol Através dos Séculos','Kennilworthy Whisp','2001','Fantasia',24.99),(42,'Os Contos de Beedle, o Bardo','Beedle, o Bardo','2008','Fantasia',24.99),(43,'A Criança Amaldiçoada','J.K. Rowling','2016','Fantasia',29.99),(44,'Quadribol Através dos Tempos','J.K. Rowling','2018','Fantasia',24.99),(45,'Os Contos de Beedle, o Bardo','J.K. Rowling','2018','Fantasia',24.99),(46,'Magia do Mundo Bruxo de J.K. Rowling','J.K. Rowling','2016','Fantasia',24.99),(47,'Harry Potter e o Legado Maldito','J.K. Rowling','2016','Fantasia',29.99),(48,'Harry Potter: Guia Cinematográfico','Brian Sibley','2017','Fantasia',24.99),(49,'Harry Potter: As Crônicas','J.K. Rowling','2020','Fantasia',29.99),(50,'Animais Fantásticos e Onde Habitam','J.K. Rowling','2016','Fantasia',24.99),(51,'Quadribol Através dos Séculos','J.K. Rowling','2016','Fantasia',24.99),(52,'Os Contos de Beedle, o Bardo','J.K. Rowling','2016','Fantasia',24.99);
/*!40000 ALTER TABLE `livros_disponiveis` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-22 16:16:30
