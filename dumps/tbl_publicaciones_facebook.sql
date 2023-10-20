-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 18-10-2023 a las 15:08:08
-- Versión del servidor: 5.7.23-23
-- Versión de PHP: 8.1.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dataser1_essential`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `predictions_publicacionesfacebook`
--

CREATE TABLE `predictions_publicacionesfacebook` (
  `id_publicacion` int(11) NOT NULL,
  `Tipo_publicacion` text COLLATE utf8_unicode_ci NOT NULL,
  `Descripcion_publicacion` text COLLATE utf8_unicode_ci,
  `imagen_publicacion` text COLLATE utf8_unicode_ci,
  `servicio_referencia` text COLLATE utf8_unicode_ci,
  `comentarios` int(11) DEFAULT '0',
  `fecha_publicacion` date DEFAULT NULL,
  `hora_publicacion` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `predictions_publicacionesfacebook`
--

INSERT INTO `predictions_publicacionesfacebook` (`id_publicacion`, `Tipo_publicacion`, `Descripcion_publicacion`, `imagen_publicacion`, `servicio_referencia`, `comentarios`, `fecha_publicacion`, `hora_publicacion`) VALUES
(1, 'Promocional', 'Nueva capacitación en Seguridad Eléctrica disponible', 'img_seguridad_electrica.jpg', 'Capacitación Seguridad Electrica', 0, '2022-10-03', '09:15:00'),
(2, 'Informativo', 'Conoce los beneficios de la Reanimación Cardiopulmonar', 'img_rcp.jpg', 'Capacitacion Reanimación Cardiopulmonar (RCP)', 0, '2022-10-06', '14:30:00'),
(3, 'Promocional', 'Mantenimiento especializado para tus espacios', NULL, 'LIMPIEZA DE PLENUM FALSO SUELO CINTOTECA', 0, '2022-10-09', '16:10:00'),
(4, 'Informativo', 'Todo sobre el Bloqueo y Etiquetado en nuestra nueva capacitación', 'img_bloqueo.jpg', 'Capacitacion Bloqueo y Etiquetado', 0, '2022-10-11', '10:45:00'),
(5, 'Informativo', 'Monitoreo de partículas: lo que debes saber', 'img_particulas.jpg', 'MONITOREO FINAL DE PARTICULAS CINTOTECA', 0, '2022-10-15', '11:15:00'),
(6, 'Promocional', 'Especialización completa en Seguridad Industrial. ¡Inscríbete ahora!', 'img_seguridad_industrial.jpg', 'Especialización en Seguridad Industrial, Higiene y Gestión Ambiental', 0, '2022-10-17', '15:00:00'),
(7, 'Promocional', 'Aprende sobre los peligros químicos en el ambiente laboral', NULL, 'Capacitacion Comunicación de Peligros Quimicos', 0, '2022-10-19', '12:05:00'),
(8, 'Informativo', 'La importancia de la seguridad en espacios confinados', 'img_espacios_confinados.jpg', 'Capacitacion Entrada de Espacio Confinados', 0, '2022-10-22', '10:30:00'),
(9, 'Promocional', 'Evita accidentes en altura. Nuestra capacitación te espera', 'img_trabajo_altura.jpg', 'Capacitación trabajo en altura', 0, '2022-10-25', '17:15:00'),
(10, 'Promocional', 'Nuevo sensor inalámbrico disponible en stock', 'img_sensor.jpg', 'FST100-6101 Lorawan Wireless', 0, '2022-10-27', '09:45:00'),
(11, 'Informativo', 'Los primeros auxilios pueden salvar vidas. Conoce más', 'img_primeros_auxilios.jpg', 'Capacitacion Primeros Auxilios', 0, '2022-10-29', '14:15:00'),
(12, 'Promocional', 'Identifica y evita peligros con nuestra nueva capacitación', NULL, 'Capacitación Identificación de peligros y evacuación de riesgos', 0, '2022-10-31', '16:50:00'),
(13, 'Promocional', 'Descubre cómo mantener tus espacios libres de polvo', 'img_control_polvo.jpg', 'MODELAMIENTO DE PARTICULAS DE POLVO CINTOTECA', 0, '2022-11-01', '10:15:00'),
(14, 'Informativo', 'La seguridad eléctrica es esencial. Aprende más con nosotros', 'img_seguridad_electrica.jpg', 'CAPACITACIÓN SEGURIDAD ELÉCTRICA.', 0, '2022-11-03', '13:50:00'),
(15, 'Promocional', 'Monitoreo avanzado de partículas: Nuevas técnicas y herramientas', 'img_monitoreo_avanzado.jpg', 'MONITOREO FINAL DE PARTICULAS CINTOTECA', 0, '2022-11-07', '09:30:00'),
(16, 'Informativo', '¿Por qué es importante el bloqueo y etiquetado?', NULL, 'Capacitacion Bloqueo y Etiquetado', 0, '2022-11-10', '15:40:00'),
(17, 'Promocional', 'Evita accidentes con una adecuada protección contra incendios', 'img_proteccion_incendios.jpg', 'Capacitacion Proteccion Contra Incendio', 0, '2022-11-14', '14:25:00'),
(18, 'Informativo', 'Las claves para un trabajo seguro en altura', 'img_trabajo_altura.jpg', 'Capacitación trabajo en altura', 0, '2022-11-17', '11:45:00'),
(19, 'Promocional', 'Técnicas avanzadas en identificación de peligros. ¡Capacítate!', 'img_identificacion_peligros.jpg', 'Capacitación Identificación de peligros y evacuación de riesgos', 0, '2022-11-20', '12:10:00'),
(20, 'Informativo', 'La importancia de los primeros auxilios y cómo actuar', NULL, 'Capacitacion Primeros Auxilios', 0, '2022-11-24', '17:00:00'),
(21, 'Promocional', 'El verano se acerca, conoce nuestros cursos de seguridad en piscinas', 'img_seguridad_piscinas.jpg', 'CAPACITACIÓN SEGURIDAD EN PISCINAS.', 0, '2022-11-27', '10:15:00'),
(22, 'Informativo', 'Cómo reducir los riesgos en espacios confinados', 'img_espacios_confinados.jpg', 'Capacitacion Entrada de Espacios Confinados', 0, '2022-11-30', '12:10:00'),
(23, 'Promocional', 'Prepárate para el 2023 con nuestras capacitaciones en seguridad eléctrica', 'img_capacitacion_electrica.jpg', 'Capacitación Seguridad Electrica', 0, '2022-12-01', '10:30:00'),
(24, 'Informativo', 'Cómo enfrentar situaciones de emergencia con técnicas de RCP', 'img_rcp.jpg', 'Capacitacion Reanimación Cardiopulmonar (RCP)', 0, '2022-12-04', '16:00:00'),
(25, 'Promocional', 'Nuevos cursos disponibles en comunicación de peligros químicos', 'img_peligros_quimicos.jpg', 'Capacitacion Comunicación de Peligros Quimicos', 0, '2022-12-06', '14:20:00'),
(26, 'Informativo', 'Beneficios de una correcta higienización en espacios industriales', NULL, 'HIGIENIZACIÓN CON HEPA CINTOTECA', 0, '2022-12-09', '13:35:00'),
(27, 'Promocional', '¡Especialízate! Únete a nuestra formación en Seguridad Industrial', 'img_especializacion_seguridad.jpg', 'Especialización en Seguridad Industrial, Higiene y Gestión Ambiental', 0, '2022-12-13', '11:55:00'),
(28, 'Informativo', 'Evita incidentes con una correcta capacitación en izaje de cargas', 'img_izaje.jpg', 'CAPACITACIÓN DE IZAJE DE CARGAS', 0, '2022-12-15', '16:45:00'),
(29, 'Promocional', 'Finaliza el año con nuestro curso en trabajo en espacios confinados', 'img_espacios_confinados.jpg', 'Capacitacion Entrada de Espacio Confinados', 0, '2022-12-18', '10:40:00'),
(30, 'Informativo', 'Celebra la llegada del nuevo año con responsabilidad. Conoce nuestros tips', 'img_responsabilidad_anio_nuevo.jpg', 'CONSEJOS DE SEGURIDAD PARA AÑO NUEVO', 0, '2022-12-28', '13:50:00'),
(31, 'Promocional', 'Recibe el 2023 con nuestro nuevo catálogo de capacitaciones', 'img_catalogo_2023.jpg', 'CATÁLOGO DE CAPACITACIONES 2023', 0, '2022-12-31', '11:30:00'),
(32, 'Informativo', '¡Bienvenido 2023! Estamos listos para un año lleno de capacitaciones y seguridad', 'img_bienvenido_2023.jpg', 'CALENDARIO DE CAPACITACIONES 2023', 0, '2023-01-01', '10:10:00'),
(33, 'Promocional', 'Enero es el mes de la prevención. Descubre nuestros cursos especializados', 'img_prevencion.jpg', 'CAPACITACIÓN EN PREVENCIÓN DE RIESGOS', 0, '2023-01-05', '14:30:00'),
(34, 'Informativo', 'Conoce la importancia de la seguridad en laboratorios', 'img_seguridad_laboratorio.jpg', 'SEGURIDAD EN LABORATORIOS', 0, '2023-01-09', '13:45:00'),
(35, 'Promocional', 'Especial descuento en cursos de primeros auxilios', 'img_descuento_auxilios.jpg', 'Capacitacion Primeros Auxilios', 0, '2023-01-12', '09:50:00'),
(36, 'Informativo', 'Todo lo que necesitas saber sobre ergonomía en el trabajo', NULL, 'Capacitacion Ergonomía', 0, '2023-01-16', '12:40:00'),
(37, 'Promocional', 'Mejora la seguridad en tu empresa con nuestra auditoría especializada', 'img_auditoria.jpg', 'AUDITORÍA DE SEGURIDAD', 0, '2023-01-20', '16:30:00'),
(38, 'Informativo', 'Protección auditiva: Una necesidad en entornos ruidosos', 'img_proteccion_auditiva.jpg', 'PROTECCIÓN AUDITIVA', 0, '2023-01-24', '10:20:00'),
(39, 'Promocional', 'Últimas plazas para nuestro curso de manejo seguro de productos químicos', 'img_productos_quimicos.jpg', 'Manejo Seguro de Productos Químicos', 0, '2023-01-28', '15:45:00'),
(40, 'Informativo', 'Beneficios de la certificación en seguridad industrial', NULL, 'CERTIFICACIÓN EN SEGURIDAD INDUSTRIAL', 0, '2023-01-31', '11:00:00'),
(41, 'Promocional', 'Celebra el amor y la amistad con un 20% de descuento en nuestros cursos', 'img_descuento_febrero.jpg', 'OFERTAS DE FEBRERO', 0, '2023-02-01', '10:15:00'),
(42, 'Informativo', 'Conoce las mejores prácticas para la seguridad en la construcción', 'img_seguridad_construccion.jpg', 'SEGURIDAD EN CONSTRUCCIÓN', 0, '2023-02-05', '14:00:00'),
(43, 'Promocional', 'Capacitación especializada en uso y mantenimiento de extintores', 'img_extintores.jpg', 'Uso y Mantenimiento de Extintores', 0, '2023-02-09', '13:30:00'),
(44, 'Informativo', '¿Por qué es vital tener una correcta señalización en la empresa?', NULL, 'Señalización de Seguridad', 0, '2023-02-12', '09:45:00'),
(45, 'Promocional', 'Asegura tu lugar en nuestra capacitación de rescate en altura', 'img_rescate_altura.jpg', 'RESCATE EN ALTURA', 0, '2023-02-16', '11:10:00'),
(46, 'Informativo', 'Entérate de los riesgos asociados al manejo de cargas y cómo prevenirlos', 'img_manejo_cargas.jpg', 'MANEJO SEGURO DE CARGAS', 0, '2023-02-20', '16:35:00'),
(47, 'Promocional', 'Inscríbete a nuestra formación sobre manejo de sustancias peligrosas', 'img_sustancias_peligrosas.jpg', 'Manejo de Sustancias Peligrosas', 0, '2023-02-24', '12:20:00'),
(48, 'Informativo', 'La importancia de los equipos de protección personal en el ámbito laboral', NULL, 'Equipos de Protección Personal (EPP)', 0, '2023-02-28', '10:00:00'),
(49, 'Promocional', '¡Inicia marzo con un descuento en nuestros cursos de emergencias!', 'img_descuento_emergencias.jpg', 'CURSOS DE EMERGENCIAS', 0, '2023-03-01', '10:05:00'),
(50, 'Informativo', 'Evita accidentes en tu empresa con una formación adecuada', 'img_prevencion_accidentes.jpg', 'CAPACITACIÓN PREVENTIVA', 0, '2023-03-04', '14:25:00'),
(51, 'Promocional', 'Aprovecha nuestra formación en manejo seguro de herramientas', 'img_herramientas.jpg', 'MANEJO SEGURO DE HERRAMIENTAS', 0, '2023-03-07', '15:10:00'),
(52, 'Informativo', 'Importancia de la gestión de residuos en empresas', NULL, 'GESTIÓN DE RESIDUOS', 0, '2023-03-10', '09:40:00'),
(53, 'Promocional', 'Conoce nuestro programa de formación en protección respiratoria', 'img_proteccion_respiratoria.jpg', 'PROTECCIÓN RESPIRATORIA', 0, '2023-03-13', '12:50:00'),
(54, 'Informativo', 'Riesgos laborales en oficinas y cómo evitarlos', 'img_oficinas.jpg', 'SEGURIDAD EN OFICINAS', 0, '2023-03-16', '16:05:00'),
(55, 'Promocional', 'Capacítate en seguridad alimentaria con nuestros expertos', 'img_seguridad_alimentaria.jpg', 'SEGURIDAD ALIMENTARIA', 0, '2023-03-20', '11:30:00'),
(56, 'Informativo', 'Mantenimiento de equipos de protección: clave para tu seguridad', NULL, 'MANTENIMIENTO DE EPP', 0, '2023-03-23', '13:15:00'),
(57, 'Promocional', 'Únete a nuestro curso avanzado de seguridad industrial', 'img_seguridad_industrial.jpg', 'SEGURIDAD INDUSTRIAL', 0, '2023-03-27', '15:20:00'),
(58, 'Informativo', 'Prácticas esenciales para un entorno laboral seguro', 'img_entorno_laboral.jpg', 'ENTORNO LABORAL', 0, '2023-03-30', '10:45:00'),
(59, 'Promocional', '¡Bienvenido abril! Descuentos especiales en todos nuestros cursos', 'img_descuento_abril.jpg', 'OFERTAS DE ABRIL', 0, '2023-04-02', '10:10:00'),
(60, 'Informativo', 'La ergonomía en el trabajo: una inversión en salud', 'img_ergonomia_trabajo.jpg', 'ERGONOMÍA LABORAL', 0, '2023-04-05', '15:45:00'),
(61, 'Promocional', 'Formación especializada en prevención de incendios', 'img_prevencion_incendios.jpg', 'PREVENCIÓN DE INCENDIOS', 0, '2023-04-08', '12:55:00'),
(62, 'Informativo', 'Identificación y manejo de riesgos laborales', NULL, 'GESTIÓN DE RIESGOS', 0, '2023-04-11', '14:00:00'),
(63, 'Promocional', 'No te pierdas nuestra capacitación sobre primeros auxilios pediátricos', 'img_auxilios_pediátricos.jpg', 'PRIMEROS AUXILIOS PEDIÁTRICOS', 0, '2023-04-14', '10:30:00'),
(64, 'Informativo', 'Recomendaciones para evitar lesiones por movimientos repetitivos', 'img_movimientos_repetitivos.jpg', 'SALUD OCUPACIONAL', 0, '2023-04-17', '16:40:00'),
(65, 'Promocional', 'Últimas plazas para el curso de seguridad en alturas', 'img_seguridad_alturas.jpg', 'SEGURIDAD EN ALTURAS', 0, '2023-04-20', '09:50:00'),
(66, 'Informativo', 'Consejos para un correcto uso de equipos de protección visual', NULL, 'PROTECCIÓN VISUAL', 0, '2023-04-23', '11:15:00'),
(67, 'Promocional', 'Inscríbete en nuestra formación sobre seguridad eléctrica', 'img_seguridad_electrica.jpg', 'SEGURIDAD ELÉCTRICA', 0, '2023-04-26', '13:25:00'),
(68, 'Informativo', 'Sistemas de alarma y prevención en empresas', 'img_sistemas_alarma.jpg', 'SISTEMAS DE ALARMA', 0, '2023-04-29', '10:50:00'),
(69, 'Promocional', '¡Bienvenido mayo! Descubre nuestras ofertas especiales.', 'img_descuento_mayo.jpg', 'OFERTAS DE MAYO', 0, '2023-05-01', '10:00:00'),
(70, 'Informativo', 'Evita lesiones con una adecuada postura laboral', 'img_postura_laboral.jpg', 'POSTURA LABORAL', 0, '2023-05-03', '14:10:00'),
(71, 'Promocional', 'Aprovecha la promoción en formación de seguridad vial', 'img_seguridad_vial.jpg', 'SEGURIDAD VIAL', 0, '2023-05-06', '15:45:00'),
(72, 'Informativo', 'La importancia de una adecuada señalización en la empresa', NULL, 'SEÑALIZACIÓN', 0, '2023-05-08', '09:20:00'),
(73, 'Promocional', 'Descubre nuestro programa avanzado de protección auditiva', 'img_proteccion_auditiva.jpg', 'PROTECCIÓN AUDITIVA', 0, '2023-05-10', '13:05:00'),
(74, 'Informativo', 'Riesgos y medidas preventivas en laboratorios', 'img_laboratorios.jpg', 'SEGURIDAD EN LABORATORIOS', 0, '2023-05-13', '15:00:00'),
(75, 'Promocional', 'Conoce nuestros cursos de gestión ambiental en la empresa', 'img_gestion_ambiental.jpg', 'GESTIÓN AMBIENTAL', 0, '2023-05-16', '12:25:00'),
(76, 'Informativo', 'Cómo prevenir accidentes en espacios confinados', NULL, 'ESPACIOS CONFINADOS', 0, '2023-05-19', '14:50:00'),
(77, 'Promocional', 'Inscríbete en nuestra formación sobre manipulación de sustancias químicas', 'img_sustancias_quimicas.jpg', 'SUSTANCIAS QUÍMICAS', 0, '2023-05-22', '16:10:00'),
(78, 'Informativo', 'Consejos para un adecuado manejo de herramientas eléctricas', 'img_herramientas_electricas.jpg', 'HERRAMIENTAS ELÉCTRICAS', 0, '2023-05-25', '10:55:00'),
(79, 'Promocional', 'Últimos días para aprovechar el descuento en primeros auxilios', 'img_descuento_auxilios.jpg', 'PRIMEROS AUXILIOS', 0, '2023-05-28', '11:45:00'),
(80, 'Promocional', '¡Hola junio! Inscríbete en nuestros cursos con descuento.', 'img_descuento_junio.jpg', 'OFERTAS DE JUNIO', 0, '2023-06-01', '09:30:00'),
(81, 'Informativo', 'Beneficios de la capacitación continua en seguridad laboral', 'img_capacitacion_continua.jpg', 'CAPACITACIÓN CONTINUA', 0, '2023-06-03', '14:45:00'),
(82, 'Promocional', 'Promoción en cursos de seguridad en maquinaria pesada', 'img_maquinaria_pesada.jpg', 'MAQUINARIA PESADA', 0, '2023-06-06', '16:20:00'),
(83, 'Informativo', 'Recomendaciones para la protección solar en trabajos al aire libre', 'img_proteccion_solar.jpg', 'PROTECCIÓN SOLAR', 0, '2023-06-08', '11:00:00'),
(84, 'Promocional', 'Oferta en formación de prevención de riesgos biológicos', 'img_riesgos_biologicos.jpg', 'RIESGOS BIOLÓGICOS', 0, '2023-06-11', '10:35:00'),
(85, 'Informativo', 'Cómo actuar en caso de un derrame químico en la empresa', NULL, 'DERRAME QUÍMICO', 0, '2023-06-13', '13:50:00'),
(86, 'Promocional', 'Inscríbete en nuestra formación de protección contra caídas', 'img_proteccion_caidas.jpg', 'PROTECCIÓN CONTRA CAÍDAS', 0, '2023-06-16', '15:30:00'),
(87, 'Informativo', 'Pasos para una correcta evacuación en caso de emergencia', 'img_evacuacion_emergencia.jpg', 'EVACUACIÓN', 0, '2023-06-19', '14:15:00'),
(88, 'Promocional', 'Últimos cupos para la formación en gestión de residuos peligrosos', 'img_residuos_peligrosos.jpg', 'RESIDUOS PELIGROSOS', 0, '2023-06-21', '12:45:00'),
(89, 'Informativo', 'Medidas preventivas contra incendios en la industria', 'img_prevencion_incendios_industria.jpg', 'PREVENCIÓN DE INCENDIOS', 0, '2023-06-24', '09:40:00'),
(90, 'Promocional', 'Descubre nuestra formación sobre sistemas de ventilación en espacios de trabajo', 'img_ventilacion.jpg', 'SISTEMAS DE VENTILACIÓN', 0, '2023-06-27', '11:20:00'),
(91, 'Informativo', 'Importancia del uso adecuado de equipos de protección en laboratorios', NULL, 'EPP LABORATORIOS', 0, '2023-06-29', '13:05:00'),
(92, 'Promocional', 'No te pierdas nuestro curso sobre medidas preventivas en construcción', 'img_construccion.jpg', 'SEGURIDAD EN CONSTRUCCIÓN', 0, '2023-06-30', '15:25:00'),
(93, 'Promocional', '¡Bienvenido Julio! Inscríbete en nuestros cursos de verano.', 'img_descuento_julio.jpg', 'CURSOS DE VERANO', 0, '2023-07-01', '09:30:00'),
(94, 'Informativo', 'Aprende cómo mantener una correcta hidratación en el trabajo.', 'img_hidratacion_trabajo.jpg', 'HIDRATACIÓN', 0, '2023-07-04', '11:45:00'),
(95, 'Promocional', 'Descuento especial en nuestro curso de gestión de calor.', 'img_gestion_calor.jpg', 'GESTIÓN DEL CALOR', 0, '2023-07-07', '15:30:00'),
(96, 'Informativo', 'Consejos para prevenir el golpe de calor en el ambiente laboral.', 'img_golpe_calor.jpg', 'GOLPE DE CALOR', 0, '2023-07-09', '10:20:00'),
(97, 'Promocional', 'Inscríbete en nuestra formación sobre seguridad en alturas.', 'img_alturas.jpg', 'SEGURIDAD EN ALTURAS', 0, '2023-07-13', '14:15:00'),
(98, 'Informativo', 'Beneficios de pausas activas en la jornada laboral.', NULL, 'PAUSAS ACTIVAS', 0, '2023-07-15', '13:00:00'),
(99, 'Promocional', 'Últimos días para aprovechar descuentos en formación de emergencias.', 'img_emergencias.jpg', 'EMERGENCIAS', 0, '2023-07-18', '09:40:00'),
(100, 'Informativo', 'Importancia de los simulacros de emergencia en la empresa.', 'img_simulacros.jpg', 'SIMULACROS', 0, '2023-07-22', '15:55:00'),
(101, 'Promocional', 'Descubre nuestro nuevo curso de seguridad en trabajos eléctricos.', 'img_trabajos_electricos.jpg', 'TRABAJOS ELÉCTRICOS', 0, '2023-07-25', '11:10:00'),
(102, 'Informativo', 'Medidas de protección en trabajos con productos químicos.', 'img_proteccion_quimicos.jpg', 'PRODUCTOS QUÍMICOS', 0, '2023-07-28', '12:50:00'),
(103, 'Promocional', 'Oferta en formación de manejo seguro de herramientas.', 'img_herramientas_seguras.jpg', 'HERRAMIENTAS SEGURAS', 0, '2023-07-30', '14:25:00'),
(104, 'Informativo', 'Cómo prevenir riesgos ergonómicos en la oficina.', NULL, 'ERGONOMÍA', 0, '2023-07-31', '10:30:00'),
(105, 'Promocional', '¡Hola Agosto! Descubre nuestros cursos especializados.', 'img_descuento_agosto.jpg', 'OFERTAS DE AGOSTO', 0, '2023-08-01', '09:15:00'),
(106, 'Informativo', 'Recomendaciones para trabajar en condiciones de lluvia.', 'img_lluvia_trabajo.jpg', 'TRABAJO BAJO LLUVIA', 0, '2023-08-03', '13:20:00'),
(107, 'Promocional', 'Descuento en curso de primeros auxilios básicos.', 'img_primeros_auxilios.jpg', 'PRIMEROS AUXILIOS', 0, '2023-08-06', '11:05:00'),
(108, 'Informativo', 'Pasos para actuar ante un accidente laboral.', 'img_accidente_laboral.jpg', 'ACCIDENTE LABORAL', 0, '2023-08-08', '12:40:00'),
(109, 'Promocional', 'Oferta en formación de manejo de cargas manuales.', 'img_cargas_manuales.jpg', 'CARGAS MANUALES', 0, '2023-08-10', '14:00:00'),
(110, 'Informativo', 'Importancia del uso de EPP en la industria.', NULL, 'EQUIPOS DE PROTECCIÓN', 0, '2023-08-13', '09:55:00'),
(111, 'Promocional', 'Descubre nuestro curso avanzado sobre riesgo eléctrico.', 'img_riesgo_electrico.jpg', 'RIESGO ELÉCTRICO', 0, '2023-08-16', '10:35:00'),
(112, 'Informativo', 'Beneficios de un adecuado sistema de iluminación en el trabajo.', 'img_iluminacion_trabajo.jpg', 'ILUMINACIÓN', 0, '2023-08-19', '12:20:00'),
(113, 'Promocional', 'Últimos cupos para nuestra formación en manejo defensivo.', 'img_manejo_defensivo.jpg', 'MANEJO DEFENSIVO', 0, '2023-08-21', '11:10:00'),
(114, 'Informativo', 'Cómo identificar y prevenir riesgos psicosociales en la empresa.', NULL, 'RIESGOS PSICOSOCIALES', 0, '2023-08-24', '15:45:00'),
(115, 'Promocional', 'Oferta especial en nuestro curso de gestión de residuos.', 'img_gestion_residuos.jpg', 'GESTIÓN DE RESIDUOS', 0, '2023-08-27', '13:30:00'),
(116, 'Informativo', 'Pasos para una correcta evacuación en caso de sismo.', 'img_evacuacion_sismo.jpg', 'SISMO', 0, '2023-08-29', '14:55:00'),
(117, 'Promocional', 'No te pierdas nuestra formación en protección respiratoria.', 'img_proteccion_respiratoria.jpg', 'PROTECCIÓN RESPIRATORIA', 0, '2023-08-31', '09:50:00'),
(118, 'Promocional', 'Oferta en curso de prevención de riesgos en construcción.', 'img_riesgos_construccion.jpg', 'RIESGOS EN CONSTRUCCIÓN', 0, '2023-09-07', '11:05:00'),
(119, 'Informativo', 'Cómo prevenir lesiones por movimientos repetitivos.', 'img_movimientos_repetitivos.jpg', 'MOVIMIENTOS REPETITIVOS', 0, '2023-09-09', '14:00:00'),
(120, 'Promocional', 'Inscríbete en nuestra formación sobre salud ocupacional.', 'img_salud_ocupacional.jpg', 'SALUD OCUPACIONAL', 0, '2023-09-11', '09:45:00'),
(121, 'Informativo', 'La importancia del descanso y la desconexión en el trabajo remoto.', NULL, 'TRABAJO REMOTO', 0, '2023-09-14', '15:30:00'),
(122, 'Promocional', 'Últimos cupos para nuestro curso de manejo seguro de maquinarias.', 'img_maquinarias_seguras.jpg', 'MAQUINARIAS SEGURAS', 0, '2023-09-17', '10:20:00'),
(123, 'Informativo', 'Consejos para mantener la concentración en jornadas prolongadas.', 'img_concentracion.jpg', 'CONCENTRACIÓN', 0, '2023-09-20', '11:35:00'),
(124, 'Promocional', 'No te pierdas nuestra oferta en formación sobre riesgos químicos.', 'img_riesgos_quimicos.jpg', 'RIESGOS QUÍMICOS', 0, '2023-09-23', '14:10:00'),
(125, 'Informativo', 'Ventajas de implementar pausas activas en la rutina laboral.', 'img_pausas_activas2.jpg', 'PAUSAS ACTIVAS', 0, '2023-09-25', '12:00:00'),
(126, 'Promocional', 'Descubre nuestro nuevo curso sobre manejo ergonómico de herramientas.', 'img_herramientas_ergonomicas.jpg', 'HERRAMIENTAS ERGONÓMICAS', 0, '2023-09-28', '16:00:00'),
(127, 'Informativo', 'Beneficios de una adecuada formación en seguridad para empresas.', NULL, 'FORMACIÓN SEGURIDAD', 0, '2023-09-30', '10:15:00');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `predictions_publicacionesfacebook`
--
ALTER TABLE `predictions_publicacionesfacebook`
  ADD PRIMARY KEY (`id_publicacion`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `predictions_publicacionesfacebook`
--
ALTER TABLE `predictions_publicacionesfacebook`
  MODIFY `id_publicacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=128;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
