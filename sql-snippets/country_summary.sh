#! /bin/bash
# Retrieves country-level summary data from BigQuery and saves it as a CSV.
rm -f country_summary.csv
DATAFOLDER=../data
DATASET='covid-project-481605:covid.country_summary'
BUCKET_URL='gs://deiwuz_covid/country_summary.csv'
bq extract $DATASET $BUCKET_URL
echo starting to copy country_summary.csv to $DATAFOLDER
mkdir -p $DATAFOLDER
gcloud storage cp $BUCKET_URL $DATAFOLDER
echo monthly_summary.csv copied to $DATAFOLDER