# ESE5023_Assignments_12631509

Comments on HW2 from Yali （95/100）

1.1 ["Deaths"]分组不对，应考虑按["Total Deaths"]分组 （-1p)

1.3: "Ms", "Mw", "Mag", "Mb", "Ml", "Mfa" 几类都表示震级；
Ms在巨震时饱和，所以应该使用 Mw/Mag。同时你没有考虑震级缺失该如何处理
采用Ms震级漏掉了Japan最大地震应该是 2011 本州（Mw 9.1）（-2p）

2. 根据质量代码筛选有效气温时，有效的数据应该只有qc=1，5，其他qc代码的仅仅是gross limits应该剔除，
值不存在时（`+9999` ）是纯粹的缺测标记，所以qc=9时也应该剔除，同时A/C/I/M/P/R/U 不是 TMP 的质控码。
考虑到季节变化，至少应该使用12个的滑动平均来分析变化趋势，而非线性拟合。（-3p)


3.3 这里`BASIN` 的取值里有`NA` （North Atlantic），你设置`dropna=False`, 非常好。（+1p)

4. Instrument_Type∈{4,5,6}，为何这样考虑？下次请提供你下载的数据，谢谢。

