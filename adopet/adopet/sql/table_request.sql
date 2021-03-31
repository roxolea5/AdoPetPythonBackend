USE adopet_django;

DROP TABLE IF EXISTS `request`;
CREATE TABLE `request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pet_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `status` enum('open','pending','close') NOT NULL,
PRIMARY KEY (`id`),
CONSTRAINT `fk_pet`
       FOREIGN KEY (`pet_id`)
       REFERENCES `pet` (`id`),
CONSTRAINT `fk_user_r`
       FOREIGN KEY (`user_id`)
       REFERENCES `user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;