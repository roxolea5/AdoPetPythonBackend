USE adopet_django;

DROP TABLE IF EXISTS `pet`;

CREATE TABLE `pet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `photo` varchar(255) NOT NULL,
  `category` enum('dog', 'cat', 'other') NOT NULL,
  `specie` varchar(50) NOT NULL,
  `sex` enum('F', 'M') NOT NULL,
  `size` enum('S', 'M', 'L') NOT NULL,
  `years` tinyint(4) DEFAULT NULL,
  `months` tinyint(4) DEFAULT NULL,
  `is_kid_friendly` enum('Y', 'N') NOT NULL,
  `is_dog_friendly` enum('Y', 'N') NOT NULL,
  `is_cat_friendly` enum('Y', 'N') NOT NULL,
  `vaccines` enum('Y', 'N') NOT NULL,
  `sterilized` enum('Y', 'N') NOT NULL,
  `payment` enum('none', 'money', 'food') NOT NULL,
  `status` enum('available','pending','adopted') NOT NULL,
  `user_id` int(11) NOT NULL,   
PRIMARY KEY (`id`),
CONSTRAINT `fk_user`
       FOREIGN KEY (`user_id`)
       REFERENCES `user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;