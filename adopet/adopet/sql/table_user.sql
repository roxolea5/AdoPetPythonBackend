USE adopet_django;

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL UNIQUE,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL UNIQUE,
  `password` varchar(255),
  `date_of_birth` DATE,
  `photo` varchar(255),
  `status` int(11) DEFAULT NULL,
  `role_id` INT(11) DEFAULT NULL,
   PRIMARY KEY (`id`),
   UNIQUE INDEX `uk_username` (`username` ASC),
       UNIQUE INDEX `uk_email` (`email` ASC),
       CONSTRAINT `fk_role_`
       FOREIGN KEY (`role_id`)
       REFERENCES `role` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_spanish_ci;

INSERT INTO `user` VALUES 
(1,'rox05','Roxana', 'Olea', 'roxana.olea@gmail.com', 'RoxOlea05', '1990-09-05', 'roxphoto', 1, 1),
(2,'betty31','Beatriz', 'Sanchez', 'betty3161@gmail.com', 'BettySanchez31', '1961-05-31', 'bettyphoto', 1, 2),
(3,'isra13','Israel', 'Olea', 'isra1386@gmail.com', 'IsraOlea13', '1986-04-13', 'israphoto', 1, 2),
(4,'coco01','Socorro', 'Arroyo', 'coco0101@gmail.com', 'CocoArroyo01', '1970-01-01', 'cocophoto', 1, 3),
(5,'mirish02','Miriam', 'Olivo', 'mirish0202@gmail.com', 'MiriamOlivo02', '1990-02-02', 'mirishphoto', 1, 3);
