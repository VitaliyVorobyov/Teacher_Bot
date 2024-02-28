--
-- PostgreSQL database dump
--

-- Dumped from database version 16rc1
-- Dumped by pg_dump version 16rc1

-- Started on 2024-02-27 20:56:35 MSK

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3667 (class 1262 OID 19086)
-- Name: teacher_bot; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE teacher_bot WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';


\connect teacher_bot

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--
DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA public;


--
-- TOC entry 3668 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 19102)
-- Name: buttons; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.buttons (
    button_id integer NOT NULL,
    name_button character varying(100) NOT NULL,
    start_button boolean DEFAULT false NOT NULL
);


--
-- TOC entry 215 (class 1259 OID 19101)
-- Name: buttons_button_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.buttons_button_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3669 (class 0 OID 0)
-- Dependencies: 215
-- Name: buttons_button_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.buttons_button_id_seq OWNED BY public.buttons.button_id;


--
-- TOC entry 218 (class 1259 OID 19112)
-- Name: buttons_to_button; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.buttons_to_button (
    buttons_to_button_id integer NOT NULL,
    button_id integer,
    button_id_to integer
);


--
-- TOC entry 217 (class 1259 OID 19111)
-- Name: buttons_to_button_buttons_to_button_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.buttons_to_button_buttons_to_button_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3670 (class 0 OID 0)
-- Dependencies: 217
-- Name: buttons_to_button_buttons_to_button_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.buttons_to_button_buttons_to_button_id_seq OWNED BY public.buttons_to_button.buttons_to_button_id;


--
-- TOC entry 226 (class 1259 OID 19465)
-- Name: content_to_button; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.content_to_button (
    content_to_button_id integer NOT NULL,
    button_id integer,
    file_to_description_id integer
);


--
-- TOC entry 225 (class 1259 OID 19464)
-- Name: content_to_button_content_to_button_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.content_to_button_content_to_button_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3671 (class 0 OID 0)
-- Dependencies: 225
-- Name: content_to_button_content_to_button_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.content_to_button_content_to_button_id_seq OWNED BY public.content_to_button.content_to_button_id;


--
-- TOC entry 222 (class 1259 OID 19441)
-- Name: description; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.description (
    description_id integer NOT NULL,
    description character varying(100) NOT NULL
);


--
-- TOC entry 221 (class 1259 OID 19440)
-- Name: description_description_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.description_description_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3672 (class 0 OID 0)
-- Dependencies: 221
-- Name: description_description_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.description_description_id_seq OWNED BY public.description.description_id;


--
-- TOC entry 224 (class 1259 OID 19448)
-- Name: file_to_description; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.file_to_description (
    file_to_description_id integer NOT NULL,
    row_id integer,
    description_id integer
);


--
-- TOC entry 223 (class 1259 OID 19447)
-- Name: file_to_description_file_to_description_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.file_to_description_file_to_description_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3673 (class 0 OID 0)
-- Dependencies: 223
-- Name: file_to_description_file_to_description_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.file_to_description_file_to_description_id_seq OWNED BY public.file_to_description.file_to_description_id;


--
-- TOC entry 220 (class 1259 OID 19434)
-- Name: files; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.files (
    row_id integer NOT NULL,
    file_id character varying(100) NOT NULL
);


--
-- TOC entry 219 (class 1259 OID 19433)
-- Name: files_row_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.files_row_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3674 (class 0 OID 0)
-- Dependencies: 219
-- Name: files_row_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.files_row_id_seq OWNED BY public.files.row_id;


--
-- TOC entry 228 (class 1259 OID 19487)
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id integer NOT NULL,
    user_id integer NOT NULL
);


--
-- TOC entry 227 (class 1259 OID 19486)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3675 (class 0 OID 0)
-- Dependencies: 227
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 3473 (class 2604 OID 19105)
-- Name: buttons button_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.buttons ALTER COLUMN button_id SET DEFAULT nextval('public.buttons_button_id_seq'::regclass);


--
-- TOC entry 3475 (class 2604 OID 19115)
-- Name: buttons_to_button buttons_to_button_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.buttons_to_button ALTER COLUMN buttons_to_button_id SET DEFAULT nextval('public.buttons_to_button_buttons_to_button_id_seq'::regclass);


--
-- TOC entry 3479 (class 2604 OID 19468)
-- Name: content_to_button content_to_button_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.content_to_button ALTER COLUMN content_to_button_id SET DEFAULT nextval('public.content_to_button_content_to_button_id_seq'::regclass);


--
-- TOC entry 3477 (class 2604 OID 19444)
-- Name: description description_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.description ALTER COLUMN description_id SET DEFAULT nextval('public.description_description_id_seq'::regclass);


--
-- TOC entry 3478 (class 2604 OID 19451)
-- Name: file_to_description file_to_description_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.file_to_description ALTER COLUMN file_to_description_id SET DEFAULT nextval('public.file_to_description_file_to_description_id_seq'::regclass);


--
-- TOC entry 3476 (class 2604 OID 19437)
-- Name: files row_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.files ALTER COLUMN row_id SET DEFAULT nextval('public.files_row_id_seq'::regclass);


--
-- TOC entry 3480 (class 2604 OID 19490)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3649 (class 0 OID 19102)
-- Dependencies: 216
-- Data for Name: buttons; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.buttons VALUES (1, 'Бар', true);
INSERT INTO public.buttons VALUES (2, 'Кухня', true);
INSERT INTO public.buttons VALUES (3, 'Учебные курсы', true);
INSERT INTO public.buttons VALUES (4, 'Новинки', true);
INSERT INTO public.buttons VALUES (5, 'Аттестация', true);
INSERT INTO public.buttons VALUES (6, 'Таблицы', true);
INSERT INTO public.buttons VALUES (7, 'Поиск', true);
INSERT INTO public.buttons VALUES (8, 'Холодные закуски', false);
INSERT INTO public.buttons VALUES (9, 'Горячие закуски', false);
INSERT INTO public.buttons VALUES (10, 'Салаты', false);
INSERT INTO public.buttons VALUES (11, 'Супы', false);
INSERT INTO public.buttons VALUES (12, 'Стейки', false);
INSERT INTO public.buttons VALUES (13, 'Горячие блюда', false);
INSERT INTO public.buttons VALUES (14, 'Гарниры', false);
INSERT INTO public.buttons VALUES (15, 'Десерты', false);
INSERT INTO public.buttons VALUES (16, 'Соусы', false);


--
-- TOC entry 3651 (class 0 OID 19112)
-- Dependencies: 218
-- Data for Name: buttons_to_button; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.buttons_to_button VALUES (1, 2, 8);
INSERT INTO public.buttons_to_button VALUES (2, 2, 9);
INSERT INTO public.buttons_to_button VALUES (3, 2, 10);
INSERT INTO public.buttons_to_button VALUES (4, 2, 11);
INSERT INTO public.buttons_to_button VALUES (5, 2, 12);
INSERT INTO public.buttons_to_button VALUES (6, 2, 13);
INSERT INTO public.buttons_to_button VALUES (7, 2, 14);
INSERT INTO public.buttons_to_button VALUES (8, 2, 15);
INSERT INTO public.buttons_to_button VALUES (9, 2, 16);


--
-- TOC entry 3659 (class 0 OID 19465)
-- Dependencies: 226
-- Data for Name: content_to_button; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.content_to_button VALUES (1, 1, 1);
INSERT INTO public.content_to_button VALUES (2, 1, 2);
INSERT INTO public.content_to_button VALUES (3, 1, 3);


--
-- TOC entry 3655 (class 0 OID 19441)
-- Dependencies: 222
-- Data for Name: description; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.description VALUES (1, '❗️❗️❗️');
INSERT INTO public.description VALUES (2, 'Первый пост');
INSERT INTO public.description VALUES (3, 'Второй пост');
INSERT INTO public.description VALUES (4, 'Третий пост');


--
-- TOC entry 3657 (class 0 OID 19448)
-- Dependencies: 224
-- Data for Name: file_to_description; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.file_to_description VALUES (1, 2, 2);
INSERT INTO public.file_to_description VALUES (2, 3, 3);
INSERT INTO public.file_to_description VALUES (3, 4, 4);


--
-- TOC entry 3653 (class 0 OID 19434)
-- Dependencies: 220
-- Data for Name: files; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.files VALUES (1, 'AgACAgIAAxkBAAIDQ2XY0SkzTlhxXcofy4HHqEzQ75XLAAI71zEbehPJSmENCWhrvB-uAQADAgADeAADNAQ');
INSERT INTO public.files VALUES (2, 'AgACAgIAAxkBAAIDS2XY8tUJiePVccnxe0hXTbNo5ocbAAJn2DEbehPJSpYBB9Yr-JxZAQADAgADeAADNAQ');
INSERT INTO public.files VALUES (3, 'AgACAgIAAxkBAAIDTmXY8zMmIrs8SeuM6PB0R2QKeu4eAAJq2DEbehPJStlAB4FqPF5ZAQADAgADeAADNAQ');
INSERT INTO public.files VALUES (4, 'AgACAgIAAxkBAAIDVWXY94BJIlkGCmrAi6rDhosusfzEAAKF2DEbehPJSvph-xWW_u1GAQADAgADeAADNAQ');


--
-- TOC entry 3661 (class 0 OID 19487)
-- Dependencies: 228
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.users VALUES (1, 133233628);
INSERT INTO public.users VALUES (3, 1080069552);


--
-- TOC entry 3676 (class 0 OID 0)
-- Dependencies: 215
-- Name: buttons_button_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.buttons_button_id_seq', 23, true);


--
-- TOC entry 3677 (class 0 OID 0)
-- Dependencies: 217
-- Name: buttons_to_button_buttons_to_button_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.buttons_to_button_buttons_to_button_id_seq', 12, true);


--
-- TOC entry 3678 (class 0 OID 0)
-- Dependencies: 225
-- Name: content_to_button_content_to_button_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.content_to_button_content_to_button_id_seq', 3, true);


--
-- TOC entry 3679 (class 0 OID 0)
-- Dependencies: 221
-- Name: description_description_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.description_description_id_seq', 4, true);


--
-- TOC entry 3680 (class 0 OID 0)
-- Dependencies: 223
-- Name: file_to_description_file_to_description_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.file_to_description_file_to_description_id_seq', 3, true);


--
-- TOC entry 3681 (class 0 OID 0)
-- Dependencies: 219
-- Name: files_row_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.files_row_id_seq', 4, true);


--
-- TOC entry 3682 (class 0 OID 0)
-- Dependencies: 227
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 3, true);


--
-- TOC entry 3482 (class 2606 OID 19110)
-- Name: buttons buttons_name_button_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.buttons
    ADD CONSTRAINT buttons_name_button_key UNIQUE (name_button);


--
-- TOC entry 3484 (class 2606 OID 19108)
-- Name: buttons buttons_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.buttons
    ADD CONSTRAINT buttons_pkey PRIMARY KEY (button_id);


--
-- TOC entry 3486 (class 2606 OID 19117)
-- Name: buttons_to_button buttons_to_button_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.buttons_to_button
    ADD CONSTRAINT buttons_to_button_pkey PRIMARY KEY (buttons_to_button_id);


--
-- TOC entry 3494 (class 2606 OID 19470)
-- Name: content_to_button content_to_button_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.content_to_button
    ADD CONSTRAINT content_to_button_pkey PRIMARY KEY (content_to_button_id);


--
-- TOC entry 3490 (class 2606 OID 19446)
-- Name: description description_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.description
    ADD CONSTRAINT description_pkey PRIMARY KEY (description_id);


--
-- TOC entry 3492 (class 2606 OID 19453)
-- Name: file_to_description file_to_description_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.file_to_description
    ADD CONSTRAINT file_to_description_pkey PRIMARY KEY (file_to_description_id);


--
-- TOC entry 3488 (class 2606 OID 19439)
-- Name: files files_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.files
    ADD CONSTRAINT files_pkey PRIMARY KEY (row_id);


--
-- TOC entry 3496 (class 2606 OID 19492)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3498 (class 2606 OID 19494)
-- Name: users users_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_user_id_key UNIQUE (user_id);


--
-- TOC entry 3499 (class 2606 OID 19118)
-- Name: buttons_to_button buttons_to_button_button_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.buttons_to_button
    ADD CONSTRAINT buttons_to_button_button_id_fkey FOREIGN KEY (button_id) REFERENCES public.buttons(button_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3500 (class 2606 OID 19123)
-- Name: buttons_to_button buttons_to_button_button_id_to_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.buttons_to_button
    ADD CONSTRAINT buttons_to_button_button_id_to_fkey FOREIGN KEY (button_id_to) REFERENCES public.buttons(button_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3503 (class 2606 OID 19471)
-- Name: content_to_button content_to_button_button_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.content_to_button
    ADD CONSTRAINT content_to_button_button_id_fkey FOREIGN KEY (button_id) REFERENCES public.buttons(button_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3504 (class 2606 OID 19476)
-- Name: content_to_button content_to_button_file_to_description_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.content_to_button
    ADD CONSTRAINT content_to_button_file_to_description_id_fkey FOREIGN KEY (file_to_description_id) REFERENCES public.file_to_description(file_to_description_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3501 (class 2606 OID 19459)
-- Name: file_to_description file_to_description_description_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.file_to_description
    ADD CONSTRAINT file_to_description_description_id_fkey FOREIGN KEY (description_id) REFERENCES public.description(description_id);


--
-- TOC entry 3502 (class 2606 OID 19454)
-- Name: file_to_description file_to_description_row_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.file_to_description
    ADD CONSTRAINT file_to_description_row_id_fkey FOREIGN KEY (row_id) REFERENCES public.files(row_id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2024-02-27 20:56:37 MSK

--
-- PostgreSQL database dump complete
--

