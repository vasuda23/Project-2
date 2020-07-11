# Project-2
Stock Data Analysis
Project Description:
1. The COVID-19 pandemic put the stock market in disarray.  Many companies were impacted to the point of bankruptcy.  Others, however, saw a significant rise in their stock price.  Our project focuses on three companies - one that’s stock was decimated, another that had significant gains, and a third that’s future is uncertain in the wake of the pandemic. We will provide visuals to show the progression of the stock price from January (before COVID was declared a pandemic) until July (current day) for the year 2020.
Chart Types:
1. Line Chart showing stock price fluctuations from quarantine order (3/10) until present.
2. Candlestick Chart showing daily high/low.
3. Dot (scatter?) Plot of quarterly earning.
Roles:
1. API/Flask -- pull data from api (robinhood, yahoo finance, investopedia (for background of the company), or any other website with information on the company/stock). 
a. Github has live stock data.
b. Taylor, Vasuda
2. Database -- create database from pulled api data (could be combined with the API/Flask section).
a. Quentin
3. HTML/CSS create the html for which all of the charts will go on.
a. Simar
4. Javascript/leaflet/plotly -- create the charts.
a. Vasuda, Taylor
Dashboard:
1. Title at the top.
2. Paragraph either analyzing the performance of the stock or giving an analyst’s position on the stock.
a. “In march, the avg price was $8.  By the end of this year, it’ll reach an average price of $(x).”
3. Another paragraph describing the background of the company, its sector.
4. Dropdown menu of the three stocks we selected, which will update the dashboard page.
5. Three charts, all on the dashboard page, that correspond to the stock selected from the dropdown menu.
