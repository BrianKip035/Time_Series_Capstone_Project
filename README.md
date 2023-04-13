# PriceWise AI


# 1. BUSINESS UNDERSTANDING

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
The Exploratory Data Analysis showed some observations on the data that was collected. Each product had a visualisation of it's price over time showing the different products change in price and also visualisations of inflation over time and the exchange rate of the dollar. 
<br>
Inflation is the rate at which the general level of prices for goods and services is rising, and a high inflation rate indicates a decrease in the purchasing power of a country's currency. From the graph, we can see that the 12-month inflation rate has been subject to fluctuations over the years. In the early years from 2014 to 2016, the inflation rate was relatively stable at around 6-8%, after which there was a gradual increase until 2017, where it peaked at around 11%. This increase in inflation could be attributed to various factors such as rising commodity prices, increased demand for goods and services, and a decrease in the value of the local currency.
![My Image](Images/inflation.jpg)

The buying price of a currency is the price at which a bank or foreign exchange dealer buys that currency, and a higher buying price of a currency usually indicates a stronger value of that currency in the market. From the graph, we can observe that the buying price of US-Dollar has been subject to fluctuations over the years. As of 2021, the buying price has remained relatively high, hovering around 105-110 Kenyan shillings per US-Dollar. This graph provides important insights into the country's economic conditions, as a higher buying price of US-Dollar can affect the cost of imports, which can have an impact on the overall economy and the cost of living for citizens.
![My Image](Images/Exchange rate.png)

 The graph plots the prices of six commodities, including bread, refined vegetable oil, cows milk, diesel, maize meal, and gasoline, along with the 12-month inflation rate.Looking at the graph, we can see that the prices of all six commodities have been increasing over time, with some fluctuations. Gasoline prices have been the most volatile among all the commodities, while the prices of cows milk and bread have been relatively stable with minor fluctuations. The prices of refined vegetable oil, diesel, and maize meal have been increasing steadily over time.

![My Image](Images/all.png)


## 5. Modelling
### 5.1 Arima 
Autoregressive Integrated Moving Average model is a statistical model for time series data that combines autoregression (AR) and moving average (MA) models, and can be used to make predictions based on past patterns in the data.

### 5.2 Simple Exponential Smoothing
this model is a  basic time series forecasting method that assumes that the future values of a time series are a weighted average of past values, with more recent values given more weight.
### 5.3 Holt-Winters Exponential Smoothing (HWES)
it is an extension of Simple Exponential Smoothing that also takes into account trends and seasonality in the data.
### 5.4  Sarima Model
this is a seasonal Autoregressive Integrated Moving Average model is an extension of ARIMA that explicitly models seasonal trends in the data.
### 5.5  LSTM
It is a type of recurrent neural network (RNN) that is well-suited for processing sequential data such as time series. LSTM networks have an internal memory state that allows them to remember information over long periods of time and selectively forget irrelevant information, making them particularly useful for modeling complex temporal relationships in data.
### 5.6 Model selection
In the process of selecting a suitable model for our time series forecasting task, we tested several models including SARIMA, Simple Exponential Smoothing, Holt-Winters Exponential Smoothing, and LSTM.

We evaluated the performance of each model using the root mean squared error (RMSE) metric. After comparing the RMSE values of each model, we found that the LSTM model had the lowest RMSE, indicating that it was the most accurate model for our time series forecasting task.

Therefore, we selected the LSTM model as our final model for time series forecasting.
### 5.7 Forecasting
Forecasting is the process of making predictions or estimates about future events, trends, or outcomes based on historical data and other relevant information. It is commonly used in various fields, such as business, finance, economics, and meteorology, to make informed decisions and plans for the future. 

## 6. Deployment
Our team has developed a web application for time series forecasting of stock prices using a deep learning model called LSTM. The application is built using the Streamlit framework, and allows users to select a specific year and month for which they want a price prediction. We have trained the LSTM model using historical stock price data and evaluated its performance using RMSE metric. We have found that the LSTM model outperformed other time series models we tested, and therefore we have selected it for deployment. The Interface lets you pick oout the month and year you want as well as the commodity and it provides the predicted price of the product. 
## 7. Conclusions 
## 8. Recommendations
