# Quantified Self

## A Personal Data Aggregator and Dashboard for Self-Trackers, Life-Loggers, and Quantified Self Enthusiasts

The project has several goals: 

* To facilitate easier data tracking (and hoarding).
* To **download all of your personal data** from various tracking services (see below for list of integration services) and store locally. 
* To provide the starting point for **personal data analysis, data visualization, and a personal data dashboard**. 

At present, the main objective is to provide working data downloaders and simple data analysis for each of the integrated modules. 

Some initial work has been started on using these data streams for predictive analytics and forecasting using Machine Learning and Artificial Intelligence, and the intention to increasingly focus on modeling in future iterations.

This particular repo is a mix and match from several different sources, *heavily* influenced by [Mark Koester](https://github.com/markwk) and his [qs_ledger](https://github.com/markwk/qs_ledger).
The fitbit downloader was heavily influenced by [Arpan Ghosh](https://github.com/arpanghosh8453) and his [Fitbit Analyzer](https://github.com/arpanghosh8453/programs/tree/master/Fitbit%20Data%20Analyzer). 

Most of the modules are in the format: 
* \<module>_**downloader**.ipynb, where you can download the data from the relevant source if applicable, and either an 
* \<module>_**analysis**.ipynb, with basic data analysis using either matplotlib/seaborn, or [plotly](https://plotly.com/), and/or a
* \<module>_**dash**.ipynb, which is generally more in depth analysis through a dashboard visualizer with [plotly-dash](https://dash.plotly.com/).
* **data**, where the data can be stored, generally in .csv format, though some of modules require a credentials.json for authentication.

This repo is a work in progress and there are many bad practices because I'm still learning. Most of the modules have a lot of my exploratory analysis throughout and are filled with outdated cells that I just commented out after I got whatever I wanted working. Generally, if you insert your own data in the beginning of the notebook (and it's in the right form, depending on the module) and run through the cells, it should output a chart or graph or dashboard using your data in a relatively pretty or readable manner.

### Current Modules: 

* [Dashboard](https://github.com/mcwaage1/qs/tree/master/dashboard): A basic dashboard example that I put on [pythonanywhere.com](http://mcwaage1.pythonanywhere.com/)
* [Fitbit](https://github.com/mcwaage1/qs/tree/master/fitbit): Fitness and health tracking and analysis of steps, sleep, and heart rate from a Fitbit wearable. More in depth Fitness analysis/collection planned, e.g. training/workout regimen performed every week.
* [GoodReads](https://github.com/mcwaage1/qs/tree/master/goodreads): Tracking books read over time and data analysis for GoodReads.
* [Google Sheets](https://github.com/mcwaage1/qs/tree/master/google_sheets): Get data from any Google Sheet.
* [Last.fm](https://github.com/mcwaage1/qs/tree/master/lastfm): Music tracking and analysis of music listening history from Last.fm.
* [Mood](https://github.com/mcwaage1/qs/tree/master/mood): Mental health and pain tracking and analysis, mostly based on the [Hamilton Depression Rating Scale](https://qxmd.com/calculate/calculator_146/hamilton-depression-rating-scale-ham-d-or-hdrs).
* [Time](https://github.com/mcwaage1/qs/tree/master/time): Time and activity tracking and analysis. The data was collected manually with [aTimeLogger](http://www.atimelogger.com/).
* [Writing](https://github.com/mcwaage1/qs/tree/master/writing): Writing/word tracking and analysis. Data manually entered in google sheet with plans to automate more of the process.

### Planned Future Modules:

* [RescueTime](https://www.rescuetime.com/): Track computer usage and analyze computer activities and time use with RescueTime. 
* [Health/Fitness](): Temperature, blood pressure, respirations, blood sugar, blood panel, gut/mouth bacteria panel, etc.
* [Food](): Calories, macronutrients, vitamins, caffeine, water consumption, etc.
* [Money/Finances/Investing/Retirement Planning/Crypto](): How my finances have (hopefully) improved over time, how they relate to other modules.
* [Weather/Sunlight](): How the weather/daylight savings/hours of sunlight in day/phases of the  moon affects my mood, if at all.
* [Combined Data Analysis](): Do each of the above module correlate with each other at all? E.g. On days I spend more or less time doing some activity, does my mood improve, etc. 
* [ML](): To improve mood/health/finances/time spent doing things you want and less on what you don't/etc.

### EXAMPLES: 

* [Combine and Merge Personal Data into Unified Data Frame](https://github.com/mcwaage1/qs/blob/master/fitbit/2020fitbit-data-project/zerotopandas-course-project.ipynb): This example notebook, from a course I took from [Jovian.ai](https://jovian.ai/learn/data-analysis-with-python-zero-to-pandas) (that actually got me started on my programming and data science and analytics journey) combines and analyzes my Fitbit and Mood data into several different charts, tables, and graphs showing how those might be related to eachother.

* Time spent programming in 2020 as a github style heatmap dashboard:
![Timeline/activity Dashboard](https://github.com/mcwaage1/qs/blob/master/images/programming_heatmap.gif)

* Timeline/activity dashboard of all my time spent in 2020:
![Github style heatmap](https://github.com/mcwaage1/qs/blob/master/images/activity_timeline.gif)

### Code / Dependencies: 

* The code is written in Python 3 (so far). 
* Shared and distributed primarily through Jupyter Notebooks (.ipynb's). 
* Most services depend on [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/) for data manipulation and [Plotly](https://plotly.com/) for data analysis and visualization. 
* For initial installation and setup help, see documentation below. 
* For setup and usage of individual services, see documentation provided by each integration.

#### Installation and Setup Locally:

If you want to create something similar, feel free to use whichever pieces you see fit.

Honestly I copy-pasted the portions of whichever portion of a file I needed from other people, though I suppose you could clone it as well. Either way, you probably should enable a virtual environment:

If you haven't already then you should: 

`mkdir <repo_name, e.g. qs>`, otherwise,

`cd <repo_name>`

`python3 -m venv <virtual_environment_name, e.g. venv>`

`source <virtual_environment_name>/bin/activate`

Using your activated virtual environment (in front of your username in the terminal it should say something like: `(<virtual_environment_name>) <username>@<username>:`, install dependencies: 

`pip install -r requirements.txt`

Then navigate into your directory and launch an individual notebook or the full project with jupyter notebook or jupyter lab: 

`jupyter-lab`

### Useful Libraries/Resources:

* [Plotly-Dash](https://dash.plotly.com/)
* [Jupyter-dash](https://github.com/plotly/jupyter-dash)
* [Jovian.ai](https://jovian.ai/learn/data-analysis-with-python-zero-to-pandas)
* [Awesome-QuantifiedSelf](https://github.com/woop/awesome-quantified-self)
* [QuantifiedSelf subreddit](https://old.reddit.com/r/QuantifiedSelf/)

#### Thanks: 

* [Mark Koester](https://github.com/markwk/) and his [blog](http://www.markwk.com/).
* [Arpan Ghosh](https://github.com/arpanghosh8453)

### Me:

Hey, I'm Matt, and I'm a grad student in Data Science and Analytics. This is my main hobby project and what got me into programming and data science and analytics in the first place. This is mostly a space for me to learn and explore, but also something I want to expand, improve, and productionize, so that anybody could easily use it and do their own data analysis on themselves to try and improve their lives. 

In the future I plan on making a blog/portfolio site and having more in depth analysis and how-to's. That will be at https://www.waage.dev (eventually)

## Questions? Bugs? Feature Requests? Suggestions?

Post a ticket in [QS Issue Queue](https://github.com/mcwaage1/qs/issues) 

**Want to help?** Fork the project and provide your own data analysis, integration, etc.