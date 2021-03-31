USE adopet_django;

DROP TABLE IF EXISTS `role`;

CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role` varchar(50) DEFAULT NULL UNIQUE,
  `description` varchar(100) DEFAULT NULL,
  `active` tinyint(4) DEFAULT NULL,
   PRIMARY KEY (`id`),
   UNIQUE INDEX `uk_role` (`role` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;

INSERT INTO `role` VALUES 
(1,'ADMIN','System Admin', 1),
(2,'RESCUER','Pet Rescuer',1),
(3,'ADOPTANT','Pet Adoptant',1);