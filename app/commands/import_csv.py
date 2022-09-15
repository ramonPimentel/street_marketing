from app.use_cases.import_street_marketing_from_csv import ImportStreetMarketingFromCSV

ImportStreetMarketingFromCSV(
  file_path='/src/DEINFO_AB_FEIRASLIVRES_2014.csv'
).execute()