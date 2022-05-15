# diabetes-ml
* Analysis of sensor data from my freestyle libre sensor, and insulin pump settings
* I don't really know what will become of this project, but maybe I can extract some meaningful trends?
* Data from: https://www.libreview.com/glucosereports and https://carelink.minimed.eu/app/reports
* Can only seem to get around 5 months of data from carelink, more available?

# Data cleaning and variable explorations
## Libre ideas
* is_rising, is_falling, is_stable var: gradient of last n(=what?) results

## Pump ideas
* Cleanup BG results with overlay of libre?
* bolus readings, convert into equivalent carbs?
	* Insulin sensitivity changes over time
* Forward fill basal rates, so we always have the current basal rate as a data point

# To-do and ideas
* Are the libre and pump BG distributions statistically similar?
	* I would expect not, but the question is how different are they
* Compare BG distributions around:
	* different days (weekend/weekday)
	* different times of day (breakfast, lunch, dinner)
	* overnight
	* after a _large_ bolus
* Can we use these factors to predict a low/high?
	* Define thresholds for these
* Low/high prediction, based on BG readings for last 30 mins?
