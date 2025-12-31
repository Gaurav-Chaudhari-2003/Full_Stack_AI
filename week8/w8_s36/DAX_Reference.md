
# DAX Queries

## Dataset Schema
FactSales(SaleID, DateKey, ProductKey, CustomerKey, RegionKey, Quantity, Revenue, Cost, Discount)  
DimDate(DateKey, Date, Year, Month, MonthName, Quarter)  
DimProduct(ProductKey, Product, Category, Brand)  
DimCustomer(CustomerKey, CustomerName, Segment)  
DimRegion(RegionKey, Region, Country)

## BASIC DAX
| Function | Description | Example |
|---|---|---|
| SUM | Adds values | Total Revenue = SUM(FactSales[Revenue]) |
| AVERAGE | Mean value | Avg Discount = AVERAGE(FactSales[Discount]) |
| COUNT | Count rows | Orders = COUNT(FactSales[SaleID]) |
| DISTINCTCOUNT | Unique count | Customers = DISTINCTCOUNT(FactSales[CustomerKey]) |
| MIN / MAX | Min / Max | Max Sale = MAX(FactSales[Revenue]) |
| IF | Conditional | High Sale = IF([Total Revenue]>100000,"Yes","No") |
| DIVIDE | Safe division | Margin % = DIVIDE([Profit],[Revenue]) |

## MEDIUM DAX
| Function | Description | Example |
|---|---|---|
| CALCULATE | Change filter context | Sales 2024 = CALCULATE([Total Revenue], DimDate[Year]=2024) |
| FILTER | Row filtering | High Sales = CALCULATE([Total Revenue], FILTER(FactSales, FactSales[Revenue]>50000)) |
| ALL | Remove filters | Total All Regions = CALCULATE([Total Revenue], ALL(DimRegion)) |
| VALUES | Current filter values | Region Count = COUNTROWS(VALUES(DimRegion[Region])) |
| RELATED | Fetch dimension value | Category = RELATED(DimProduct[Category]) |
| SUMX | Row-wise sum | Total Cost = SUMX(FactSales, FactSales[Quantity]*FactSales[Cost]) |
| RANKX | Ranking | Product Rank = RANKX(ALL(DimProduct), [Total Revenue]) |

## ADVANCED DAX
| Function | Description | Example |
|---|---|---|
| TREATAS | Virtual relationship | Sales via Country = CALCULATE([Total Revenue], TREATAS(VALUES(DimRegion[Country]), DimRegion[Country])) |
| USERELATIONSHIP | Activate inactive relation | Alt Date Sales = CALCULATE([Total Revenue], USERELATIONSHIP(FactSales[ShipDateKey],DimDate[DateKey])) |
| CROSSFILTER | Control relationship direction | BiDir = CALCULATE([Total Revenue], CROSSFILTER(DimProduct[ProductKey],FactSales[ProductKey],BOTH)) |
| EARLIER | Nested row context | Running Total = SUMX(FILTER(FactSales, FactSales[DateKey]<=EARLIER(FactSales[DateKey])), FactSales[Revenue]) |
| PATH | Hierarchy traversal | Level = PATHLENGTH(DimRegion[Hierarchy]) |
| REMOVEFILTERS | Clear specific filters | All Time Sales = CALCULATE([Total Revenue], REMOVEFILTERS(DimDate)) |
| TOPN | Top rows | Top 5 Products = TOPN(5, DimProduct, [Total Revenue]) |
| ISINSCOPE | Detect drilldown | Drill Level = IF(ISINSCOPE(DimProduct[Category]),"Category","Product") |

## TIME INTELLIGENCE
| Function | Description | Example |
|---|---|---|
| TOTALYTD | Year-to-date | Sales YTD = TOTALYTD([Total Revenue], DimDate[Date]) |
| SAMEPERIODLASTYEAR | YoY | Sales LY = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DimDate[Date])) |
| DATESMTD | Month-to-date | Sales MTD = TOTALMTD([Total Revenue], DimDate[Date]) |
| DATEADD | Shift time | Sales Prev Month = CALCULATE([Total Revenue], DATEADD(DimDate[Date],-1,MONTH)) |

## PERFORMANCE
| Function | Description | Example |
|---|---|---|
| VAR | Store intermediate | VAR Rev=[Total Revenue] RETURN IF(Rev>100000,"High","Low") |
| KEEPFILTERS | Preserve slicers | Filtered Sales = CALCULATE([Total Revenue],KEEPFILTERS(DimRegion[Region]="North")) |
| SUMMARIZE | Group data | Summary = SUMMARIZE(FactSales,DimProduct[Category],"Sales",[Total Revenue]) |

## BUSINESS METRICS
| Metric | Formula |
|---|---|
| Profit | [Total Revenue] - [Total Cost] |
| Margin % | DIVIDE([Profit],[Total Revenue]) |
| Contribution | DIVIDE([Total Revenue],CALCULATE([Total Revenue],ALL(DimProduct))) |
| Market Share | DIVIDE([Total Revenue],CALCULATE([Total Revenue],ALL(DimRegion))) |

## Takeaway
- Basic = Aggregation  
- Medium = Context control  
- Advanced = Relationship + hierarchy + performance tuning  
- Time = Trend analysis  
- Performance = Scaling on big data
