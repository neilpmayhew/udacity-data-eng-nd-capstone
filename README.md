# Capstone project for udacity data engineering nanodegree

## Project Scope and Goals
I have a keen interest in weightlifting and recently came across a great resource for international Power Lifting results. The data comes in the form of a rather unwieldy single csv file. This file will make up the bulk of the data for this project and will seek other source with which to enrich this.

The project goal is to produce a data model that will allow the end user to slice, dice and aggregate the various Powerlifting meet results to gain insights. For example to find the heaviest squat, bench and eadlift within each weight class, which lifter has the heaviest deadlift of all time etc.

## Data Sources

main csv: https://github.com/sstangl/openpowerlifting-static/raw/gh-pages/openpowerlifting-latest.zip

PL Federation details scraped from: https://www.powerliftingwatch.com/compare-federations using pandas read_html() function


