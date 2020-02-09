age_class
  age_class_key, integer, not nullable
  age_class_from, smallint, not nullable
  age_class_to, smallint, not nullable
birth_year_class
  birth_year_class_key, integer, not nullable
  birth_year_class_from, smallint, not nullable
  birth_year_class_to, smallint, not nullable
date
  date_value, date, not nullable
  day, integer, not nullable
  week, integer, not nullable
  month, integer, not nullable
  year, integer, not nullable
  weekday, integer, not nullable
federation
  federation_code, character varying, not nullable
  division, character varying, not nullable
  bench_shirts_plies, character varying, not nullable
  bench_shirts_material, character varying, not nullable
  lifting_suits_plies, character varying, not nullable
  lifting_suits_material, character varying, not nullable
  lifting_suits_brief, boolean, not nullable
  mono, boolean, nullable
  test, boolean, nullable
federation_meet
  federation_meet_key, character, not nullable
  federation_code, character varying, not nullable
  meet_name, character varying, not nullable
  meet_event_type, character varying, not nullable
  meet_division, character varying, not nullable
  meet_state, character varying, not nullable
  meet_country, character varying, not nullable
  meet_tested, boolean, nullable
  meet_equipment, character varying, nullable
lifter
  lifter_key, integer, not nullable
  name, character varying, not nullable
  sex, character, not nullable
meet_result
  meet_result_key, integer, not nullable
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
weight_class
  weight_class_key, integer, not nullable
  federation_meet_key, character, not nullable
  weight_class_from_inclusive, smallint, not nullable
  weight_class_to_exclusive, smallint, not nullable
