DROP TABLE IF EXISTS public.staging_federation;
CREATE TABLE public.staging_federation(
  federation VARCHAR(256),
  division VARCHAR(256),
  bench_shirts_plies VARCHAR(256),
  bench_shirts_material VARCHAR(256),
  lifting_suits_plies VARCHAR(256),
  lifting_suits_material VARCHAR(256),
  lifting_suits_brief VARCHAR(256),
  mono VARCHAR(256),
  test VARCHAR(256)
);
DROP TABLE IF EXISTS public.staging_oplmain;
CREATE TABLE public.staging_oplmain(
Name VARCHAR(256) NULL
,Sex VARCHAR(256) NULL
,Event VARCHAR(256) NULL
,Equipment VARCHAR(256) NULL
,Age FLOAT NULL
,AgeClass VARCHAR(256) NULL
,BirthYearClass VARCHAR(256) NULL
,Division VARCHAR(256) NULL
,BodyweightKg FLOAT NULL
,WeightClassKg VARCHAR(256) NULL
,Squat1Kg FLOAT NULL
,Squat2Kg FLOAT NULL
,Squat3Kg FLOAT NULL
,Squat4Kg FLOAT NULL
,Best3SquatKg FLOAT NULL
,Bench1Kg FLOAT NULL
,Bench2Kg FLOAT NULL
,Bench3Kg FLOAT NULL
,Bench4Kg FLOAT NULL
,Best3BenchKg FLOAT NULL
,Deadlift1Kg FLOAT NULL
,Deadlift2Kg FLOAT NULL
,Deadlift3Kg FLOAT NULL
,Deadlift4Kg FLOAT NULL
,Best3DeadliftKg FLOAT NULL
,TotalKg FLOAT NULL
,Place VARCHAR(256) NULL
,Wilks FLOAT NULL
,McCulloch FLOAT NULL
,Glossbrenner FLOAT NULL
,IPFPoINTs FLOAT NULL
,Tested VARCHAR(256) NULL
,Country VARCHAR(256) NULL
,Federation VARCHAR(256) NULL
,Date VARCHAR(256) NULL
,MeetCountry VARCHAR(256) NULL
,MeetState VARCHAR(256) NULL
,MeetName VARCHAR(256) NULL
);

DROP TABLE IF EXISTS public.staging_oplmain_deduplicated;
CREATE TABLE public.staging_oplmain_deduplicated(
Name VARCHAR(256) NULL
,Sex VARCHAR(256) NULL
,Event VARCHAR(256) NULL
,Equipment VARCHAR(256) NULL
,Age FLOAT NULL
,AgeClass VARCHAR(256) NULL
,BirthYearClass VARCHAR(256) NULL
,Division VARCHAR(256) NULL
,BodyweightKg FLOAT NULL
,WeightClassKg VARCHAR(256) NULL
,Squat1Kg FLOAT NULL
,Squat2Kg FLOAT NULL
,Squat3Kg FLOAT NULL
,Squat4Kg FLOAT NULL
,Best3SquatKg FLOAT NULL
,Bench1Kg FLOAT NULL
,Bench2Kg FLOAT NULL
,Bench3Kg FLOAT NULL
,Bench4Kg FLOAT NULL
,Best3BenchKg FLOAT NULL
,Deadlift1Kg FLOAT NULL
,Deadlift2Kg FLOAT NULL
,Deadlift3Kg FLOAT NULL
,Deadlift4Kg FLOAT NULL
,Best3DeadliftKg FLOAT NULL
,TotalKg FLOAT NULL
,Place VARCHAR(256) NULL
,Wilks FLOAT NULL
,McCulloch FLOAT NULL
,Glossbrenner FLOAT NULL
,IPFPoINTs FLOAT NULL
,Tested VARCHAR(256) NULL
,Country VARCHAR(256) NULL
,Federation VARCHAR(256) NULL
,Date VARCHAR(256) NULL
,MeetCountry VARCHAR(256) NULL
,MeetState VARCHAR(256) NULL
,MeetName VARCHAR(256) NULL
,federation_meet_key CHAR(32) NOT NULL
,weight_class_kg FLOAT NULL
,age_class_from SMALLINT NOT NULL
,age_class_to SMALLINT NOT NULL
,birth_year_class_from SMALLINT NOT NULL
,birth_year_class_to SMALLINT NOT NULL
);
DROP TABLE IF EXISTS public.staging_oplmain_weight_class;
CREATE TABLE public.staging_oplmain_weight_class(
 federation_meet_key CHAR(32) NOT NULL
,weight_class_kg FLOAT NOT NULL
);

DROP TABLE IF EXISTS public.weight_class;
CREATE TABLE public.weight_class(
  weight_class_key INT IDENTITY(1,1) NOT NULL PRIMARY KEY ,
  federation_meet_key CHAR(32) NOT NULL UNIQUE,
  weight_class_from_inclusive SMALLINT NOT NULL,
  weight_class_to_exclusive SMALLINT NOT NULL
);

DROP TABLE IF EXISTS lifter;
CREATE TABLE public.lifter(
  lifter_key INT IDENTITY (1,1) NOT NULL PRIMARY KEY,
  Name VARCHAR(256) NOT NULL,
  Sex CHAR(2) NOT NULL
);

DROP TABLE IF EXISTS public.age_class;
CREATE TABLE public.age_class(
  age_class_key INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  age_class_from SMALLINT NOT NULL,
  age_class_to SMALLINT NOT NULL
);


DROP TABLE IF EXISTS public.birth_year_class;

CREATE TABLE public.birth_year_class(
  birth_year_class_key INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
  birth_year_class_from SMALLINT NOT NULL,
  birth_year_class_to SMALLINT NOT NULL
  );

DROP TABLE IF EXISTS federation_meet;
CREATE TABLE public.federation_meet(
  federation_meet_key CHAR(32) NOT NULL PRIMARY KEY,
  federation_code VARCHAR(20) NOT NULL,
  meet_name VARCHAR(256) NOT NULL,
  meet_event_type VARCHAR(50) NOT NULL,
  meet_division VARCHAR(50) NOT NULL,
  meet_state VARCHAR(256) NOT NULL,
  meet_country VARCHAR(256) NOT NULL,
  meet_tested BOOLEAN NULL,
  meet_equipment VARCHAR(100) NULL
 );
 
 DROP TABLE IF EXISTS federation;
 CREATE TABLE public.federation(
  federation_code VARCHAR(256) NOT NULL PRIMARY KEY,
  division VARCHAR(256) NOT NULL,
  bench_shirts_plies VARCHAR(256) NOT NULL,
  bench_shirts_material VARCHAR(256) NOT NULL,
  lifting_suits_plies VARCHAR(256) NOT NULL,
  lifting_suits_material VARCHAR(256) NOT NULL,
  lifting_suits_brief BOOLEAN NOT NULL,
  mono BOOLEAN,
  test BOOLEAN
);
DROP TABLE IF EXISTS public.date;
CREATE TABLE public.date (
    date_value DATE NOT NULL, 
    day SMALLINT NOT NULL, 
    week SMALLINT NOT NULL, 
    month SMALLINT NOT NULL, 
    year SMALLINT NOT NULL, 
    weekday SMALLINT NOT NULL,
    CONSTRAINT date_pkey PRIMARY KEY (date_value)
);

DROP TABLE IF EXISTS public.meet_result;
CREATE TABLE public.meet_result(
  meet_result_key INT IDENTITY(1,1) NOT NULL,
  federation_meet_key char(32) NOT NULL,
  weight_class_key INT  NULL,
  lifter_key INT NOT NULL,
  age_class_key INT NULL,
  birth_year_class_key INT NULL,
  meet_date date NOT NULL,
  body_weight_kg FLOAT NULL,
  age SMALLINT NULL,
  squat_1_kg FLOAT NULL,
  squat_2_kg FLOAT NULL,
  squat_3_kg FLOAT NULL,
  squat_4_kg FLOAT NULL,
  best_3_squat_kg FLOAT NULL,
  bench_1_kg FLOAT NULL,
  bench_2_kg FLOAT NULL,
  bench_3_kg FLOAT NULL,
  bench_4_kg FLOAT NULL,
  best_3_bench_kg FLOAT NULL,
  deadlift_1_kg FLOAT NULL,
  deadlift_2_kg FLOAT NULL,
  deadlift_3_kg FLOAT NULL,
  deadlift_4_kg FLOAT NULL,
  best_3_deadlift_kg FLOAT NULL,
  total_kg FLOAT NULL,
  place_numeric SMALLINT NULL,
  place VARCHAR(10) NULL,
  wilks FLOAT  NULL,
  mcculloch FLOAT NULL,
  gloss_brenner FLOAT NULL,
  ipf_points FLOAT  NULL
);
