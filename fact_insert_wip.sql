SELECT    o.federation_meet_key,
  wc.weight_class_key,
  o.weight_class_kg,
  l.lifter_key,
  ac.age_class_key,
  0 birth_year_class_key,
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
JOIN public.age_class ac
ON 
WHERE wc.weight_class_key IS NULL
LIMIT 20;

