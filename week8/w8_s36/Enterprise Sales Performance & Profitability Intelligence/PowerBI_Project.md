# Power BI Project: Enterprise Sales Performance & Profitability Intelligence

## Objective
Analyze sales, profit, and performance across products, customers, regions, and time to support business decisions.

## Data
- FactSales.csv
- DimDate.csv
- DimProduct.csv
- DimCustomer.csv
- DimRegion.csv

## Dashboard Pages

### 1. Executive Overview
KPIs:
- Total Revenue
- Total Profit
- Profit Margin %
- Orders Count
- Average Discount

Visuals:
- KPI cards
- Revenue & Profit trend (line)
- Top 5 products by revenue (bar)
- Region-wise revenue (map/bar)

### 2. Product & Category Analysis
Questions:
- Which category is more profitable?
- Are high-selling products actually profitable?

Visuals:
- Revenue vs Profit by Product
- Category contribution %
- Discount vs Profit scatter

### 3. Customer & Segment Insights
Questions:
- Who are our most valuable customers?
- Which segment gives better margin?

Visuals:
- Revenue by Segment
- Customer ranking (RANKX)
- Customer lifetime value proxy

### 4. Region Performance
Questions:
- Which region has high sales but low profit?
- Where should the company expand?

Visuals:
- Region vs Profit Margin heatmap
- Trend per region
- Market share per region

### 5. Time Intelligence
Questions:
- Are we growing?
- Is performance seasonal?

Visuals:
- YTD vs LY comparison
- YoY growth %
- Monthly trend

## DAX Used
- CALCULATE
- RANKX
- SAMEPERIODLASTYEAR
- TOTALYTD
- DIVIDE
- ALL / REMOVEFILTERS
- VAR
- TOPN

## Deliverables
- Power BI .pbix file
- Dataset CSVs
- Dashboard screenshots
- README explaining insights
