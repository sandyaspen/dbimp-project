DROP TABLE public.onektup;

CREATE TABLE public.onektup
(
    unique1 integer NOT NULL,
    unique2 integer NOT NULL,
    two integer NOT NULL,
    four integer NOT NULL,
    ten integer NOT NULL,
    twenty integer NOT NULL,
    one_percent integer NOT NULL,
    ten_percent integer NOT NULL,
    twenty_percent integer NOT NULL,
    fifty_percent integer NOT NULL,
    unique3 integer NOT NULL,
    even_one_percent integer NOT NULL,
    odd_one_percent character(52) COLLATE pg_catalog."default" NOT NULL,
    stringu1 character(52) COLLATE pg_catalog."default" NOT NULL,
    stringu2 character(52) COLLATE pg_catalog."default" NOT NULL,
    string4 character(52) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT onektup_pkey PRIMARY KEY (unique2)
);


DROP TABLE public.tenktup1;

CREATE TABLE public.tenktup1
(
    unique1 integer NOT NULL,
    unique2 integer NOT NULL,
    two integer NOT NULL,
    four integer NOT NULL,
    ten integer NOT NULL,
    twenty integer NOT NULL,
    one_percent integer NOT NULL,
    ten_percent integer NOT NULL,
    twenty_percent integer NOT NULL,
    fifty_percent integer NOT NULL,
    unique3 integer NOT NULL,
    even_one_percent integer NOT NULL,
    odd_one_percent character(52) COLLATE pg_catalog."default" NOT NULL,
    stringu1 character(52) COLLATE pg_catalog."default" NOT NULL,
    stringu2 character(52) COLLATE pg_catalog."default" NOT NULL,
    string4 character(52) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT tenktup1_pkey PRIMARY KEY (unique2)
);

DROP TABLE public.tenktup2;

CREATE TABLE public.tenktup2
(
    unique1 integer NOT NULL,
    unique2 integer NOT NULL,
    two integer NOT NULL,
    four integer NOT NULL,
    ten integer NOT NULL,
    twenty integer NOT NULL,
    one_percent integer NOT NULL,
    ten_percent integer NOT NULL,
    twenty_percent integer NOT NULL,
    fifty_percent integer NOT NULL,
    unique3 integer NOT NULL,
    even_one_percent integer NOT NULL,
    odd_one_percent character(52) COLLATE pg_catalog."default" NOT NULL,
    stringu1 character(52) COLLATE pg_catalog."default" NOT NULL,
    stringu2 character(52) COLLATE pg_catalog."default" NOT NULL,
    string4 character(52) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT tenktup2_pkey PRIMARY KEY (unique2)
);

