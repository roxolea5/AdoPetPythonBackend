USE adopet_django;
DROP TABLE IF EXISTS `questionary`;
CREATE TABLE `questionary` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address_street` varchar(100) NOT NULL,
  `address_ext_num` tinyint(4) NOT NULL,
  `address_int_num` varchar(5) NULL,
  `address_city` varchar(80) NOT NULL,
  `address_zip_code` int(11) NOT NULL,
  `pet_owner` enum('Y', 'N') NOT NULL,
  `family_members` int(11) NOT NULL,
  `family_agreement` enum('Y', 'N') NOT NULL,
  `document_id` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL,   
PRIMARY KEY (`id`),
CONSTRAINT `fk_user_q`
       FOREIGN KEY (`user_id`)
       REFERENCES `user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;