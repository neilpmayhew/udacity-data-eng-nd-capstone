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
end) as weight_class_kg
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
,LEAD(weight_class_kg)OVER(PARTITION BY federation_meet_key ORDER BY weight_class_kg) weight_class_to_exclusive
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
  CONVERT(smallint,COALESCE(NULLIF(SPLIT_PART(AgeClass,'-',1),''),'0')) age_class_from
, CONVERT(smallint,COALESCE(NULLIF(SPLIT_PART(AgeClass,'-',2),''),'0')) age_class_to
FROM public.staging_oplmain_deduplicated
""")
    birth_year_class_table_insert=("""
SELECT DISTINCT 
  CONVERT(smallint,COALESCE(NULLIF(SPLIT_PART(BirthYearClass,'-',1),''),'0')) birth_year_class_from
, CONVERT(smallint,COALESCE(NULLIF(SPLIT_PART(BirthYearClass,'-',2),''),'0')) birth_year_class_to
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
    
    