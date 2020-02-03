# Capstone project for udacity data engineering nanodegree

## Project Scope and Goals
I have a keen interest in weightlifting and recently came across a great resource for international Power Lifting results. The data comes in the form of a rather unwieldy single csv file. This file will make up the bulk of the data for this project and will seek other source with which to enrich this.

The project goal is to produce a data model that will allow the end user to slice, dice and aggregate the various Powerlifting meet results to gain insights. For example to find the heaviest squat, bench and eadlift within each weight class, which lifter has the heaviest deadlift of all time etc.

## Technology Choices

### Redshift
I have chosen to use AWS's Redshift database for this problem. Redshift has the following advantages:

1. It is an extremely powerful, horizontally scaleable, cloud based data warehouse
2. It will facilitate the creation of a dimensional model allowing the slicing, dicing and grouping of the data required
3. Will enable an ELT style of architecture. Simple COPY command will stage the data into staging table in the database then the power of Redshift will be transform and load the data all within Redshift itself making the code simpler to write and easier to maintain.

### Apache airflow
I am using Airflow to build the data pipeline which has the following advantages:
1. Able to build reusable operators in python code to facilitate the staging and transformation of data
2. A plethora hooks to interface with external platforms including Redshift which will make the operators simple to write
3. Tasks (such stage data into a table or transform and load a dimension) are easily declared and configured using configuration-as-code in python
4. Task dependencies and relationships are easily declared allowing Airflow to honour these dependencies and parallel execute as appropriate
5. Airflow includes a full featured schedulier

## Addressing Future Scenarios/Requirements

If the data was increassed 100x I would still use Redshift which is more than capable of handling such volumes. Redshift is horizontally scaleable so extra nodes can easily be added when needed. This scalebility also gives Redshift the ability to support 100+ concurrent users with ease.

If the need to run daily at 7 am were to arise this would be no problem for the airflow pipeline which is able to support a schedule such as this. Currently the main dataset is not available at this frequency so a source that could provide this would need to be found.

## Data Sources

main csv: https://github.com/sstangl/openpowerlifting-static/raw/gh-pages/openpowerlifting-latest.zip

PL Federation details scraped from: https://www.powerliftingwatch.com/compare-federations using pandas read_html() function

## Data Exploration

Data exploration was conducted using jupyter notebooks and pandas. Please see data-exploration-opl.ipynb and data-exploration-federdation.ipynb for documentation of this process and findings.

## Data Model



