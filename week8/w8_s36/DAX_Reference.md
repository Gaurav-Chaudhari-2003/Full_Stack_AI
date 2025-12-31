
# DAX Queries

## Assumed Dataset Schema
FactSales(SaleID, DateKey, ProductKey, CustomerKey, RegionKey, Quantity, Revenue, Cost, Discount)  
DimDate(DateKey, Date, Year, Month, MonthName, Quarter)  
DimProduct(ProductKey, Product, Category, Brand)  
DimCustomer(CustomerKey, CustomerName, Segment)  
DimRegion(RegionKey, Region, Country)

---

## 🟢 BASIC DAX
| Function | Description | Example |
|---|---|---|
| SUM | Adds values | Total Revenue = SUM(FactSales[Revenue]) |
| AVERAGE | Mean value | Avg Discount = AVERAGE(FactSales[Discount]) |
| COUNT | Count rows | Orders = COUNT(FactSales[SaleID]) |
| DISTINCTCOUNT | Unique count | Customers = DISTINCTCOUNT(FactSales[CustomerKey]) |
| IF | Conditional | High Sale = IF([Total Revenue]>100000,"Yes","No") |

## 🟡 MEDIUM DAX
| Function | Description | Example |
|---|---|---|
| CALCULATE | Change filter context | Sales 2024 = CALCULATE([Total Revenue], DimDate[Year]=2024) |
| FILTER | Row filtering | High Sales = CALCULATE([Total Revenue], FILTER(FactSales, FactSales[Revenue]>50000)) |
| RANKX | Ranking | Product Rank = RANKX(ALL(DimProduct), [Total Revenue]) |

## 🔵 ADVANCED DAX
| Function | Description | Example |
|---|---|---|
| TREATAS | Virtual relationship | CALCULATE([Total Revenue], TREATAS(VALUES(DimRegion[Country]), DimRegion[Country])) |
| USERELATIONSHIP | Activate inactive relation | CALCULATE([Total Revenue], USERELATIONSHIP(FactSales[ShipDateKey],DimDate[DateKey])) |
| TOPN | Top rows | TOPN(5, DimProduct, [Total Revenue]) |

## 🟣 TIME INTELLIGENCE
| Function | Description | Example |
|---|---|---|
| TOTALYTD | Year-to-date | Sales YTD = TOTALYTD([Total Revenue], DimDate[Date]) |
| SAMEPERIODLASTYEAR | YoY | Sales LY = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(DimDate[Date])) |

## 🟤 PERFORMANCE
| Function | Description | Example |
|---|---|---|
| VAR | Store intermediate | VAR Rev=[Total Revenue] RETURN IF(Rev>100000,"High","Low") |
| KEEPFILTERS | Preserve slicers | CALCULATE([Total Revenue],KEEPFILTERS(DimRegion[Region]="North")) |
