# Hypo prediction
* Can I use a sequence of libre readings to predict a hypo?
* Start with simple LSTM model
* Have libre readings from 2019
* Later, would want to add basal and pump data (boluses, food, over-corrections from high BG readings, etc)
* Only have 90 days of pump data, with very limited bolus info, hard to develop anything
* Can I get more data from my medtronic website?


## How to define a hypo?
* Threshold BG value
* data['reading'] < value = hypo
* Dataset is probably going to be very imbalanced!
* How to deal with biasing time ordering with this labelling?

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
