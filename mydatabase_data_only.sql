-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (arm64)
--
-- Host: localhost    Database: menu_system
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add 用户表',7,'add_user'),(26,'Can change 用户表',7,'change_user'),(27,'Can delete 用户表',7,'delete_user'),(28,'Can view 用户表',7,'view_user'),(29,'Can add 菜品表',8,'add_cuisine'),(30,'Can change 菜品表',8,'change_cuisine'),(31,'Can delete 菜品表',8,'delete_cuisine'),(32,'Can view 菜品表',8,'view_cuisine'),(33,'Can add 分类表',9,'add_category'),(34,'Can change 分类表',9,'change_category'),(35,'Can delete 分类表',9,'delete_category'),(36,'Can view 分类表',9,'view_category'),(37,'Can add 订单表',10,'add_order'),(38,'Can change 订单表',10,'change_order'),(39,'Can delete 订单表',10,'delete_order'),(40,'Can view 订单表',10,'view_order'),(41,'Can add 订单菜品关联表',11,'add_ordercuisine'),(42,'Can change 订单菜品关联表',11,'change_ordercuisine'),(43,'Can delete 订单菜品关联表',11,'delete_ordercuisine'),(44,'Can view 订单菜品关联表',11,'view_ordercuisine');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$PzmfCIeceBTeYnyGYsK9h4$qZ9iBPTNUt54bd1zfzaP1GtvyKXhXdQDWAp4BjB0RBc=','2024-12-19 04:04:08.054326',1,'admin','','','',1,1,'2024-12-16 04:15:30.477621');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (3,'甜品'),(1,'肉'),(2,'菜'),(4,'饮料');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cuisine`
--

LOCK TABLES `cuisine` WRITE;
/*!40000 ALTER TABLE `cuisine` DISABLE KEYS */;
INSERT INTO `cuisine` VALUES (1,'小炒黄牛肉',20,'','小炒黄牛肉.jpeg',1),(2,'麻婆豆腐',18,'','麻婆豆腐.jpeg',2),(3,'糖醋排骨',22,'','糖醋排骨.jpeg',1),(4,'番茄鸡蛋',18,'','番茄鸡蛋.jpeg',2),(5,'巧克力布丁',6,'','巧克力布丁.jpeg',3),(6,'冰拿铁',6,'','冰拿铁.jpeg',4);
/*!40000 ALTER TABLE `cuisine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-12-16 04:25:51.765690','1','User object (1)',1,'[{\"added\": {}}]',7,1),(2,'2024-12-16 04:26:12.859573','1','User object (1)',3,'',7,1),(3,'2024-12-16 04:27:32.380344','2','User object (2)',1,'[{\"added\": {}}]',7,1),(4,'2024-12-16 04:27:44.179254','3','User object (3)',1,'[{\"added\": {}}]',7,1),(5,'2024-12-16 04:34:18.355263','1','Cuisine object (1)',1,'[{\"added\": {}}]',8,1),(6,'2024-12-16 04:34:38.583960','2','Cuisine object (2)',1,'[{\"added\": {}}]',8,1),(7,'2024-12-16 04:34:53.923896','3','Cuisine object (3)',1,'[{\"added\": {}}]',8,1),(8,'2024-12-16 04:35:05.599923','4','Cuisine object (4)',1,'[{\"added\": {}}]',8,1),(9,'2024-12-16 04:36:02.997692','1','Order object (1)',1,'[{\"added\": {}}]',10,1),(10,'2024-12-16 04:52:35.634435','1','Order object (1)',3,'',10,1),(11,'2024-12-16 04:53:01.349220','2','Order object (2)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"\\u8ba2\\u5355\\u83dc\\u54c1\\u5173\\u8054\\u8868\", \"object\": \"OrderCuisine object (1)\"}}, {\"added\": {\"name\": \"\\u8ba2\\u5355\\u83dc\\u54c1\\u5173\\u8054\\u8868\", \"object\": \"OrderCuisine object (2)\"}}]',10,1),(12,'2024-12-16 04:53:16.108412','3','Order object (3)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"\\u8ba2\\u5355\\u83dc\\u54c1\\u5173\\u8054\\u8868\", \"object\": \"OrderCuisine object (3)\"}}, {\"added\": {\"name\": \"\\u8ba2\\u5355\\u83dc\\u54c1\\u5173\\u8054\\u8868\", \"object\": \"OrderCuisine object (4)\"}}]',10,1),(13,'2024-12-16 04:53:30.852254','4','Order object (4)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"\\u8ba2\\u5355\\u83dc\\u54c1\\u5173\\u8054\\u8868\", \"object\": \"OrderCuisine object (5)\"}}, {\"added\": {\"name\": \"\\u8ba2\\u5355\\u83dc\\u54c1\\u5173\\u8054\\u8868\", \"object\": \"OrderCuisine object (6)\"}}]',10,1),(14,'2024-12-18 03:34:12.882206','5','Order object (5)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"\\u8ba2\\u5355\\u83dc\\u54c1\\u5173\\u8054\\u8868\", \"object\": \"OrderCuisine object (7)\"}}]',10,1),(15,'2024-12-18 03:34:22.925141','6','Order object (6)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"\\u8ba2\\u5355\\u83dc\\u54c1\\u5173\\u8054\\u8868\", \"object\": \"OrderCuisine object (8)\"}}]',10,1),(16,'2024-12-19 04:07:38.955565','5','Cuisine object (5)',1,'[{\"added\": {}}]',8,1),(17,'2024-12-19 04:07:55.756906','6','Cuisine object (6)',1,'[{\"added\": {}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'cuisine','category'),(8,'cuisine','cuisine'),(10,'order','order'),(11,'order','ordercuisine'),(6,'sessions','session'),(7,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-12-16 04:11:13.981799'),(2,'auth','0001_initial','2024-12-16 04:11:14.012085'),(3,'admin','0001_initial','2024-12-16 04:11:14.070042'),(4,'admin','0002_logentry_remove_auto_add','2024-12-16 04:11:14.085757'),(5,'admin','0003_logentry_add_action_flag_choices','2024-12-16 04:11:14.088283'),(6,'contenttypes','0002_remove_content_type_name','2024-12-16 04:11:14.101469'),(7,'auth','0002_alter_permission_name_max_length','2024-12-16 04:11:14.110355'),(8,'auth','0003_alter_user_email_max_length','2024-12-16 04:11:14.117742'),(9,'auth','0004_alter_user_username_opts','2024-12-16 04:11:14.120356'),(10,'auth','0005_alter_user_last_login_null','2024-12-16 04:11:14.129296'),(11,'auth','0006_require_contenttypes_0002','2024-12-16 04:11:14.129993'),(12,'auth','0007_alter_validators_add_error_messages','2024-12-16 04:11:14.132774'),(13,'auth','0008_alter_user_username_max_length','2024-12-16 04:11:14.142465'),(14,'auth','0009_alter_user_last_name_max_length','2024-12-16 04:11:14.152318'),(15,'auth','0010_alter_group_name_max_length','2024-12-16 04:11:14.158334'),(16,'auth','0011_update_proxy_permissions','2024-12-16 04:11:14.161005'),(17,'auth','0012_alter_user_first_name_max_length','2024-12-16 04:11:14.170828'),(18,'cuisine','0001_initial','2024-12-16 04:11:14.175854'),(19,'cuisine','0002_auto_20241216_0407','2024-12-16 04:11:14.200365'),(20,'user','0001_initial','2024-12-16 04:11:14.204386'),(21,'order','0001_initial','2024-12-16 04:11:14.213603'),(22,'order','0002_auto_20241211_1140','2024-12-16 04:11:14.260140'),(23,'order','0003_auto_20241212_0427','2024-12-16 04:11:14.270535'),(24,'order','0004_order_status','2024-12-16 04:11:14.280504'),(25,'sessions','0001_initial','2024-12-16 04:11:14.284428'),(26,'user','0002_auto_20241211_1140','2024-12-16 04:11:14.308847'),(27,'user','0003_auto_20241212_0427','2024-12-16 04:11:14.313374'),(28,'user','0004_auto_20241215_0632','2024-12-16 04:11:14.318749'),(29,'cuisine','0003_auto_20241216_0416','2024-12-16 04:17:01.525115');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('of0r7hy6g1pu44ux38mqhb8c76iux6qj','.eJxVjM0OwiAQhN-FsyELWH48evcZyC5spWogKe3J-O62SQ-auc33zbxFxHUpce08xymLi1Di9NsRpifXHeQH1nuTqdVlnkjuijxol7eW-XU93L-Dgr1s65B9AODRWrADUgojGw_OKVTgPWqyIW3RYEATKUM00JlBARCDS058vtAdN1s:1tO7lg:zzxvrpTqBw9JQ3o_WoLMjeTYUZ60YbPqO0u2m3iWIGs','2025-01-02 04:04:08.055633');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (2,'2024-12-16 04:53:01.346602',2,1),(3,'2024-12-16 04:53:16.107066',3,1),(4,'2024-12-16 04:53:30.850500',3,1),(5,'2024-12-18 03:34:12.873175',3,1),(6,'2024-12-18 03:34:22.923877',3,1);
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ordercuisine`
--

LOCK TABLES `ordercuisine` WRITE;
/*!40000 ALTER TABLE `ordercuisine` DISABLE KEYS */;
INSERT INTO `ordercuisine` VALUES (1,2,2,2),(2,1,1,2),(3,1,2,3),(4,2,3,3),(5,1,4,4),(6,3,1,4),(7,3,2,5),(8,2,4,6);
/*!40000 ALTER TABLE `ordercuisine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (2,'小王','avatars/download.jpeg'),(3,'小林','avatars/download2.jpeg');
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

-- Dump completed on 2024-12-19 15:49:16
