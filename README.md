# Python Plausible stats

This repo contains the data from the [Plausible](https://plausible.io/) 
analytics trial for the [docs.python.org](https://docs.python.org) website, which ran for 30 days
ending on 2023-08-10.

Data:

* `2023-08-10-1925/` - JSON data downloaded via the Plausible API
* `2023-08-10-1925-combined/` - the same data combined into single files

Scripts:

* `plausible-get.py` - was used to download the data, requires a [token](https://plausible.io/settings)
* `plausible-process.py` - an example you can edit to process data

See also:

* https://discuss.python.org/t/docs-metrics-trial-with-plausible/28896
