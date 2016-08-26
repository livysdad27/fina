# Fina
Welcome to Fina, the personal analyzer.

[![Build Status](https://travis-ci.org/livysdad27/fina.svg?branch=master)](https://travis-ci.org/livysdad27/fina)

[![Coverage Status](https://coveralls.io/repos/github/livysdad27/fina/badge.svg)](https://coveralls.io/github/livysdad27/fina)

#API Spec
Base URL
/v1

GET
/transactions - Show list of transactions 
/transactions/id - Show a particular transaction 

Filters/Sorts
  graph?graphtype
  table?sortby
  startdate?enddate

PUT
/transactions - import set of transactions/dedup 
/transactions/id - Import a particular transaction/dedup 

POST
/transactions - update categories for a set of transactions 
/transactions/id - update a category for a single transaction 

Parameters
  payee
  category  
  startdate?enddate
