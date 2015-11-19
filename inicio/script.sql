/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;

SET NAMES 'utf8';
USE db_mtvmcotizacion;

--
-- Create table cliente_tipocliente
--
CREATE TABLE cliente_tipocliente (
  id INT(11) NOT NULL AUTO_INCREMENT,
  tipo_cliente VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
)
ENGINE = INNODB
CHARACTER SET utf8
COLLATE utf8_bin;


INSERT INTO cliente_tipocliente VALUES
  (1, 'Particular'),
  (2, 'Empresa'),
  (3, 'Gobierno');

--
-- Alter table cliente_cliente
--
ALTER TABLE cliente_cliente
  ADD COLUMN tipo_cliente_id INT(11) NOT NULL AFTER sexo_id;

ALTER TABLE cliente_cliente
  ADD INDEX cliente_cliente_5a33fb5a (tipo_cliente_id);

ALTER TABLE cliente_cliente
  ADD CONSTRAINT cliente_clien_tipo_cliente_id_6cc48744_fk_cliente_tipocliente_id FOREIGN KEY (tipo_cliente_id)
    REFERENCES cliente_tipocliente(id) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Alter table presupuesto_presupuesto
--
ALTER TABLE presupuesto_presupuesto
  ADD COLUMN tipo_cliente VARCHAR(100) NOT NULL AFTER tipo_duracion;

--
-- Enable foreign keys
--
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
