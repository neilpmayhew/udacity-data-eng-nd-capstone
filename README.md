# Capstone project for udacity data engineering nanodegree

## Project Scope and Goals
https://www.openpowerlifting.org/ is a superb resource for international Power Lifting results. The web interface is limited to simple filters and the download for the data comes in the form of a single, rather unwieldy single csv file.

The project goal is to produce a data model that will allow the end user to slice, dice and aggregate the various Powerlifting meet results to allow analysis and gain insights. For example to find the heaviest squat, bench and deadlift within each weight class, which lifter has the heaviest deadlift of all time etc.

The file will make up the bulk of the data for this project and I will seek other source with which to enrich this dataset.

## Technology Choices

### Redshift
I have chosen to use AWS's Redshift database for this problem. Redshift has the following advantages:

1. It is an extremely powerful, horizontally scaleable, cloud based data warehouse
2. It will facilitate the creation of a dimensional model allowing the slicing, dicing and grouping of the data required
3. Enables an ELT style of architecture. Simple COPY commands can stage the data into staging tables in the database then the massively power processing power of Redshift can be used to transform and load the data all within Redshift itself. This leads to a performant solution with simple code that is easier to write and maintain.

### Apache airflow
I am using Airflow to build the data pipeline which has the following advantages:
1. Able to build reusable operators in python code to facilitate the staging and transformation of data
2. A plethora hooks to interface with external platforms including Redshift which will make the operators simple to write
3. Tasks (such stage data into a table or transform and load a dimension) are easily declared and configured using configuration-as-code in python
4. Task dependencies and relationships are easily declared allowing Airflow to honour these dependencies and parallel execute as appropriate
5. Airflow includes a full featured scheduler

## Addressing Future Scenarios/Requirements

If the data was increassed 100x I would still use Redshift which is more than capable of handling such volumes. Redshift is horizontally scaleable so extra nodes can easily be added when needed. This scalebility also gives Redshift the ability to support 100+ concurrent users with ease.

If the need to run daily at 7 am were to arise this would be no problem for the airflow pipeline which is able to support a schedule such as this. Currently the main dataset is not available at this frequency so a source that could provide this would need to be found.

## Data Sources

main csv: https://github.com/sstangl/openpowerlifting-static/raw/gh-pages/openpowerlifting-latest.zip

PL Federation details scraped from: https://www.powerliftingwatch.com/compare-federations using pandas read_html() function

## Data Exploration

Data exploration was conducted using jupyter notebooks and pandas. Please see data-exploration-opl.ipynb and data-exploration-federdation.ipynb for documentation of this process and findings.

## Data Model

### Fact table: meet_result
In a powerlifting meet a lifter has 3 attempts at each of the 3 lifts, 3 squat, 3 bench and 3 deadlift. The highest number from each lift are added together to form a total. A single meet_result record represent an instance of a lifter's result for a meet on a specific date, for a federation within whatever classes and equipment restrictions that are applicable to that meet.

### Dimension tables
the dimension tables have been chosen to allow the end user to aggregate, slice and data the meet_result data for example highest totalling female lifter within a specific weight range for a specific federation.

#### AgeClass and BirthYearClass
In Powerlifting competition these fields are ranges that may or may not be standard across the different federation. To make analysis easier the text hyphenated ranges were each split into two numeric values a from and a to value. As the ranges are not necessarily standardised the from and to values and be used in queries across the ranges overlaps to produce aggregates not easily available with the data in its native form
#### WeightClass
Weight class are actually ranges similar to AgeClass and BirthYearClass above but it is the convention to write them as just the lower boundary leaving the reader to infer the upper boundary for example a meet might have the following weight class 56, 63, 78, 95, 100, 110+. Again these are not standardised and to facilitate range overlap queries we use window function to produce a from inclusive and and a tor exclusive range value e.g. [56,63), [63,78),[78,95),[100,110),[110,999) (note that as per standard mathmatical notation square brackets denote inclusive, parenthesis exclusive).

