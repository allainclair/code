## Code challenge

This is a code challenge to create a REST API that makes requests to
[LibreView](https://www.libreview.com/) and it returns glucose values given
a date interval.

Example:
```
request:
/glucose?start_date=2022-04-20&end_date=2022-04-25

response:
{"data":
  [
    {
      "glucose_average":6.2,
      "glucose_max":6.9,
      "date_start":"2022-04-20T21:00:00",
      "date_end":"2022-04-21T21:00:00",
      "patient_id":"3f5e19e1-d667-11ea-a179-0242ac110007"
    },
    {
      "glucose_average":6.3,
      "glucose_max":6.8,
      "date_start":"2022-04-21T21:00:00",
      "date_end":"2022-04-22T21:00:00",
      "patient_id":"3f5e19e1-d667-11ea-a179-0242ac110007"
    },
    {
      "glucose_average":6.3,
      "glucose_max":7.6,
      "date_start":"2022-04-22T21:00:00",
      "date_end":"2022-04-23T21:00:00",
      "patient_id":"3f5e19e1-d667-11ea-a179-0242ac110007"
    },
    ...
  ]
```

## Requirements and running app

1. Install [PDM](https://pdm.fming.dev/latest/) to manage the packages.

2. Run `pdm instsall`.

3. Create the `.env` file with the credentials given.
See `.env-example` for email/password.

4. `pdm run start` starts the Web/FastAPI server.

## Requests for the server

There is a manual step to make the requests to the server to work.
The first time a request is made we need to input manually the
**security code** sent to the credential email. Please input the code in
the web server terminal of the command `pdm run start` after making a valid 
first request to the server. `Email Code >` message will be waiting for the code.

There will be probably some "Exceptions" in the web server logged to stdio.
But they are just cases where there is no data for a specific date.

## Test

[Pytest](https://docs.pytest.org/) is necessary to run the tests.

`pdm run pytest` to run the tests. Some tests will need the **security code** to 
be run
 
## Suggestion of improvements

* Apply async to the webserver.
* Remove the manual step for the security code.
* Bypass captcha from `https://api-eu.libreview.io/patients/<patiend_id>/export`
  * The CSV data from this URL seems to be the best data format to get data from.
  * If the previous doesn't work, we can try `https://api-eu.libreview.io/reports`. But
    I don't see a good way of parsing the data from the "PDF/SVG" formats here. A
    lot of time was expended here.
  * If the previous doesn't work we should improve the calls to the
    `'https://api-eu.libreview.io/patients/glucoseHistory?from=<from_date>&numPeriods=<num_periods>&period=<period>'`
    trying to avoid many calls to this URL. We have some 'blocks' list fields
    that I didn't understand the meaning of them.
* Cache data as suggested (SQLite for example) to avoid getting
  repeated data from LibreView.
* Mock external/IO requests for the tests.

## Questions and suggestions?

Please email me at: allainclair@gmail.com
