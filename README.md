### Tags in Code#

- why  :   不解
-

## Numpy and Pandas

### Numpy

- numpy array
  - ndim维度
  - shape几行几列
  - size几个元素
  - numpy Tuple 和 array类似
  - zeros(x,y)零矩阵
  - one(x, y) 1 矩阵
- operations
  - // 整除
- Slice
  - `[1:5][:]`代表的是第1,2,3,4行不包括第5行
- 算术函数和统计函数
  - sort()从小到大排序
  - sign()判断正负
  - arrange() 区间也是左闭右开
  - numpy.random.randn(3,3) 返回3行3列随机的标准正态分布数据
  - numpy.random.randn(4) 返回一行4个标准正太分布数据
  - rand() 则是 [0,1)
  - mean()/average() 平均值
  - std 标准差(standard deviation)
- 线性代数
  - numpyArray.T  矩阵转置

### Pandas

- series 一维数组化
  - 可自定义index
    - eg: s = Series([1.2, 2.5, 4.3], index = [ 'Jan1', 'Jan2', 'Jan3'])
  - 可以由dict字典转化
  - slice
    - .iloc([:])
- DataFrame
  - index默认从0开始，可自定义index，DataFrame(myDict, index = [2, 3, 4, 'aa']) 
  - tupleList中 一个 元组代表一行数据 ，列名需自定义， DataFrame(tupleList, columns=['year', 'temp', 'precip'])
  - iloc 取得是默认有的从0开始的索引  ，loc取得是自定义的索引
  - Data['column1'] 和 Data.column1 一样
  - max() 每列的最大值 ，max(axis=1)每行的最大值
  - 自定义算法 data.apply(lamda x: x.max()-x.min() , axis=1)
- Series与DataFrame的绘制
  - %matplotlib inline 为jupyter的魔法函数，调用了matplotlib
  - 可直接mySeries.plot(kind='line', title='MyPlot')



## Data Exploration

- pd.read_csv为DataFrame对象
- value_counts()计算各个值的个数
- describe()对属性进行摘要描述
- cov()直接可求定量列间的协方差
- **corr()求列之间的相关性**

## Data Preprocessing

### 数据质量问题

- drop(['Sample code'],axis=1) 丢弃一整列
- fillna(x)填充用x 填充NaN
- dropna()去除NaN的行
- shape()是矩阵几行几列，shape[0]表示行数

### 聚合(Aggregation)

- 降雨量数据直接是聚合为月和年
- var() 无偏方差
- to_datetime()将时间转成pandas时间
- groupby(pd.Grouper(freq='M')).sum()  将数据按月份分组求和得到新DataFrame对象

### 抽样(sampling)

- sample(n=抽样数量,frac=抽样比例,replace=是否有放回抽样,random_state=随机数种子...)



## PROBLEMS

- [ ] `nbArray[:][2] `#代表的是第三行？！
- [ ] 感觉zeros(), ones()多打了一对括号， eye()不多打却没问题，和参数个数有关？
- [ ] dot()?
- [ ] Histogram直方图？y坐标为频率，横坐标的区间？

