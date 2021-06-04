-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 30, 2021 at 10:58 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `degree_overview`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(32) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`id`, `username`, `password`, `type`) VALUES
(1, 'S00001', '123456', 'Student'),
(2, 'S00002', '654321', 'Student'),
(3, 'S00003', '147369', 'Student'),
(4, 'S00004', '369147', 'Student'),
(5, 'S00005', '123456', 'Student'),
(6, 'S00006', '654321', 'Student'),
(7, 'S00007', '123456', 'Student'),
(8, 'S00008', '654321', 'Student'),
(9, 'S00009', '123456', 'Student'),
(10, 'S00010', '654321', 'Student'),
(11, 'D00001', '123456', 'CourseDesigner'),
(12, 'D00002', '369147', 'CourseDesigner'),
(13, 'D00003', '123456', 'CourseDesigner'),
(14, 'D00004', '369147', 'CourseDesigner'),
(15, 'D00005', '147369', 'CourseDesigner'),
(16, 'D00006', '369147', 'CourseDesigner'),
(17, 'D00007', '147369', 'CourseDesigner'),
(18, 'D00008', '654321', 'CourseDesigner'),
(19, 'D00009', '147369', 'CourseDesigner'),
(20, 'D00010', '369147', 'CourseDesigner'),
(21, 'N00001', '123456', 'NonCourseDesigner'),
(22, 'N00002', '369147', 'NonCourseDesigner'),
(23, 'N00003', '147369', 'NonCourseDesigner'),
(24, 'N00004', '369147', 'NonCourseDesigner'),
(25, 'N00005', '147369', 'NonCourseDesigner'),
(26, 'N00006', '369147', 'NonCourseDesigner');

-- --------------------------------------------------------

--
-- Table structure for table `assessment`
--

CREATE TABLE `assessment` (
  `AssessmentID` int(11) NOT NULL,
  `MethodName` varchar(25) NOT NULL,
  `CILOIDs` varchar(25) NOT NULL,
  `AcademicYear` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `Percentage` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `assessment`
--

INSERT INTO `assessment` (`AssessmentID`, `MethodName`, `CILOIDs`, `AcademicYear`, `course_id`, `Percentage`) VALUES
(1, 'Quiz and Assignment', '1-2', 2021, 4, 30),
(2, 'Project', '2-3', 2021, 4, 30),
(3, 'Final examination', '1-3', 2021, 4, 40),
(4, 'Quiz and Assignment', '4-5', 2020, 7, 20),
(5, 'Mid term', '4', 2020, 7, 20),
(6, 'Final', '4-5-6', 2020, 7, 60),
(7, 'Assignment', '1', 2019, 6, 10),
(8, 'Lab', '2', 2019, 6, 20),
(9, 'Project', '1-2', 2019, 6, 30),
(10, 'Final', '1', 2019, 6, 40),
(11, 'Final', '1', 2020, 6, 40),
(12, 'Project', '1-2', 2020, 6, 30),
(13, 'Lab', '2', 2020, 6, 20),
(14, 'Assignment', '1', 2020, 6, 10);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add account', 7, 'add_account'),
(26, 'Can change account', 7, 'change_account'),
(27, 'Can delete account', 7, 'delete_account'),
(28, 'Can view account', 7, 'view_account'),
(29, 'Can add course_designer', 8, 'add_coursedesigner'),
(30, 'Can change course_designer', 8, 'change_coursedesigner'),
(31, 'Can delete course_designer', 8, 'delete_coursedesigner'),
(32, 'Can view course_designer', 8, 'view_coursedesigner'),
(33, 'Can add noncourse_designer', 9, 'add_noncoursedesigner'),
(34, 'Can change noncourse_designer', 9, 'change_noncoursedesigner'),
(35, 'Can delete noncourse_designer', 9, 'delete_noncoursedesigner'),
(36, 'Can view noncourse_designer', 9, 'view_noncoursedesigner'),
(37, 'Can add student', 10, 'add_student'),
(38, 'Can change student', 10, 'change_student'),
(39, 'Can delete student', 10, 'delete_student'),
(40, 'Can view student', 10, 'view_student'),
(41, 'Can add course', 11, 'add_course'),
(42, 'Can change course', 11, 'change_course'),
(43, 'Can delete course', 11, 'delete_course'),
(44, 'Can view course', 11, 'view_course'),
(45, 'Can add assessment', 12, 'add_assessment'),
(46, 'Can change assessment', 12, 'change_assessment'),
(47, 'Can delete assessment', 12, 'delete_assessment'),
(48, 'Can view assessment', 12, 'view_assessment'),
(49, 'Can add cilo', 13, 'add_cilo'),
(50, 'Can change cilo', 13, 'change_cilo'),
(51, 'Can delete cilo', 13, 'delete_cilo'),
(52, 'Can view cilo', 13, 'view_cilo'),
(53, 'Can add grade report', 14, 'add_gradereport'),
(54, 'Can change grade report', 14, 'change_gradereport'),
(55, 'Can delete grade report', 14, 'delete_gradereport'),
(56, 'Can view grade report', 14, 'view_gradereport'),
(57, 'Can add student_ course', 15, 'add_student_course'),
(58, 'Can change student_ course', 15, 'change_student_course'),
(59, 'Can delete student_ course', 15, 'delete_student_course'),
(60, 'Can view student_ course', 15, 'view_student_course');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$150000$jY4QSXbzAjm8$8yD5anyXCFd3BZtYAlqHBZesoNe5wKW2Kb4DRweY1+g=', '2021-05-30 13:56:04.398326', 1, 'jasmine', '', '', 'jasmine@mail.edu.cn', 1, 1, '2021-05-19 15:25:29.711361');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `cilo`
--

CREATE TABLE `cilo` (
  `CILOID` int(11) NOT NULL,
  `CILOName` varchar(25) NOT NULL,
  `Description` longtext NOT NULL,
  `PreCILO` varchar(25) DEFAULT NULL,
  `AcademicYear` int(11) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cilo`
--

INSERT INTO `cilo` (`CILOID`, `CILOName`, `Description`, `PreCILO`, `AcademicYear`, `course_id`) VALUES
(1, '1', 'Explain the underlying concepts and write representations of different algorithm of compter vision', '', 2021, 4),
(2, '2', 'Apply fundamental techniques in computer vision using PyTorch', NULL, 2021, 4),
(3, '3', 'Develop a system related to the computer vision to solve a problem in the real world.', '1-2', 2021, 4),
(4, '1', 'Describe the basic concepts in linear transformations, orthogonality and eigenvalues.', 'Null', 2020, 7),
(5, '2', 'Apply the properties of these concepts to the study of the properties of differnt forms of matirces', '4', 2020, 7),
(6, '3', 'Use Matlab, a mathematical software, to study a matrix based on the concepts in CILO1', '4', 2020, 7),
(7, '1', 'Lecture and assignment will be distributed to the students.', '7', 2019, 6),
(8, '2', 'To enhance student\'s ability in applying machine learning method to real-world application, group projects will be give.', '7', 2019, 6),
(22, '1', 'new CILO1', '7', 2020, 6),
(23, '2', 'new CILO2', '7', 2020, 6);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `CourseID` int(11) NOT NULL,
  `CourseName` varchar(25) NOT NULL,
  `Code` varchar(10) NOT NULL,
  `Type` varchar(10) NOT NULL,
  `Program` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`CourseID`, `CourseName`, `Code`, `Type`, `Program`) VALUES
(1, 'Calculus I', 'MATH1073', 'MR', 'CST'),
(2, 'Calculus II', 'MATH1083', 'ME', 'CST'),
(3, 'Discrete Structures', 'MATH2003', 'MR', 'CST'),
(4, 'Computer Vision', 'COMP4113', 'ME', 'CST'),
(5, 'Deep Learning', 'COMP4163', 'ME', 'CST'),
(6, 'Machine learning', 'COMP4103', 'FE', 'CST'),
(7, 'Linear Algebra', 'MATH1003', 'MR', 'CST'),
(8, 'Workshop I', 'COMP2023', 'MR', 'CST'),
(9, 'Workshop II', 'COMP3043', 'MR', 'CST'),
(10, 'Workshop III', 'COMP3053', 'MR', 'CST'),
(11, 'Calculus II', 'MATH1083', 'FE', 'CST');

-- --------------------------------------------------------

--
-- Table structure for table `course_designer`
--

CREATE TABLE `course_designer` (
  `fullname` varchar(30) NOT NULL,
  `programme` varchar(15) NOT NULL,
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course_designer`
--

INSERT INTO `course_designer` (`fullname`, `programme`, `id`, `account_id`) VALUES
('Judy', 'CST', 1, 11),
('Jefferson', 'DS', 2, 12),
('Roger', 'FM', 3, 13),
('Keren', 'FST', 4, 14),
('Amy', 'ACCT', 5, 15),
('Elina', 'STAT', 6, 16),
('Steven', 'MHR', 7, 17),
('Jay', 'ATS', 8, 18),
('Bills', 'CTV', 9, 19),
('Sa', 'SWAS', 10, 20);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-05-19 17:55:13.346779', '1', 'UserJudy', 1, '[{\"added\": {}}]', 7, 1),
(2, '2021-05-19 17:55:51.889876', '2', 'UserBrian', 1, '[{\"added\": {}}]', 7, 1),
(3, '2021-05-19 17:56:12.930600', '3', 'UserLily', 1, '[{\"added\": {}}]', 7, 1),
(4, '2021-05-19 18:50:47.792473', '1', '1_Judy FENG_CST', 1, '[{\"added\": {}}]', 8, 1),
(5, '2021-05-19 18:51:55.433239', '1', '1_Brian XIA_CST_2005', 1, '[{\"added\": {}}]', 10, 1),
(6, '2021-05-19 18:52:42.102188', '3', 'UserLina', 2, '[{\"changed\": {\"fields\": [\"username\", \"password\"]}}]', 7, 1),
(7, '2021-05-19 18:53:08.517229', '1', '1_Lina MA_CST', 1, '[{\"added\": {}}]', 9, 1),
(8, '2021-05-19 19:27:26.109545', '3', 'UserLina', 2, '[{\"changed\": {\"fields\": [\"type\"]}}]', 7, 1),
(9, '2021-05-19 19:27:32.238650', '2', 'UserBrian', 2, '[{\"changed\": {\"fields\": [\"type\"]}}]', 7, 1),
(10, '2021-05-19 19:27:43.041465', '1', 'UserJudy', 2, '[{\"changed\": {\"fields\": [\"type\"]}}]', 7, 1),
(11, '2021-05-23 13:40:45.087468', '1', 'Course object (1)', 1, '[{\"added\": {}}]', 11, 1),
(12, '2021-05-23 13:43:02.782567', '1', 'CILO object (1)', 1, '[{\"added\": {}}]', 13, 1),
(13, '2021-05-23 13:44:35.553868', '2', 'Course object (2)', 1, '[{\"added\": {}}]', 11, 1),
(14, '2021-05-23 13:52:20.480304', '3', 'Course object (3)', 1, '[{\"added\": {}}]', 11, 1),
(15, '2021-05-23 14:03:32.709310', '2', 'CILO object (2)', 1, '[{\"added\": {}}]', 13, 1),
(16, '2021-05-24 04:45:35.776031', '3', '3_3.0_This is CILO3 for CG__2005', 3, '', 13, 1),
(17, '2021-05-24 04:50:27.336434', '4', '4_3.0_This is CILO3 for CG__2005', 3, '', 13, 1),
(18, '2021-05-24 04:50:35.276242', '2', '2_2_This is CILO2 for CG_Null_2005', 3, '', 13, 1),
(19, '2021-05-24 04:52:12.113026', '7', '7_2.0_This is CILO2 for CG__2005', 3, '', 13, 1),
(20, '2021-05-24 04:52:15.471597', '6', '6_3.0_This is CILO3 for CG__2005', 3, '', 13, 1),
(21, '2021-05-24 04:52:18.801774', '1', '1_1_This is CILO1 for CG_Null_2005', 3, '', 13, 1),
(22, '2021-05-24 04:53:33.617972', '9', '9_2.0_This is CILO2 for CG__2005', 3, '', 13, 1),
(23, '2021-05-24 05:01:27.199421', '8', '8_3.0_This is CILO3 for CG__2005', 3, '', 13, 1),
(24, '2021-05-24 08:03:19.718121', '11', '11_2_This is CILO2 for CG__2005', 3, '', 13, 1),
(25, '2021-05-24 08:28:16.968973', '10', '10_3_This is CILO3 for CG__2005', 3, '', 13, 1),
(26, '2021-05-24 08:29:41.889289', '13', '13_2_This is CILO2 for CG__2021', 3, '', 13, 1),
(27, '2021-05-24 08:32:25.836998', '14', '14_3_This is CILO3 for CG__2021', 3, '', 13, 1),
(28, '2021-05-24 08:32:29.002661', '15', '15_2_This is CILO2 for CG__2021', 3, '', 13, 1),
(29, '2021-05-24 08:32:31.972688', '12', '12_3_This is CILO3 for CG__2021', 3, '', 13, 1),
(30, '2021-05-24 08:33:02.670515', '16', '16_3_This is CILO3 for CG__2021', 3, '', 13, 1),
(31, '2021-05-24 08:33:49.201569', '17', '17_2_This is CILO2 for CG__2021', 3, '', 13, 1),
(32, '2021-05-24 09:24:17.824756', '2', '2_Quiz_0.0_1_2_2005', 1, '[{\"added\": {}}]', 12, 1),
(33, '2021-05-24 09:24:42.066879', '2', '2_Quiz_15.0_1_2_2005', 2, '[{\"changed\": {\"fields\": [\"Percentage\"]}}]', 12, 1),
(34, '2021-05-24 09:25:05.341645', '3', '3_Midterm_30.0_1_2_3_2005', 1, '[{\"added\": {}}]', 12, 1),
(35, '2021-05-24 09:25:29.447041', '4', '4_Final_55.0_1_2_3_2005', 1, '[{\"added\": {}}]', 12, 1),
(36, '2021-05-25 11:04:27.107950', '19', '19_2_This is CILO2 for CG__2021', 3, '', 13, 1),
(37, '2021-05-25 12:03:54.675858', '4', '4_Final_55.0_1-2-3_2005', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(38, '2021-05-25 12:04:02.553955', '3', '3_Midterm_30.0_1-2-3_2005', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(39, '2021-05-25 12:04:09.277802', '2', '2_Quiz_15.0_1-2_2005', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(40, '2021-05-25 12:19:08.985230', '3', '3_Midterm_10.0_1-2-3_2005', 2, '[{\"changed\": {\"fields\": [\"Percentage\"]}}]', 12, 1),
(41, '2021-05-25 12:19:09.184693', '2', '2_Quiz_5.0_1-2_2005', 2, '[{\"changed\": {\"fields\": [\"Percentage\"]}}]', 12, 1),
(42, '2021-05-25 12:20:22.711512', '18', '18_1_This is CILO1 for CG_Null_2021', 2, '[{\"changed\": {\"fields\": [\"CILOName\", \"Description\", \"PreCILO\"]}}]', 13, 1),
(43, '2021-05-25 12:21:11.051137', '4', '4_Final_55.0_1-2-3_2021', 2, '[{\"changed\": {\"fields\": [\"AcademicYear\"]}}]', 12, 1),
(44, '2021-05-25 12:21:17.075572', '3', '3_Midterm_10.0_1-2-3_2021', 2, '[{\"changed\": {\"fields\": [\"AcademicYear\"]}}]', 12, 1),
(45, '2021-05-25 12:21:22.829152', '2', '2_Quiz_5.0_1-2_2021', 2, '[{\"changed\": {\"fields\": [\"AcademicYear\"]}}]', 12, 1),
(46, '2021-05-25 13:12:07.758957', '11', 'UserD00001', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 7, 1),
(47, '2021-05-25 16:17:01.041882', '3', '1_Roger_CST_2018_1_Quiz and Assignment_30.0_1_2_2021_27_2018', 1, '[{\"added\": {}}]', 14, 1),
(48, '2021-05-25 16:36:25.365377', '4', '1_Roger_CST_2018_3_Final examination_40.0_1_3_2021_35_2018', 1, '[{\"added\": {}}]', 14, 1),
(49, '2021-05-25 16:37:56.054979', '5', '1_Roger_CST_2018_2_Project_30.0_2_3_2021_25_2018', 1, '[{\"added\": {}}]', 14, 1),
(50, '2021-05-25 16:38:22.435237', '6', '1_Roger_CST_2018_4_Quiz and Assignment_20.0_4_5_2020_15_2018', 1, '[{\"added\": {}}]', 14, 1),
(51, '2021-05-25 16:38:42.614536', '7', '1_Roger_CST_2018_5_Mid term_20.0_4_2020_18_2018', 1, '[{\"added\": {}}]', 14, 1),
(52, '2021-05-25 16:39:00.637993', '8', '1_Roger_CST_2018_6_Final_60.0_4_5_6_2020_55_2005', 1, '[{\"added\": {}}]', 14, 1),
(53, '2021-05-25 16:39:23.059900', '9', '1_Roger_CST_2018_7_Assignment_10.0_7_2019_6_2018', 1, '[{\"added\": {}}]', 14, 1),
(54, '2021-05-25 16:42:25.281240', '10', '1_Roger_CST_2018_8_Lab_20.0_7_2019_8_2005', 1, '[{\"added\": {}}]', 14, 1),
(55, '2021-05-25 16:42:50.542173', '11', '1_Roger_CST_2018_9_Project_30.0_7_8_2019_15_2018', 1, '[{\"added\": {}}]', 14, 1),
(56, '2021-05-25 16:43:12.127157', '12', '1_Roger_CST_2018_10_Final_40.0_7_2019_20_2005', 1, '[{\"added\": {}}]', 14, 1),
(57, '2021-05-25 17:56:48.333855', '11', '11_Calculus II_MATH1083_FE_CST', 1, '[{\"added\": {}}]', 11, 1),
(58, '2021-05-25 18:29:15.155481', '1', '1_Roger_CST_2018|1_Calculus I_MATH1073_MR_CST', 1, '[{\"added\": {}}]', 15, 1),
(59, '2021-05-25 18:31:38.284624', '12', '1_Roger_CST_2018_10_Final_40.0_7_2019_20_2018', 2, '[{\"changed\": {\"fields\": [\"AcademicYear\"]}}]', 14, 1),
(60, '2021-05-25 18:37:03.495428', '1', '1_Roger_CST_2018|6_Machine learning_COMP4103_FE_CST', 2, '[{\"changed\": {\"fields\": [\"course\"]}}]', 15, 1),
(61, '2021-05-25 18:37:10.655105', '2', '1_Roger_CST_2018|7_Linear Algebra_MATH1003_MR_CST', 1, '[{\"added\": {}}]', 15, 1),
(62, '2021-05-25 18:37:19.225067', '3', '1_Roger_CST_2018|4_Computer Vision_COMP4113_ME_CST', 1, '[{\"added\": {}}]', 15, 1),
(63, '2021-05-26 08:00:26.099178', '3', '1_Roger_CST_2018|4_Computer Vision_COMP4113_ME_CST', 2, '[{\"changed\": {\"fields\": [\"Semester\"]}}]', 15, 1),
(64, '2021-05-26 08:00:32.977532', '2', '1_Roger_CST_2018|7_Linear Algebra_MATH1003_MR_CST', 2, '[{\"changed\": {\"fields\": [\"Semester\"]}}]', 15, 1),
(65, '2021-05-26 08:00:39.735304', '1', '1_Roger_CST_2018|6_Machine learning_COMP4103_FE_CST', 2, '[{\"changed\": {\"fields\": [\"Semester\"]}}]', 15, 1),
(66, '2021-05-28 02:32:19.873695', '7', '7_Assignment_10.0_1_2019', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(67, '2021-05-28 02:32:27.210594', '8', '8_Lab_20.0_1-2_2019', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(68, '2021-05-28 02:33:56.591413', '10', '10_Final_40.0_1_2019', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(69, '2021-05-28 02:34:09.291342', '9', '9_Project_30.0_1-2_2019', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(70, '2021-05-28 02:34:17.741202', '8', '8_Lab_20.0_2_2019', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(71, '2021-05-28 03:25:34.659842', '8', '8_2_To enhance student\'s ability in applying machine learning method to real-world application, group projects will be give._7_2019', 2, '[{\"changed\": {\"fields\": [\"CILOName\"]}}]', 13, 1),
(72, '2021-05-28 03:25:56.385547', '7', '7_1_Lecture and assignment will be distributed to the students._7_2019', 2, '[{\"changed\": {\"fields\": [\"CILOName\", \"Description\", \"PreCILO\"]}}]', 13, 1),
(73, '2021-05-30 02:33:15.764635', '14', '9_Coco_ELLS_2014_1_Quiz and Assignment_30.0_1_2_2021_28', 1, '[{\"added\": {}}]', 14, 1),
(74, '2021-05-30 02:33:30.115966', '15', '9_Coco_ELLS_2014_2_Project_30.0_2_3_2021_28', 1, '[{\"added\": {}}]', 14, 1),
(75, '2021-05-30 02:34:00.731927', '16', '9_Coco_ELLS_2014_3_Final examination_40.0_1_3_2021_35', 1, '[{\"added\": {}}]', 14, 1),
(76, '2021-05-30 02:34:20.725089', '17', '9_Coco_ELLS_2014_4_Quiz and Assignment_20.0_4_5_2020_15', 1, '[{\"added\": {}}]', 14, 1),
(77, '2021-05-30 02:34:42.187516', '18', '9_Coco_ELLS_2014_5_Mid term_20.0_4_2020_18', 1, '[{\"added\": {}}]', 14, 1),
(78, '2021-05-30 02:35:30.253305', '19', '9_Coco_ELLS_2014_6_Final_60.0_4_5_6_2020_50', 1, '[{\"added\": {}}]', 14, 1),
(79, '2021-05-30 02:35:49.371236', '20', '9_Coco_ELLS_2014_7_Assignment_10.0_1_2019_8', 1, '[{\"added\": {}}]', 14, 1),
(80, '2021-05-30 02:36:05.128604', '21', '9_Coco_ELLS_2014_8_Lab_20.0_2_2019_17', 1, '[{\"added\": {}}]', 14, 1),
(81, '2021-05-30 02:36:17.679706', '22', '9_Coco_ELLS_2014_9_Project_30.0_1-2_2019_22', 1, '[{\"added\": {}}]', 14, 1),
(82, '2021-05-30 02:37:12.821294', '23', '9_Coco_ELLS_2014_10_Final_40.0_1_2019_38', 1, '[{\"added\": {}}]', 14, 1),
(83, '2021-05-30 02:38:35.243427', '4', '9_Coco_ELLS_2014|4_Computer Vision_COMP4113_ME_CST', 1, '[{\"added\": {}}]', 15, 1),
(84, '2021-05-30 02:39:40.440380', '5', '9_Coco_ELLS_2014|7_Linear Algebra_MATH1003_MR_CST', 1, '[{\"added\": {}}]', 15, 1),
(85, '2021-05-30 02:40:14.771233', '6', '9_Coco_ELLS_2014|6_Machine learning_COMP4103_FE_CST', 1, '[{\"added\": {}}]', 15, 1),
(86, '2021-05-30 02:41:58.970532', '24', '2_Joni_CST_2019_1_Quiz and Assignment_30.0_1_2_2021_18', 1, '[{\"added\": {}}]', 14, 1),
(87, '2021-05-30 02:42:19.778542', '25', '2_Joni_CST_2019_2_Project_30.0_2_3_2021_22', 1, '[{\"added\": {}}]', 14, 1),
(88, '2021-05-30 02:42:39.546952', '26', '2_Joni_CST_2019_3_Final examination_40.0_1_3_2021_23', 1, '[{\"added\": {}}]', 14, 1),
(89, '2021-05-30 02:42:56.041170', '27', '2_Joni_CST_2019_4_Quiz and Assignment_20.0_4_5_2020_9', 1, '[{\"added\": {}}]', 14, 1),
(90, '2021-05-30 02:43:29.587383', '28', '2_Joni_CST_2019_5_Mid term_20.0_4_2020_13', 1, '[{\"added\": {}}]', 14, 1),
(91, '2021-05-30 02:43:57.669234', '29', '2_Joni_CST_2019_6_Final_60.0_4_5_6_2020_36', 1, '[{\"added\": {}}]', 14, 1),
(92, '2021-05-30 02:45:12.705498', '30', '2_Joni_CST_2019_7_Assignment_10.0_1_2019_8', 1, '[{\"added\": {}}]', 14, 1),
(93, '2021-05-30 02:45:29.302132', '31', '2_Joni_CST_2019_8_Lab_20.0_2_2019_15', 1, '[{\"added\": {}}]', 14, 1),
(94, '2021-05-30 02:45:48.749726', '32', '2_Joni_CST_2019_9_Project_30.0_1-2_2019_26', 1, '[{\"added\": {}}]', 14, 1),
(95, '2021-05-30 02:46:03.968152', '33', '2_Joni_CST_2019_10_Final_40.0_1_2019_25', 1, '[{\"added\": {}}]', 14, 1),
(96, '2021-05-30 02:47:02.741163', '12', '12_Calculus II_MATH1083_FE_CST', 1, '[{\"added\": {}}]', 11, 1),
(97, '2021-05-30 02:47:17.513194', '6', '9_Coco_ELLS_2014|6_Machine learning_COMP4103_FE_CST', 3, '', 15, 1),
(98, '2021-05-30 02:47:44.591176', '7', '9_Coco_ELLS_2014|6_Machine learning_COMP4103_FE_CST', 1, '[{\"added\": {}}]', 15, 1),
(99, '2021-05-30 02:47:57.379356', '8', '2_Joni_CST_2019|4_Computer Vision_COMP4113_ME_CST', 1, '[{\"added\": {}}]', 15, 1),
(100, '2021-05-30 02:48:16.009185', '9', '2_Joni_CST_2019|6_Machine learning_COMP4103_FE_CST', 1, '[{\"added\": {}}]', 15, 1),
(101, '2021-05-30 02:48:40.951846', '10', '2_Joni_CST_2019|7_Linear Algebra_MATH1003_MR_CST', 1, '[{\"added\": {}}]', 15, 1),
(102, '2021-05-30 02:55:07.786244', '21', 'User:N00001', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 7, 1),
(103, '2021-05-30 04:31:30.032594', '12', '12_Calculus II_MATH1083_FE_CST', 3, '', 11, 1),
(104, '2021-05-30 05:21:29.416660', '6', '6_Final_60.0_4-5-6_2020', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(105, '2021-05-30 05:21:35.873099', '4', '4_Quiz and Assignment_20.0_4-5_2020', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(106, '2021-05-30 05:21:42.530715', '3', '3_Final examination_40.0_1-3_2021', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(107, '2021-05-30 05:21:55.761332', '2', '2_Project_30.0_2-3_2021', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(108, '2021-05-30 05:22:02.807153', '1', '1_Quiz and Assignment_30.0_1-2_2021', 2, '[{\"changed\": {\"fields\": [\"CILOIDs\"]}}]', 12, 1),
(109, '2021-05-30 08:04:49.897704', '6', '6_3_Use Matlab, a mathematical software, to study a matrix based on the concepts in CILO1_4_2020', 2, '[{\"changed\": {\"fields\": [\"CILOName\"]}}]', 13, 1),
(110, '2021-05-30 08:04:55.867990', '5', '5_2_Apply the properties of these concepts to the study of the properties of differnt forms of matirces_4_2020', 2, '[{\"changed\": {\"fields\": [\"CILOName\"]}}]', 13, 1),
(111, '2021-05-30 08:05:13.755606', '3', '3_3_Develop a system related to the computer vision to solve a problem in the real world._1_2_2021', 2, '[{\"changed\": {\"fields\": [\"CILOName\"]}}]', 13, 1),
(112, '2021-05-30 08:05:25.166134', '3', '3_3_Develop a system related to the computer vision to solve a problem in the real world._1-2_2021', 2, '[{\"changed\": {\"fields\": [\"PreCILO\"]}}]', 13, 1),
(113, '2021-05-30 08:05:31.670132', '2', '2_2_Apply fundamental techniques in computer vision using PyTorch_1_2021', 2, '[{\"changed\": {\"fields\": [\"CILOName\"]}}]', 13, 1),
(114, '2021-05-30 08:07:53.787085', '4', '4_1_Describe the basic concepts in linear transformations, orthogonality and eigenvalues._Null_2020', 2, '[{\"changed\": {\"fields\": [\"CILOName\", \"PreCILO\"]}}]', 13, 1),
(115, '2021-05-30 08:08:18.479872', '1', '1_1_Explain the underlying concepts and write representations of different algorithm of compter vision_Null_2021', 2, '[{\"changed\": {\"fields\": [\"CILOName\", \"PreCILO\"]}}]', 13, 1),
(116, '2021-05-30 08:08:57.241597', '22', '22_1_new CILO1_7_2020', 1, '[{\"added\": {}}]', 13, 1),
(117, '2021-05-30 08:09:23.259636', '23', '23_2_new CILO2_7_2020', 1, '[{\"added\": {}}]', 13, 1),
(118, '2021-05-30 08:10:51.386751', '11', '11_Final_40.0_1_2020', 1, '[{\"added\": {}}]', 12, 1),
(119, '2021-05-30 08:11:16.970535', '12', '12_Project_30.0_1-2_2020', 1, '[{\"added\": {}}]', 12, 1),
(120, '2021-05-30 08:11:36.100135', '13', '13_Lab_20.0_2_2020', 1, '[{\"added\": {}}]', 12, 1),
(121, '2021-05-30 08:12:37.735273', '14', '14_Assignment_10.0_1_2020', 1, '[{\"added\": {}}]', 12, 1),
(122, '2021-05-30 08:14:18.241487', '34', '3_Timmy_DS_2020_11_Final_40.0_1_2020_38', 1, '[{\"added\": {}}]', 14, 1),
(123, '2021-05-30 08:14:37.924278', '35', '3_Timmy_DS_2020_12_Project_30.0_1-2_2020_28', 1, '[{\"added\": {}}]', 14, 1),
(124, '2021-05-30 08:15:02.943480', '36', '3_Timmy_DS_2020_13_Lab_20.0_2_2020_17', 1, '[{\"added\": {}}]', 14, 1),
(125, '2021-05-30 08:15:16.704473', '37', '3_Timmy_DS_2020_14_Assignment_10.0_1_2020_8', 1, '[{\"added\": {}}]', 14, 1),
(126, '2021-05-30 08:15:36.283605', '11', '3_Timmy_DS_2020|6_Machine learning_COMP4103_FE_CST', 1, '[{\"added\": {}}]', 15, 1),
(127, '2021-05-30 08:16:05.460890', '38', '4_Tony_FM_2021_11_Final_40.0_1_2020_35', 1, '[{\"added\": {}}]', 14, 1),
(128, '2021-05-30 08:16:33.644041', '39', '4_Tony_FM_2021_12_Project_30.0_1-2_2020_27', 1, '[{\"added\": {}}]', 14, 1),
(129, '2021-05-30 08:16:47.012696', '40', '4_Tony_FM_2021_12_Project_30.0_1-2_2020_18', 1, '[{\"added\": {}}]', 14, 1),
(130, '2021-05-30 08:17:08.080839', '41', '4_Tony_FM_2021_14_Assignment_10.0_1_2020_9', 1, '[{\"added\": {}}]', 14, 1),
(131, '2021-05-30 08:17:21.294984', '12', '4_Tony_FM_2021|6_Machine learning_COMP4103_FE_CST', 1, '[{\"added\": {}}]', 15, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(12, 'course', 'assessment'),
(13, 'course', 'cilo'),
(11, 'course', 'course'),
(6, 'sessions', 'session'),
(7, 'user', 'account'),
(8, 'user', 'coursedesigner'),
(9, 'user', 'noncoursedesigner'),
(10, 'user', 'student'),
(14, 'visGrade', 'gradereport'),
(15, 'visGrade', 'student_course');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-05-19 15:21:35.761590'),
(2, 'auth', '0001_initial', '2021-05-19 15:21:37.621442'),
(3, 'admin', '0001_initial', '2021-05-19 15:21:46.973487'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-05-19 15:21:49.322170'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-05-19 15:21:49.368046'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-05-19 15:21:50.197828'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-05-19 15:21:51.100412'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-05-19 15:21:51.221127'),
(9, 'auth', '0004_alter_user_username_opts', '2021-05-19 15:21:51.281925'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-05-19 15:21:52.029924'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-05-19 15:21:52.239367'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-05-19 15:21:52.301199'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-05-19 15:21:52.461245'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-05-19 15:21:52.624625'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-05-19 15:21:52.776595'),
(16, 'auth', '0011_update_proxy_permissions', '2021-05-19 15:21:52.837433'),
(17, 'sessions', '0001_initial', '2021-05-19 15:21:53.171900'),
(18, 'user', '0001_initial', '2021-05-19 17:48:06.431481'),
(19, 'user', '0002_auto_20210520_0153', '2021-05-19 17:53:31.110035'),
(20, 'user', '0003_auto_20210520_0218', '2021-05-19 18:18:40.717164'),
(21, 'user', '0004_account_type', '2021-05-19 19:26:31.002217'),
(22, 'user', '0005_auto_20210522_0956', '2021-05-22 01:56:37.858131'),
(23, 'course', '0001_initial', '2021-05-23 02:48:22.154570'),
(24, 'course', '0002_auto_20210524_1204', '2021-05-24 04:04:14.463533'),
(25, 'course', '0003_auto_20210524_1722', '2021-05-24 09:22:47.858328'),
(26, 'course', '0004_auto_20210525_1858', '2021-05-25 10:58:13.009116'),
(27, 'visGrade', '0001_initial', '2021-05-25 13:42:18.699276'),
(28, 'visGrade', '0002_auto_20210525_2151', '2021-05-25 13:51:30.623460'),
(29, 'visGrade', '0003_auto_20210526_0228', '2021-05-25 18:28:28.367626'),
(30, 'visGrade', '0004_auto_20210526_1559', '2021-05-26 07:59:36.903534'),
(31, 'course', '0005_auto_20210530_1606', '2021-05-30 08:07:06.786357'),
(32, 'visGrade', '0005_auto_20210530_1606', '2021-05-30 08:07:06.848854');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('005irxkqa31369tpy3xb839outbqzx6v', 'MjlmY2YwYTY0MGZiOGFlYWMyZWY4ZjE0OWRjZDNmNzI3ZDBjNjIzZTp7InVzZXJuYW1lIjoiQnJpYW4iLCJ1aWQiOjIsInV0eXBlIjoiU3R1ZGVudCJ9', '2021-06-05 02:14:14.753095'),
('7rtg52bcw1tdsvw6p3u3uebibwibvixg', 'MjlmY2YwYTY0MGZiOGFlYWMyZWY4ZjE0OWRjZDNmNzI3ZDBjNjIzZTp7InVzZXJuYW1lIjoiQnJpYW4iLCJ1aWQiOjIsInV0eXBlIjoiU3R1ZGVudCJ9', '2021-06-05 04:18:09.116693'),
('8hm5vjc63bq0730ut541o2xkk9x36g9r', 'MjlmY2YwYTY0MGZiOGFlYWMyZWY4ZjE0OWRjZDNmNzI3ZDBjNjIzZTp7InVzZXJuYW1lIjoiQnJpYW4iLCJ1aWQiOjIsInV0eXBlIjoiU3R1ZGVudCJ9', '2021-06-05 04:18:08.988030'),
('9jh1koya8oye04z7g6jniuxw9igb579u', 'OWQzY2JiYTZmZDdiODI5ZTgzNzc5MzNhYTM2ZTA1NjE1ODhhYTU4Zjp7InVzZXJuYW1lIjoiUzAwMDAxIiwidWlkIjoxLCJ1dHlwZSI6IlN0dWRlbnQifQ==', '2021-06-08 16:56:33.930237'),
('dmpucobkyyhxtyu6ek1o18o6y0i8wtgj', 'MjlmY2YwYTY0MGZiOGFlYWMyZWY4ZjE0OWRjZDNmNzI3ZDBjNjIzZTp7InVzZXJuYW1lIjoiQnJpYW4iLCJ1aWQiOjIsInV0eXBlIjoiU3R1ZGVudCJ9', '2021-06-05 02:42:52.569534'),
('e3ni7k5fv0fdftwqnepgeteknnpicitb', 'MjlmY2YwYTY0MGZiOGFlYWMyZWY4ZjE0OWRjZDNmNzI3ZDBjNjIzZTp7InVzZXJuYW1lIjoiQnJpYW4iLCJ1aWQiOjIsInV0eXBlIjoiU3R1ZGVudCJ9', '2021-06-05 04:18:09.354051'),
('fdm5kobquecby2s0j3d5v81nn6omktwv', 'YzAyMTAxYWQ3ZjU3MGYxMDg5ODhmMmE0M2I4ZjVkMTZjNzBiOTEyMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwODU3NWRhZTY2NmJkOWE5ZDcxYTIwNGI4NWNmMmIxMWQ5YThkOGE3IiwidXNlcm5hbWUiOiJTMDAwMDEiLCJ1aWQiOjEsInV0eXBlIjoiU3R1ZGVudCJ9', '2021-06-08 17:52:29.999811'),
('h3o4uwwi29v50ou8wpssbtmlgrsdnjqk', 'MjlmY2YwYTY0MGZiOGFlYWMyZWY4ZjE0OWRjZDNmNzI3ZDBjNjIzZTp7InVzZXJuYW1lIjoiQnJpYW4iLCJ1aWQiOjIsInV0eXBlIjoiU3R1ZGVudCJ9', '2021-06-05 04:18:09.116693'),
('l5umnmqnk84g1qg5j70fuql77tbg1z3q', 'MjlmY2YwYTY0MGZiOGFlYWMyZWY4ZjE0OWRjZDNmNzI3ZDBjNjIzZTp7InVzZXJuYW1lIjoiQnJpYW4iLCJ1aWQiOjIsInV0eXBlIjoiU3R1ZGVudCJ9', '2021-06-05 04:18:09.117684'),
('lm348o0e5ibvlzzdule1l0ah6eskmqsa', 'NjVjNzBiMDkzZDNkYmU1MWRmYWUwY2NlYjg3ZDdlYWQxMzBmMDk1MTp7InVzZXJuYW1lIjoiRDAwMDAxIiwidWlkIjoxMSwidXR5cGUiOiJDb3Vyc2VEZXNpZ25lciJ9', '2021-06-08 17:38:58.741093'),
('r3oxzszequ6fsjuaumwr90wjx4n99s53', 'OWQzY2JiYTZmZDdiODI5ZTgzNzc5MzNhYTM2ZTA1NjE1ODhhYTU4Zjp7InVzZXJuYW1lIjoiUzAwMDAxIiwidWlkIjoxLCJ1dHlwZSI6IlN0dWRlbnQifQ==', '2021-06-08 19:51:02.584594'),
('u65vo3042199ppimwhdczjy4xtwu9toa', 'MDg5ODYwNmE5MGEzODkyYzNhNzQyYzQ3OTY0YWM1ZTcxODUwOTk0ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwODU3NWRhZTY2NmJkOWE5ZDcxYTIwNGI4NWNmMmIxMWQ5YThkOGE3IiwidXNlcm5hbWUiOiJKdWR5IiwidWlkIjoxLCJ1dHlwZSI6IkNvdXJzZURlc2lnbmVyIn0=', '2021-06-05 09:09:55.618800'),
('ul5txjw7ec7z3yonih0pgr22w9obww5r', 'MjlmY2YwYTY0MGZiOGFlYWMyZWY4ZjE0OWRjZDNmNzI3ZDBjNjIzZTp7InVzZXJuYW1lIjoiQnJpYW4iLCJ1aWQiOjIsInV0eXBlIjoiU3R1ZGVudCJ9', '2021-06-05 04:18:08.992019'),
('xphv9bdayxk83wz4jamf8emqa7ccrvfu', 'NTZjM2ZlMDIxOTk3NDQ4YTU1NTMzYjk3NWU2NWY1ODA1Njk3Mzc5Zjp7InVzZXJuYW1lIjoiUzAwMDAxIiwidWlkIjoxLCJ1dHlwZSI6IlN0dWRlbnQiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDg1NzVkYWU2NjZiZDlhOWQ3MWEyMDRiODVjZjJiMTFkOWE4ZDhhNyJ9', '2021-06-08 17:52:05.792292'),
('y0ean0z8s3rvegs537rk6bb4kdsv4465', 'MjlmY2YwYTY0MGZiOGFlYWMyZWY4ZjE0OWRjZDNmNzI3ZDBjNjIzZTp7InVzZXJuYW1lIjoiQnJpYW4iLCJ1aWQiOjIsInV0eXBlIjoiU3R1ZGVudCJ9', '2021-06-05 04:18:09.117684'),
('y0qor2uhnkvwbxfeucadz3tw3so1qxp2', 'MjlmY2YwYTY0MGZiOGFlYWMyZWY4ZjE0OWRjZDNmNzI3ZDBjNjIzZTp7InVzZXJuYW1lIjoiQnJpYW4iLCJ1aWQiOjIsInV0eXBlIjoiU3R1ZGVudCJ9', '2021-06-05 04:18:09.116693'),
('zoflog8k0w1qcorb40v245d51cu4qk62', 'ZTA0YTNkYTQxYzFjYWMzOWIzY2NhYjBiY2M1ZGZkMGMyMGZiMzIwNjp7InVzZXJuYW1lIjoiSnVkeSIsInVpZCI6MSwidXR5cGUiOiJDb3Vyc2VEZXNpZ25lciJ9', '2021-06-05 09:44:13.235464');

-- --------------------------------------------------------

--
-- Table structure for table `grade_report`
--

CREATE TABLE `grade_report` (
  `id` int(11) NOT NULL,
  `Marks` int(11) NOT NULL,
  `assessment_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `StudentName` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `grade_report`
--

INSERT INTO `grade_report` (`id`, `Marks`, `assessment_id`, `student_id`, `StudentName`) VALUES
(3, 27, 1, 1, 'Roger'),
(4, 35, 3, 1, 'Roger'),
(5, 25, 2, 1, 'Roger'),
(6, 15, 4, 1, 'Roger'),
(7, 18, 5, 1, 'Roger'),
(8, 55, 6, 1, 'Roger'),
(9, 6, 7, 1, 'Roger'),
(10, 8, 8, 1, 'Roger'),
(11, 15, 9, 1, 'Roger'),
(12, 20, 10, 1, 'Roger'),
(14, 28, 1, 9, 'CoCo'),
(15, 28, 2, 9, 'CoCo'),
(16, 35, 3, 9, 'CoCo'),
(17, 15, 4, 9, 'CoCo'),
(18, 18, 5, 9, 'CoCo'),
(19, 50, 6, 9, 'CoCo'),
(20, 8, 7, 9, 'CoCo'),
(21, 17, 8, 9, 'CoCo'),
(22, 22, 9, 9, 'CoCo'),
(23, 38, 10, 9, 'CoCo'),
(24, 18, 1, 2, 'Joni'),
(25, 22, 2, 2, 'Joni'),
(26, 23, 3, 2, 'Joni'),
(27, 9, 4, 2, 'Joni'),
(28, 13, 5, 2, 'Joni'),
(29, 36, 6, 2, 'Joni'),
(30, 8, 7, 2, 'Joni'),
(31, 15, 8, 2, 'Joni'),
(32, 26, 9, 2, 'Joni'),
(33, 25, 10, 2, 'Joni'),
(34, 38, 11, 3, 'Timmy'),
(35, 28, 12, 3, 'Timmy'),
(36, 17, 13, 3, 'Timmy'),
(37, 8, 14, 3, 'Timmy'),
(38, 35, 11, 4, 'Tony'),
(39, 27, 12, 4, 'Tony'),
(40, 18, 12, 4, 'Tony'),
(41, 9, 14, 4, 'Tony');

-- --------------------------------------------------------

--
-- Table structure for table `noncourse_designer`
--

CREATE TABLE `noncourse_designer` (
  `fullname` varchar(30) NOT NULL,
  `programme` varchar(15) NOT NULL,
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `noncourse_designer`
--

INSERT INTO `noncourse_designer` (`fullname`, `programme`, `id`, `account_id`) VALUES
('Lili', 'CST', 1, 21),
('Cici', 'DS', 2, 22),
('Titi', 'FM', 3, 23),
('Kiki', 'FST', 4, 24),
('Jina', 'ACCT', 5, 25),
('Piso', 'FIN', 6, 26);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `fullname` varchar(30) NOT NULL,
  `programme` varchar(15) NOT NULL,
  `id` int(11) NOT NULL,
  `enrollmentYear` int(11) NOT NULL,
  `account_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`fullname`, `programme`, `id`, `enrollmentYear`, `account_id`) VALUES
('Roger', 'CST', 1, 2018, 1),
('Joni', 'CST', 2, 2019, 2),
('Timmy', 'DS', 3, 2020, 3),
('Tony', 'FM', 4, 2021, 4),
('Saxon', 'APSY', 5, 2014, 5),
('Bill', 'ENVS', 6, 2016, 6),
('Helen', 'FIN', 7, 2015, 7),
('Mike', 'ACCT', 8, 2019, 8),
('Coco', 'ELLS', 9, 2014, 9),
('Nina', 'PRA', 10, 2008, 10);

-- --------------------------------------------------------

--
-- Table structure for table `student_course`
--

CREATE TABLE `student_course` (
  `id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `Semester` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_course`
--

INSERT INTO `student_course` (`id`, `course_id`, `student_id`, `Semester`) VALUES
(1, 6, 1, 2019),
(2, 7, 1, 2020),
(3, 4, 1, 2021),
(4, 4, 9, 2021),
(5, 7, 9, 2020),
(7, 6, 9, 2019),
(8, 4, 2, 2021),
(9, 6, 2, 2019),
(10, 7, 2, 2020),
(11, 6, 3, 2020),
(12, 6, 4, 2020);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `assessment`
--
ALTER TABLE `assessment`
  ADD PRIMARY KEY (`AssessmentID`),
  ADD KEY `Assessment_course_id_668297fd_fk_Course_courseID` (`course_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `cilo`
--
ALTER TABLE `cilo`
  ADD PRIMARY KEY (`CILOID`),
  ADD KEY `CILO_course_id_f89cb264_fk_Course_courseID` (`course_id`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`CourseID`);

--
-- Indexes for table `course_designer`
--
ALTER TABLE `course_designer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_id` (`account_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `grade_report`
--
ALTER TABLE `grade_report`
  ADD PRIMARY KEY (`id`),
  ADD KEY `GradeReport_assessment_id_4a760735_fk_Assessment_AssessmentID` (`assessment_id`),
  ADD KEY `GradeReport_student_id_834b14de_fk_student_id` (`student_id`);

--
-- Indexes for table `noncourse_designer`
--
ALTER TABLE `noncourse_designer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_id` (`account_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_id` (`account_id`);

--
-- Indexes for table `student_course`
--
ALTER TABLE `student_course`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Student_Course_student_id_course_id_74deab22_uniq` (`student_id`,`course_id`),
  ADD KEY `Student_Course_course_id_a0b6a8cc_fk_Course_CourseID` (`course_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `assessment`
--
ALTER TABLE `assessment`
  MODIFY `AssessmentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cilo`
--
ALTER TABLE `cilo`
  MODIFY `CILOID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `CourseID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `course_designer`
--
ALTER TABLE `course_designer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=132;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `grade_report`
--
ALTER TABLE `grade_report`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `noncourse_designer`
--
ALTER TABLE `noncourse_designer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `student_course`
--
ALTER TABLE `student_course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `assessment`
--
ALTER TABLE `assessment`
  ADD CONSTRAINT `Assessment_course_id_668297fd_fk_Course_courseID` FOREIGN KEY (`course_id`) REFERENCES `course` (`courseID`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `cilo`
--
ALTER TABLE `cilo`
  ADD CONSTRAINT `CILO_course_id_f89cb264_fk_Course_courseID` FOREIGN KEY (`course_id`) REFERENCES `course` (`courseID`);

--
-- Constraints for table `course_designer`
--
ALTER TABLE `course_designer`
  ADD CONSTRAINT `course_designer_account_id_f4ec223a_fk_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `grade_report`
--
ALTER TABLE `grade_report`
  ADD CONSTRAINT `GradeReport_assessment_id_4a760735_fk_Assessment_AssessmentID` FOREIGN KEY (`assessment_id`) REFERENCES `assessment` (`AssessmentID`),
  ADD CONSTRAINT `GradeReport_student_id_834b14de_fk_student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`);

--
-- Constraints for table `noncourse_designer`
--
ALTER TABLE `noncourse_designer`
  ADD CONSTRAINT `noncourse_designer_account_id_18a91ef0_fk_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`);

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_account_id_34e2a8a4_fk_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`);

--
-- Constraints for table `student_course`
--
ALTER TABLE `student_course`
  ADD CONSTRAINT `Student_Course_course_id_a0b6a8cc_fk_Course_CourseID` FOREIGN KEY (`course_id`) REFERENCES `course` (`CourseID`),
  ADD CONSTRAINT `Student_Course_student_id_20c41944_fk_student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
