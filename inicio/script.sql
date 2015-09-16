CREATE DATABASE  IF NOT EXISTS `db_mtvmcotizacion` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
USE `db_mtvmcotizacion`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: db_mtvmcotizacion
-- ------------------------------------------------------
-- Server version   5.6.21-log

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

--
-- Table structure for table `ambiente_ambiente`
--

DROP TABLE IF EXISTS `ambiente_ambiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ambiente_ambiente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ambiente` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ambiente_ambiente`
--

LOCK TABLES `ambiente_ambiente` WRITE;
/*!40000 ALTER TABLE `ambiente_ambiente` DISABLE KEYS */;
INSERT INTO `ambiente_ambiente` VALUES (1,'Atico'),(2,'Baño principal'),(3,'Baño auxiliar'),(4,'Baño de visitas'),(5,'Baulera'),(6,'Bodega'),(7,'Cocina'),(8,'Comedor principal'),(9,'Comedor diario'),(10,'Escritorio / Oficce'),(11,'Habitación principal'),(12,'Habitación auxiliar'),(13,'Habitación de Servicio'),(14,'Hall de entrada'),(15,'Jardin delantero'),(16,'Jardin trasero'),(17,'Lavadero'),(18,'Living'),(19,'Living - Comedor'),(20,'Patio'),(21,'Playroom'),(22,'Sala de TV / Cine'),(23,'Sótano'),(24,'Garage');
/*!40000 ALTER TABLE `ambiente_ambiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ambiente_ambiente_tipo_inmueble`
--

DROP TABLE IF EXISTS `ambiente_ambiente_tipo_inmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ambiente_ambiente_tipo_inmueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ambiente_id` int(11) NOT NULL,
  `tipo_inmueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `ambiente_ambiente_tipo_inmueble_ambiente_id_7ba7a4df_uniq` (`ambiente_id`,`tipo_inmueble_id`) USING BTREE,
  KEY `ambiente_ambiente_tipo_inmueble_672bf590` (`ambiente_id`) USING BTREE,
  KEY `ambiente_ambiente_tipo_inmueble_0a525c68` (`tipo_inmueble_id`) USING BTREE,
  CONSTRAINT `ambiente_ambiente_t_ambiente_id_1a2e0d98_fk_ambiente_ambiente_id` FOREIGN KEY (`ambiente_id`) REFERENCES `ambiente_ambiente` (`id`),
  CONSTRAINT `ambiente_tipo_inmueble_id_1ecea4b5_fk_direccion_tipo_inmueble_id` FOREIGN KEY (`tipo_inmueble_id`) REFERENCES `direccion_tipo_inmueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ambiente_ambiente_tipo_inmueble`
--

LOCK TABLES `ambiente_ambiente_tipo_inmueble` WRITE;
/*!40000 ALTER TABLE `ambiente_ambiente_tipo_inmueble` DISABLE KEYS */;
INSERT INTO `ambiente_ambiente_tipo_inmueble` VALUES (1,1,1),(3,2,2),(2,4,1),(4,11,1),(5,12,1);
/*!40000 ALTER TABLE `ambiente_ambiente_tipo_inmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `group_id` (`group_id`,`permission_id`) USING BTREE,
  KEY `auth_group_permissions_0e939a4f` (`group_id`) USING BTREE,
  KEY `auth_group_permissions_8373b171` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissi_permission_id_7e336f96_fk_auth` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_1bb1e253_fk_auth_g` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`) USING BTREE,
  KEY `auth_permission_417f1b1c` (`content_type_id`) USING BTREE,
  CONSTRAINT `auth_permissi_content_type_id_5e820315_fk_django_c` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=199 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add Pais',7,'add_pais'),(20,'Can change Pais',7,'change_pais'),(21,'Can delete Pais',7,'delete_pais'),(22,'Can add Provincia',8,'add_provincia'),(23,'Can change Provincia',8,'change_provincia'),(24,'Can delete Provincia',8,'delete_provincia'),(25,'Can add Ciudad',9,'add_ciudad'),(26,'Can change Ciudad',9,'change_ciudad'),(27,'Can delete Ciudad',9,'delete_ciudad'),(28,'Can add Zona',10,'add_zona'),(29,'Can change Zona',10,'change_zona'),(30,'Can delete Zona',10,'delete_zona'),(31,'Can add Tipo de direccion',11,'add_tipo_direccion'),(32,'Can change Tipo de direccion',11,'change_tipo_direccion'),(33,'Can delete Tipo de direccion',11,'delete_tipo_direccion'),(34,'Can add Direccion',12,'add_direccion'),(35,'Can change Direccion',12,'change_direccion'),(36,'Can delete Direccion',12,'delete_direccion'),(37,'Can add Tipo de inmueble',13,'add_tipo_inmueble'),(38,'Can change Tipo de inmueble',13,'change_tipo_inmueble'),(39,'Can delete Tipo de inmueble',13,'delete_tipo_inmueble'),(40,'Can add complejidad del inmueble',14,'add_complejidad_inmueble'),(41,'Can change complejidad del inmueble',14,'change_complejidad_inmueble'),(42,'Can delete complejidad del inmueble',14,'delete_complejidad_inmueble'),(46,'Can add Inmueble',16,'add_inmueble'),(47,'Can change Inmueble',16,'change_inmueble'),(48,'Can delete Inmueble',16,'delete_inmueble'),(52,'Can add Sexo',18,'add_sexo'),(53,'Can change Sexo',18,'change_sexo'),(54,'Can delete Sexo',18,'delete_sexo'),(55,'Can add Estado civil',19,'add_estado_civil'),(56,'Can change Estado civil',19,'change_estado_civil'),(57,'Can delete Estado civil',19,'delete_estado_civil'),(58,'Can add Cliente',20,'add_cliente'),(59,'Can change Cliente',20,'change_cliente'),(60,'Can delete Cliente',20,'delete_cliente'),(61,'Can add Email',21,'add_email'),(62,'Can change Email',21,'change_email'),(63,'Can delete Email',21,'delete_email'),(64,'Can add Tipo de telefono',22,'add_tipo_telefono'),(65,'Can change Tipo de telefono',22,'change_tipo_telefono'),(66,'Can delete Tipo de telefono',22,'delete_tipo_telefono'),(67,'Can add Telefono',23,'add_telefono'),(68,'Can change Telefono',23,'change_telefono'),(69,'Can delete Telefono',23,'delete_telefono'),(70,'Can add Ambiente',24,'add_ambiente'),(71,'Can change Ambiente',24,'change_ambiente'),(72,'Can delete Ambiente',24,'delete_ambiente'),(73,'Can add Ambiente por tipo inmueble',25,'add_ambiente_tipo_inmueble'),(74,'Can change Ambiente por tipo inmueble',25,'change_ambiente_tipo_inmueble'),(75,'Can delete Ambiente por tipo inmueble',25,'delete_ambiente_tipo_inmueble'),(76,'Can add servicio',26,'add_servicio'),(77,'Can change servicio',26,'change_servicio'),(78,'Can delete servicio',26,'delete_servicio'),(79,'Can add Material',27,'add_material'),(80,'Can change Material',27,'change_material'),(81,'Can delete Material',27,'delete_material'),(82,'Can add Material del Servicio',28,'add_servicio_material'),(83,'Can change Material del Servicio',28,'change_servicio_material'),(84,'Can delete Material del Servicio',28,'delete_servicio_material'),(85,'Can add Nivel de complejidad',29,'add_complejidad'),(86,'Can change Nivel de complejidad',29,'change_complejidad'),(87,'Can delete Nivel de complejidad',29,'delete_complejidad'),(88,'Can add Complejidad del Servicio',30,'add_complejidad_servicio'),(89,'Can change Complejidad del Servicio',30,'change_complejidad_servicio'),(90,'Can delete Complejidad del Servicio',30,'delete_complejidad_servicio'),(91,'Can add Tipo mueble',31,'add_tipo_mueble'),(92,'Can change Tipo mueble',31,'change_tipo_mueble'),(93,'Can delete Tipo mueble',31,'delete_tipo_mueble'),(94,'Can add Ocupacion',32,'add_ocupacion'),(95,'Can change Ocupacion',32,'change_ocupacion'),(96,'Can delete Ocupacion',32,'delete_ocupacion'),(97,'Can add Forma del Mueble',33,'add_forma_mueble'),(98,'Can change Forma del Mueble',33,'change_forma_mueble'),(99,'Can delete Forma del Mueble',33,'delete_forma_mueble'),(100,'Can add Mueble',34,'add_mueble'),(101,'Can change Mueble',34,'change_mueble'),(102,'Can delete Mueble',34,'delete_mueble'),(103,'Can add Tamano',35,'add_tamano'),(104,'Can change Tamano',35,'change_tamano'),(105,'Can delete Tamano',35,'delete_tamano'),(106,'Can add Densidad',36,'add_densidad'),(107,'Can change Densidad',36,'change_densidad'),(108,'Can delete Densidad',36,'delete_densidad'),(109,'Can add Tamano del mueble',37,'add_tamano_mueble'),(110,'Can change Tamano del mueble',37,'change_tamano_mueble'),(111,'Can delete Tamano del mueble',37,'delete_tamano_mueble'),(112,'Can add Mueble del Ambiente',38,'add_mueble_ambiente'),(113,'Can change Mueble del Ambiente',38,'change_mueble_ambiente'),(114,'Can delete Mueble del Ambiente',38,'delete_mueble_ambiente'),(118,'Can add contenido',40,'add_contenido'),(119,'Can change contenido',40,'change_contenido'),(120,'Can delete contenido',40,'delete_contenido'),(121,'Can add Contenido Tipico',41,'add_contenido_tipico'),(122,'Can change Contenido Tipico',41,'change_contenido_tipico'),(123,'Can delete Contenido Tipico',41,'delete_contenido_tipico'),(124,'Can add Cargo de trabajador',42,'add_cargo_trabajador'),(125,'Can change Cargo de trabajador',42,'change_cargo_trabajador'),(126,'Can delete Cargo de trabajador',42,'delete_cargo_trabajador'),(127,'Can add estado',43,'add_estado_cotizacion'),(128,'Can change estado',43,'change_estado_cotizacion'),(129,'Can delete estado',43,'delete_estado_cotizacion'),(130,'Can add tiempo de carga',44,'add_tiempo_carga'),(131,'Can change tiempo de carga',44,'change_tiempo_carga'),(132,'Can delete tiempo de carga',44,'delete_tiempo_carga'),(133,'Can add piso',45,'add_piso'),(134,'Can change piso',45,'change_piso'),(135,'Can delete piso',45,'delete_piso'),(136,'Can add Cotizacion',46,'add_cotizacion'),(137,'Can change Cotizacion',46,'change_cotizacion'),(138,'Can delete Cotizacion',46,'delete_cotizacion'),(139,'Can add Vehiculo',47,'add_vehiculo'),(140,'Can change Vehiculo',47,'change_vehiculo'),(141,'Can delete Vehiculo',47,'delete_vehiculo'),(142,'Can add Vehiculo de la cotizacion',48,'add_vehiculo_cotizacion'),(143,'Can change Vehiculo de la cotizacion',48,'change_vehiculo_cotizacion'),(144,'Can delete Vehiculo de la cotizacion',48,'delete_vehiculo_cotizacion'),(145,'Can add direccion de la cotizacion',49,'add_cotizacion_direccion'),(146,'Can change direccion de la cotizacion',49,'change_cotizacion_direccion'),(147,'Can delete direccion de la cotizacion',49,'delete_cotizacion_direccion'),(148,'Can add trabajador de la cotizacion',50,'add_cotizacion_trabajador'),(149,'Can change trabajador de la cotizacion',50,'change_cotizacion_trabajador'),(150,'Can delete trabajador de la cotizacion',50,'delete_cotizacion_trabajador'),(151,'Can add Ambiente de la cotizacion',51,'add_cotizacion_ambiente'),(152,'Can change Ambiente de la cotizacion',51,'change_cotizacion_ambiente'),(153,'Can delete Ambiente de la cotizacion',51,'delete_cotizacion_ambiente'),(154,'Can add Mueble del Ambiente',52,'add_cotizacion_mueble'),(155,'Can change Mueble del Ambiente',52,'change_cotizacion_mueble'),(156,'Can delete Mueble del Ambiente',52,'delete_cotizacion_mueble'),(157,'Can add Servicio del mueble',53,'add_cotizacion_servicio'),(158,'Can change Servicio del mueble',53,'change_cotizacion_servicio'),(159,'Can delete Servicio del mueble',53,'delete_cotizacion_servicio'),(160,'Can add Material del mueble',54,'add_cotizacion_material'),(161,'Can change Material del mueble',54,'change_cotizacion_material'),(162,'Can delete Material del mueble',54,'delete_cotizacion_material'),(166,'Can add contenido en el contenedor',56,'add_cotizacion_contenido'),(167,'Can change contenido en el contenedor',56,'change_cotizacion_contenido'),(168,'Can delete contenido en el contenedor',56,'delete_cotizacion_contenido'),(169,'Can add Unidad',57,'add_unidad'),(170,'Can change Unidad',57,'change_unidad'),(171,'Can delete Unidad',57,'delete_unidad'),(172,'Can add Contenido Servicio',58,'add_contenido_servicio'),(173,'Can change Contenido Servicio',58,'change_contenido_servicio'),(174,'Can delete Contenido Servicio',58,'delete_contenido_servicio'),(175,'Can add Presupuesto',59,'add_presupuesto'),(176,'Can change Presupuesto',59,'change_presupuesto'),(177,'Can delete Presupuesto',59,'delete_presupuesto'),(178,'Can add direccion del presupuesto',60,'add_presupuesto_direccion'),(179,'Can change direccion del presupuesto',60,'change_presupuesto_direccion'),(180,'Can delete direccion del presupuesto',60,'delete_presupuesto_direccion'),(181,'Can add detalle del presupuesto',61,'add_presupuesto_detalle'),(182,'Can change detalle del presupuesto',61,'change_presupuesto_detalle'),(183,'Can delete detalle del presupuesto',61,'delete_presupuesto_detalle'),(184,'Can add Servicio',62,'add_presupuesto_servicio'),(185,'Can change Servicio',62,'change_presupuesto_servicio'),(186,'Can delete Servicio',62,'delete_presupuesto_servicio'),(187,'Can add Dato Precargado',63,'add_datosprecargado'),(188,'Can change Dato Precargado',63,'change_datosprecargado'),(189,'Can delete Dato Precargado',63,'delete_datosprecargado'),(190,'Can add empresa',64,'add_empresa'),(191,'Can change empresa',64,'change_empresa'),(192,'Can delete empresa',64,'delete_empresa'),(193,'Can see presupuesto',59,'see_presupuestoitem'),(194,'Can see detalle del presupuesto',61,'see_detallepresupuestoitem'),(195,'Can see servicio',62,'see_servicioitem'),(196,'Can add fuente promocion',65,'add_fuentepromocion'),(197,'Can change fuente promocion',65,'change_fuentepromocion'),(198,'Can delete fuente promocion',65,'delete_fuentepromocion');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `email` varchar(254) COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `username` (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$4zJoFe6mK0or$zxdihjWlTMdLexABZc9VT2QjILitlt9+azwRX82vXHU=','2015-09-09 14:53:10.800128',1,'admin','','','yusnelvy@gmail.com',1,1,'2015-06-18 21:19:32'),(2,'pbkdf2_sha256$20000$CSQ4ootz6pL0$R5m7W/+sk9L5mj1ZUXRJOy6D2d3qxOEQDOMlgXiZcM0=','2015-09-03 20:23:36.558202',0,'yusnelvy','yusnelvy','Arrieche','yusnelvy@gmail.com',0,1,'2015-07-09 19:32:22');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `user_id` (`user_id`,`group_id`) USING BTREE,
  KEY `auth_user_groups_e8701ad4` (`user_id`) USING BTREE,
  KEY `auth_user_groups_0e939a4f` (`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_17160da7_fk_auth_group_i` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_3d0d766f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `user_id` (`user_id`,`permission_id`) USING BTREE,
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`) USING BTREE,
  KEY `auth_user_user_permissions_8373b171` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_perm_permission_id_267ceb85_fk_auth` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_1cf43736_fk_aut` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_cliente`
--

DROP TABLE IF EXISTS `cliente_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_principal` varchar(250) COLLATE utf8_bin NOT NULL,
  `dni` varchar(15) COLLATE utf8_bin NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `comentarios` longtext COLLATE utf8_bin NOT NULL,
  `adicional1` varchar(50) COLLATE utf8_bin NOT NULL,
  `adicional2` varchar(50) COLLATE utf8_bin NOT NULL,
  `adicional3` varchar(50) COLLATE utf8_bin NOT NULL,
  `adicional4` varchar(50) COLLATE utf8_bin NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `estado_civil_id` int(11) NOT NULL,
  `sexo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cliente_cliente_5c2a6c5d` (`estado_civil_id`) USING BTREE,
  KEY `cliente_cliente_68bc6daa` (`sexo_id`) USING BTREE,
  CONSTRAINT `cliente_clie_estado_civil_id_2b598a50_fk_cliente_estado_civil_id` FOREIGN KEY (`estado_civil_id`) REFERENCES `cliente_estado_civil` (`id`),
  CONSTRAINT `cliente_cliente_sexo_id_278bb5c4_fk_cliente_sexo_id` FOREIGN KEY (`sexo_id`) REFERENCES `cliente_sexo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_cliente`
--

LOCK TABLES `cliente_cliente` WRITE;
/*!40000 ALTER TABLE `cliente_cliente` DISABLE KEYS */;
INSERT INTO `cliente_cliente` VALUES (1,'Yusnelvy Arrieche','17308789','2001-01-01','','','','','',1,1,1),(2,'Yohandri Miguel Ramírez Pérez','1','2001-01-01','Sin comentarios','','','','',1,1,1);
/*!40000 ALTER TABLE `cliente_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_email`
--

DROP TABLE IF EXISTS `cliente_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_email` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) COLLATE utf8_bin NOT NULL,
  `cliente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE,
  KEY `cliente_email_4a860110` (`cliente_id`) USING BTREE,
  CONSTRAINT `cliente_email_cliente_id_5d3d2700_fk_cliente_clien` FOREIGN KEY (`cliente_id`) REFERENCES `cliente_cliente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_email`
--

LOCK TABLES `cliente_email` WRITE;
/*!40000 ALTER TABLE `cliente_email` DISABLE KEYS */;
INSERT INTO `cliente_email` VALUES (1,'yusnelvy@gmail.com',1);
/*!40000 ALTER TABLE `cliente_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_estado_civil`
--

DROP TABLE IF EXISTS `cliente_estado_civil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_estado_civil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado_civil` varchar(25) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `estado_civil` (`estado_civil`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_estado_civil`
--

LOCK TABLES `cliente_estado_civil` WRITE;
/*!40000 ALTER TABLE `cliente_estado_civil` DISABLE KEYS */;
INSERT INTO `cliente_estado_civil` VALUES (2,'Casado'),(3,'Divorciado'),(6,'Otro'),(1,'Soltero'),(5,'Unión libre'),(4,'Viudo');
/*!40000 ALTER TABLE `cliente_estado_civil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_sexo`
--

DROP TABLE IF EXISTS `cliente_sexo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_sexo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sexo` varchar(25) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `sexo` (`sexo`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_sexo`
--

LOCK TABLES `cliente_sexo` WRITE;
/*!40000 ALTER TABLE `cliente_sexo` DISABLE KEYS */;
INSERT INTO `cliente_sexo` VALUES (1,'Femenino'),(2,'Masculino'),(3,'Otro');
/*!40000 ALTER TABLE `cliente_sexo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contenido_contenido`
--

DROP TABLE IF EXISTS `contenido_contenido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contenido_contenido` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contenido` varchar(100) COLLATE utf8_bin NOT NULL,
  `densidad_baja` decimal(7,2) NOT NULL,
  `densidad_media` decimal(7,2) NOT NULL,
  `densidad_alta` decimal(7,2) NOT NULL,
  `densidad_superalta` decimal(7,2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `contenido` (`contenido`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contenido_contenido`
--

LOCK TABLES `contenido_contenido` WRITE;
/*!40000 ALTER TABLE `contenido_contenido` DISABLE KEYS */;
INSERT INTO `contenido_contenido` VALUES (1,'Ropa',250.00,500.00,800.00,1200.00),(2,'Adornos',300.00,600.00,1000.00,1500.00),(3,'Vajilla',300.00,600.00,1000.00,1500.00),(4,'Juguetes',300.00,600.00,1000.00,1200.00),(5,'Impresos y papelería',250.00,500.00,750.00,1000.00),(6,'Joyas',500.00,750.00,1000.00,1500.00),(7,'Lencería',100.00,250.00,400.00,600.00),(8,'Herramientas y ferretería',1000.00,1500.00,2000.00,2500.00),(9,'Varios ligeros',250.00,500.00,750.00,1000.00),(10,'Varios pesados',1250.00,1500.00,1750.00,2000.00);
/*!40000 ALTER TABLE `contenido_contenido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contenido_contenido_servicio`
--

DROP TABLE IF EXISTS `contenido_contenido_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contenido_contenido_servicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `predefinido` tinyint(1) NOT NULL,
  `contenido_id` int(11) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `contenido_contenido_servicio_contenido_id_ee7e5ad_uniq` (`contenido_id`,`servicio_id`) USING BTREE,
  KEY `contenido_contenido_servicio_0a9ab757` (`contenido_id`) USING BTREE,
  KEY `contenido_contenido_servicio_4bb699dc` (`servicio_id`) USING BTREE,
  CONSTRAINT `contenido_conten_contenido_id_5e09a9bb_fk_contenido_contenido_id` FOREIGN KEY (`contenido_id`) REFERENCES `contenido_contenido` (`id`),
  CONSTRAINT `contenido_contenido_servicio_id_62907984_fk_servicio_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicio_servicio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contenido_contenido_servicio`
--

LOCK TABLES `contenido_contenido_servicio` WRITE;
/*!40000 ALTER TABLE `contenido_contenido_servicio` DISABLE KEYS */;
INSERT INTO `contenido_contenido_servicio` VALUES (1,0,3,11),(2,1,1,15);
/*!40000 ALTER TABLE `contenido_contenido_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contenido_contenido_tipico`
--

DROP TABLE IF EXISTS `contenido_contenido_tipico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contenido_contenido_tipico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` decimal(8,3) NOT NULL,
  `contenido_id` int(11) NOT NULL,
  `mueble_id` int(11) NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `contenido_contenido_tipico_contenido_id_181c52cc_uniq` (`contenido_id`,`mueble_id`) USING BTREE,
  KEY `contenido_contenido_tipico_0a9ab757` (`contenido_id`) USING BTREE,
  KEY `contenido_contenido_tipico_49933347` (`mueble_id`) USING BTREE,
  CONSTRAINT `contenido_conten_contenido_id_3ce1b6a5_fk_contenido_contenido_id` FOREIGN KEY (`contenido_id`) REFERENCES `contenido_contenido` (`id`),
  CONSTRAINT `contenido_contenido_tipic_mueble_id_473e3f56_fk_mueble_mueble_id` FOREIGN KEY (`mueble_id`) REFERENCES `mueble_mueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contenido_contenido_tipico`
--

LOCK TABLES `contenido_contenido_tipico` WRITE;
/*!40000 ALTER TABLE `contenido_contenido_tipico` DISABLE KEYS */;
INSERT INTO `contenido_contenido_tipico` VALUES (1,0.010,2,7,0),(2,0.060,2,1,1),(3,1.000,1,2,1),(5,0.060,3,34,1);
/*!40000 ALTER TABLE `contenido_contenido_tipico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_cotizacion`
--

DROP TABLE IF EXISTS `cotizacion_cotizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_cotizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero_contrato` varchar(100) COLLATE utf8_bin NOT NULL,
  `numero_cotizacion` varchar(100) COLLATE utf8_bin NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `fecha_culminacion` datetime NOT NULL,
  `fecha_estimadamudanza` datetime NOT NULL,
  `cantidad_ambientes` int(10) unsigned NOT NULL,
  `cantidad_muebles` int(10) unsigned NOT NULL,
  `volumen_muebles_sugerido` decimal(8,3) NOT NULL,
  `volumen_muebles_cotizado` decimal(8,3) NOT NULL,
  `peso_muebles` decimal(9,3) NOT NULL,
  `cantidad_contenedores` int(10) unsigned NOT NULL,
  `peso_contenedores` decimal(9,3) NOT NULL,
  `volumen_contenedores` decimal(8,3) NOT NULL,
  `peso_contenidos` decimal(9,3) NOT NULL,
  `volumen_contenidos` decimal(8,3) NOT NULL,
  `peso_materiales` decimal(9,3) NOT NULL,
  `monto_muebles` decimal(9,2) NOT NULL,
  `monto_material` decimal(9,2) NOT NULL,
  `monto_descuento` decimal(9,2) NOT NULL,
  `total_sin_impuesto` decimal(9,2) NOT NULL,
  `monto_impuesto` decimal(9,2) NOT NULL,
  `total_con_impuesto` decimal(9,2) NOT NULL,
  `tiempo_carga` decimal(7,2) NOT NULL,
  `total_recorrido_tiempo` decimal(7,2) NOT NULL,
  `total_recorrido_km` decimal(7,2) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `cotizador_id` int(11) NOT NULL,
  `creadopor_id` int(11) NOT NULL,
  `estado_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `numero_contrato` (`numero_contrato`) USING BTREE,
  UNIQUE KEY `numero_cotizacion` (`numero_cotizacion`) USING BTREE,
  KEY `cotizacion_cotizacion_4a860110` (`cliente_id`) USING BTREE,
  KEY `cotizacion_cotizacion_0f3c5103` (`cotizador_id`) USING BTREE,
  KEY `cotizacion_cotizacion_0fbfac26` (`creadopor_id`) USING BTREE,
  KEY `cotizacion_cotizacion_2c189993` (`estado_id`) USING BTREE,
  CONSTRAINT `cotizacion_cotizacion_cliente_id_3c9f3cf0_fk_clien` FOREIGN KEY (`cliente_id`) REFERENCES `cliente_cliente` (`id`),
  CONSTRAINT `cotizacion_cotizacion_cotizador_id_227888a5_fk_aut` FOREIGN KEY (`cotizador_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `cotizacion_cotizacion_creadopor_id_a50e140_fk_auth` FOREIGN KEY (`creadopor_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `cotizacion_estado_id_725bfc18_fk_cotizacion_estado` FOREIGN KEY (`estado_id`) REFERENCES `cotizacion_estado_cotizacion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_cotizacion`
--

LOCK TABLES `cotizacion_cotizacion` WRITE;
/*!40000 ALTER TABLE `cotizacion_cotizacion` DISABLE KEYS */;
INSERT INTO `cotizacion_cotizacion` VALUES (1,'654654','65465','2015-06-04 15:07:46','2015-12-06 00:00:00','2015-12-06 00:00:00',5,12,12.000,12.000,12.000,12,12.000,12.000,12.000,12.000,12.000,12.00,12.00,12.00,12.00,12.00,12.00,20000.00,20000.00,12.00,2,1,1,4);
/*!40000 ALTER TABLE `cotizacion_cotizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_cotizacion_ambiente`
--

DROP TABLE IF EXISTS `cotizacion_cotizacion_ambiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_cotizacion_ambiente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad_muebles` decimal(7,2) NOT NULL,
  `volumen_muebles` decimal(8,3) NOT NULL,
  `peso_muebles` decimal(9,3) NOT NULL,
  `cantidad_contenedores` decimal(7,2) NOT NULL,
  `volumen_contenedores` decimal(8,3) NOT NULL,
  `peso_contenedores` decimal(9,3) NOT NULL,
  `volumen_contenidos` decimal(8,3) NOT NULL,
  `peso_contenidos` decimal(9,3) NOT NULL,
  `peso_materiales` decimal(9,3) NOT NULL,
  `observaciones` longtext COLLATE utf8_bin NOT NULL,
  `ambiente_id` int(11) NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `piso_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cotizacion_cotizacion_ambiente_672bf590` (`ambiente_id`) USING BTREE,
  KEY `cotizacion_cotizacion_ambiente_1b44b901` (`cotizacion_id`) USING BTREE,
  KEY `cotizacion_cotizacion_ambiente_b96ace6f` (`piso_id`) USING BTREE,
  CONSTRAINT `cotizacion_cot_cotizacion_id_6be28da_fk_cotizacion_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacion_cotizacion` (`id`),
  CONSTRAINT `cotizacion_cotizaci_ambiente_id_6acfaf5e_fk_ambiente_ambiente_id` FOREIGN KEY (`ambiente_id`) REFERENCES `ambiente_ambiente` (`id`),
  CONSTRAINT `cotizacion_cotizacion_amb_piso_id_2ea195aa_fk_cotizacion_piso_id` FOREIGN KEY (`piso_id`) REFERENCES `cotizacion_piso` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_cotizacion_ambiente`
--

LOCK TABLES `cotizacion_cotizacion_ambiente` WRITE;
/*!40000 ALTER TABLE `cotizacion_cotizacion_ambiente` DISABLE KEYS */;
INSERT INTO `cotizacion_cotizacion_ambiente` VALUES (1,3.00,0.030,0.040,4.00,0.070,0.040,0.060,0.070,0.020,'',11,1,4),(2,9.00,0.020,0.030,3.00,0.060,0.040,0.050,0.060,0.030,'',18,1,4),(3,1.00,0.000,0.000,0.00,0.000,0.000,0.000,0.000,0.000,'',12,1,4),(4,10.00,0.000,0.000,0.00,0.000,0.000,0.000,0.000,0.000,'',2,1,4),(5,0.00,0.000,0.000,0.00,0.000,0.000,0.000,0.000,0.000,'',1,1,5);
/*!40000 ALTER TABLE `cotizacion_cotizacion_ambiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_cotizacion_contenido`
--

DROP TABLE IF EXISTS `cotizacion_cotizacion_contenido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_cotizacion_contenido` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `densidad` decimal(7,2) NOT NULL,
  `volumen_contenido` decimal(8,3) NOT NULL,
  `peso_contenido` decimal(9,3) NOT NULL,
  `porcentaje` decimal(5,2) DEFAULT NULL,
  `contenido_id` int(11) NOT NULL,
  `cotizacion_mueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cotizacion_cotizacion_contenido_0a9ab757` (`contenido_id`) USING BTREE,
  KEY `cotizacion_cotizacion_contenido_c01c3066` (`cotizacion_mueble_id`) USING BTREE,
  CONSTRAINT `D592dd68862d13c41653dee60d797c74` FOREIGN KEY (`cotizacion_mueble_id`) REFERENCES `cotizacion_cotizacion_mueble` (`id`),
  CONSTRAINT `cotizacion_cotiza_contenido_id_8398dce_fk_contenido_contenido_id` FOREIGN KEY (`contenido_id`) REFERENCES `contenido_contenido` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_cotizacion_contenido`
--

LOCK TABLES `cotizacion_cotizacion_contenido` WRITE;
/*!40000 ALTER TABLE `cotizacion_cotizacion_contenido` DISABLE KEYS */;
INSERT INTO `cotizacion_cotizacion_contenido` VALUES (1,0.02,0.020,0.040,0.02,3,1),(2,0.06,0.040,0.030,0.05,2,3);
/*!40000 ALTER TABLE `cotizacion_cotizacion_contenido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_cotizacion_direccion`
--

DROP TABLE IF EXISTS `cotizacion_cotizacion_direccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_cotizacion_direccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `direccion` varchar(550) COLLATE utf8_bin NOT NULL,
  `tipo_direccion` varchar(100) COLLATE utf8_bin NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `ascensor` tinyint(1) NOT NULL,
  `ascensor_servicio` tinyint(1) NOT NULL,
  `complejidad` varchar(100) COLLATE utf8_bin NOT NULL,
  `distancia_vehiculo` int(11) NOT NULL,
  `inmueble` varchar(100) COLLATE utf8_bin NOT NULL,
  `pisos` int(11) NOT NULL,
  `pisos_ascensor` int(11) NOT NULL,
  `pisos_ascensor_servicio` int(11) NOT NULL,
  `pisos_escalera` int(11) NOT NULL,
  `rampa` tinyint(1) NOT NULL,
  `tipo_inmueble` varchar(100) COLLATE utf8_bin NOT NULL,
  `total_m2` decimal(7,2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cotizacion_cotizacion_direccion_1b44b901` (`cotizacion_id`) USING BTREE,
  CONSTRAINT `cotizacion_co_cotizacion_id_5cc6412f_fk_cotizacion_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacion_cotizacion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_cotizacion_direccion`
--

LOCK TABLES `cotizacion_cotizacion_direccion` WRITE;
/*!40000 ALTER TABLE `cotizacion_cotizacion_direccion` DISABLE KEYS */;
INSERT INTO `cotizacion_cotizacion_direccion` VALUES (1,'Pais Argentina (AR) provincia Buenos Aires ciudad Buenos Aires Zona Centro calle LA calle del medio numero 299 piso PB  Punto de referencia Bien lejos','Origen',1,1,0,'Alta',50,'Origen',1,10,0,10,0,'Oficina',30.00),(2,'Pais Argentina (AR) provincia Buenos Aires ciudad Buenos Aires Zona Centro calle LA calle del medio numero 299 piso PB  Punto de referencia Bien lejos','Destino',1,1,0,'Media',20,'Torre cavendes',1,3,0,3,0,'Oficina',40.00);
/*!40000 ALTER TABLE `cotizacion_cotizacion_direccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_cotizacion_material`
--

DROP TABLE IF EXISTS `cotizacion_cotizacion_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_cotizacion_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` decimal(7,2) NOT NULL,
  `precio_unitario` decimal(9,2) NOT NULL,
  `precio_total` decimal(9,2) NOT NULL,
  `peso_unitario` decimal(9,3) NOT NULL,
  `peso_total` decimal(9,3) NOT NULL,
  `recuperable` tinyint(1) NOT NULL,
  `material_id` int(11) NOT NULL,
  `cotizacion_servicio_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `cotizacion_cotizacion_mater_cotizacion_servicio_id_2e45b032_uniq` (`cotizacion_servicio_id`,`material_id`) USING BTREE,
  KEY `cotizacion_cotizacion_material_eb4b9aaa` (`material_id`) USING BTREE,
  KEY `cotizacion_cotizacion_material_0efeca26` (`cotizacion_servicio_id`) USING BTREE,
  CONSTRAINT `cotizacion_cotizaci_material_id_7bf6e5a4_fk_servicio_material_id` FOREIGN KEY (`material_id`) REFERENCES `servicio_material` (`id`),
  CONSTRAINT `d09c653cf72992f8e405d67a993de563` FOREIGN KEY (`cotizacion_servicio_id`) REFERENCES `cotizacion_cotizacion_servicio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_cotizacion_material`
--

LOCK TABLES `cotizacion_cotizacion_material` WRITE;
/*!40000 ALTER TABLE `cotizacion_cotizacion_material` DISABLE KEYS */;
INSERT INTO `cotizacion_cotizacion_material` VALUES (1,1.00,0.03,0.03,0.050,0.030,0,2,1),(2,1.00,1.00,1.00,1.000,1.000,0,1,2),(3,1.00,0.03,0.03,0.020,0.020,0,2,3),(4,1.00,0.02,0.02,0.030,0.030,0,4,4);
/*!40000 ALTER TABLE `cotizacion_cotizacion_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_cotizacion_mueble`
--

DROP TABLE IF EXISTS `cotizacion_cotizacion_mueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_cotizacion_mueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tamano` varchar(100) COLLATE utf8_bin NOT NULL,
  `ancho` decimal(7,2) NOT NULL,
  `alto` decimal(7,2) NOT NULL,
  `largo` decimal(7,2) NOT NULL,
  `volumen` decimal(8,3) NOT NULL,
  `capacidad` decimal(8,3) NOT NULL,
  `ocupacion` decimal(5,2) DEFAULT NULL,
  `forma` varchar(100) COLLATE utf8_bin NOT NULL,
  `trasladable` tinyint(1) NOT NULL,
  `apilable` tinyint(1) NOT NULL,
  `capacidad_carga` tinyint(1) NOT NULL,
  `capacidad_interna` tinyint(1) NOT NULL,
  `observaciones` longtext COLLATE utf8_bin NOT NULL,
  `cotizacion_ambiente_id` int(11) NOT NULL,
  `mueble_id` int(11) NOT NULL,
  `densidad` varchar(100) COLLATE utf8_bin NOT NULL,
  `peso` decimal(9,3) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cotizacion_cotizacion_mueble_57d468d7` (`cotizacion_ambiente_id`) USING BTREE,
  KEY `cotizacion_cotizacion_mueble_49933347` (`mueble_id`) USING BTREE,
  CONSTRAINT `D8a02815931df906aa099e0a1f35b3c7` FOREIGN KEY (`cotizacion_ambiente_id`) REFERENCES `cotizacion_cotizacion_ambiente` (`id`),
  CONSTRAINT `cotizacion_cotizacion_mue_mueble_id_188a23e5_fk_mueble_mueble_id` FOREIGN KEY (`mueble_id`) REFERENCES `mueble_mueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_cotizacion_mueble`
--

LOCK TABLES `cotizacion_cotizacion_mueble` WRITE;
/*!40000 ALTER TABLE `cotizacion_cotizacion_mueble` DISABLE KEYS */;
INSERT INTO `cotizacion_cotizacion_mueble` VALUES (1,'Pequeño',0.60,2.00,0.50,0.700,1.000,0.94,'Cubo',0,0,0,0,'',2,2,'1',1.000),(2,'Pequeño',0.06,0.03,0.03,0.030,0.020,0.02,'Cubo',1,1,1,0,'',1,39,'1',1.000),(3,'Pequeño',0.03,0.04,0.02,0.040,0.050,0.03,'Plano',1,0,0,0,'',1,5,'Baja',0.010),(4,'Pequeño',0.02,0.02,0.02,0.010,0.010,0.01,'Plano',1,1,0,0,'',3,38,'Baja',0.010),(5,'mediana',0.03,0.02,0.02,0.010,0.010,0.02,'Cubo',1,0,0,0,'',1,87,'Baja',0.010),(6,'Pequeño',0.01,0.01,0.01,0.010,0.010,0.01,'Cubo',1,0,0,0,'',4,64,'Baja',0.010);
/*!40000 ALTER TABLE `cotizacion_cotizacion_mueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_cotizacion_servicio`
--

DROP TABLE IF EXISTS `cotizacion_cotizacion_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_cotizacion_servicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cotizacion_mueble_id` int(11) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  `cotizacion_contenido_id` int(11) DEFAULT NULL,
  `complejidad` varchar(100) COLLATE utf8_bin NOT NULL,
  `tarifa` decimal(9,2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cotizacion_cotizacion_servicio_c01c3066` (`cotizacion_mueble_id`) USING BTREE,
  KEY `cotizacion_cotizacion_servicio_4bb699dc` (`servicio_id`) USING BTREE,
  KEY `cotizacion_cotizacion_servicio_a068eccf` (`cotizacion_contenido_id`) USING BTREE,
  CONSTRAINT `D74bb3d33b8b3eebbac864be305f0b09` FOREIGN KEY (`cotizacion_mueble_id`) REFERENCES `cotizacion_cotizacion_mueble` (`id`),
  CONSTRAINT `cotizacion_cotizaci_servicio_id_3d7d767e_fk_servicio_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicio_servicio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_cotizacion_servicio`
--

LOCK TABLES `cotizacion_cotizacion_servicio` WRITE;
/*!40000 ALTER TABLE `cotizacion_cotizacion_servicio` DISABLE KEYS */;
INSERT INTO `cotizacion_cotizacion_servicio` VALUES (1,2,5,NULL,'Muy baja',30.00),(2,1,3,NULL,'Muy baja',20.00),(3,3,7,NULL,'Muy baja',20.00),(4,3,13,2,'Media',35.00);
/*!40000 ALTER TABLE `cotizacion_cotizacion_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_cotizacion_trabajador`
--

DROP TABLE IF EXISTS `cotizacion_cotizacion_trabajador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_cotizacion_trabajador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tarifa` decimal(9,2) NOT NULL,
  `cantidad` int(10) unsigned NOT NULL,
  `total_sin_recargo` decimal(9,2) NOT NULL,
  `nocturno` tinyint(1) NOT NULL,
  `fin_semana` tinyint(1) NOT NULL,
  `recargo_nocturno` decimal(9,2) NOT NULL,
  `recargo_fin_semana` decimal(9,2) NOT NULL,
  `total_con_recargo` decimal(9,2) NOT NULL,
  `cargo_id` int(11) NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cotizacion_cotizacion_trabajador_d036ebc9` (`cargo_id`) USING BTREE,
  KEY `cotizacion_cotizacion_trabajador_1b44b901` (`cotizacion_id`) USING BTREE,
  CONSTRAINT `cotizacion_co_cargo_id_156bb34_fk_trabajador_cargo_trabajador_id` FOREIGN KEY (`cargo_id`) REFERENCES `trabajador_cargo_trabajador` (`id`),
  CONSTRAINT `cotizacion_co_cotizacion_id_7db8d092_fk_cotizacion_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacion_cotizacion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_cotizacion_trabajador`
--

LOCK TABLES `cotizacion_cotizacion_trabajador` WRITE;
/*!40000 ALTER TABLE `cotizacion_cotizacion_trabajador` DISABLE KEYS */;
INSERT INTO `cotizacion_cotizacion_trabajador` VALUES (1,0.01,1,0.01,0,0,0.00,0.00,0.01,1,1),(2,0.01,1,0.01,0,0,0.00,0.00,0.01,2,1);
/*!40000 ALTER TABLE `cotizacion_cotizacion_trabajador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_estado_cotizacion`
--

DROP TABLE IF EXISTS `cotizacion_estado_cotizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_estado_cotizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `estado` (`estado`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_estado_cotizacion`
--

LOCK TABLES `cotizacion_estado_cotizacion` WRITE;
/*!40000 ALTER TABLE `cotizacion_estado_cotizacion` DISABLE KEYS */;
INSERT INTO `cotizacion_estado_cotizacion` VALUES (5,'Cerrada'),(2,'Cotizada'),(4,'En revisión'),(1,'Iniciada'),(3,'Realizada');
/*!40000 ALTER TABLE `cotizacion_estado_cotizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_piso`
--

DROP TABLE IF EXISTS `cotizacion_piso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_piso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `piso` varchar(100) COLLATE utf8_bin NOT NULL,
  `factor` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `piso` (`piso`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_piso`
--

LOCK TABLES `cotizacion_piso` WRITE;
/*!40000 ALTER TABLE `cotizacion_piso` DISABLE KEYS */;
INSERT INTO `cotizacion_piso` VALUES (1,'Sótano 1',1.00),(2,'Nivel de entrada',0.00),(3,'Ático',2.00),(4,'Piso 1',1.00),(5,'Piso 2',2.00),(6,'Piso 3',3.00),(7,'Piso 4',4.00),(8,'Sótano 2',2.00);
/*!40000 ALTER TABLE `cotizacion_piso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_tiempo_carga`
--

DROP TABLE IF EXISTS `cotizacion_tiempo_carga`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_tiempo_carga` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tiempo_carga` decimal(7,2) NOT NULL,
  `volumen_min` decimal(8,3) NOT NULL,
  `volumen_max` decimal(8,3) NOT NULL,
  `nro_objeto_min` int(10) unsigned NOT NULL,
  `nro_objeto_max` int(10) unsigned NOT NULL,
  `peso_min` decimal(9,3) NOT NULL,
  `peso_max` decimal(9,3) NOT NULL,
  `cantidad_trabajador` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_tiempo_carga`
--

LOCK TABLES `cotizacion_tiempo_carga` WRITE;
/*!40000 ALTER TABLE `cotizacion_tiempo_carga` DISABLE KEYS */;
INSERT INTO `cotizacion_tiempo_carga` VALUES (1,30000.00,12.000,1.000,120,150,10000.000,15000.000,2),(2,50000.00,16.100,1.000,151,200,15001.000,20000.000,1);
/*!40000 ALTER TABLE `cotizacion_tiempo_carga` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_vehiculo`
--

DROP TABLE IF EXISTS `cotizacion_vehiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_vehiculo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modelo` varchar(100) COLLATE utf8_bin NOT NULL,
  `tarifa_hora` decimal(9,2) NOT NULL,
  `tarifa_recorrido` decimal(9,2) NOT NULL,
  `capacidad_volumen` decimal(8,3) NOT NULL,
  `capacidad_peso` decimal(9,3) NOT NULL,
  `cargo_id` int(11) NOT NULL,
  `cantidad_disponible` int(10) unsigned NOT NULL,
  `cantidad_total` int(10) unsigned NOT NULL,
  `cantidad_ayudante` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `modelo` (`modelo`) USING BTREE,
  KEY `cotizacion_vehiculo_d036ebc9` (`cargo_id`) USING BTREE,
  CONSTRAINT `cotizacion_v_cargo_id_2aad98fa_fk_trabajador_cargo` FOREIGN KEY (`cargo_id`) REFERENCES `trabajador_cargo_trabajador` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_vehiculo`
--

LOCK TABLES `cotizacion_vehiculo` WRITE;
/*!40000 ALTER TABLE `cotizacion_vehiculo` DISABLE KEYS */;
INSERT INTO `cotizacion_vehiculo` VALUES (1,'Mercedes Benz 1418 Atego',260.00,15.00,43.000,9230.000,1,1,2,6),(2,'Mercedes Benz 710',240.00,15.00,34.000,7500.000,1,2,3,6),(3,'Mercedes Benz Sprinter 413 cdi',220.00,15.00,25.000,3200.000,1,1,2,4),(4,'Mercedes Benz Sprinter 313 CDI Panel Van',150.00,15.00,13.000,1500.000,1,2,3,4);
/*!40000 ALTER TABLE `cotizacion_vehiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_vehiculo_cotizacion`
--

DROP TABLE IF EXISTS `cotizacion_vehiculo_cotizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacion_vehiculo_cotizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(10) unsigned NOT NULL,
  `cantidad_hora` decimal(7,2) NOT NULL,
  `tarifa_hora` decimal(9,2) NOT NULL,
  `costo_hora` decimal(9,2) NOT NULL,
  `recorrido` decimal(7,2) NOT NULL,
  `tarifa_recorrido` decimal(9,2) NOT NULL,
  `costo_recorrido` decimal(9,2) NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `vehiculo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cotizacion_vehiculo_cotizacion_1b44b901` (`cotizacion_id`) USING BTREE,
  KEY `cotizacion_vehiculo_cotizacion_31609bf9` (`vehiculo_id`) USING BTREE,
  CONSTRAINT `cotizacion_veh_cotizacion_id_4d0b1a5_fk_cotizacion_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacion_cotizacion` (`id`),
  CONSTRAINT `cotizacion_vehicu_vehiculo_id_711b91f3_fk_cotizacion_vehiculo_id` FOREIGN KEY (`vehiculo_id`) REFERENCES `cotizacion_vehiculo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_vehiculo_cotizacion`
--

LOCK TABLES `cotizacion_vehiculo_cotizacion` WRITE;
/*!40000 ALTER TABLE `cotizacion_vehiculo_cotizacion` DISABLE KEYS */;
INSERT INTO `cotizacion_vehiculo_cotizacion` VALUES (1,1,20000.00,10.00,13.00,0.09,8.00,12.00,1,1);
/*!40000 ALTER TABLE `cotizacion_vehiculo_cotizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_ciudad`
--

DROP TABLE IF EXISTS `direccion_ciudad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_ciudad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ciudad` varchar(100) COLLATE utf8_bin NOT NULL,
  `provincia_id` int(11) NOT NULL,
  `pais_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `direccion_ciudad_ciudad_b2a453f_uniq` (`ciudad`,`provincia_id`) USING BTREE,
  KEY `direccion_ciudad_54bf7e76` (`provincia_id`) USING BTREE,
  KEY `direccion_ciudad_847ec16e` (`pais_id`) USING BTREE,
  CONSTRAINT `direccion_ciudad_pais_id_1d49c071_fk_direccion_pai` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`),
  CONSTRAINT `direccion_ciudad_provincia_id_9d5fb9a_fk_direccion` FOREIGN KEY (`provincia_id`) REFERENCES `direccion_provincia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=159 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_ciudad`
--

LOCK TABLES `direccion_ciudad` WRITE;
/*!40000 ALTER TABLE `direccion_ciudad` DISABLE KEYS */;
INSERT INTO `direccion_ciudad` VALUES (1,'Buenos Aires',1,10),(2,'Córdoba',7,10),(3,'Rosario',22,10),(4,'La Plata',1,10),(5,'Mar del Plata',1,10),(6,'San Miguel de Tucumán',25,10),(7,'Ciudad de Salta',18,10),(8,'Ciudad de Santa Fe',22,10),(9,'Ciudad de Corrientes',8,10),(10,'Bahía Blanca',1,10),(11,'Resistencia',5,10),(12,'Vicente López',1,10),(13,'Posadas',15,10),(14,'Merlo',1,10),(15,'Paraná',9,10),(16,'San Salvador de Jujuy',11,10),(17,'Quilmes',1,10),(18,'Ciudad de Santiago del Estero',23,10),(19,'Pilar',1,10),(20,'Banfield',1,10),(21,'Guaymallén',14,10),(22,'José C. Paz',1,10),(23,'Lanús',1,10),(24,'Ciudad de Neuquén',16,10),(25,'Ciudad de Formosa',10,10),(26,'Godoy Cruz',14,10),(27,'Las Heras',14,10),(28,'Gregorio de Laferrere',1,10),(29,'Berazategui',1,10),(30,'González Catán',1,10),(31,'San Miguel',1,10),(32,'Ciudad de Río Cuarto',7,10),(33,'Ciudad de San Luis',20,10),(34,'Moreno',1,10),(35,'Concordia',9,10),(36,'Ciudad de La Rioja',13,10),(37,'San Fernando del Valle de Catamarca',4,10),(38,'Comodoro Rivadavia',6,10),(39,'Isidro Casanova',1,10),(40,'San Rafael',14,10),(41,'Ituzaingó',1,10),(42,'San Nicolás de los Arroyos',1,10),(43,'Florencio Varela',1,10),(44,'Ciudad de San Juan',19,10),(45,'Lomas de Zamora',1,10),(46,'Temperley',1,10),(47,'Ciudad de Mendoza',14,10),(48,'Monte Grande',1,10),(49,'Bernal',1,10),(50,'San Justo',1,10),(51,'San Carlos de Bariloche',17,10),(52,'Pergamino',1,10),(53,'Castelar',1,10),(54,'Rafael Castillo',1,10),(55,'Trelew',6,10),(56,'Santa Rosa',12,10),(57,'Tandil',1,10),(58,'Libertad',1,10),(59,'Ramos Mejía',1,10),(60,'Villa Mercedes',20,10),(61,'Río Gallegos',21,10),(62,'Caseros',1,10),(63,'La Banda',23,10),(64,'Trujui',1,10),(65,'Ezeiza',1,10),(66,'Morón',1,10),(67,'Virrey del Pino',1,10),(69,'Maipú',14,10),(70,'Zárate',1,10),(71,'Burzaco',1,10),(72,'Grand Bourg',1,10),(73,'Monte Chingolo',1,10),(74,'Olavarría',1,10),(75,'Rawson',6,10),(76,'Rafaela',22,10),(77,'Junín',1,10),(78,'Remedios de Escalada (Partido de Lanús)',1,10),(79,'La Tablada',1,10),(80,'Campana',1,10),(81,'Presidencia Roque Sáenz Peña',5,10),(82,'Rivadavia',19,10),(83,'Florida (no es ciudad sino barrio)',1,10),(84,'Villa Madero',1,10),(85,'Olivos (no es ciudad sino barrio)',1,10),(86,'Gualeguaychú',9,10),(87,'Villa Gobernador Gálvez',22,10),(88,'Villa Luzuriaga',1,10),(89,'Boulogne Sur Mer',1,10),(90,'Chimbas',19,10),(91,'Ciudadela',1,10),(92,'Luján de Cuyo',14,10),(93,'Ezpeleta',1,10),(94,'Villa María',7,10),(95,'Alderetes',7,10),(96,'General Roca',17,10),(97,'San Fernando',1,10),(98,'Ciudad Evita',1,10),(99,'Venado Tuerto',22,10),(100,'Bella Vista',1,10),(101,'Luján',1,10),(102,'San Ramón de la Nueva Orán',18,10),(103,'Cipolletti',17,10),(104,'Goya',8,10),(105,'Reconquista',22,10),(106,'Wilde',1,10),(107,'Martínez',1,10),(108,'Necochea',1,10),(109,'Don Torcuato',1,10),(110,'Banda del Río Salí',25,10),(111,'Concepción del Uruguay',9,10),(112,'General Rodríguez',1,10),(113,'Villa Tesei',1,10),(114,'Ciudad Jardín El Libertador',1,10),(115,'Villa Carlos Paz',7,10),(116,'Sarandí',1,10),(117,'Chivilcoy',1,10),(118,'Villa Domínico',1,10),(119,'Béccar',1,10),(120,'San Francisco',7,10),(121,'Glew',1,10),(122,'Puerto Madryn',6,10),(123,'Punta Alta',1,10),(124,'El Palomar',1,10),(125,'Rafael Calzada',1,10),(126,'Tartagal',18,10),(127,'San Pedro de Jujuy',11,10),(128,'Belén de Escobar',1,10),(129,'Berisso',1,10),(130,'Mariano Acosta',1,10),(131,'San Francisco Solano',1,10),(132,'Los Polvorines',1,10),(133,'Azul',1,10),(134,'Lomas del Mirador',1,10),(135,'Río Grande',24,10),(136,'Presidente Perón',1,10),(137,'General Pico',12,10),(138,'Mercedes',1,10),(139,'Bosques',1,10),(140,'Oberá',15,10),(141,'Barranqueras',5,10),(142,'Yerba Buena/Marcos Paz',25,10),(143,'Villa Centenario',1,10),(144,'San Martín',14,10),(145,'Gobernador Julio A Costa',1,10),(146,'William Morris',1,10),(147,'El Jagüel',1,10),(148,'Villa Mariano Moreno-El Colmenar',25,10),(149,'Eldorado',15,10),(150,'Longchamps',1,10),(151,'Clorinda',10,10),(152,'Viedma',17,10),(153,'Concepción',25,10),(154,'Tres Arroyos',1,10),(155,'Ushuaia',24,10),(156,'San Isidro',1,10),(157,'Palpalá',11,10),(158,'Barquisimeto',26,256);
/*!40000 ALTER TABLE `direccion_ciudad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_complejidad_inmueble`
--

DROP TABLE IF EXISTS `direccion_complejidad_inmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_complejidad_inmueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `complejidad` varchar(100) COLLATE utf8_bin NOT NULL,
  `factor` decimal(5,2) NOT NULL,
  `valor_ambiente` decimal(9,2) NOT NULL,
  `valor_metrocubico` decimal(9,2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `complejidad` (`complejidad`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_complejidad_inmueble`
--

LOCK TABLES `direccion_complejidad_inmueble` WRITE;
/*!40000 ALTER TABLE `direccion_complejidad_inmueble` DISABLE KEYS */;
INSERT INTO `direccion_complejidad_inmueble` VALUES (1,'Muy bajo',0.60,1000.00,100.00),(2,'Bajo',0.80,1200.00,120.00),(3,'Media',1.00,1400.00,140.00),(4,'Alta',1.20,1600.00,160.00),(5,'Muy alta',1.40,1800.00,180.00);
/*!40000 ALTER TABLE `direccion_complejidad_inmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_direccion`
--

DROP TABLE IF EXISTS `direccion_direccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_direccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `calle` varchar(100) COLLATE utf8_bin NOT NULL,
  `numero` varchar(100) COLLATE utf8_bin NOT NULL,
  `piso` varchar(100) COLLATE utf8_bin NOT NULL,
  `adicional` varchar(250) COLLATE utf8_bin NOT NULL,
  `zip1` varchar(100) COLLATE utf8_bin NOT NULL,
  `punto_referencia` varchar(250) COLLATE utf8_bin NOT NULL,
  `ciudad_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `pais_id` int(11) NOT NULL,
  `provincia_id` int(11) NOT NULL,
  `tipo_direccion_id` int(11) NOT NULL,
  `zona_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `direccion_direccion_0201ed81` (`ciudad_id`) USING BTREE,
  KEY `direccion_direccion_4a860110` (`cliente_id`) USING BTREE,
  KEY `direccion_direccion_847ec16e` (`pais_id`) USING BTREE,
  KEY `direccion_direccion_54bf7e76` (`provincia_id`) USING BTREE,
  KEY `direccion_direccion_aa27db54` (`tipo_direccion_id`) USING BTREE,
  KEY `direccion_direccion_8d8c29ed` (`zona_id`) USING BTREE,
  CONSTRAINT `direcc_tipo_direccion_id_1c09d12a_fk_direccion_tip` FOREIGN KEY (`tipo_direccion_id`) REFERENCES `direccion_tipo_direccion` (`id`),
  CONSTRAINT `direccion_direcci_provincia_id_bfb5338_fk_direccio` FOREIGN KEY (`provincia_id`) REFERENCES `direccion_provincia` (`id`),
  CONSTRAINT `direccion_direccion_ciudad_id_1ec1061c_fk_direccio` FOREIGN KEY (`ciudad_id`) REFERENCES `direccion_ciudad` (`id`),
  CONSTRAINT `direccion_direccion_cliente_id_396923a4_fk_cliente` FOREIGN KEY (`cliente_id`) REFERENCES `cliente_cliente` (`id`),
  CONSTRAINT `direccion_direccion_pais_id_2416fca5_fk_direccion_pais_id` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`),
  CONSTRAINT `direccion_direccion_zona_id_16fbcf34_fk_direccion_` FOREIGN KEY (`zona_id`) REFERENCES `direccion_zona` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_direccion`
--

LOCK TABLES `direccion_direccion` WRITE;
/*!40000 ALTER TABLE `direccion_direccion` DISABLE KEYS */;
INSERT INTO `direccion_direccion` VALUES (1,'23','18','PH','','3001','Principe',1,1,10,1,1,1),(2,'LA calle del medio','299','PB','Por chirgua','3001','Bien lejos',1,2,10,1,1,1),(3,'23','20','1','','3001','esquina de la 20',1,1,10,1,2,1);
/*!40000 ALTER TABLE `direccion_direccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_inmueble`
--

DROP TABLE IF EXISTS `direccion_inmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_inmueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `inmueble` varchar(100) COLLATE utf8_bin NOT NULL,
  `numero_ambientes` int(11) NOT NULL,
  `pisos` int(11) NOT NULL,
  `pisos_escalera` int(11) NOT NULL,
  `rampa` tinyint(1) NOT NULL,
  `ascensor` tinyint(1) NOT NULL,
  `ascensor_servicio` tinyint(1) NOT NULL,
  `pisos_ascensor_servicio` int(11) NOT NULL,
  `pisos_ascensor` int(11) NOT NULL,
  `distancia_vehiculo` int(11) NOT NULL,
  `complejidad_id` int(11) NOT NULL,
  `direccion_id` int(11) NOT NULL,
  `tipo_inmueble_id` int(11) NOT NULL,
  `total_m2` decimal(7,2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `direccion_inmueble_008d38e3` (`complejidad_id`) USING BTREE,
  KEY `direccion_inmueble_84a32fcd` (`direccion_id`) USING BTREE,
  KEY `direccion_inmueble_0a525c68` (`tipo_inmueble_id`) USING BTREE,
  CONSTRAINT `dir_complejidad_id_44d72601_fk_direccion_complejid` FOREIGN KEY (`complejidad_id`) REFERENCES `direccion_complejidad_inmueble` (`id`),
  CONSTRAINT `direccio_tipo_inmueble_id_250a00ce_fk_direccion_ti` FOREIGN KEY (`tipo_inmueble_id`) REFERENCES `direccion_tipo_inmueble` (`id`),
  CONSTRAINT `direccion_inmueb_direccion_id_50718c56_fk_direccio` FOREIGN KEY (`direccion_id`) REFERENCES `direccion_direccion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_inmueble`
--

LOCK TABLES `direccion_inmueble` WRITE;
/*!40000 ALTER TABLE `direccion_inmueble` DISABLE KEYS */;
INSERT INTO `direccion_inmueble` VALUES (1,'Origen',5,1,10,0,0,0,0,0,50,4,1,2,0.00),(2,'Torre cavendes',3,1,3,0,1,0,0,3,20,3,2,2,0.00);
/*!40000 ALTER TABLE `direccion_inmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_pais`
--

DROP TABLE IF EXISTS `direccion_pais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_pais` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pais` varchar(250) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `pais` (`pais`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=265 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_pais`
--

LOCK TABLES `direccion_pais` WRITE;
/*!40000 ALTER TABLE `direccion_pais` DISABLE KEYS */;
INSERT INTO `direccion_pais` VALUES (1,'Afghanistan (AF)'),(264,'Aland Islands (AX)'),(2,'Albania (AL)'),(3,'Algeria (DZ)'),(4,'American Samoa (AS)'),(5,'Andorra (AD)'),(6,'Angola (AO)'),(7,'Anguilla (AI)'),(8,'Antarctica (AQ)'),(9,'Antigua and Barbuda (AG)'),(10,'Argentina (AR)'),(11,'Armenia (AM)'),(12,'Aruba (AW)'),(13,'Australia (AU)'),(14,'Austria (AT)'),(15,'Azerbaijan (AZ)'),(16,'Bahamas (BS)'),(17,'Bahrain (BH)'),(18,'Bangladesh (BD)'),(19,'Barbados (BB)'),(20,'Belarus (BY)'),(21,'Belgium (BE)'),(22,'Belize (BZ)'),(23,'Benin (BJ)'),(24,'Bermuda (BM)'),(25,'Bhutan (BT)'),(26,'Bolivia (BO)'),(27,'Bosnia and Herzegovina (BA)'),(28,'Botswana (BW)'),(29,'Bouvet Island (BV)'),(30,'Brazil (BR)'),(31,'British Antarctic Territory (BQ)'),(32,'British Indian Ocean Territory (IO)'),(33,'British Virgin Islands (VG)'),(34,'Brunei (BN)'),(35,'Bulgaria (BG)'),(36,'Burkina Faso (BF)'),(37,'Burundi (BI)'),(60,'C?te d?Ivoire (CI)'),(38,'Cambodia (KH)'),(39,'Cameroon (CM)'),(40,'Canada (CA)'),(41,'Canton and Enderbury Islands (CT)'),(42,'Cape Verde (CV)'),(43,'Cayman Islands (KY)'),(44,'Central African Republic (CF)'),(45,'Chad (TD)'),(46,'Chile (CL)'),(47,'China (CN)'),(48,'Christmas Island (CX)'),(49,'Cocos [Keeling] Islands (CC)'),(50,'Colombia (CO)'),(51,'Comoros (KM)'),(52,'Congo - Brazzaville (CG)'),(53,'Congo - Kinshasa (CD)'),(54,'Cook Islands (CK)'),(55,'Costa Rica (CR)'),(56,'Croatia (HR)'),(57,'Cuba (CU)'),(58,'Cyprus (CY)'),(59,'Czech Republic (CZ)'),(61,'Denmark (DK)'),(62,'Djibouti (DJ)'),(63,'Dominica (DM)'),(64,'Dominican Republic (DO)'),(65,'Dronning Maud Land (NQ)'),(66,'East Germany (DD)'),(67,'Ecuador (EC)'),(68,'Egypt (EG)'),(69,'El Salvador (SV)'),(70,'Equatorial Guinea (GQ)'),(71,'Eritrea (ER)'),(72,'Estonia (EE)'),(73,'Ethiopia (ET)'),(74,'Falkland Islands (FK)'),(75,'Faroe Islands (FO)'),(76,'Fiji (FJ)'),(77,'Finland (FI)'),(78,'France (FR)'),(79,'French Guiana (GF)'),(80,'French Polynesia (PF)'),(81,'French Southern Territories (TF)'),(82,'French Southern and Antarctic Territories (FQ)'),(83,'Gabon (GA)'),(84,'Gambia (GM)'),(85,'Georgia (GE)'),(86,'Germany (DE)'),(87,'Ghana (GH)'),(88,'Gibraltar (GI)'),(89,'Greece (GR)'),(90,'Greenland (GL)'),(91,'Grenada (GD)'),(92,'Guadeloupe (GP)'),(93,'Guam (GU)'),(94,'Guatemala (GT)'),(95,'Guernsey (GG)'),(96,'Guinea (GN)'),(97,'Guinea-Bissau (GW)'),(98,'Guyana (GY)'),(99,'Haiti (HT)'),(100,'Heard Island and McDonald Islands (HM)'),(101,'Honduras (HN)'),(102,'Hong Kong SAR China (HK)'),(103,'Hungary (HU)'),(104,'Iceland (IS)'),(105,'India (IN)'),(106,'Indonesia (ID)'),(107,'Iran (IR)'),(108,'Iraq (IQ)'),(109,'Ireland (IE)'),(110,'Isle of Man (IM)'),(111,'Israel (IL)'),(112,'Italy (IT)'),(113,'Jamaica (JM)'),(114,'Japan (JP)'),(115,'Jersey (JE)'),(116,'Johnston Island (JT)'),(117,'Jordan (JO)'),(118,'Kazakhstan (KZ)'),(119,'Kenya (KE)'),(120,'Kiribati (KI)'),(121,'Kuwait (KW)'),(122,'Kyrgyzstan (KG)'),(123,'Laos (LA)'),(124,'Latvia (LV)'),(125,'Lebanon (LB)'),(126,'Lesotho (LS)'),(127,'Liberia (LR)'),(128,'Libya (LY)'),(129,'Liechtenstein (LI)'),(130,'Lithuania (LT)'),(131,'Luxembourg (LU)'),(132,'Macau SAR China (MO)'),(133,'Macedonia (MK)'),(134,'Madagascar (MG)'),(135,'Malawi (MW)'),(136,'Malaysia (MY)'),(137,'Maldives (MV)'),(138,'Mali (ML)'),(139,'Malta (MT)'),(140,'Marshall Islands (MH)'),(141,'Martinique (MQ)'),(142,'Mauritania (MR)'),(143,'Mauritius (MU)'),(144,'Mayotte (YT)'),(145,'Metropolitan France (FX)'),(146,'Mexico (MX)'),(147,'Micronesia (FM)'),(148,'Midway Islands (MI)'),(149,'Moldova (MD)'),(150,'Monaco (MC)'),(151,'Mongolia (MN)'),(152,'Montenegro (ME)'),(153,'Montserrat (MS)'),(154,'Morocco (MA)'),(155,'Mozambique (MZ)'),(156,'Myanmar [Burma] (MM)'),(157,'Namibia (NA)'),(158,'Nauru (NR)'),(159,'Nepal (NP)'),(160,'Netherlands (NL)'),(161,'Netherlands Antilles (AN)'),(162,'Neutral Zone (NT)'),(163,'New Caledonia (NC)'),(164,'New Zealand (NZ)'),(165,'Nicaragua (NI)'),(166,'Niger (NE)'),(167,'Nigeria (NG)'),(168,'Niue (NU)'),(169,'Norfolk Island (NF)'),(170,'North Korea (KP)'),(171,'North Vietnam (VD)'),(172,'Northern Mariana Islands (MP)'),(173,'Norway (NO)'),(174,'Oman (OM)'),(175,'Pacific Islands Trust Territory (PC)'),(176,'Pakistan (PK)'),(177,'Palau (PW)'),(178,'Palestinian Territories (PS)'),(179,'Panama (PA)'),(180,'Panama Canal Zone (PZ)'),(181,'Papua New Guinea (PG)'),(182,'Paraguay (PY)'),(183,'People\'s Democratic Republic of Yemen (YD)'),(184,'Peru (PE)'),(185,'Philippines (PH)'),(186,'Pitcairn Islands (PN)'),(187,'Poland (PL)'),(188,'Portugal (PT)'),(189,'Puerto Rico (PR)'),(190,'Qatar (QA)'),(194,'R?union (RE)'),(191,'Romania (RO)'),(192,'Russia (RU)'),(193,'Rwanda (RW)'),(227,'S?o Tom? and Pr?ncipe (ST)'),(195,'Saint Barth?lemy (BL)'),(196,'Saint Helena (SH)'),(197,'Saint Kitts and Nevis (KN)'),(198,'Saint Lucia (LC)'),(199,'Saint Martin (MF)'),(200,'Saint Pierre and Miquelon (PM)'),(201,'Saint Vincent and the Grenadines (VC)'),(202,'Samoa (WS)'),(203,'San Marino (SM)'),(204,'Saudi Arabia (SA)'),(205,'Senegal (SN)'),(206,'Serbia (RS)'),(207,'Serbia and Montenegro (CS)'),(208,'Seychelles (SC)'),(209,'Sierra Leone (SL)'),(210,'Singapore (SG)'),(211,'Slovakia (SK)'),(212,'Slovenia (SI)'),(213,'Solomon Islands (SB)'),(214,'Somalia (SO)'),(215,'South Africa (ZA)'),(216,'South Georgia and the South Sandwich Islands (GS)'),(217,'South Korea (KR)'),(218,'Spain (ES)'),(219,'Sri Lanka (LK)'),(220,'Sudan (SD)'),(221,'Suriname (SR)'),(222,'Svalbard and Jan Mayen (SJ)'),(223,'Swaziland (SZ)'),(224,'Sweden (SE)'),(225,'Switzerland (CH)'),(226,'Syria (SY)'),(228,'Taiwan (TW)'),(229,'Tajikistan (TJ)'),(230,'Tanzania (TZ)'),(231,'Thailand (TH)'),(232,'Timor-Leste (TL)'),(233,'Togo (TG)'),(234,'Tokelau (TK)'),(235,'Tonga (TO)'),(236,'Trinidad and Tobago (TT)'),(237,'Tunisia (TN)'),(238,'Turkey (TR)'),(239,'Turkmenistan (TM)'),(240,'Turks and Caicos Islands (TC)'),(241,'Tuvalu (TV)'),(242,'U.S. Minor Outlying Islands (UM)'),(243,'U.S. Miscellaneous Pacific Islands (PU)'),(244,'U.S. Virgin Islands (VI)'),(245,'Uganda (UG)'),(246,'Ukraine (UA)'),(247,'Union of Soviet Socialist Republics (SU)'),(248,'United Arab Emirates (AE)'),(249,'United Kingdom (GB)'),(250,'United States (US)'),(251,'Unknown or Invalid Region (ZZ)'),(252,'Uruguay (UY)'),(253,'Uzbekistan (UZ)'),(254,'Vanuatu (VU)'),(255,'Vatican City (VA)'),(256,'Venezuela (VE)'),(257,'Vietnam (VN)'),(258,'Wake Island (WK)'),(259,'Wallis and Futuna (WF)'),(260,'Western Sahara (EH)'),(261,'Yemen (YE)'),(262,'Zambia (ZM)'),(263,'Zimbabwe (ZW)');
/*!40000 ALTER TABLE `direccion_pais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_provincia`
--

DROP TABLE IF EXISTS `direccion_provincia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_provincia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provincia` varchar(100) COLLATE utf8_bin NOT NULL,
  `pais_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `direccion_provincia_provincia_646a35c1_uniq` (`provincia`,`pais_id`) USING BTREE,
  KEY `direccion_provincia_847ec16e` (`pais_id`) USING BTREE,
  CONSTRAINT `direccion_provincia_pais_id_6fa21912_fk_direccion_` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_provincia`
--

LOCK TABLES `direccion_provincia` WRITE;
/*!40000 ALTER TABLE `direccion_provincia` DISABLE KEYS */;
INSERT INTO `direccion_provincia` VALUES (1,'Buenos Aires',10),(2,'Buenos Aires-GBA',10),(3,'Capital Federal',10),(4,'Catamarca',10),(5,'Chaco',10),(6,'Chubut',10),(8,'Corrientes',10),(7,'Córdoba',10),(9,'Entre Ríos',10),(10,'Formosa',10),(11,'Jujuy',10),(12,'La Pampa',10),(13,'La Rioja',10),(26,'Lara',256),(14,'Mendoza',10),(15,'Misiones',10),(16,'Neuquén',10),(17,'Río Negro',10),(18,'Salta',10),(19,'San Juan',10),(20,'San Luis',10),(21,'Santa Cruz',10),(22,'Santa Fe',10),(23,'Santiago del Estero',10),(24,'Tierra del Fuego',10),(25,'Tucumán',10);
/*!40000 ALTER TABLE `direccion_provincia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_tipo_direccion`
--

DROP TABLE IF EXISTS `direccion_tipo_direccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_tipo_direccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_direccion` varchar(50) COLLATE utf8_bin NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `tipo_direccion` (`tipo_direccion`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_tipo_direccion`
--

LOCK TABLES `direccion_tipo_direccion` WRITE;
/*!40000 ALTER TABLE `direccion_tipo_direccion` DISABLE KEYS */;
INSERT INTO `direccion_tipo_direccion` VALUES (1,'Origen',1),(2,'Destino',1);
/*!40000 ALTER TABLE `direccion_tipo_direccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_tipo_inmueble`
--

DROP TABLE IF EXISTS `direccion_tipo_inmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_tipo_inmueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_inmueble` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_tipo_inmueble`
--

LOCK TABLES `direccion_tipo_inmueble` WRITE;
/*!40000 ALTER TABLE `direccion_tipo_inmueble` DISABLE KEYS */;
INSERT INTO `direccion_tipo_inmueble` VALUES (1,'Apartamento'),(2,'Oficina'),(3,'Town house'),(4,'Casa'),(5,'Quinta'),(6,'Pent-house'),(7,'Baulera'),(8,'Galpón');
/*!40000 ALTER TABLE `direccion_tipo_inmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_zona`
--

DROP TABLE IF EXISTS `direccion_zona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_zona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `zona` varchar(100) COLLATE utf8_bin NOT NULL,
  `ciudad_id` int(11) NOT NULL,
  `pais_id` int(11) NOT NULL,
  `provincia_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `direccion_zona_zona_1146d1e4_uniq` (`zona`,`ciudad_id`) USING BTREE,
  KEY `direccion_zona_0201ed81` (`ciudad_id`) USING BTREE,
  KEY `direccion_zona_847ec16e` (`pais_id`) USING BTREE,
  KEY `direccion_zona_54bf7e76` (`provincia_id`) USING BTREE,
  CONSTRAINT `direccion_zona_ciudad_id_222e10ed_fk_direccion_ciu` FOREIGN KEY (`ciudad_id`) REFERENCES `direccion_ciudad` (`id`),
  CONSTRAINT `direccion_zona_pais_id_209d4c37_fk_direccion_pais_` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`),
  CONSTRAINT `direccion_zona_provincia_id_6fb98cf2_fk_direccion_` FOREIGN KEY (`provincia_id`) REFERENCES `direccion_provincia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_zona`
--

LOCK TABLES `direccion_zona` WRITE;
/*!40000 ALTER TABLE `direccion_zona` DISABLE KEYS */;
INSERT INTO `direccion_zona` VALUES (1,'Centro',1,10,10),(3,'Centro',158,256,26);
/*!40000 ALTER TABLE `direccion_zona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext COLLATE utf8_bin,
  `object_repr` varchar(200) COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `django_admin_log_417f1b1c` (`content_type_id`) USING BTREE,
  KEY `django_admin_log_e8701ad4` (`user_id`) USING BTREE,
  CONSTRAINT `django_admin__content_type_id_4e50f396_fk_django_c` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_eccecc5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-06-12 18:43:41','2','yusnelvy',2,'Changed user_permissions.',4,1),(2,'2015-08-05 20:47:50','1',' 1',1,'',63,1),(3,'2015-08-19 18:24:36','3',' Armario empotrado - Mediano - Media',2,'Changed ancho, largo, alto and peso.',37,1),(4,'2015-08-19 18:24:55','2',' Armario empotrado - Pequeño - Baja',2,'Changed largo, alto and peso.',37,1),(5,'2015-08-19 18:43:20','3',' Armario empotrado - Mediano - Media',2,'No fields changed.',37,1),(6,'2015-08-25 16:29:21','1','Empresa object',1,'',64,1),(7,'2015-08-25 18:13:19','1','Empresa object',2,'Changed logo.',64,1),(8,'2015-08-25 18:15:18','1','Empresa object',2,'Changed logo.',64,1),(9,'2015-08-25 18:15:40','1','Empresa object',2,'Changed logo.',64,1),(10,'2015-08-25 19:15:42','1','Empresa object',2,'Changed logo.',64,1),(11,'2015-09-02 20:34:34','1',' 1',2,'Changed volmaterial and pesomaterial.',63,1),(12,'2015-09-03 18:55:45','2','yusnelvy',2,'Changed user_permissions.',4,1),(13,'2015-09-03 18:57:23','2','yusnelvy',2,'Changed user_permissions.',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `django_content_type_app_label_119dd4ba_uniq` (`app_label`,`model`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(24,'ambiente','ambiente'),(25,'ambiente','ambiente_tipo_inmueble'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(20,'cliente','cliente'),(21,'cliente','email'),(19,'cliente','estado_civil'),(18,'cliente','sexo'),(40,'contenido','contenido'),(58,'contenido','contenido_servicio'),(41,'contenido','contenido_tipico'),(5,'contenttypes','contenttype'),(46,'cotizacion','cotizacion'),(51,'cotizacion','cotizacion_ambiente'),(56,'cotizacion','cotizacion_contenido'),(49,'cotizacion','cotizacion_direccion'),(54,'cotizacion','cotizacion_material'),(52,'cotizacion','cotizacion_mueble'),(53,'cotizacion','cotizacion_servicio'),(50,'cotizacion','cotizacion_trabajador'),(43,'cotizacion','estado_cotizacion'),(45,'cotizacion','piso'),(44,'cotizacion','tiempo_carga'),(47,'cotizacion','vehiculo'),(48,'cotizacion','vehiculo_cotizacion'),(9,'direccion','ciudad'),(14,'direccion','complejidad_inmueble'),(12,'direccion','direccion'),(16,'direccion','inmueble'),(7,'direccion','pais'),(8,'direccion','provincia'),(11,'direccion','tipo_direccion'),(13,'direccion','tipo_inmueble'),(10,'direccion','zona'),(36,'mueble','densidad'),(33,'mueble','forma_mueble'),(34,'mueble','mueble'),(38,'mueble','mueble_ambiente'),(32,'mueble','ocupacion'),(35,'mueble','tamano'),(37,'mueble','tamano_mueble'),(31,'mueble','tipo_mueble'),(64,'premisas','empresa'),(65,'premisas','fuentepromocion'),(63,'presupuesto','datosprecargado'),(59,'presupuesto','presupuesto'),(61,'presupuesto','presupuesto_detalle'),(60,'presupuesto','presupuesto_direccion'),(62,'presupuesto','presupuesto_servicio'),(29,'servicio','complejidad'),(30,'servicio','complejidad_servicio'),(27,'servicio','material'),(26,'servicio','servicio'),(28,'servicio','servicio_material'),(57,'servicio','unidad'),(6,'sessions','session'),(23,'telefono','telefono'),(22,'telefono','tipo_telefono'),(42,'trabajador','cargo_trabajador');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-06-18 21:16:03'),(2,'auth','0001_initial','2015-06-18 21:16:13'),(3,'admin','0001_initial','2015-06-18 21:16:16'),(4,'sessions','0001_initial','2015-06-18 21:16:16'),(5,'cliente','0001_initial','2015-06-18 21:19:51'),(6,'direccion','0001_initial','2015-06-18 21:20:26'),(7,'ambiente','0001_initial','2015-06-18 21:20:30'),(8,'mueble','0001_initial','2015-06-18 21:20:46'),(9,'contenido','0001_initial','2015-06-18 21:20:53'),(10,'trabajador','0001_initial','2015-06-18 21:20:54'),(11,'servicio','0001_initial','2015-06-18 21:21:01'),(12,'cotizacion','0001_initial','2015-06-18 21:21:46'),(13,'telefono','0001_initial','2015-06-18 21:21:51'),(14,'ambiente','0002_auto_20150619_1535','2015-06-19 20:05:40'),(15,'cliente','0002_auto_20150619_1535','2015-06-19 20:05:42'),(16,'ambiente','0002_auto_20150619_1555','2015-06-19 20:27:10'),(17,'cliente','0002_auto_20150619_1555','2015-06-19 20:27:12'),(18,'servicio','0002_auto_20150619_1555','2015-06-19 20:27:38'),(19,'cotizacion','0002_auto_20150619_1555','2015-06-19 20:52:54'),(20,'contenido','0002_auto_20150619_1555','2015-06-19 20:53:02'),(21,'mueble','0002_auto_20150619_1555','2015-06-19 20:53:03'),(22,'servicio','0003_material_unidad','2015-06-22 13:57:58'),(23,'cotizacion','0003_auto_20150622_1004','2015-06-22 14:34:08'),(24,'cotizacion','0004_auto_20150622_1005','2015-06-22 14:36:03'),(25,'contenido','0003_auto_20150623_1553','2015-06-23 20:23:27'),(26,'cotizacion','0005_auto_20150623_1602','2015-06-23 20:33:57'),(27,'direccion','0002_auto_20150623_1553','2015-06-23 20:34:09'),(28,'direccion','0003_auto_20150623_1611','2015-06-23 20:42:00'),(29,'direccion','0004_auto_20150626_1546','2015-06-26 20:16:51'),(30,'cotizacion','0006_auto_20150630_1205','2015-06-30 16:35:35'),(31,'contenttypes','0002_remove_content_type_name','2015-07-09 19:31:40'),(32,'auth','0002_alter_permission_name_max_length','2015-07-09 19:31:41'),(33,'auth','0003_alter_user_email_max_length','2015-07-09 19:31:41'),(34,'auth','0004_alter_user_username_opts','2015-07-09 19:31:42'),(35,'auth','0005_alter_user_last_login_null','2015-07-09 19:31:42'),(36,'auth','0006_require_contenttypes_0002','2015-07-09 19:31:43'),(37,'cliente','0003_auto_20150710_0941','2015-07-10 14:12:05'),(38,'cotizacion','0007_auto_20150710_0941','2015-07-10 14:12:16'),(39,'mueble','0003_auto_20150713_1023','2015-07-13 14:53:48'),(40,'servicio','0004_remove_material_volumen','2015-07-13 14:53:49'),(41,'presupuesto','0001_initial','2015-07-13 15:04:19'),(42,'presupuesto','0002_auto_20150715_1648','2015-07-15 21:27:42'),(43,'servicio','0005_complejidad_servicio_factor_tiempo','2015-07-15 21:27:45'),(44,'presupuesto','0003_presupuesto_servicio','2015-07-22 19:59:20'),(45,'contenido','0004_contenido_tipico_predefinido','2015-07-27 16:38:00'),(46,'cotizacion','0008_auto_20150727_1207','2015-07-27 16:38:02'),(47,'presupuesto','0004_presupuesto_detalle_descripcion_contenedor','2015-07-27 16:38:03'),(48,'presupuesto','0005_auto_20150729_1010','2015-07-29 14:40:42'),(49,'presupuesto','0006_presupuesto_servicio_tiempo_aplicado','2015-07-29 14:43:30'),(50,'presupuesto','0007_auto_20150729_1028','2015-07-29 15:02:34'),(51,'presupuesto','0008_auto_20150731_1610','2015-07-31 20:55:26'),(52,'presupuesto','0009_presupuesto_total_volumen_materiales','2015-07-31 20:59:45'),(53,'presupuesto','0010_presupuesto_activo','2015-08-04 14:37:14'),(54,'cotizacion','0009_auto_20150805_1400','2015-08-05 18:31:32'),(55,'mueble','0004_auto_20150805_1400','2015-08-05 18:31:34'),(56,'presupuesto','0011_auto_20150805_1400','2015-08-05 18:32:16'),(57,'servicio','0006_auto_20150805_1400','2015-08-05 18:32:21'),(58,'presupuesto','0012_datosprecargado','2015-08-05 20:43:08'),(59,'presupuesto','0013_auto_20150807_1041','2015-08-07 15:24:47'),(60,'ambiente','0003_auto_20150810_1105','2015-08-10 15:36:05'),(61,'cliente','0004_auto_20150810_1105','2015-08-10 15:36:08'),(62,'contenido','0005_auto_20150810_1105','2015-08-10 15:36:15'),(63,'cotizacion','0010_auto_20150810_1105','2015-08-10 15:36:39'),(64,'direccion','0005_auto_20150810_1105','2015-08-10 15:36:41'),(65,'mueble','0005_auto_20150810_1105','2015-08-10 15:36:49'),(66,'presupuesto','0014_auto_20150810_1105','2015-08-10 15:36:56'),(67,'servicio','0007_auto_20150810_1105','2015-08-10 15:37:03'),(68,'contenido','0006_auto_20150813_1015','2015-08-13 14:46:55'),(69,'cotizacion','0011_auto_20150813_1015','2015-08-13 14:48:22'),(70,'direccion','0006_auto_20150813_1015','2015-08-13 14:48:27'),(71,'mueble','0006_auto_20150813_1015','2015-08-13 14:48:36'),(72,'presupuesto','0015_auto_20150813_1015','2015-08-13 14:49:36'),(73,'servicio','0008_auto_20150813_1015','2015-08-13 14:49:49'),(74,'trabajador','0002_auto_20150813_1015','2015-08-13 14:49:53'),(75,'cotizacion','0012_auto_20150813_1020','2015-08-13 14:50:43'),(76,'servicio','0009_auto_20150813_1555','2015-08-13 20:26:12'),(77,'servicio','0010_auto_20150813_1600','2015-08-13 20:30:30'),(78,'presupuesto','0016_auto_20150818_0923','2015-08-18 13:53:42'),(79,'servicio','0011_auto_20150818_0923','2015-08-18 13:53:43'),(80,'cotizacion','0013_vehiculo_cantidad_ayudante','2015-08-18 14:20:00'),(81,'presupuesto','0017_auto_20150818_1343','2015-08-18 18:14:21'),(82,'presupuesto','0018_auto_20150819_0838','2015-08-19 13:08:22'),(83,'presupuesto','0019_remove_presupuesto_cantidad_persona','2015-08-20 14:03:28'),(85,'presupuesto','0020_presupuesto_detalle_trasladable','2015-08-24 18:20:37'),(86,'premisas','0001_initial','2015-08-25 16:16:54'),(87,'premisas','0002_auto_20150826_1621','2015-08-26 20:51:53'),(88,'presupuesto','0021_auto_20150826_1621','2015-08-26 20:51:56'),(89,'presupuesto','0022_presupuesto_monto_descuesto_regargo','2015-08-27 18:40:18'),(90,'cotizacion','0014_auto_20150909_1153','2015-09-09 16:24:47'),(91,'presupuesto','0023_auto_20150909_1153','2015-09-09 16:24:53'),(92,'presupuesto','0024_presupuesto_monto_recursos_revisado','2015-09-09 19:58:19'),(93,'premisas','0003_fuentepromocion','2015-09-15 14:43:22'),(94,'presupuesto','0025_auto_20150915_1018','2015-09-15 14:50:16');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_bin NOT NULL,
  `session_data` longtext COLLATE utf8_bin NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  KEY `django_session_de54fa62` (`expire_date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0wxu967j8qu8w3oozetv8kbxjdq51iky','MTdhYTcwODdiZDBiODU1N2Y4ZTZmOGE0ODEyYjJkMWMyZTMwODU2ODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2NmMWZlNDkyMGI0MGM2ZWJmYWMzMDJjZjAwMzZiMThmODhkMjFlOCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-07-02 21:28:14'),('3cbhfc05gw9m6lio477e87r51n68nuef','ZDQ3NjY4ZTFmYjA5Y2VjMGQ3ZDZjODYzYmY4ZjdkNWM3NDNiZDk2ODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MSwiX2F1dGhfdXNlcl9oYXNoIjoiNDg4MzFlZmM4N2RlNjllMWNmMzIyYTlhNzVjY2U5OWMzYmRlNjU1MSJ9','2015-06-03 20:52:23'),('82xu5lfotcl4ph45dvuyjf7tkt50pxgh','OGFmYzM0ZDA4YzRiOTk5MWJlY2IxMDJkNThhY2YwYjljYWQ1MjEyMDp7Il9hdXRoX3VzZXJfaWQiOjEsIl9hdXRoX3VzZXJfaGFzaCI6IjQ4ODMxZWZjODdkZTY5ZTFjZjMyMmE5YTc1Y2NlOTljM2JkZTY1NTEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9','2015-05-26 21:15:45'),('bac4wtx05suh64fzc5cx1i8xkahh8p3g','NWNkMjM3N2M4NzliNzU3MDZmMWE0Y2MyMzc3YThkNDM4MTdlMzVjYTp7fQ==','2015-06-30 15:29:15'),('c8eh3fw9f9t0ogrmqj46oua86la5zaou','MGU1MDVkMjgwNzZhNDdiMjVhMjYzYTUwZDk0MDI5MzE4MGE3ZTY1NTp7Il9hdXRoX3VzZXJfaGFzaCI6IjljMzUyNjY5NTBjNWM0N2ZiNTY2MmY1ZDk0MjNmNDdiN2ZmOTQxOGQiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-09-22 16:14:13'),('corqt3u05xahyphqg4qu4ziy14pbuces','MGU1MDVkMjgwNzZhNDdiMjVhMjYzYTUwZDk0MDI5MzE4MGE3ZTY1NTp7Il9hdXRoX3VzZXJfaGFzaCI6IjljMzUyNjY5NTBjNWM0N2ZiNTY2MmY1ZDk0MjNmNDdiN2ZmOTQxOGQiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-09-23 14:53:11'),('fz9hzi42yqu6b313rsoe6vqhe1v03sa9','NTk4ZTU0MjJkZTAyYzk2Mzc2NDZjOWIyY2I2ZjJiYTliNzk2ZmMzMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiOWMzNTI2Njk1MGM1YzQ3ZmI1NjYyZjVkOTQyM2Y0N2I3ZmY5NDE4ZCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-08-19 20:45:28'),('hdmyi7d7mef5embcmxu6i740hke2dnts','NDY5OTY1YmMyNDA1YTllMGNjMWZkMGI1OTI2ZTliNzNkNGIyMGY3NDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5YzM1MjY2OTUwYzVjNDdmYjU2NjJmNWQ5NDIzZjQ3YjdmZjk0MThkIn0=','2015-09-08 16:22:39'),('hv118jkkrf0qbvrypoadntouilhqbzc8','NTBhNTk5Y2ZiYmI0MTUyYTBjMjg1YTBhMWU5OWI3YTJkMjUwNzY0YTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9oYXNoIjoiY2I1ZGUxYjlmODhiZmIxNTk1NzNhNGI2ZDdmZTc0NzkzY2I0MzUwMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwid2l6YXJkX2NvbnRhY3Rfd2l6YXJkIjp7InN0ZXBfZmlsZXMiOnt9LCJzdGVwIjpudWxsLCJzdGVwX2RhdGEiOnt9LCJleHRyYV9kYXRhIjp7fX19','2015-08-10 15:19:16'),('mx8i8uwkcy6qq4pmus701zrqb6jgdex6','N2VjYTEyODNhMDJiNTk4ZTMzOTQ2M2M4ZDY2ODUxMTRmZDBjNjg2OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjljMzUyNjY5NTBjNWM0N2ZiNTY2MmY1ZDk0MjNmNDdiN2ZmOTQxOGQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-09-17 20:26:06'),('ot5hr6mjfaubex9edzkh55983d8nelpe','NWNkMjM3N2M4NzliNzU3MDZmMWE0Y2MyMzc3YThkNDM4MTdlMzVjYTp7fQ==','2015-06-29 21:32:01'),('rvqk6v9meabdf9n7lieh2fcobzu0rq7c','MGU1MDVkMjgwNzZhNDdiMjVhMjYzYTUwZDk0MDI5MzE4MGE3ZTY1NTp7Il9hdXRoX3VzZXJfaGFzaCI6IjljMzUyNjY5NTBjNWM0N2ZiNTY2MmY1ZDk0MjNmNDdiN2ZmOTQxOGQiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-09-23 13:02:06'),('slm6qp5ykqn8reaprslifxkpxb3qialx','ZmI3Mjk2OTg3MzFhN2QxYmQ4MDg1MDhmMDI4YmZmZDY1ZGMyMGE4Njp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiNWRlMWI5Zjg4YmZiMTU5NTczYTRiNmQ3ZmU3NDc5M2NiNDM1MDIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2015-08-12 15:34:19'),('zmvv79azsqq0vc1e5nxo08me65d9vrko','ZWFlNTEwZTM5OTYzMTU3YjhlZWUyMmU1MmYwMDZmODhmY2UzNDBhMDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MiwiX2F1dGhfdXNlcl9oYXNoIjoiMWViMjg0ZWViNjNkN2FhOTVkNWY2MDY4NDUyOWE0NTY5Nzk4YTkzMyJ9','2015-07-02 14:56:45');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_densidad`
--

DROP TABLE IF EXISTS `mueble_densidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_densidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `descripcion` (`descripcion`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_densidad`
--

LOCK TABLES `mueble_densidad` WRITE;
/*!40000 ALTER TABLE `mueble_densidad` DISABLE KEYS */;
INSERT INTO `mueble_densidad` VALUES (3,'Alta'),(1,'Baja'),(2,'Media'),(4,'Muy alta');
/*!40000 ALTER TABLE `mueble_densidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_forma_mueble`
--

DROP TABLE IF EXISTS `mueble_forma_mueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_forma_mueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `forma` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `forma` (`forma`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_forma_mueble`
--

LOCK TABLES `mueble_forma_mueble` WRITE;
/*!40000 ALTER TABLE `mueble_forma_mueble` DISABLE KEYS */;
INSERT INTO `mueble_forma_mueble` VALUES (5,'Alto'),(4,'Ancho'),(7,'Cilindro'),(1,'Cubo'),(6,'Esfera'),(8,'Forma irregular'),(3,'Plano'),(2,'Rectángulo');
/*!40000 ALTER TABLE `mueble_forma_mueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_mueble`
--

DROP TABLE IF EXISTS `mueble_mueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_mueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mueble` varchar(100) COLLATE utf8_bin NOT NULL,
  `capacidad` decimal(8,3) NOT NULL,
  `trasladable` tinyint(1) NOT NULL,
  `apilable` tinyint(1) NOT NULL,
  `capacidad_carga` tinyint(1) NOT NULL,
  `capacidad_interna` tinyint(1) NOT NULL,
  `forma_id` int(11) NOT NULL,
  `ocupacion_id` int(11) NOT NULL,
  `tipo_mueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `mueble` (`mueble`) USING BTREE,
  KEY `mueble_mueble_6393d075` (`forma_id`) USING BTREE,
  KEY `mueble_mueble_f4701cc2` (`ocupacion_id`) USING BTREE,
  KEY `mueble_mueble_3cda6187` (`tipo_mueble_id`) USING BTREE,
  CONSTRAINT `mueble_mueble_forma_id_ed07595_fk_mueble_forma_mueble_id` FOREIGN KEY (`forma_id`) REFERENCES `mueble_forma_mueble` (`id`),
  CONSTRAINT `mueble_mueble_ocupacion_id_384fcfda_fk_mueble_ocupacion_id` FOREIGN KEY (`ocupacion_id`) REFERENCES `mueble_ocupacion` (`id`),
  CONSTRAINT `mueble_mueble_tipo_mueble_id_7755acaa_fk_mueble_tipo_mueble_id` FOREIGN KEY (`tipo_mueble_id`) REFERENCES `mueble_tipo_mueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_mueble`
--

LOCK TABLES `mueble_mueble` WRITE;
/*!40000 ALTER TABLE `mueble_mueble` DISABLE KEYS */;
INSERT INTO `mueble_mueble` VALUES (1,'Mesa de comedor redonda',0.000,1,1,1,0,3,1,4),(2,'Armario empotrado',0.800,0,0,0,1,1,1,11),(3,'Mesa de metal y vidrio',0.000,1,1,1,0,3,1,4),(4,'Mesa de piedra y vidrio',0.000,1,1,1,0,3,1,4),(5,'Mesita de noche',0.000,1,1,1,0,3,1,4),(6,'Mesa ratona',0.000,0,1,1,0,3,1,4),(7,'Mesa de centro',0.000,0,1,1,0,3,1,4),(8,'Mesa de café',0.000,0,1,1,0,3,1,4),(9,'Mesa de apoyo',0.000,0,1,1,0,3,1,4),(10,'Silla de comedor sin asas',0.000,0,1,1,0,1,1,2),(11,'Silla de comedor con asas',0.000,0,1,1,0,1,1,2),(12,'Silla metálica',0.000,0,1,1,0,1,1,2),(13,'Sillón con posa brazos',0.000,0,1,1,0,1,1,12),(14,'Sillón en L de 2 cuerpos',0.000,0,1,1,0,1,1,12),(15,'Sillón en L de 3 cuerpos',0.000,0,1,1,0,1,1,12),(16,'Silla mecedora',0.000,0,1,1,0,1,1,2),(17,'Banqueta de madera',0.000,0,1,1,0,1,1,2),(19,'Banqueta de plástico',0.000,0,1,1,0,1,1,2),(20,'Sillón de 2 puestos',0.000,0,1,1,0,1,1,12),(21,'Sillón de 3 puestos',0.000,0,1,1,0,1,1,12),(22,'Sillón sin posa brazos',0.000,0,1,1,0,1,1,12),(23,'Silla descalzadora',0.000,0,1,1,0,1,1,2),(24,'Sofá de 1 puesto',0.000,0,1,1,0,1,1,5),(25,'Sofá de 2 puestos',0.000,0,1,1,0,1,1,5),(26,'Sofá de 3 puestos',0.000,0,1,1,0,1,1,5),(27,'Sofá sin posa brazos',0.000,0,1,1,0,1,1,5),(28,'Vidriera / Aparador',0.000,0,1,1,0,1,1,11),(29,'Pie de amigo',0.000,0,1,1,0,1,1,11),(30,'Aeroclóset',0.000,0,1,1,0,3,1,11),(31,'Armario / Ropero',0.000,0,1,1,0,1,1,11),(32,'Cónsola de Hall',0.000,0,1,1,0,1,1,11),(33,'Centro de entretenimiento',0.000,0,1,1,0,1,1,11),(34,'Alacena',0.050,0,1,1,0,1,1,11),(35,'Cómoda',0.000,0,1,1,0,1,1,11),(36,'Gavetero sencillo',0.000,0,1,1,0,1,1,11),(37,'Gavetero doble',0.000,0,1,1,0,1,1,11),(38,'Cama individual',0.000,1,1,1,0,2,1,3),(39,'Cama matrimonial',0.000,1,1,1,0,2,1,3),(40,'Cama Queen',0.000,1,1,1,0,2,1,3),(41,'Cama King',0.000,1,1,1,0,2,1,3),(42,'Cama litera',0.000,1,1,1,0,2,1,3),(43,'Cama duplex',0.000,1,1,1,0,2,1,3),(44,'Cabecera / Tope',0.000,1,1,1,0,2,1,3),(45,'Box-Spring individual',0.000,1,1,1,0,2,1,3),(46,'Box-Spring matrimonial',0.000,1,1,1,0,2,1,3),(47,'Box-Spring Queen',0.000,1,1,1,0,2,1,3),(48,'Box-Spring King',0.000,1,1,1,0,2,1,3),(49,'Colchón individual',0.000,0,1,1,0,2,1,3),(50,'Colchón matrimonial',0.000,0,1,1,0,2,1,3),(51,'Colchón Queen',0.000,0,1,1,0,2,1,3),(52,'Colchón King',0.000,0,1,1,0,2,1,3),(53,'Colchoneta',0.000,0,1,1,0,2,1,3),(54,'Cuadro con madera',0.000,0,1,1,0,3,1,8),(55,'Cuadro con metal',0.000,0,1,1,0,3,1,8),(56,'Cuadro de cristal',0.000,0,1,1,0,3,1,8),(57,'Lámpara de pie',0.000,0,1,1,0,1,1,8),(58,'Alfombra',0.000,0,1,1,0,7,1,14),(59,'Escultura de piedra',0.000,0,1,1,0,1,1,8),(60,'Escultura de madera',0.000,0,1,1,0,1,1,8),(61,'Escultura de metal',0.000,0,1,1,0,1,1,8),(62,'Acordeón',0.000,1,1,1,0,3,1,1),(63,'Jarrón cerámico',0.000,0,1,1,0,1,1,1),(64,'Cesta / Canasto',0.000,0,1,1,0,1,1,1),(65,'Revistero',0.000,0,1,1,0,1,1,1),(66,'Vinera',0.000,0,1,1,0,1,1,13),(67,'Mesón / tope de cocina',0.000,0,1,1,0,1,1,13),(68,'Muebles aéreos empotrables',0.000,0,1,1,0,1,1,13),(69,'Muebles bajos empotrables',0.000,0,1,1,0,1,1,13),(70,'TV Plano',0.000,0,1,1,0,1,1,6),(71,'TV Normal',0.000,0,1,1,0,1,1,6),(72,'Equipo de sonido',0.000,0,1,1,0,1,1,6),(73,'Cornetas',0.000,0,1,1,0,1,1,6),(74,'Micro ondas',0.000,1,1,1,0,1,1,6),(75,'Electrodomésticos mayores',0.000,0,1,1,0,1,1,6),(76,'Cocina',0.000,0,1,1,0,1,1,4),(77,'Lavadora',0.000,0,1,1,0,1,1,4),(78,'Nevera de 1 puerta',0.000,0,1,1,0,1,1,4),(79,'Nevera de varias puertas',0.000,0,1,1,0,1,1,4),(80,'Congelador',0.000,0,1,1,0,1,1,4),(81,'Congelador / Vitrina',0.000,0,1,1,0,1,1,4),(82,'Lavadora de platos',0.000,0,1,1,0,1,1,4),(83,'Secadora',0.000,0,1,1,0,1,1,4),(84,'Aspiradora',0.000,0,1,1,0,8,1,4),(85,'Lavadora / Secadora',0.000,0,1,1,0,1,1,4),(86,'Aire acondicionado portátil',0.000,0,1,1,0,1,1,4),(87,'Aire acondicionado Split',0.000,0,1,1,0,1,1,4),(88,'Aire acondicionado Integral',0.000,0,1,1,0,1,1,4),(89,'Otros de línea blanca mayores',0.000,0,1,1,0,1,1,4),(90,'Otros de línea blanca menores',0.000,0,1,1,0,1,1,4),(91,'Mesa de comedor cuadrada',0.000,0,1,1,0,1,1,4);
/*!40000 ALTER TABLE `mueble_mueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_mueble_ambiente`
--

DROP TABLE IF EXISTS `mueble_mueble_ambiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_mueble_ambiente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `predefinido` tinyint(1) NOT NULL,
  `ambiente_id` int(11) NOT NULL,
  `mueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `mueble_mueble_ambiente_mueble_id_34c19162_uniq` (`mueble_id`,`ambiente_id`) USING BTREE,
  KEY `mueble_mueble_ambiente_672bf590` (`ambiente_id`) USING BTREE,
  KEY `mueble_mueble_ambiente_49933347` (`mueble_id`) USING BTREE,
  CONSTRAINT `mueble_mueble_ambie_ambiente_id_2800c904_fk_ambiente_ambiente_id` FOREIGN KEY (`ambiente_id`) REFERENCES `ambiente_ambiente` (`id`),
  CONSTRAINT `mueble_mueble_ambiente_mueble_id_493d2911_fk_mueble_mueble_id` FOREIGN KEY (`mueble_id`) REFERENCES `mueble_mueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_mueble_ambiente`
--

LOCK TABLES `mueble_mueble_ambiente` WRITE;
/*!40000 ALTER TABLE `mueble_mueble_ambiente` DISABLE KEYS */;
INSERT INTO `mueble_mueble_ambiente` VALUES (1,0,18,1),(2,0,11,2),(3,0,11,39),(4,0,11,5),(5,0,11,62),(6,0,13,62),(7,0,12,62);
/*!40000 ALTER TABLE `mueble_mueble_ambiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_ocupacion`
--

DROP TABLE IF EXISTS `mueble_ocupacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_ocupacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) COLLATE utf8_bin NOT NULL,
  `valor` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `descripcion` (`descripcion`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_ocupacion`
--

LOCK TABLES `mueble_ocupacion` WRITE;
/*!40000 ALTER TABLE `mueble_ocupacion` DISABLE KEYS */;
INSERT INTO `mueble_ocupacion` VALUES (1,'Vacío',0.00),(2,'Medio vacío',0.30),(3,'Medio Lleno',0.60),(4,'Lleno',0.90);
/*!40000 ALTER TABLE `mueble_ocupacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_tamano`
--

DROP TABLE IF EXISTS `mueble_tamano`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_tamano` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `descripcion` (`descripcion`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_tamano`
--

LOCK TABLES `mueble_tamano` WRITE;
/*!40000 ALTER TABLE `mueble_tamano` DISABLE KEYS */;
INSERT INTO `mueble_tamano` VALUES (4,'Enorme'),(3,'Grande'),(2,'Mediano'),(1,'Pequeño');
/*!40000 ALTER TABLE `mueble_tamano` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_tamano_mueble`
--

DROP TABLE IF EXISTS `mueble_tamano_mueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_tamano_mueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ancho` decimal(7,2) NOT NULL,
  `largo` decimal(7,2) NOT NULL,
  `alto` decimal(7,2) NOT NULL,
  `peso` decimal(9,3) NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  `densidad_id` int(11) NOT NULL,
  `mueble_id` int(11) NOT NULL,
  `tamano_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `mueble_tamano_mueble_tamano_id_6352bdf4_uniq` (`tamano_id`,`mueble_id`,`densidad_id`) USING BTREE,
  KEY `mueble_tamano_mueble_5b1b1ad3` (`densidad_id`) USING BTREE,
  KEY `mueble_tamano_mueble_49933347` (`mueble_id`) USING BTREE,
  KEY `mueble_tamano_mueble_ef0d9c99` (`tamano_id`) USING BTREE,
  CONSTRAINT `mueble_tamano_mueble_densidad_id_114fdc64_fk_muebl` FOREIGN KEY (`densidad_id`) REFERENCES `mueble_densidad` (`id`),
  CONSTRAINT `mueble_tamano_mueble_mueble_id_1e5e15ab_fk_mueble_` FOREIGN KEY (`mueble_id`) REFERENCES `mueble_mueble` (`id`),
  CONSTRAINT `mueble_tamano_mueble_tamano_id_7a7219ad_fk_mueble_` FOREIGN KEY (`tamano_id`) REFERENCES `mueble_tamano` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_tamano_mueble`
--

LOCK TABLES `mueble_tamano_mueble` WRITE;
/*!40000 ALTER TABLE `mueble_tamano_mueble` DISABLE KEYS */;
INSERT INTO `mueble_tamano_mueble` VALUES (1,1.00,0.60,2.00,0.050,0,1,1,1),(2,50.00,30.00,200.00,0.000,0,1,2,1),(3,100.00,60.00,200.00,0.000,0,2,2,2),(4,1.00,1.00,1.00,1.000,0,2,2,1),(5,30.00,51.00,38.00,2.000,0,2,74,1),(6,100.00,50.00,100.00,2.000,1,2,34,2);
/*!40000 ALTER TABLE `mueble_tamano_mueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_tipo_mueble`
--

DROP TABLE IF EXISTS `mueble_tipo_mueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_tipo_mueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_mueble` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `tipo_mueble` (`tipo_mueble`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_tipo_mueble`
--

LOCK TABLES `mueble_tipo_mueble` WRITE;
/*!40000 ALTER TABLE `mueble_tipo_mueble` DISABLE KEYS */;
INSERT INTO `mueble_tipo_mueble` VALUES (10,'Armarios y roperos'),(3,'Camas'),(13,'Cocina'),(8,'Cuadros y adornos colgantes'),(6,'Electrodomésticos'),(11,'Estanterias'),(7,'Floreros y jarrones'),(4,'Línea blanca'),(1,'Mesas'),(9,'Percheros y colgadores'),(2,'Sillas'),(12,'Sillones'),(14,'Sobre pisos'),(5,'Sofás');
/*!40000 ALTER TABLE `mueble_tipo_mueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `premisas_empresa`
--

DROP TABLE IF EXISTS `premisas_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `premisas_empresa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `empresa` varchar(250) COLLATE utf8_bin NOT NULL,
  `telefonos` varchar(250) COLLATE utf8_bin NOT NULL,
  `direccion` varchar(250) COLLATE utf8_bin NOT NULL,
  `sitio_web` varchar(200) COLLATE utf8_bin NOT NULL,
  `correo` varchar(254) COLLATE utf8_bin NOT NULL,
  `responsable` varchar(250) COLLATE utf8_bin DEFAULT NULL,
  `cuit` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `logo` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premisas_empresa`
--

LOCK TABLES `premisas_empresa` WRITE;
/*!40000 ALTER TABLE `premisas_empresa` DISABLE KEYS */;
INSERT INTO `premisas_empresa` VALUES (1,'Mudarte','4701 1177','3 de Febrero 3455 | Nuñez Ciudad Autónoma de Buenos Aires, Argentina','http://www.mudarte.com.ar','info@mudarte.com.ar','','','static/image/logo.png');
/*!40000 ALTER TABLE `premisas_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `premisas_fuentepromocion`
--

DROP TABLE IF EXISTS `premisas_fuentepromocion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `premisas_fuentepromocion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fuente_promocion` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premisas_fuentepromocion`
--

LOCK TABLES `premisas_fuentepromocion` WRITE;
/*!40000 ALTER TABLE `premisas_fuentepromocion` DISABLE KEYS */;
/*!40000 ALTER TABLE `premisas_fuentepromocion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presupuesto_datosprecargado`
--

DROP TABLE IF EXISTS `presupuesto_datosprecargado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `presupuesto_datosprecargado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `complejidadinmueble` varchar(100) COLLATE utf8_bin NOT NULL,
  `factorcomplejidadinmueble` decimal(5,2) NOT NULL,
  `valorambcompleinmueble` decimal(9,2) NOT NULL,
  `valorm3compleinmueble` decimal(9,2) NOT NULL,
  `ocupacioninmueble` varchar(100) COLLATE utf8_bin NOT NULL,
  `valorocupacioninmueble` decimal(5,2) NOT NULL,
  `densidadcontenidomueble` decimal(7,2) NOT NULL,
  `volcontenedormueble` decimal(8,3) NOT NULL,
  `peso_contenedormueble` decimal(9,3) NOT NULL,
  `capvolcontenedormueble` decimal(8,3) NOT NULL,
  `cappesocontenedormueble` decimal(9,3) NOT NULL,
  `tamanomueble` varchar(100) COLLATE utf8_bin NOT NULL,
  `densidadmueble` varchar(100) COLLATE utf8_bin NOT NULL,
  `anchomueble` decimal(7,2) NOT NULL,
  `largomueble` decimal(7,2) NOT NULL,
  `altomueble` decimal(7,2) NOT NULL,
  `pesomueble` decimal(9,3) NOT NULL,
  `valordensidadmueble` decimal(5,2) NOT NULL,
  `volumenmueble` decimal(8,3) NOT NULL,
  `tarifacomplejidadservicio` decimal(9,2) NOT NULL,
  `factortiempocompservicio` decimal(7,2) NOT NULL,
  `materialservicio` varchar(100) COLLATE utf8_bin NOT NULL,
  `preciomaterial` decimal(9,2) NOT NULL,
  `volmaterial` decimal(8,3) NOT NULL,
  `pesomaterial` decimal(9,3) NOT NULL,
  `cantidadmaterial` decimal(7,2) NOT NULL,
  `montomaterial` decimal(9,2) NOT NULL,
  `duracion_optimamudanza` decimal(7,2) NOT NULL,
  `rendimiento_peso` decimal(9,3) NOT NULL,
  `rendimiento_unidad` int(10) unsigned NOT NULL,
  `rendimiento_volumen` decimal(8,3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presupuesto_datosprecargado`
--

LOCK TABLES `presupuesto_datosprecargado` WRITE;
/*!40000 ALTER TABLE `presupuesto_datosprecargado` DISABLE KEYS */;
INSERT INTO `presupuesto_datosprecargado` VALUES (1,'No definida',1.00,0.01,0.01,'No definida',0.01,0.01,0.001,0.001,0.001,0.001,'No definido','No definida',0.01,0.01,0.01,0.001,0.01,0.001,0.01,0.10,'No aplica',0.00,0.001,0.001,0.00,0.00,4.00,250.000,20,1.500);
/*!40000 ALTER TABLE `presupuesto_datosprecargado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presupuesto_presupuesto`
--

DROP TABLE IF EXISTS `presupuesto_presupuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `presupuesto_presupuesto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dni` varchar(20) NOT NULL,
  `nombre_cliente` varchar(250) NOT NULL,
  `telefono` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `fecha_estimadamudanza` date NOT NULL,
  `descripcion_vehiculo` longtext NOT NULL,
  `descripcion_persona` longtext NOT NULL,
  `cantidad_vehiculo` int(11) NOT NULL,
  `cantidad_ambientes` int(11) NOT NULL,
  `cantidad_muebles` int(11) NOT NULL,
  `cantidad_contenedores` int(11) NOT NULL,
  `total_peso_contenedores` decimal(9,3) NOT NULL,
  `total_peso_muebles` decimal(9,3) NOT NULL,
  `total_peso_contenidos` decimal(9,3) NOT NULL,
  `total_volumen_muebles` decimal(8,3) NOT NULL,
  `total_volumen_contenedores` decimal(8,3) NOT NULL,
  `total_volumen_contenidos` decimal(8,3) NOT NULL,
  `total_m3` decimal(8,3) NOT NULL,
  `recorrido_km` decimal(7,2) NOT NULL,
  `tiempo_recorrido` decimal(7,2) NOT NULL,
  `tiempo_carga` decimal(7,2) NOT NULL,
  `tiempo_total` decimal(7,2) NOT NULL,
  `monto_vehiculo_hora` decimal(9,2) NOT NULL,
  `monto_vehiculo_recorrido` decimal(9,2) NOT NULL,
  `monto_personaoptima` decimal(9,2) DEFAULT NULL,
  `monto_sin_impuesto` decimal(9,2) NOT NULL,
  `monto_impuesto` decimal(9,2) NOT NULL,
  `monto_con_impuesto` decimal(9,2) NOT NULL,
  `cotizador_id` int(11) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `total_capacidad_vehiculokg` decimal(8,3) DEFAULT NULL,
  `total_peso_materiales` decimal(9,3) NOT NULL,
  `total_peso_mudanza` decimal(9,3) NOT NULL,
  `total_volumen_materiales` decimal(8,3) NOT NULL,
  `activo` varchar(20) NOT NULL,
  `monto_materiales` decimal(9,2) NOT NULL,
  `monto_servicios` decimal(9,2) NOT NULL,
  `tiempo_servicios` decimal(7,2) NOT NULL,
  `cantidad_ayudante` int(11) NOT NULL,
  `cantidad_ayudanteadicional` int(11) NOT NULL,
  `duracion_teorica` decimal(7,2) NOT NULL,
  `monto_amb_inmueble` decimal(9,2) NOT NULL,
  `monto_m3_inmueble` decimal(9,2) NOT NULL,
  `monto_mudanza_hrsdirectas` decimal(9,2) NOT NULL,
  `monto_mundanza_hrsoptimas` decimal(9,2) NOT NULL,
  `duracion_optima` decimal(7,2) NOT NULL,
  `monto_personateorica` decimal(9,2) NOT NULL,
  `total_capacidad_vehiculovol` decimal(8,3) NOT NULL,
  `monto_descuesto_regargo` decimal(9,2) NOT NULL,
  `monto_materiales_revisado` decimal(9,2) NOT NULL,
  `monto_mundanza_revisada` decimal(9,2) NOT NULL,
  `monto_servicios_revisado` decimal(9,2) NOT NULL,
  `monto_vehiculo_revisado` decimal(9,2) NOT NULL,
  `tipo_calculo` varchar(20) NOT NULL,
  `monto_recursos_revisado` decimal(9,2) NOT NULL,
  `cargo_cliente` varchar(250) NOT NULL,
  `empresa_cliente` varchar(250) NOT NULL,
  `fuente_promocion` varchar(100) NOT NULL,
  `hora_creacion` time(6) NOT NULL,
  `hora_estimadamudanza` time(6) NOT NULL,
  `telefono_celular` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `presupuesto_presupuesto_cotizador_id_25e7c2c5_fk_auth_user_id` (`cotizador_id`),
  CONSTRAINT `presupuesto_presupuesto_cotizador_id_25e7c2c5_fk_auth_user_id` FOREIGN KEY (`cotizador_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presupuesto_presupuesto`
--

LOCK TABLES `presupuesto_presupuesto` WRITE;
/*!40000 ALTER TABLE `presupuesto_presupuesto` DISABLE KEYS */;
INSERT INTO `presupuesto_presupuesto` VALUES (1,'17308789','yusnel','04140576077','yusnelvy@gmail.com','2015-07-13','2015-07-30','Modelo: Mercedes Benz Sprinter 313 CDI Panel Van - Tarifa $/h: 150.00 - Tarifa $/Km: 15.00 - Capacidad m3: 13.000 - Capacidad Kgs: 1500.000 - Cantidad: 1 - Volumen Total: 13.000 - Total Tarifa $/h: 150.00 - Total Tarifa $/Km: 300.00','Conductor asignado: Chofer tipo 1 al modelo: Mercedes Benz Sprinter 313 CDI Panel Van - Tarifa $/día: 75.00 - Cantidad de conductor: 1 - Total Tarifa $/hrs: 75.00 - Cantidad de ayudantes: 4 - Tarifa $/día: 50.00 - Total Tarifa $/hrs: 200.00',1,2,2,6,30.000,0.002,144.000,2.156,1.500,0.288,3.657,20.00,1.00,0.00,0.00,150.00,300.00,341.00,0.00,0.00,0.00,2,'Terminado cotizador',1500.000,0.001,174.003,0.001,'Activado',0.00,0.01,0.10,4,0,1.24,2800.00,511.98,3250.01,3250.01,4.00,341.00,13.000,0.00,40.00,3000.00,30.00,130.00,'Optimizado',2800.00,'','','Cliente','01:00:00.000000','01:00:00.000000',''),(2,'123456','Pedro','12344','yusnelvy2@gmail.com','2015-09-09','2015-09-09','0','0',0,0,0,0,0.000,0.000,0.000,0.000,0.000,0.000,0.000,20.00,1.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1,'Iniciado',0.000,0.000,0.000,0.000,'Activado',0.00,0.00,0.00,0,0,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.000,0.00,0.00,0.00,0.00,0.00,'Optimizado',0.00,'','','Cliente','01:00:00.000000','01:00:00.000000','');
/*!40000 ALTER TABLE `presupuesto_presupuesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presupuesto_presupuesto_detalle`
--

DROP TABLE IF EXISTS `presupuesto_presupuesto_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `presupuesto_presupuesto_detalle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ambiente` varchar(100) NOT NULL,
  `mueble` varchar(100) NOT NULL,
  `tamano` varchar(100) NOT NULL,
  `ancho` decimal(7,2) NOT NULL,
  `largo` decimal(7,2) NOT NULL,
  `alto` decimal(7,2) NOT NULL,
  `densidad` varchar(100) NOT NULL,
  `valor_densidad` decimal(9,2) NOT NULL,
  `peso` decimal(9,3) NOT NULL,
  `ocupacidad` varchar(100) NOT NULL,
  `valor_ocupacidad` decimal(5,2) NOT NULL,
  `cantidad_contenedor` int(11) NOT NULL,
  `volumen_contenido` decimal(8,3) NOT NULL,
  `volumen_contenedor` decimal(8,3) NOT NULL,
  `volumen_mueble` decimal(8,3) NOT NULL,
  `capacidad_peso_contenedor` decimal(9,3) NOT NULL,
  `capacidad_volumen_contenedor` decimal(8,3) NOT NULL,
  `peso_contenido` decimal(9,3) NOT NULL,
  `peso_contenedor` decimal(9,3) NOT NULL,
  `presupuesto_id` int(11) NOT NULL,
  `descripcion_contenedor` varchar(100) NOT NULL,
  `trasladable` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `presupuest_presupuesto_id_5551e79f_fk_presupuesto_presupuesto_id` (`presupuesto_id`),
  CONSTRAINT `presupuest_presupuesto_id_5551e79f_fk_presupuesto_presupuesto_id` FOREIGN KEY (`presupuesto_id`) REFERENCES `presupuesto_presupuesto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presupuesto_presupuesto_detalle`
--

LOCK TABLES `presupuesto_presupuesto_detalle` WRITE;
/*!40000 ALTER TABLE `presupuesto_presupuesto_detalle` DISABLE KEYS */;
INSERT INTO `presupuesto_presupuesto_detalle` VALUES (1,'Habitación principal','Cama matrimonial','No definido',150.00,200.00,20.00,'No definida',0.00,0.001,'Vacío',0.00,0,0.000,0.000,0.599,0.001,0.001,0.000,0.000,1,'No definido',1),(2,'Habitación principal','Armario empotrado','Mediano',100.00,60.00,200.00,'Media',0.00,0.000,'Medio vacío',0.30,6,0.288,1.500,1.200,25.000,0.200,144.000,30.000,1,'Ropero',0),(3,'Cocina','Nevera de varias puertas','No definido',84.00,112.00,165.50,'No definida',0.00,0.001,'Vacío',0.00,0,0.000,0.000,1.557,0.001,0.001,0.000,0.000,1,'No definido',1);
/*!40000 ALTER TABLE `presupuesto_presupuesto_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presupuesto_presupuesto_direccion`
--

DROP TABLE IF EXISTS `presupuesto_presupuesto_direccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `presupuesto_presupuesto_direccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `direccion` longtext NOT NULL,
  `tipo_direccion` varchar(100) NOT NULL,
  `tipo_inmueble` varchar(100) NOT NULL,
  `ocupacidad_inmueble` varchar(100) NOT NULL,
  `valor_ocupacidad` decimal(5,2) NOT NULL,
  `pisos` int(11) NOT NULL,
  `pisos_escalera` int(11) NOT NULL,
  `rampa` tinyint(1) NOT NULL,
  `ascensor` tinyint(1) NOT NULL,
  `ascensor_servicio` tinyint(1) NOT NULL,
  `pisos_ascensor_servicio` int(11) NOT NULL,
  `pisos_ascensor` int(11) NOT NULL,
  `complejidad` varchar(100) NOT NULL,
  `factor_complejidad` decimal(5,2) NOT NULL,
  `valor_ambiente_complejidad` decimal(9,2) NOT NULL,
  `valor_metrocubico_complejiadad` decimal(9,2) NOT NULL,
  `distancia_vehiculo` int(11) NOT NULL,
  `total_m2` decimal(7,2) NOT NULL,
  `presupuesto_id` int(11) NOT NULL,
  `orden` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `presupuest_presupuesto_id_17f2d8fb_fk_presupuesto_presupuesto_id` (`presupuesto_id`),
  CONSTRAINT `presupuest_presupuesto_id_17f2d8fb_fk_presupuesto_presupuesto_id` FOREIGN KEY (`presupuesto_id`) REFERENCES `presupuesto_presupuesto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presupuesto_presupuesto_direccion`
--

LOCK TABLES `presupuesto_presupuesto_direccion` WRITE;
/*!40000 ALTER TABLE `presupuesto_presupuesto_direccion` DISABLE KEYS */;
INSERT INTO `presupuesto_presupuesto_direccion` VALUES (1,'Carrera 19 entre 24 y 25, zona centro','Destino','Oficina','Medio vacío',0.30,10,10,0,1,0,0,10,'Media',0.40,1.00,1.00,10,40.00,1,1),(9,'Carrera 18 entre 23 y 24','Origen','Oficina','Medio Lleno',0.60,1,10,0,1,0,0,10,'Media',1.00,1400.00,140.00,10,40.00,1,1);
/*!40000 ALTER TABLE `presupuesto_presupuesto_direccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `presupuesto_presupuesto_servicio`
--

DROP TABLE IF EXISTS `presupuesto_presupuesto_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `presupuesto_presupuesto_servicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `servicio` varchar(100) NOT NULL,
  `cantidad_material` decimal(7,2) DEFAULT NULL,
  `material` longtext NOT NULL,
  `monto_material` decimal(9,2) NOT NULL,
  `volumen_material` decimal(8,3) NOT NULL,
  `peso_material` decimal(9,3) NOT NULL,
  `detalle_presupuesto_id` int(11) NOT NULL,
  `tiempo_aplicado` decimal(7,2) NOT NULL,
  `monto_servicio` decimal(9,2) NOT NULL,
  `precio_material` decimal(9,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `D76317b5086058f57ff4e5e2c432fbf9` (`detalle_presupuesto_id`),
  CONSTRAINT `D76317b5086058f57ff4e5e2c432fbf9` FOREIGN KEY (`detalle_presupuesto_id`) REFERENCES `presupuesto_presupuesto_detalle` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presupuesto_presupuesto_servicio`
--

LOCK TABLES `presupuesto_presupuesto_servicio` WRITE;
/*!40000 ALTER TABLE `presupuesto_presupuesto_servicio` DISABLE KEYS */;
INSERT INTO `presupuesto_presupuesto_servicio` VALUES (4,'Desarmar',0.00,'No aplica',0.00,0.001,0.001,1,0.10,0.01,0.00);
/*!40000 ALTER TABLE `presupuesto_presupuesto_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_complejidad`
--

DROP TABLE IF EXISTS `servicio_complejidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio_complejidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `descripcion` (`descripcion`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_complejidad`
--

LOCK TABLES `servicio_complejidad` WRITE;
/*!40000 ALTER TABLE `servicio_complejidad` DISABLE KEYS */;
INSERT INTO `servicio_complejidad` VALUES (4,'Alta'),(2,'Baja'),(3,'Media'),(5,'Muy alta'),(1,'Muy baja');
/*!40000 ALTER TABLE `servicio_complejidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_complejidad_servicio`
--

DROP TABLE IF EXISTS `servicio_complejidad_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio_complejidad_servicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tarifa` decimal(9,2) NOT NULL,
  `complejidad_id` int(11) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  `factor_tiempo` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `servicio_complejidad_servicio_servicio_id_79095e8f_uniq` (`servicio_id`,`complejidad_id`) USING BTREE,
  KEY `servicio_complejidad_servicio_008d38e3` (`complejidad_id`) USING BTREE,
  KEY `servicio_complejidad_servicio_4bb699dc` (`servicio_id`) USING BTREE,
  CONSTRAINT `servicio_comp_complejidad_id_362df05f_fk_servicio_complejidad_id` FOREIGN KEY (`complejidad_id`) REFERENCES `servicio_complejidad` (`id`),
  CONSTRAINT `servicio_complejidad_servicio_id_f87f6e9_fk_servicio_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicio_servicio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_complejidad_servicio`
--

LOCK TABLES `servicio_complejidad_servicio` WRITE;
/*!40000 ALTER TABLE `servicio_complejidad_servicio` DISABLE KEYS */;
INSERT INTO `servicio_complejidad_servicio` VALUES (1,5.00,1,4,1.00),(2,50.00,3,2,1.00),(3,40.00,1,2,1.00),(4,45.00,2,2,1.00),(5,60.00,4,2,1.00),(6,70.00,5,2,1.00),(7,25.00,1,13,1.00),(8,30.00,2,13,1.00),(9,35.00,3,13,1.00),(10,40.00,4,13,1.00),(11,45.00,5,13,1.00),(12,25.00,1,14,1.00),(13,30.00,2,14,1.00),(14,35.00,3,14,1.00),(15,40.00,4,14,1.00),(16,45.00,5,14,1.00),(17,30.00,1,5,1.00),(18,20.00,1,3,1.00),(19,25.00,1,7,0.10),(20,30.00,2,7,0.15),(21,35.00,3,7,0.20),(22,40.00,4,7,0.25),(23,45.00,5,7,0.30);
/*!40000 ALTER TABLE `servicio_complejidad_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_material`
--

DROP TABLE IF EXISTS `servicio_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `material` varchar(100) COLLATE utf8_bin NOT NULL,
  `precio` decimal(9,2) NOT NULL,
  `peso` decimal(9,3) NOT NULL,
  `recuperable` tinyint(1) NOT NULL,
  `alto` decimal(7,2) NOT NULL,
  `ancho` decimal(7,2) NOT NULL,
  `capacidad_peso` decimal(9,3) NOT NULL,
  `capacidad_volumen` decimal(8,3) NOT NULL,
  `contenedor` tinyint(1) NOT NULL,
  `largo` decimal(7,2) NOT NULL,
  `unidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `material` (`material`) USING BTREE,
  KEY `servicio_material_d8b8136c` (`unidad_id`) USING BTREE,
  CONSTRAINT `servicio_material_unidad_id_258a6c1f_fk_servicio_unidad_id` FOREIGN KEY (`unidad_id`) REFERENCES `servicio_unidad` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_material`
--

LOCK TABLES `servicio_material` WRITE;
/*!40000 ALTER TABLE `servicio_material` DISABLE KEYS */;
INSERT INTO `servicio_material` VALUES (1,'Pluriball',138.00,6.000,0,10.00,250.00,1.000,1.000,0,10.00,1),(2,'Stretch',178.00,4.000,0,0.01,50.00,0.000,0.000,0,4500.00,1),(3,'Corrugado',70.00,20.000,1,1.00,1.00,1.000,1.000,0,1.00,1),(4,'Cintas de embalar',15.00,0.075,0,0.00,0.00,0.000,0.000,0,0.00,1),(5,'Caja 40',14.00,12.000,0,1.00,1.00,1.000,1.000,1,1.00,1),(6,'Caja grande',19.00,0.200,0,1.00,1.00,1.000,1.000,1,1.00,1),(7,'Canasto',500.00,5.000,1,1.00,1.00,1.000,1.000,1,1.00,1),(8,'Ropero',500.00,5.000,1,100.00,50.00,25.000,0.800,1,50.00,1),(9,'Cordel de nylon 2 mm',10.00,0.100,0,0.00,0.00,0.000,0.000,0,0.00,1),(10,'Papel manteca',10.00,0.100,0,0.01,0.01,0.001,0.001,0,0.01,1);
/*!40000 ALTER TABLE `servicio_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_servicio`
--

DROP TABLE IF EXISTS `servicio_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio_servicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `servicio` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `servicio` (`servicio`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_servicio`
--

LOCK TABLES `servicio_servicio` WRITE;
/*!40000 ALTER TABLE `servicio_servicio` DISABLE KEYS */;
INSERT INTO `servicio_servicio` VALUES (4,'Armar'),(6,'Baulera'),(13,'Caja 40'),(10,'Caja fuerte'),(14,'Canasto'),(2,'Corrugado'),(5,'Desarmar'),(11,'Frágil'),(9,'Piano'),(3,'Pluriball'),(15,'Ropero'),(12,'Seguro'),(1,'Soga'),(7,'Stretch');
/*!40000 ALTER TABLE `servicio_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_servicio_material`
--

DROP TABLE IF EXISTS `servicio_servicio_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio_servicio_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` decimal(7,2) NOT NULL,
  `material_id` int(11) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  `calculo` varchar(200) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `servicio_servicio_material_servicio_id_75f76c93_uniq` (`servicio_id`,`material_id`) USING BTREE,
  KEY `servicio_servicio_material_eb4b9aaa` (`material_id`) USING BTREE,
  KEY `servicio_servicio_material_4bb699dc` (`servicio_id`) USING BTREE,
  CONSTRAINT `servicio_servicio_m_material_id_6a0517d7_fk_servicio_material_id` FOREIGN KEY (`material_id`) REFERENCES `servicio_material` (`id`),
  CONSTRAINT `servicio_servicio_m_servicio_id_336b5873_fk_servicio_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicio_servicio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_servicio_material`
--

LOCK TABLES `servicio_servicio_material` WRITE;
/*!40000 ALTER TABLE `servicio_servicio_material` DISABLE KEYS */;
INSERT INTO `servicio_servicio_material` VALUES (1,1.00,3,2,'1'),(2,1.00,1,3,'1'),(3,1.00,2,7,'2'),(4,0.50,4,2,'3'),(5,1.00,4,3,'3'),(6,1.00,5,13,'4'),(7,1.00,4,13,'3'),(8,1.00,7,14,'1'),(9,1.00,8,15,'4');
/*!40000 ALTER TABLE `servicio_servicio_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_unidad`
--

DROP TABLE IF EXISTS `servicio_unidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio_unidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `unidad` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `unidad` (`unidad`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_unidad`
--

LOCK TABLES `servicio_unidad` WRITE;
/*!40000 ALTER TABLE `servicio_unidad` DISABLE KEYS */;
INSERT INTO `servicio_unidad` VALUES (4,'cms'),(2,'kgs'),(5,'kms'),(6,'m2'),(7,'m3'),(3,'mts'),(1,'und');
/*!40000 ALTER TABLE `servicio_unidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `telefono_telefono`
--

DROP TABLE IF EXISTS `telefono_telefono`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `telefono_telefono` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero` varchar(50) COLLATE utf8_bin NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `tipo_telefono_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `telefono_telefono_4a860110` (`cliente_id`) USING BTREE,
  KEY `telefono_telefono_3fdaa609` (`tipo_telefono_id`) USING BTREE,
  CONSTRAINT `telefono__tipo_telefono_id_65705ef3_fk_telefono_ti` FOREIGN KEY (`tipo_telefono_id`) REFERENCES `telefono_tipo_telefono` (`id`),
  CONSTRAINT `telefono_telefono_cliente_id_23a3a462_fk_cliente_c` FOREIGN KEY (`cliente_id`) REFERENCES `cliente_cliente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telefono_telefono`
--

LOCK TABLES `telefono_telefono` WRITE;
/*!40000 ALTER TABLE `telefono_telefono` DISABLE KEYS */;
INSERT INTO `telefono_telefono` VALUES (1,'04140576077',1,1);
/*!40000 ALTER TABLE `telefono_telefono` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `telefono_tipo_telefono`
--

DROP TABLE IF EXISTS `telefono_tipo_telefono`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `telefono_tipo_telefono` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_telefono` varchar(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `tipo_telefono` (`tipo_telefono`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `telefono_tipo_telefono`
--

LOCK TABLES `telefono_tipo_telefono` WRITE;
/*!40000 ALTER TABLE `telefono_tipo_telefono` DISABLE KEYS */;
INSERT INTO `telefono_tipo_telefono` VALUES (5,'Extensión'),(4,'Fax'),(2,'Hogar'),(1,'Móvil'),(3,'Trabajo');
/*!40000 ALTER TABLE `telefono_tipo_telefono` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajador_cargo_trabajador`
--

DROP TABLE IF EXISTS `trabajador_cargo_trabajador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trabajador_cargo_trabajador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cargo` varchar(100) COLLATE utf8_bin NOT NULL,
  `tarifa_dia` decimal(9,2) NOT NULL,
  `recargo_fin_semana` decimal(9,2) NOT NULL,
  `recargo_nocturno` decimal(9,2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `cargo` (`cargo`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajador_cargo_trabajador`
--

LOCK TABLES `trabajador_cargo_trabajador` WRITE;
/*!40000 ALTER TABLE `trabajador_cargo_trabajador` DISABLE KEYS */;
INSERT INTO `trabajador_cargo_trabajador` VALUES (1,'Chofer tipo 1',75.00,0.50,0.20),(2,'Chofer tipo 2',100.00,0.50,0.20),(3,'Ayudante de mudanza',50.00,0.50,0.20);
/*!40000 ALTER TABLE `trabajador_cargo_trabajador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'db_mtvmcotizacion'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-15 10:23:39
