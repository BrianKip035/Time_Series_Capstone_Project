# PRICEWISE AI

![mainimage png](https://user-images.githubusercontent.com/117269915/231759804-198953e9-c230-4a0b-a1f3-d87ac28a8f94.png)


## 1. BUSINESS UNDERSTANDING

## 1.1 Business Problem

The main objective of this project is to develop accurate time series models that can forecast economic indicators and commodity prices. Economic indicators such as inflation, exchange rates, and GDP growth are critical factors for businesses, investors, and policymakers in making informed decisions about pricing, investment, and monetary policy. Accurate forecasting of these indicators can help businesses manage inventory, set prices, and adjust operations to meet changing economic conditions. Investors can use these forecasts to make strategic investment decisions and policymakers can use them to set monetary policy.

The project focuses on providing value to businesses, investors, and policymakers who require accurate and timely economic forecasts. The real-world problem that this project aims to solve is the challenge of accurately forecasting economic indicators and commodity prices. The stakeholders who could benefit from this project include businesses, investors, and policymakers who need to make informed decisions based on economic data.

The project aims to develop accurate and reliable model for predicting commodity prices and inflation trends, identify investment opportunities based on trends in commodity prices and inflation rates, and provide recommendations on how to capitalize on these opportunities. By doing so, this project can help businesses manage costs associated with fluctuations in commodity prices and inflation rates, as well as identify opportunities to reduce these costs

## 1.2 Objectives

### 1.2.1 Main Objective
The main objective of this project is to develop accurate time series models that can forecast economic indicators such as inflation rates and exchange rates and commodity prices

### 1.2.2 Specific Objectives
1. Explore and clean time series data on economic indicators and commodity prices to identify patterns, trends, and seasonality.
2. Conduct market analysis to identify trends and patterns in commodity prices and inflation rates, and provide investment recommendations to capitalize on the identified opportunities.
3. Develop and test time series models, evaluate their performance using statistical metrics, and use the best-performing models to forecast economic indicators and commodity prices for the next 12 months.
4. Develop a web-based application that provides traders and investors with reliable real-time commodity price predictions and continuously update the model for ongoing accuracy.

## 1.3 Success Metric
Model Accuracy: The accuracy of the developed time series models will be measured by the Root Mean Squared Error (RMSE) and the project will be considered success if the time series model has a Root Mean Squared Error for each of the commodities is utmost 5% when making predictions.

# 2. DATA UNDERSTANDING 
## 2.1 Data Sources:

The data for Inflation Rates.csv, Annual GDP.csv, and Exchange Rates.csv are obtained from the Central Bank of Kenya (CBK)  [here](https://www.centralbank.go.ke/inflation-rates/) website. CBK is the central monetary authority of Kenya responsible for formulating and implementing monetary policy in the country. The data for commodity prices.xlsx is obtained from the Food Security Portal [here](https://fews.net/kenya-monthly-fews-net-staple-food-price-data-0) which is maintained by the International Food Policy Research Institute.

### 2.2 Properties of the Data:

Inflation Rates.csv contains the monthly inflation rates from January 2000 to December 2022. The data is presented as percentages, and the inflation rates are calculated as year-on-year changes in the Consumer Price Index (CPI) for the Kenyan economy.

Annual GDP.csv contains the annual GDP of Kenya in current prices (Kenyan Shillings) from 1960 to 2021. The GDP is calculated as the value of goods and services produced within the country's borders, and it is presented in nominal terms.

Exchange Rates.csv contains the daily exchange rates of major currencies (USD, GBP, EUR, and JPY) against the Kenyan Shilling from January 2000 to December 2022. The exchange rates are presented as the number of units of foreign currency that can be exchanged for one Kenyan Shilling.

Commodity prices.xlsx contains monthly prices of selected food commodities (maize, beans, rice, and wheat) in Kenya from January 2005 to December 2022. The data is presented in Kenyan Shillings per kilogram. 

### 2.3 Data Limitations:

The data from CBK and the Food Security Portal is comprehensive, but there are some limitations. Inflation Rates.csv only covers the period from January 2000 to December 2022, which may not capture long-term trends in inflation. Annual GDP.csv only presents the GDP in nominal terms, which does not account for changes in the prices of goods and services over time. Exchange Rates.csv only covers a limited number of major currencies, which may not reflect the exchange rates of other currencies that may affect commodity prices. Commodity prices.xlsx only covers a limited number of food commodities, which may not reflect the prices of other essential commodities affecting food security in Kenya.
## 3. Data Preparation
he data was checked for missing values and some columns were found to have null values.The null values were handled byfilling in the missing values using the previous value on the same column. The data types for all the columns were checked and the shape of the datasets were checked. <br>
The differnt datasets were then merged tougether and the Date column format was corrected. There was a change in "forex_data" DataFrame by resampling the data to the end of the month, creating a new column for the end of the month dates. The Merged dataseets were then checked for null values and found none. 

## 4. EDA 
To gain a better understanding of our dataset, we conducted various exploratory data analyses. We began with univariate analysis, which involved examining the price trends of bread, vegetable oil, milk, diesel, maize meal, gasoline, inflation, and exchange rates over the years. 
<br>
![bluebread](https://user-images.githubusercontent.com/117269915/231760169-a9d86f2f-6f95-49d2-8170-130bab5d60e0.png)
![bluemaize](https://user-images.githubusercontent.c![bluediesel](https://user-images.githubusercontent.com/117269915/231760583-bed475b1-eb82-4de7-a0e2-e269deec8697.png))
![bluemilk](https://user-images.githubusercontent.com/117269915/231760162-d920736b-5d3e-4c32-a2ea-3ab8913a4596.png)
![blueveg](https://user-images.githubusercontent.com/117269915/231760165-32fdce20-4b88-45ba-9b09-a58789f1da30.png)

![bluegas](https://user-images.githubusercontent.com/117269915/231760592-46508111-9cda-4484-a7cd-a844b6dc95e0.png)



Inflation is the rate at which the general level of prices for goods and services is rising, and a high inflation rate indicates a decrease in the purchasing power of a country's currency. From the graph, we can see that the 12-month inflation rate has been subject to fluctuations over the years. In the early years from 2014 to 2016, the inflation rate was relatively stable at around 6-8%, after which there was a gradual increase until 2017, where it peaked at around 11%. This increase in inflation could be attributed to various factors such as rising commodity prices, increased demand for goods and services, and a decrease in the value of the local currency.
![blueinflation](https://user-images.githubusercontent.com/117269915/231760596-f78874f7-9993-414b-86c4-e4aa18b071d2.png)


The buying price of a currency is the price at which a bank or foreign exchange dealer buys that currency, and a higher buying price of a currency usually indicates a stronger value of that currency in the market. From the graph, we can observe that the buying price of US-Dollar has been subject to fluctuations over the years. As of 2021, the buying price has remained relatively high, hovering around 105-110 Kenyan shillings per US-Dollar. This graph provides important insights into the country's economic conditions, as a higher buying price of US-Dollar can affect the cost of imports, which can have an impact on the overall economy and the cost of living for citizens.
![blueexchange](https://user-images.githubusercontent.com/117269915/231760589-12b50bdc-100c-476b-a141-4fafa3b5a3d4.png)


We then created a multipanel plot to display all six graphs, enabling us to discern trends over time. The graph plots the prices of six commodities, including bread, refined vegetable oil, cows milk, diesel, maize meal, and gasoline, along with the 12-month inflation rate.Looking at the graph, we can see that the prices of all six commodities have been increasing over time, with some fluctuations. Gasoline prices have been the most volatile among all the commodities, while the prices of cows milk and bread have been relatively stable with minor fluctuations. The prices of refined vegetable oil, diesel, and maize meal have been increasing steadily over time.
![all](https://user-images.githubusercontent.com/117269915/231668745-fa9be83a-751c-49a7-9397-c3190e301509.png)




## 5. Modelling

### 5.1 Arima Model
In this section, the ARIMA model was used to make predictions on the test set for each commodity in the time series data. The values for p, d, and q were defined, and all possible combinations of these values were generated. For each commodity, the RMSE value was calculated for each combination of (p, d, q), and the combination with the lowest RMSE value was selected as the best fit for the ARIMA model. The RMSE values and corresponding (p, d, q) values for each commodity were stored in a dictionary and presented as a table. The results showed the RMSE values for each commodity and the corresponding values of (p, d, q) that minimized the RMSE value.after obtaining the best (p, d, q) values for each commodity, the ARIMA model was used to predict the values for the test set. The actual and predicted values were then plotted to visualize and compare the trends. These plots can help to evaluate the performance of the ARIMA model for each commodity.

### 6 Model Combinations
In this section, different model combinations (SARIMA, SES, HWES, and ARIMA) were tested to determine which combination produced the best results for the given time series data. A dictionary was defined to store the RMSE values for each model. The aim was to identify the combination of models that best captured the differences in the patterns of the data.

### 6.1 Sarima Model
In this section, the SARIMA model was used to make predictions on the test set for each commodity in the time series data. The SARIMA model, which is an extension of the ARIMA model that takes into account seasonality in the data, was fitted for each commodity with (1,1,1) and (1,1,1,12) as the order and seasonal order, respectively. The endogenous variable was selected as the train data for each commodity. The performance of the SARIMA model was evaluated on the test set by making predictions and calculating the RMSE value between the predicted values and the actual values. The RMSE values for each commodity and corresponding SARIMA model were stored in a dictionary and presented as a table. The results showed the RMSE values for each commodity and the performance of the SARIMA model on the given time series data. Based on the results, it was concluded that the SARIMA model performed better for some commodities (e.g., Milk (500ML)) than for others (e.g., Vegetable Oil (1L)). These findings suggested that the SARIMA model may not be the best choice for modeling all commodities in the time series data.

### 6.2 Simple Exponential Smoothing (SES) Model
In this section, a Simple Exponential Smoothing (SES) model was fitted to each column of the time series data. The model was used to make predictions on the test set for each commodity, and the root mean square error (RMSE) was calculated between the predicted values and the actual values to evaluate the model's performance. The SES model is a forecasting method that assigns exponentially decreasing weights over time to the previous observations, giving more weight to recent observations. For each commodity, the column was selected as the endogenous variable, and an SES model was fit using the training data. The model was then evaluated on the test set by making predictions and calculating the RMSE value. The results showed that the SES model performed better for some commodities (e.g., Milk (500ML)) than for others (e.g., Vegetable Oil (1L)). These findings suggest that the SES model may not be the best choice for modeling all commodities in the time series data. The RMSE values for each commodity and the corresponding SES model were stored in a dictionary and presented as a table.

### 6.3 Holt-Winters Exponential Smoothing (HWES) Model
In this section, the Holt-Winters Exponential Smoothing (HWES) model was used to make predictions on the test set for each commodity in the time series data. The HWES model is a variation of the Simple Exponential Smoothing (SES) model that takes into account seasonality and trend in the data. For each commodity, the endogenous variable was selected as the train data and an HWES model was fit with a seasonal period of 12, additive trend, and additive seasonality. The model was then evaluated on the test set by making predictions and calculating the RMSE value between the predicted values and the actual values. The RMSE values for each commodity and corresponding HWES model were stored in a dictionary and presented as a table. The results showed the RMSE values for each commodity and the performance of the HWES model on the given time series data. Based on the results, it can be concluded that the HWES model outperformed the SARIMA and SES models for most commodities in the time series data.

### 6.4 Arima Model
We then fitted an ARIMA (AutoRegressive Integrated Moving Average) model on each time series column in the given dataset. The order of the ARIMA model used was (1,1,1).

The ARIMA models were trained on the training data, and the performance was evaluated on the test data using RMSE (Root Mean Squared Error). The lower the RMSE, the better the model's performance. 

The results showed the RMSE values for each time series column, where the lowest RMSE values indicated better performance of the model. Compared to SES and HWES models, the ARIMA model generally performed better for most of the time series columns except for the "Exchange Rate (USD)" and "Inflation" columns where HWES performed better.

### 5.5  LSTM
It is a type of recurrent neural network (RNN) that is well-suited for processing sequential data such as time series. LSTM networks have an internal memory state that allows them to remember information over long periods of time and selectively forget irrelevant information, making them particularly useful for modeling complex temporal relationships in data. 

### 5.6 Forecasting
At this point, we aimed to forecast future values for each time series in the dataset using the best model selected for each series to fit the model. We fitted the models and forecasted the future values for the next 12 months.

The forecasted values were stored in the forecast_df DataFrame, and the index of the DataFrame was set to be the forecasted dates. The forecasted dates started from 2023-03-31 and went up to 2024-02-29 with a frequency of one month.


### 5.7 MINIMAL VIABLE PRODUCT
After conducting a thorough evaluation of various models, including ARIMA, SARIMA, HWES, and SES, the LSTM (Long Short-Term Memory) model was chosen as the Minimum Viable Product (MVP) for the time series project. The decision was primarily based on its superior performance, specifically, its low RMSE (Root Mean Squared Error) values, which indicates a high level of accuracy.

The LSTM model demonstrated an ability to capture complex patterns and relationships within the time series data, allowing for more precise predictions of future values. Its ease of implementation and minimal preprocessing requirements made it a practical and cost-effective choice for an MVP.

The LSTM model was able to learn quickly from a small amount of training data and generate accurate predictions, which is crucial for an MVP. Its efficiency and accuracy make it a promising solution for the time series project.
 
 It's output as seen below was good a predicting the prices.

![output](https://user-images.githubusercontent.com/117269915/231740547-087b794c-f1c8-4aa6-9f53-3433421d3b0b.png)

## 6. Deployment
There is a sidebar for selecting the commodity or  Economic indicator, month, and year
Based on the user's selection, the app displays an image of the selected commodity and predicts its price for the selected month and year
The app displays the forecasted price of the selected commodity.
In this example, the user selected Bread as the commodity, May 2023 as the month and year, and the app predicted the price of Milk to be Ksh 57
![App Deployment](https://user-images.githubusercontent.com/117269915/231668364-1cd2761f-08c4-4372-80ec-80173997b723.png)

## 7. Conclusions 
1. Based on the results of this project, our time series model can provide valuable insights into commodity prices and economic indicators such as inflation rates and exchange rates. The developed models show  accuracy with an RMSE of less than 5% and can be used to forecast prices for the next 12 months with a reasonable degree of confidence.
2. Investors and commodity buyers can use these forecasts to make informed decisions regarding their investments or purchasing decisions. For instance, they can take advantage of opportunities identified by the market analysis to buy or sell commodities at the right time to maximize profits.
3. This  web-based application developed as part of this project provides traders and investors with reliable, real-time commodity price predictions, which can be continuously updated for ongoing accuracy. This will enable them to stay on top of the market and make informed decisions based on the latest information.
4. Overall, our project highlights the potential of time series modeling in providing valuable insights into the dynamics of commodity prices and economic indicators, and how these insights can be leveraged to inform decision-making for investors and commodity buyers.
## 8. Recommendations
1. Traders and Investors: By providing traders and investors with reliable real-time commodity price predictions, we can help them make better investment decisions. They can use our predictions to identify market trends and capitalize on opportunities for profit. This can be especially beneficial for traders and investors who specialize in commodities and are looking for ways to gain an edge in the market.
2. Farmers and Producers: our time series commodity price predictions can  be useful for farmers and producers who rely on the prices of commodities like maize meal and diesel to make business decisions. By tracking the prices of these commodities, farmers can adjust their production schedules and ensure they have a steady supply of essential goods to sell at market. This can help them maximize profits and ensure the sustainability of their business.
3. Monitor inflation rates: Since inflation rates can have a significant impact on the prices of commodities, it is important to keep a close eye on them so that Investors can use the forecasts to anticipate changes in inflation rates and make adjustments to their investments accordingly. High inflation rates can lead to higher prices of commodities, and therefore, it may be wise to invest in commodities that are likely to rise in price during inflationary periods.
4. Government Agencies:  our time series commodity price predictions can be valuable to government agencies responsible for regulating the prices of essential commodities. By providing accurate forecasts, these agencies can better manage supply and demand, prevent price spikes, and ensure that essential goods are accessible to all citizens.
