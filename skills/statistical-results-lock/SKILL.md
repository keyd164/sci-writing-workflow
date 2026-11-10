---
name: statistical-results-lock
description: 核对论文数字、统计口径和登记册，识别数字漂移、单位或模型混用；不重跑分析或修改数据。
---
# statistical-results-lock
本技能只读审计，可在 G1/G2 批准前准备核验材料；不得据此放行下游写作。
读取 results.yml、methods.yml、terminology.yml、decisions.yml 以及被引用的源输出。
逐条核对 R-id、来源行/列和筛选条件、outcome、暴露单位、模型、样本/国家数、系数、CI、p 值及呈现精度；不以登记册自证登记册。
检查 CI 的水平与方法、聚类/自由度约定及不同不确定性来源。CI 不含零与显著性不一致只列疑点，先查实际检验方法，不强行用正态近似纠正。
衍生量记录公式、输入 R-id、分母、尺度及误差传播；只有可核验的既有输出才可建议 verified，不能用估算填空。
输出 R-id/源位置/登记值/源值/结论/缺口表。缺源写 unverifiable；冲突交 evidence-lock。
报告遵循 paper-workflow 的输入身份与覆盖缺口约定；严重程度区分 blocking（影响当前所用证据）、major、minor，建议须有可定位依据。

