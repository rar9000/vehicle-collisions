# vehicle-collisions

Data analysis of vehicle collisions from 2019-2020 for Jefferson County Kentucky 
Data was extracted from http://crashinformationky.org/AdvancedSearch

I analyzed vehicle collision data to better understand the specific locations, times and circumstances that existed when a vehicle collision in Jefferson County Kentucky occured. One of the biggest factors for exploring this data was to see how the frequency of collisions declined during the covid-19 shutdown of 2020 as there were presumably less drivers on the road. To get a sense for this change I compared crash data from 2019 to crash data from 2020. In addition to this I also combined the two years to explore overall collision trends. I compiled a list of questions with answers to represent my findings below.

Implemented features:
1. Read in multiple data files
2. Cleaned data and performed a pandas merge
3. Made 5 visualizations to display my data
4. Utilized a virtual environment (see requirements.txt file)
5. Annotated code with markdown cells in Jupyter Notebooks

To run my program create a virtual environment and install the requirements. Then start with the cleaning scripts and progress through them sequentially 1-5. If error occurs restart over at 1.

I have jupyter notebooks you can open to see how I came to my conclusions. One for exploring raw data, one dedicated to overall analysis, one for covid comparison and finally one to represent my findings visually.

Questions and answers

- Q:Overall collisions for 2019-2020?
- A: 48,005

- Q: Total number of deaths?
- A: 217

- Q: Roads with most collisions?
- A: Dixie, Bardstown, Shelbyville

- Q: Deadliest roads?
- A: Dixie, I64 W, Preston

- Q: Intersection with most collisions?
- A: 7th Street and Hill Street 

-Q: What make and model of vehicle is involved in the most collisions?
-A: Toyota Camry

- Q: Most common weather condition for collision?
- A: Clear

- Q: Most common weather when collision results in a death?
- A: Clear (Snow almost a non factor)

- Q: How many cars typically involved in a collision? 
- A: Typically at least two vehicles involved and only one involved coming in 2nd  

- Q: Most cars involved in a collision?
- A: On two occasions 8 vehicles involved in a single collision 

Covid 

- Q: How many collisions before covid from March 16, 2019 - December 31, 2019
- (Gov. Andy Beshear implemented Covid restrictions beginning March 16, 2020)
- A: 26,418 collisions

- Q: How many collisions during covid from March 16, 2020 - December 31, 2020
- A: 9,487 collisions

- Q: What percentage did collisions drop during Covid?
- A: 54%

- Q: What days of the week had the most and least collisions before Covid?
- A: most - Friday 4,497 
   - least - Sunday 2,545
- Q: Percent change?
- A: 55%

- Q: Worst time to drive for Friday before Covid?
- A: 5:00-6:00pm (rush hour!)

- Q: What days of the week had the most and least collisions during Covid?
- A: most - Friday 1,496 
   - least - Sunday 1,227
- Q: Percent change?
- A: 20% (much smaller change) 

- Q: Worst time to drive for Friday during Covid?
- A: 5:00-6:00pm (rush hour again!)








