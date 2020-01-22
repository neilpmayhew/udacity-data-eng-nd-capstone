# Capstone project for udacity data engineering nanodegree

## Project Scope and Goals
I have a keen interest in weightlifting and recently came across a great resource for international Power Lifting results. The data comes in the form of a rather unwieldy single csv file. This file will make up the bulk of the data for this project and will seek other source with which to enrich this.

The project will utilise Apache airflow to schedule and run the data pipeline producing a Redshift dimensional model that will allow the end user to slice, dice and aggregate the various Powerlifting meet results as they see fit.

## Data Source

main csv: https://github.com/sstangl/openpowerlifting-static/raw/gh-pages/openpowerlifting-latest.zip

PL Federation details scrapped from: https://www.powerliftingwatch.com/compare-federations
