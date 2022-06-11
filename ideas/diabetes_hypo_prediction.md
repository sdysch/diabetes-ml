# Hypo prediction
* Can I use a sequence of libre readings to predict a hypo?
* Start with simple LSTM model
* Have libre readings from 2019
* Later, would want to add basal and pump data (boluses, food, over-corrections from high BG readings, etc)
* Only have 90 days of pump data, with very limited bolus info, hard to develop anything
* Can I get more data from my medtronic website?
	* Using pump data also assumes a relationship between BG/food/insulin sensitivity/etc that does not change
	* I know this assumption is invalid
* These relationships will differ between person to person
	* Using libre-only data would allow for a "person-agnostic" model


## How to define a hypo?
* Threshold BG value
* data['reading'] < value = hypo
* Dataset is probably going to be very imbalanced!
* How to deal with biasing time ordering with this labelling?

## Models
* Baseline: RandomForest/BRT with lag variables
* LSTM (+CNN for smoothing?)
* Transformer encoders: https://keras.io/examples/timeseries/timeseries_transformer_classification/

## Misc
* When creating lookbacks, ensure that I don't skip over a period where I wasn't wearing the sensor

## Variable ideas
* Can I replicate the libre "arrows"?
	* positive/negative gradient ---> is BG increasing/decreasing? At what rate (mmol/L per timestep)?
* Use absolute BG values, or *difference* since previous reading? Similar to previous point -- idea is how quickly is BG changing?
* Time since last hypo?
* Time since mealtime?
* Is morning/afternoon/evening
* 

## Extensions
* 3-way classification, is_low, is_high, is_ok?

## TODO
* Drop rate features?
* Drop diff features, turn into is_decreasing/is_stable/is_increasing bools (with sensible threshold)
* What is a sensible threshold?

## Random thoughts
* Will lagged_hypo variables be skewed by overnight hypos that I missed/slept through?
	* Something to evaluate in a later model validation step

# Extensions
* LogisticRegression:
	* Probability that I will have a hypo
