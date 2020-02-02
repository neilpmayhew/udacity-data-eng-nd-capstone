class SqlQueries:
    staging_oplmain_dedupe_insert=("""
SELECT DISTINCT Name, Sex, Event, Equipment, Age, AgeClass, BirthYearClass, Division, BodyweightKg, WeightClassKg, Squat1Kg, Squat2Kg, Squat3Kg, Squat4Kg, Best3SquatKg, Bench1Kg, Bench2Kg, Bench3Kg, Bench4Kg, Best3BenchKg, Deadlift1Kg, Deadlift2Kg, Deadlift3Kg, Deadlift4Kg, Best3DeadliftKg, TotalKg, Place, Wilks, McCulloch, Glossbrenner, IPFPoints, Tested, Country, Federation, Date, MeetCountry, MeetState, MeetName
FROM public.staging_oplmain;
""")
    lifter_table_insert = ("""
SELECT DISTINCT 
  Name
, Sex
FROM public.staging_oplmain;
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
    federation_table_insert=("""
SELECT DISTINCT
federation
FROM staging_oplmain_deduplicated
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
    weight_class_table_insert=("""
SELECT DISTINCT date,Federation,meetname,event,WeightClassKg,
LEAD(WeightClassKg)OVER(PARTITION BY date,Federation,meetname,event ORDER BY WeightClassKg) WeightClassKgto
FROM staging_oplmain_deduplicated
ORDER BY date,Federation,meetname,event,WeightClassKg
""")