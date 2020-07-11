# Project-2
Project Idea:
Three shares whose values are increasing and worth investing in based on the impact of COVID-19
Looking at current initiatives of the companies
Before/After quarantine data (stock price)
Web scraping or Live updates of stock data (postgresql?)
Research/consider analyst opinions(?)
EPS/quarterly info
Morningstar
RobinHood → primary source for live stock price information (can also get industry info)
Yahoo! Finance
Companies:
Ideas of companies : netflix /disney / amazon prime / hulu/hbo max / apple tv/cbs/vs espn +
Companies like uber buying postmates
How that impact other delivery companies ( stock value) short and mid terms
Casinos?
Categories for Stocks:
Stock that got profitable bc of covid
Amazon -- Web Services/Online Retail/Online streaming
Stock that is going bankrupt
American Eagle -- Retail
Nordstrom’s --
Stock which is riskier/heavily impacted by covid, future is uncertain
MFA Financial -- Real Estate

Stock Data Analysis
Project Description:
The COVID-19 pandemic put the stock market in disarray.  Many companies were impacted to the point of bankruptcy.  Others, however, saw a significant rise in their stock price.  Our project focuses on three companies - one that’s stock was decimated, another that had significant gains, and a third that’s future is uncertain in the wake of the pandemic. We will provide visuals to show the progression of the stock price from January (before COVID was declared a pandemic) until July (current day) for the year 2020.
Chart Types:
Line Chart showing stock price fluctuations from quarantine order (3/10) until present.
Candlestick Chart showing daily high/low.
Dot (scatter?) Plot of quarterly earning.
Roles:
API/Flask -- pull data from api (robinhood, yahoo finance, investopedia (for background of the company), or any other website with information on the company/stock).
Github has live stock data.
Taylor, Vasuda
Database -- create database from pulled api data (could be combined with the API/Flask section).
Quentin
HTML/CSS create the html for which all of the charts will go on.
Simar
Javascript/leaflet/plotly -- create the charts.
Vasuda, Taylor
Dashboard:
Title at the top.
Paragraph either analyzing the performance of the stock or giving an analyst’s position on the stock.
“In march, the avg price was $8.  By the end of this year, it’ll reach an average price of $(x).”
Another paragraph describing the background of the company, its sector.
Dropdown menu of the three stocks we selected, which will update the dashboard page.
