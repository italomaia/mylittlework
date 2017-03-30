# Programming test

For backend application developer

## Objective

To estimate the learning skills, experience, quality of development of the
candidate using a simple real world example and software libraries that are
in use at Mylittlejob.

## Requirements

* The test result must be complete
* It should be developed using Python (ideally 3.4+), optionally using a web framework
* A requirements file for Python pip should exist for easy installation of dependencies
* Result should be submitted as a Git repository (github.com, ideally public)
* Result should be submitted by 20:00 (local time) on the same day the test was scheduled

## Judging process

We will look at the completeness of the assignment, code quality, structure,
modularity and documentation of the code. If there is an accompanying readme
file to setup the project, this will be a plus point.

## Test

* Using the given HTML template, create a simple music browser utilizing the Spotify search Web API
* The user should be able to choose the “Filter” option from the top navigation bar.
* You may convert the filter to a simple <select> dropdown
* When user selects a filter and types a search term, the backend should make request to the Spotify API (you may use Python Requests library)
* Parse the results (use Python simplejson if you like) from Spotify and generate the page with these results
* The “Counter” should show the count of results returned from Spotify API
* Search results should contain 64x64 thumbnail beside them whenever available (as in the HTML template)
* Pagination is not needed
* Feel free to use the existing HTML we have given (you may use any templating language like Django Templates or Jinja2)
