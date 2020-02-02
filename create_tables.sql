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
,Age float NULL
,AgeClass VARCHAR(256) NULL
,BirthYearClass VARCHAR(256) NULL
,Division VARCHAR(256) NULL
,BodyweightKg float NULL
,WeightClassKg VARCHAR(256) NULL
,Squat1Kg float NULL
,Squat2Kg float NULL
,Squat3Kg float NULL
,Squat4Kg float NULL
,Best3SquatKg float NULL
,Bench1Kg float NULL
,Bench2Kg float NULL
,Bench3Kg float NULL
,Bench4Kg float NULL
,Best3BenchKg float NULL
,Deadlift1Kg float NULL
,Deadlift2Kg float NULL
,Deadlift3Kg float NULL
,Deadlift4Kg float NULL
,Best3DeadliftKg float NULL
,TotalKg float NULL
,Place VARCHAR(256) NULL
,Wilks float NULL
,McCulloch float NULL
,Glossbrenner float NULL
,IPFPoints float NULL
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
,Age float NULL
,AgeClass VARCHAR(256) NULL
,BirthYearClass VARCHAR(256) NULL
,Division VARCHAR(256) NULL
,BodyweightKg float NULL
,WeightClassKg VARCHAR(256) NULL
,Squat1Kg float NULL
,Squat2Kg float NULL
,Squat3Kg float NULL
,Squat4Kg float NULL
,Best3SquatKg float NULL
,Bench1Kg float NULL
,Bench2Kg float NULL
,Bench3Kg float NULL
,Bench4Kg float NULL
,Best3BenchKg float NULL
,Deadlift1Kg float NULL
,Deadlift2Kg float NULL
,Deadlift3Kg float NULL
,Deadlift4Kg float NULL
,Best3DeadliftKg float NULL
,TotalKg float NULL
,Place VARCHAR(256) NULL
,Wilks float NULL
,McCulloch float NULL
,Glossbrenner float NULL
,IPFPoints float NULL
,Tested VARCHAR(256) NULL
,Country VARCHAR(256) NULL
,Federation VARCHAR(256) NULL
,Date VARCHAR(256) NULL
,MeetCountry VARCHAR(256) NULL
,MeetState VARCHAR(256) NULL
,MeetName VARCHAR(256) NULL
,federation_meet_key CHAR(32) NOT NULL
);
DROP TABLE IF EXISTS public.staging_oplmain_weight_class;
CREATE TABLE public.staging_oplmain_weight_class(
 federation_meet_key CHAR(32) NOT NULL
,weight_class_kg FLOAT NOT NULL
);

DROP TABLE IF EXISTS public.weight_class;
CREATE TABLE public.weight_class(
  weight_class_key int IDENTITY(1,1) NOT NULL PRIMARY KEY ,
  federation_meet_key CHAR(32) NOT NULL UNIQUE,
  weight_class_from_inclusive smallint NULL,
  weight_class_to_exclusive smallint NULL
);

DROP TABLE IF EXISTS lifter;
CREATE TABLE public.lifter(
  lifter_key int IDENTITY (1,1) NOT NULL PRIMARY KEY,
  Name VARCHAR(256),
  Sex CHAR(2) NOT NULL
);

DROP TABLE IF EXISTS public.age_class;
CREATE TABLE public.age_class(
  age_key int IDENTITY(1,1) NOT NULL PRIMARY KEY,
  age_class_from smallint NULL,
  age_class_to smallint NULL
);


DROP TABLE IF EXISTS public.birth_year_class;

CREATE TABLE public.birth_year_class(
  birth_year_class_key int IDENTITY(1,1) NOT NULL PRIMARY KEY,
  birth_year_class_from smallint null,
  birth_year_class_to smallint null
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
  federation_code VARCHAR(256) PRIMARY KEY,
  division VARCHAR(256),
  bench_shirts_plies VARCHAR(256),
  bench_shirts_material VARCHAR(256),
  lifting_suits_plies VARCHAR(256),
  lifting_suits_material VARCHAR(256),
  lifting_suits_brief BOOLEAN,
  mono BOOLEAN,
  test BOOLEAN
);
DROP TABLE IF EXISTS public.date;
CREATE TABLE public.date (
    date_value DATE NOT NULL, 
    day int NOT NULL, 
    week int NOT NULL, 
    month int NOT NULL, 
    year int NOT NULL, 
    weekday int NOT NULL,
    CONSTRAINT date_pkey PRIMARY KEY (date_value)
);

DROP TABLE IF EXISTS meet_result;
CREATE TABLE public.meet_result(
  meet_result_key int NOT NULL,
  federation_meet_key CHAR(32) NOT NULL,
  weight_class_key int  NOT NULL,
  lifter_key int NOT NULL,
  meet_date date NOT NULL,
  BodyweightKg float NOT NULL,
  Age smallint NULL,
  Squat1Kg float NOT NULL,
  Squat2Kg float NOT NULL,
  Squat3Kg float NOT NULL,
  Squat4Kg float NOT NULL,
  Best3SquatKg float NOT NULL,
  Bench1Kg float NOT NULL,
  Bench2Kg float NOT NULL,
  Bench3Kg float NOT NULL,
  Bench4Kg float NOT NULL,
  Best3BenchKg float NOT NULL,
  Deadlift1Kg float NOT NULL,
  Deadlift2Kg float NOT NULL,
  Deadlift3Kg float NOT NULL,
  Deadlift4Kg float NOT NULL,
  Best3DeadliftKg float NOT NULL,
  TotalKg float NOT NULL,
  Wilks float NOT NULL,
  McCulloch float NOT NULL,
  Glossbrenner float NOT NULL,
  IPFPoints float NOT NULL
);
