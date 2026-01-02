#! /bin/bash
# Retrieves monthly statistics from BigQuery and saves it as a CSV.
rm -f monthly_summary.csv
DATAFOLDER=../data
DATASET='covid-project-481605:covid.monthly_summary'
BUCKET_URL='gs://deiwuz_covid/monthly_summary.csv'
bq extract $DATASET $BUCKET_URL
echo starting to copy monthly_summary.csv to $DATAFOLDER
mkdir -p $DATAFOLDER
gcloud storage cp $BUCKET_URL $DATAFOLDER
echo monthly_summary.csv copied to $DATAFOLDER