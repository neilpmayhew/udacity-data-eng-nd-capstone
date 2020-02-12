# meet_result
  meet_result_key, integer, not nullable - autoincrementing identity, primary key
  federation_meet_key, character, not nullable, an MD5 hash of key fields for a federation meet, join to federation_meet dimension table
  weight_class_key, integer, nullable, joins to weight_class dimension table
  lifter_key, integer, not nullable, joins to lifter dimension table
  age_class_key, integer, nullable, joins to age_class dimension table
  birth_year_class_key, integer, nullable, joins to birth_year_class dimension table
  meet_date, date, not nullable, joins to date dimension table
  body_weight_kg, double precision, nullable, lifter's body weight in kilos for the meet
  age, smallint, nullable, lifters age for the meet
  squat_1_kg, double precision, nullable, weight in kg of first squat attempt (for a failing atttempt the attempted weight is multiplied by -1)
  squat_2_kg, double precision, nullable, weight in kg of second squat attempt (for a failing atttempt the attempted weight is multiplied by -1)
  squat_3_kg, double precision, nullable, weight in kg of third squat attempt (for a failing atttempt the attempted weight is multiplied by -1)
  squat_4_kg, double precision, nullable, weight in kg of fourth squat attempt (for a failing atttempt the attempted weight is multiplied by -1)
  best_3_squat_kg, double precision, nullable, highest squat weight successfully achieved
  bench_1_kg, double precision, nullable, weight in kg of first bench press attempt (for a failing atttempt the attempted weight is multiplied by -1)
  bench_2_kg, double precision, nullable, weight in kg of second bench press attempt (for a failing atttempt the attempted weight is multiplied by -1)
  bench_3_kg, double precision, nullable, weight in kg of third bench press attempt (for a failing atttempt the attempted weight is multiplied by -1)
  bench_4_kg, double precision, nullable, weight in kg of fourth bench press attempt (for a failing atttempt the attempted weight is multiplied by -1)
  best_3_bench_kg, double precision, nullable, highest bench press weight successfully achieved 
  deadlift_1_kg, double precision, nullable, weight in kg of first deadlift attempt (for a failing atttempt the attempted weight is multiplied by -1)
  deadlift_2_kg, double precision, nullable, weight in kg of second deadlift attempt (for a failing atttempt the attempted weight is multiplied by -1)
  deadlift_3_kg, double precision, nullable, weight in kg of third deadlift attempt (for a failing atttempt the attempted weight is multiplied by -1)
  deadlift_4_kg, double precision, nullable, weight in kg of fourth deadlift attempt (for a failing atttempt the attempted weight is multiplied by -1)
  best_3_deadlift_kg, double precision, nullable, highest bench press weight successfully achieved
  total_kg, double precision, nullable,summation of highest weight achieved in each lift 
  wilks, double precision, nullable, wilks coeffient which measures strength of lifter despite their body weight
  mcculloch, double precision, nullable, mccullock coefficient measuring strength allowing for age. Used for masters or older lifters
  gloss_brenner, double precision, nullable, coeffient for strength allowing for body weight an alternative to wilks
  ipf_points, double precision, nullable, an alternative coeffient used by the ipf
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
  federation_code, character varying, not nullable - code for the federation, joins to federation.federation_code
  meet_name, character varying, not nullable
  meet_event_type, character varying, not nullable. 1-3 characters representing the lifts at the meet S = Squat, B = Bench Press, D = Deadlift
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
  weight_class_from_inclusive, smallint, not nullable - inclusive lower boundary for the weight class
  weight_class_to_exclusive, smallint, not nullable - exclusive upper boundary for the weight class
