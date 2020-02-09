# meet_result
  meet_result_key, integer, not nullable - autoincrementing identity, primary key
  federation_meet_key, character, not nullable
  weight_class_key, integer, nullable
  lifter_key, integer, not nullable
  age_class_key, integer, nullable
  birth_year_class_key, integer, nullable
  meet_date, date, not nullable
  body_weight_kg, double precision, nullable
  age, smallint, nullable
  squat_1_kg, double precision, nullable
  squat_2_kg, double precision, nullable
  squat_3_kg, double precision, nullable
  squat_4_kg, double precision, nullable
  best_3_squat_kg, double precision, nullable
  bench_1_kg, double precision, nullable
  bench_2_kg, double precision, nullable
  bench_3_kg, double precision, nullable
  bench_4_kg, double precision, nullable
  best_3_bench_kg, double precision, nullable
  deadlift_1_kg, double precision, nullable
  deadlift_2_kg, double precision, nullable
  deadlift_3_kg, double precision, nullable
  deadlift_4_kg, double precision, nullable
  best_3_deadlift_kg, double precision, nullable
  total_kg, double precision, nullable
  wilks, double precision, nullable
  mcculloch, double precision, nullable
  gloss_brenner, double precision, nullable
  ipf_points, double precision, nullable
# age_class
dimension table:- represents an age class for a meet e.g. from 20-39 years of age
  age_class_key, integer, not nullable - autoincrementing identity, primary key
  age_class_from, smallint, not nullable - lower boundary, inclusive for the age class
  age_class_to, smallint, not nullable - upper boundary, inclusive for the age class
birth_year_class
dimension table:- represents a birth class for a meet e.g. from 1990-2039 
  birth_year_class_key, integer, not nullable - autoincrementing identity, primary key
  birth_year_class_from, smallint, not nullable - lower boundary, inclusive for the birth year class
  birth_year_class_to, smallint, not nullable - upper boundary, inclusive for the birth year class
# date
  date_value, date, not nullable - date, primary key
  day, small integer, not nullable - integer day of the month 
  week, small integer, not nullable - integer week number 1-52
  month, small integer, not nullable - integer month
  year, small integer, not nullable - integer year
  weekday, small integer, not nullable - integer day of week 1-7
# federation
  federation_code, character varying, not nullable - autoincrementing identity, primary key
  division, character varying, not nullable
  bench_shirts_plies, character varying, not nullable
  bench_shirts_material, character varying, not nullable
  lifting_suits_plies, character varying, not nullable
  lifting_suits_material, character varying, not nullable
  lifting_suits_brief, boolean, not nullable
  mono, boolean, nullable
  test, boolean, nullable
# federation_meet
  federation_meet_key, character, not nullable - primary key, an MD5 hash of key fields for a federation meet
  federation_code, character varying, not nullable
  meet_name, character varying, not nullable
  meet_event_type, character varying, not nullable
  meet_division, character varying, not nullable
  meet_state, character varying, not nullable
  meet_country, character varying, not nullable
  meet_tested, boolean, nullable
  meet_equipment, character varying, nullable
# lifter
  lifter_key, integer, not nullable - autoincrementing identity, primary key
  name, character varying, not nullable
  sex, character, not nullable
# weight_class
  weight_class_key, integer, not nullable
  federation_meet_key, character, not nullable
  weight_class_from_inclusive, smallint, not nullable
  weight_class_to_exclusive, smallint, not nullable
