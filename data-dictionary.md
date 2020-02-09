age_class
  age_class_key, integer, NO
  age_class_from, smallint, NO
  age_class_to, smallint, NO
birth_year_class
  birth_year_class_key, integer, NO
  birth_year_class_from, smallint, NO
  birth_year_class_to, smallint, NO
date
  date_value, date, NO
  day, integer, NO
  week, integer, NO
  month, integer, NO
  year, integer, NO
  weekday, integer, NO
federation
  federation_code, character varying, NO
  division, character varying, NO
  bench_shirts_plies, character varying, NO
  bench_shirts_material, character varying, NO
  lifting_suits_plies, character varying, NO
  lifting_suits_material, character varying, NO
  lifting_suits_brief, boolean, NO
  mono, boolean, YES
  test, boolean, YES
federation_meet
  federation_meet_key, character, NO
  federation_code, character varying, NO
  meet_name, character varying, NO
  meet_event_type, character varying, NO
  meet_division, character varying, NO
  meet_state, character varying, NO
  meet_country, character varying, NO
  meet_tested, boolean, YES
  meet_equipment, character varying, YES
lifter
  lifter_key, integer, NO
  name, character varying, NO
  sex, character, NO
meet_result
  meet_result_key, integer, NO
  federation_meet_key, character, NO
  weight_class_key, integer, YES
  lifter_key, integer, NO
  age_class_key, integer, YES
  birth_year_class_key, integer, YES
  meet_date, date, NO
  body_weight_kg, double precision, YES
  age, smallint, YES
  squat_1_kg, double precision, YES
  squat_2_kg, double precision, YES
  squat_3_kg, double precision, YES
  squat_4_kg, double precision, YES
  best_3_squat_kg, double precision, YES
  bench_1_kg, double precision, YES
  bench_2_kg, double precision, YES
  bench_3_kg, double precision, YES
  bench_4_kg, double precision, YES
  best_3_bench_kg, double precision, YES
  deadlift_1_kg, double precision, YES
  deadlift_2_kg, double precision, YES
  deadlift_3_kg, double precision, YES
  deadlift_4_kg, double precision, YES
  best_3_deadlift_kg, double precision, YES
  total_kg, double precision, YES
  wilks, double precision, YES
  mcculloch, double precision, YES
  gloss_brenner, double precision, YES
  ipf_points, double precision, YES
weight_class
  weight_class_key, integer, NO
  federation_meet_key, character, NO
  weight_class_from_inclusive, smallint, NO
  weight_class_to_exclusive, smallint, NO
