def get_data_quality_queries():
    
    data_quality_queries = {}
    
    tables_to_check = ['public.staging_federation','public.staging_oplmain','public.staging_oplmain_deduplicated','public.staging_oplmain_weight_class'
                       ,'public.weight_class','public.lifter','public.age_class','public.birth_year_class','public.federation_meet','public.federation'
                       ,'public.date','public.meet_result']
    
    for table_name in tables_to_check:
        data_quality_queries[f'{table_name}_has_rows'] = f"SELECT COUNT(*) row_count FROM {table_name};"
        
    return data_quality_queries