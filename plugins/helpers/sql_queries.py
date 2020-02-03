class SqlQueries:
    staging_oplmain_dedupe_insert=("""
SELECT DISTINCT Name, Sex, Event, Equipment, Age, AgeClass, BirthYearClass, Division, BodyweightKg, WeightClassKg, Squat1Kg, Squat2Kg, Squat3Kg, Squat4Kg, Best3SquatKg, Bench1Kg, Bench2Kg, Bench3Kg, Bench4Kg, Best3BenchKg, Deadlift1Kg, Deadlift2Kg, Deadlift3Kg, Deadlift4Kg, Best3DeadliftKg, TotalKg, Place, Wilks, McCulloch, Glossbrenner, IPFPoints, Tested, Country, Federation, Date, MeetCountry, MeetState, MeetName, md5(
   COALESCE(date,'')
|| COALESCE(Federation,'')
|| COALESCE(meetname,'')
|| COALESCE(event,'')
) federation_meet_key, CONVERT(float,case
    when REPLACE(trim(weightclasskg),'+','') ~ '^[0-9\.]+$' then trim(weightclasskg)
    else null 
end) as weight_class_kg,
CONVERT(smallint,COALESCE(NULLIF(SPLIT_PART(AgeClass,'-',1),''),'0')) age_class_from,
CONVERT(smallint,COALESCE(NULLIF(SPLIT_PART(AgeClass,'-',2),''),'0')) age_class_to,
CONVERT(smallint,COALESCE(NULLIF(SPLIT_PART(BirthYearClass,'-',1),''),'0')) birth_year_class_from,
CONVERT(smallint,COALESCE(NULLIF(SPLIT_PART(BirthYearClass,'-',2),''),'0')) birth_year_class_to
FROM public.staging_oplmain;
""")    
    staging_weight_class_table_insert=("""
SELECT DISTINCT federation_meet_key
, weight_class_kg
FROM public.staging_oplmain_deduplicated
WHERE weight_class_kg IS NOT NULL
""")
    weight_class_table_insert=("""
SELECT federation_meet_key
,weight_class_kg weight_class_from_inclusive
,COALESCE(LEAD(weight_class_kg)OVER(PARTITION BY federation_meet_key ORDER BY weight_class_kg),999) weight_class_to_exclusive
FROM staging_oplmain_weight_class
""")
    lifter_table_insert = ("""
SELECT DISTINCT 
  Name
, Sex
FROM public.staging_oplmain_deduplicated;
    """)
    age_class_table_insert=("""
SELECT DISTINCT 
  age_class_from
, age_class_to
FROM public.staging_oplmain_deduplicated
""")
    birth_year_class_table_insert=("""
SELECT DISTINCT 
  birth_year_class_from
, birth_year_class_to
FROM public.staging_oplmain_deduplicated
""")
    federation_meet_table_insert=("""
SELECT DISTINCT
   federation_meet_key
  ,federation federation_code
  ,meetname meet_name
  ,event meet_event_type
  ,division meet_division
  ,meetstate meet_state
  ,meetcountry meet_country
  ,CONVERT(BOOLEAN,CASE tested WHEN 'Yes' THEN 1 WHEN 'No' THEN 0 END) meet_tested
  ,equipment meet_equipment
FROM staging_oplmain_deduplicated
""")
    federation_table_insert=("""
SELECT federation federation_code
, division
,  bench_shirts_plies
,  bench_shirts_material
,  lifting_suits_plies
,  lifting_suits_material
,  CASE lifting_suits_brief WHEN 'Yes' THEN 1 ELSE 0 END lifting_suits_brief
,  CASE mono WHEN 'Yes' THEN 1 ELSE 0 END mono
,  CASE test WHEN 'Yes' THEN 1 ELSE 0 END test
FROM staging_federation
""")
    date_table_insert=("""
SELECT DISTINCT TO_DATE (date, 'yyyy-MM-dd')  date_value
, EXTRACT(day from TO_DATE (date, 'yyyy-MM-dd')) day_value
, EXTRACT(week from TO_DATE (date, 'yyyy-MM-dd')) week_value
, EXTRACT(month from TO_DATE (date, 'yyyy-MM-dd')) month_value
, EXTRACT(year from TO_DATE (date, 'yyyy-MM-dd')) year_value
, EXTRACT(weekday from TO_DATE (date, 'yyyy-MM-dd')) weekday_value
FROM staging_oplmain_deduplicated
""")
    meet_result_table_insert=("""
SELECT    o.federation_meet_key,
  wc.weight_class_key,
  l.lifter_key,
  ac.age_class_key,
  bc.birth_year_class_key,
  TO_DATE (o.date, 'yyyy-MM-dd') meet_date,
  o.BodyWeightKg body_weight_kg,
  o.Age age,
  o.Squat1Kg squat_1_kg,
  o.Squat2Kg squat_2_kg,
  o.Squat3Kg squat_3_kg,
  o.Squat4Kg squat_4_kg,
  o.Best3SquatKg best_3_squat_kg,
  o.Bench1Kg bench_1_kg,
  o.Bench2Kg bench_2_kg,
  o.Bench3Kg bench_3_kg,
  o.Bench4Kg bench_4_kg,
  o.Best3BenchKg best_3_bench_kg,
  o.Deadlift1Kg deadlift_1_kg,
  o.Deadlift2Kg deadlift_2_kg,
  o.Deadlift3Kg deadlift_3_kg,
  o.Deadlift4Kg deadlift_4_kg,
  o.Best3DeadliftKg best_3_deadlift_kg,
  o.TotalKg total_kg,
  o.Wilks wilks,
  o.Mcculloch mcculloch,
  o.GlossBrenner gloss_brenner,
  o.IPFPoints ipf_points
FROM public.staging_oplmain_deduplicated o
LEFT JOIN public.weight_class wc
ON wc.federation_meet_key = o.federation_meet_key
AND o.weight_class_kg >= wc.weight_class_from_inclusive
AND o.weight_class_kg < wc.weight_class_to_exclusive
LEFT JOIN public.lifter l
ON l.name = o.Name
AND l.Sex = o.Sex
LEFT JOIN public.age_class ac
ON ac.age_class_from = o.age_class_from
AND ac.age_class_to = o.age_class_to
LEFT JOIN public.birth_year_class bc
ON bc.birth_year_class_from = o.birth_year_class_from
AND bc.birth_year_class_to = o.birth_year_class_to
""")
    
    