-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.16-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para redsocialbd
CREATE DATABASE IF NOT EXISTS `redsocialbd` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `redsocialbd`;

-- Volcando estructura para procedimiento redsocialbd.agregar_amigo
DELIMITER //
CREATE PROCEDURE `agregar_amigo`(
	IN `mi_id` CHAR(50),
	IN `amigo_id` CHAR(50)
)
BEGIN
	DECLARE aux CHAR(50) DEFAULT "";
	if EXISTS(SELECT usuarios_id FROM usuarios WHERE usuarios_id = amigo_id) then
		if NOT EXISTS(SELECT usuario_id_amigo FROM amistades WHERE usuario_id_1 = mi_id AND usuario_id_amigo = amigo_id) then
			INSERT INTO amistades
			SELECT NULL, (SELECT usuarios_id AS 'u_1' FROM usuarios WHERE usuarios_id = mi_id) AS 'mi_id', usuarios_id AS 'amigo_id'
			FROM usuarios
			WHERE usuarios_id = amigo_id;
			set aux = 'amigo agregado';
		else
			set aux = 'el amigo especificado ya se encuentra en tu lista de amigos';
		END if;
	else
		set aux = 'el id especificado no se encuentra registrado';
	END if;
	SELECT aux;
END//
DELIMITER ;

-- Volcando estructura para procedimiento redsocialbd.agregar_publicacion
DELIMITER //
CREATE PROCEDURE `agregar_publicacion`(
	IN `mi_id` CHAR(50),
	IN `cont` CHAR(50),
	IN `categoria_id` CHAR(50)
)
BEGIN
	DECLARE aux CHAR(50) DEFAULT "";
	if EXISTS(SELECT CategoriasDePost_id FROM categoriasdepost WHERE CategoriasDePost_id = categoria_id) then
		INSERT INTO posteos (posteos_id, contenido, fechaDePublicacion, categoriaDePost_id, usuario_id_2)
		VALUES (0, cont, CURDATE(), categoria_id, mi_id);
		set aux = 'publicacion agregada';
	else
		SET aux = 'no se encontro la categoria especificada';
	END if;
	SELECT aux;
END//
DELIMITER ;

-- Volcando estructura para tabla redsocialbd.amistades
CREATE TABLE IF NOT EXISTS `amistades` (
  `amistades_id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id_1` int(11) DEFAULT NULL,
  `usuario_id_amigo` int(11) DEFAULT NULL,
  PRIMARY KEY (`amistades_id`),
  KEY `usuario_id_1` (`usuario_id_1`),
  KEY `usuario_id_amigo` (`usuario_id_amigo`),
  CONSTRAINT `amistades_ibfk_1` FOREIGN KEY (`usuario_id_1`) REFERENCES `usuarios` (`usuarios_id`),
  CONSTRAINT `amistades_ibfk_2` FOREIGN KEY (`usuario_id_amigo`) REFERENCES `usuarios` (`usuarios_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla redsocialbd.categoriasdepost
CREATE TABLE IF NOT EXISTS `categoriasdepost` (
  `CategoriasDePost_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`CategoriasDePost_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla redsocialbd.ciudades
CREATE TABLE IF NOT EXISTS `ciudades` (
  `ciudad_id` int(11) NOT NULL AUTO_INCREMENT,
  `pais_codigo` varchar(2) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`ciudad_id`)
) ENGINE=InnoDB AUTO_INCREMENT=269415 DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla redsocialbd.cuentas
CREATE TABLE IF NOT EXISTS `cuentas` (
  `cuenta_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_name` varchar(50) NOT NULL,
  `login_pass` varchar(50) NOT NULL,
  `usuario_id_2` int(11) NOT NULL,
  `mail_primario` varchar(50) NOT NULL,
  `mail_secundario` varchar(50) NOT NULL,
  PRIMARY KEY (`cuenta_id`),
  KEY `usuario_id_2` (`usuario_id_2`),
  CONSTRAINT `cuentas_ibfk_1` FOREIGN KEY (`usuario_id_2`) REFERENCES `usuarios` (`usuarios_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para procedimiento redsocialbd.eliminar_amigo
DELIMITER //
CREATE PROCEDURE `eliminar_amigo`(
	IN `mi_id` CHAR(50),
	IN `amigo_id` CHAR(50)
)
BEGIN
	DECLARE aux CHAR(50) DEFAULT "";
	if EXISTS(SELECT usuarios_id FROM usuarios WHERE usuarios_id = amigo_id) then
		if EXISTS(SELECT usuario_id_amigo FROM amistades WHERE usuario_id_1 = mi_id AND usuario_id_amigo = amigo_id) then
			DELETE FROM amistades
			WHERE usuario_id_1 = mi_id AND usuario_id_amigo = amigo_id;
			set aux = 'amigo eliminado';
		else
			set aux = 'el amigo especificado no se encuentra en tu lista de amigos';
		END if;
	else
		set aux = 'el id especificado no se encuentra registrado';
	END if;
	SELECT aux;
END//
DELIMITER ;

-- Volcando estructura para procedimiento redsocialbd.eliminar_cuenta
DELIMITER //
CREATE PROCEDURE `eliminar_cuenta`(mi_id CHAR(50))
BEGIN
	DECLARE aux CHAR(50) DEFAULT "";
	CALL eliminar_todas_las_amistades(mi_id);
	DELETE FROM amistades WHERE usuario_id_amigo = mi_id;
	CALL eliminar_todas_las_publicaciones(mi_id);
	DELETE FROM cuentas WHERE cuenta_id = (SELECT cuenta_id FROM cuentas WHERE usuario_id_2 = mi_id);
	DELETE FROM usuarios WHERE usuarios_id = mi_id;
	SELECT aux;
END//
DELIMITER ;

-- Volcando estructura para procedimiento redsocialbd.eliminar_publicacion
DELIMITER //
CREATE PROCEDURE `eliminar_publicacion`(mi_id CHAR(50), post_id CHAR(50))
BEGIN
	DECLARE aux CHAR(50) DEFAULT "";
	if EXISTS(SELECT posteos_id FROM posteos WHERE posteos_id = post_id AND usuario_id_2 = mi_id) then
		DELETE FROM posteos
		WHERE usuario_id_2 = mi_id AND posteos_id = post_id;
		set aux = 'post eliminado';
	else
		set aux = 'el post no se encuentra en tu lista de posteos';
	END if;
	SELECT aux;
END//
DELIMITER ;

-- Volcando estructura para procedimiento redsocialbd.eliminar_todas_las_amistades
DELIMITER //
CREATE PROCEDURE `eliminar_todas_las_amistades`(mi_id CHAR(50))
BEGIN
	DECLARE aux CHAR(50) DEFAULT "";
	if EXISTS(SELECT usuario_id_amigo FROM amistades WHERE usuario_id_1 = mi_id) then
		DELETE FROM amistades
		WHERE usuario_id_1 = mi_id;
		set aux = 'lista de amigos eliminada';
	else
		set aux = 'tu lista de amigos se encuentra actualmente vacia';
	END if;
	SELECT aux;
END//
DELIMITER ;

-- Volcando estructura para procedimiento redsocialbd.eliminar_todas_las_publicaciones
DELIMITER //
CREATE PROCEDURE `eliminar_todas_las_publicaciones`(mi_id CHAR(50))
BEGIN
	DECLARE aux CHAR(50) DEFAULT "";
	DECLARE contador INT(50) DEFAULT 0;
	SET contador = (SELECT count(posteos_id) FROM posteos WHERE usuario_id_2 = mi_id);
	if (contador > 0) then
		DELETE FROM posteos
		WHERE usuario_id_2 = mi_id;
		set aux = CONCAT('se eliminaron ', contador, ' posts');
	else
		set aux = 'tu lista de posts se encuentra vacia';
	END if;
	SELECT aux;
END//
DELIMITER ;

-- Volcando estructura para tabla redsocialbd.paises
CREATE TABLE IF NOT EXISTS `paises` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(2) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=503 DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla redsocialbd.posteos
CREATE TABLE IF NOT EXISTS `posteos` (
  `posteos_id` int(11) NOT NULL AUTO_INCREMENT,
  `contenido` varchar(300) NOT NULL,
  `fechaDePublicacion` date DEFAULT NULL,
  `categoriaDePost_id` int(11) DEFAULT NULL,
  `usuario_id_2` int(11) DEFAULT NULL,
  PRIMARY KEY (`posteos_id`),
  KEY `categoriaDePost_id` (`categoriaDePost_id`),
  KEY `usuario_id_2` (`usuario_id_2`),
  CONSTRAINT `posteos_ibfk_1` FOREIGN KEY (`categoriaDePost_id`) REFERENCES `categoriasdepost` (`CategoriasDePost_id`),
  CONSTRAINT `posteos_ibfk_2` FOREIGN KEY (`usuario_id_2`) REFERENCES `usuarios` (`usuarios_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para procedimiento redsocialbd.save_acc
DELIMITER //
CREATE PROCEDURE `save_acc`(
	IN `c_id` CHAR(50),
	IN `log_n` CHAR(50),
	IN `log_p` CHAR(50),
	IN `u_id` CHAR(50),
	IN `mail_p` CHAR(50),
	IN `mail_s` CHAR(50)
)
BEGIN
	DECLARE ultimo_id_insertado CHAR(50) DEFAULT '';
	INSERT INTO cuentas (cuenta_id, login_name, login_pass, usuario_id_2, mail_primario, mail_secundario)
        VALUES (c_id, log_n, log_p, u_id, mail_p, mail_s)
        ON DUPLICATE KEY
		  UPDATE login_name = log_n,
		  login_pass = log_p,
		  usuario_id_2 = u_id,
		  mail_primario = mail_p,
		  mail_secundario = mail_s;
	SET ultimo_id_insertado = LAST_INSERT_ID();
	SELECT ultimo_id_insertado;
END//
DELIMITER ;

-- Volcando estructura para procedimiento redsocialbd.save_user
DELIMITER //
CREATE PROCEDURE `save_user`(
	IN `u_id` CHAR(50),
	IN `nom` CHAR(50),
	IN `ape` CHAR(50),
	IN `ed` CHAR(50),
	IN `gen` CHAR(50),
	IN `c_id` CHAR(50),
	IN `tel` CHAR(50)
)
BEGIN
	DECLARE ultimo_id_insertado CHAR(50) DEFAULT '';
	INSERT INTO usuarios (usuarios_id, nombre, apellido, edad, genero, ciudad_id_1, telefono)
	VALUES (u_id, nom, ape, ed, gen, c_id, tel)
	ON DUPLICATE KEY 
	UPDATE nombre = nom,
			 apellido = ape,
			 edad = ed,
			 genero = gen,
			 ciudad_id_1 = c_id,
			 telefono = tel;
	SET ultimo_id_insertado = LAST_INSERT_ID();
	SELECT ultimo_id_insertado;
END//
DELIMITER ;

-- Volcando estructura para tabla redsocialbd.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `usuarios_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `edad` varchar(3) NOT NULL,
  `genero` varchar(10) DEFAULT NULL,
  `ciudad_id_1` int(11) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  PRIMARY KEY (`usuarios_id`),
  KEY `ciudad_ibfk_1` (`ciudad_id_1`),
  CONSTRAINT `ciudad_ibfk_1` FOREIGN KEY (`ciudad_id_1`) REFERENCES `ciudades` (`ciudad_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para vista redsocialbd.vista_usuario_edades
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `vista_usuario_edades` (
	`usuario` VARCHAR(101) NOT NULL COLLATE 'utf8mb4_general_ci',
	`edad` VARCHAR(3) NOT NULL COLLATE 'utf8mb4_general_ci'
) ENGINE=MyISAM;

-- Volcando estructura para vista redsocialbd.vista_usuario_edades
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `vista_usuario_edades`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vista_usuario_edades` AS SELECT CONCAT(nombre, ' ', apellido) AS usuario, edad FROM usuarios ORDER BY edad ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
