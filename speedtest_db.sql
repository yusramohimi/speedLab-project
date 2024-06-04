-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 04 juin 2024 à 16:18
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `speedtest_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `results`
--

CREATE TABLE `results` (
  `id` int(11) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `download` float DEFAULT NULL,
  `upload` float DEFAULT NULL,
  `ping` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `results`
--

INSERT INTO `results` (`id`, `timestamp`, `download`, `upload`, `ping`) VALUES
(1, '2024-06-04 15:08:43', 16671000, 9147830, 20.181),
(2, '2024-06-04 15:10:05', 14964400, 9232800, 14.523),
(3, '2024-06-04 15:10:27', 17651400, 9331690, 14.95),
(4, '2024-06-04 15:10:49', 16118100, 9301940, 18.023),
(5, '2024-06-04 15:11:11', 17225800, 9271410, 15.034),
(6, '2024-06-04 15:11:33', 16338300, 9325520, 14.056),
(7, '2024-06-04 15:11:56', 16761900, 9197950, 13.84),
(8, '2024-06-04 15:12:18', 17376600, 9415710, 14.902),
(9, '2024-06-04 15:12:42', 12250000, 9140700, 15.817),
(10, '2024-06-04 15:13:04', 8578300, 9143190, 16.117),
(11, '2024-06-04 15:13:29', 4942140, 9174620, 36.931),
(12, '2024-06-04 15:13:51', 8721530, 9244540, 14.01),
(13, '2024-06-04 15:14:13', 12415000, 9403790, 13.705);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `results`
--
ALTER TABLE `results`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `results`
--
ALTER TABLE `results`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
