
# Client Project: Estimating Economic Impact of Hurricanes

## Purpose

**Assess the economic impact of hurricanes using ARIMA time series modeling**
> For this project, we decided to look at Hurricane Harvey and Hurricane Rita and how they affected regions in Texas to carry out our analysis

## Collaborators
> Grace Campbell:                https://www.linkedin.com/in/gracecampbell4/
>
> Kevin Kim:                     https://www.linkedin.com/in/kkim0817/ 
>
> CJ Warner:                     https://www.linkedin.com/in/christopher-c-j-warner-51559911/
>
> Marie Downer 

## Methodology
> 1. Gather the data
> 2. Explore/analyze the data
> 3. Model the data
> 4. Make conclusions/give recommendations

> ### 1. Gather the Data
> - **US Department of Commerce, Bureau of Economic Analysis (BEA)**:
>   - Gross Domestic Product, Population, Personal Income (County Level - Annual)
> - **US Department of Labor**:  
>   - Unemployment Insurance Claims Data (State Level - Weekly)
> - **Texas Labor Market Information**:  
>   - Quarterly Census of Employment and Wages (State/County - Quarterly/Monthly)
>      - Construction Employment (County - Quarterly/Monthly)
> - **Federal Emergency Management Agency (FEMA)**:  
>   - Individual Assistance Housing Registrants Large Disasters (County - Per Storm)

> ### 2. Explore/Analyze the Data
> ![image](materials/fig2.png)
> ![image](materials/fig1.png)

> ### 3. Model the Data
> Our overall strategy was to compare the actual post-hurricane trajectory of economic indicators to a predicted trajectory of those indicators based on pre-hurricane data. In other words, what would the economy look like if that hurricane never happened?
>
> We used the difference between the predicted values and the actual values to quantify the effect of the hurricane on those indicators.
>
> We chose a seasonal ARIMA model to forecast the hypothetical values of our economic indicators. We modeled: 
> - Weekly unemployment insurance initial claims (statewide)
> - Monthly employment in the construction industry (by county)
>    - We modeled on the three counties with the highest dollar amount in damage for each hurricane
>
> ![image](materials/fig3.png)
> ![image](materials/fig4.png)
> ![image](materials/fig5.png)

> ### 4. Make Conclusions/Give Recommendations
> **Practical Implications**
> - National government programs/actions:
>    - Fallout and disbursement of funds for hazard and flood mitigation
>    - Areas of focus for government programs (i.e. employment)
>    - Predictive budget allocation to areas that will be impacted more heavily
> - Texas-specific actions:
>    - Using the unemployment data that we have, use the model as a basis to prepare for possible employment displacement  during future hurricanes
>
> **Limitations**
> - Data
>   - Empirical evidence of difficulty in data scraping
>   - Granularity (annual vs monthly vs weekly)
>   - Housing (Zillow)
> - Economic Measures
>   - No aggregate way to indicate “economic loss”
> - Limited in scope
>   - Looking at unemployment, employment, and wages does not begin to cover the entirety of economic factors impacted by a disaster
>
> **Next Steps**
> - Formulate an economic loss indicator to more accurately and holistically measure economic loss (economics degree?)
> - Time-series model tuning
>   - Hyperparameters (naive)
>   - Seasonality component (P,D,Q)
> - County data aggregation method
>   - Find a way to aggregate economic measures (i.e. weighted system) to target just the counties that were heavily affected by a specific disaster
> - Investigate different regions / different disasters




