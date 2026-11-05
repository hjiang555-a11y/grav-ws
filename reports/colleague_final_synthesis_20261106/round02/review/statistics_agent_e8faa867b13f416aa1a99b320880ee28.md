**总体评价：v60的主要推断与验证包一致，两路估计没有被拼成一个“更精确”的结果。太阳扰动界在明确的固定设计和幅度约束下定义正确、可以达到。未发现需要推翻主结果的确证统计错误；有一处权重措辞应纠正，另有两项证据边界需要明确。**

本轮实际读取了稿件、验证包、R3原始证据JSON及两份脚本，只做静态审查和保存值核对；未执行脚本、未独立读取原始观测，也未打开图片。验证包中的PASS是提供的执行记录，不是本轮重算结论。

1. **【红色警报：局部方法表述】将标准差写成“权重”，与实际WLS实现不符。**  
   来源：v60“Comparison…”第二段写“weights each bin by its period-noise coefficient divided by the square root of its member count”；但`independent_replay.py`先用该量除设计和响应，即它是\(\sigma_i\)，实际逆方差权重为\(n_i/\alpha_p^2\)。ED10末注已经解释正确，主段应与之统一：
   *“The R3 route assigns bin standard deviations \(\sigma_i=\alpha_{p(i)}/\sqrt{n_i}\) and fits by inverse-variance weighting, \(w_i=1/\sigma_i^2\).”*  
   这是文字定义错误，不是已证明的拟合错误。

2. **太阳界数学成立，但“抑制扰动”的主文表达应指向估计量偏差。**  
   来源：`independent_replay.py:gains`及`verify_solar_gain.py`。设\(v_p=h_LI_pQ_\tau\)，共享相位的最大偏移为\(\|\sum_pv_p\|\)，分期相位则为\(\sum_p\|v_p\|\)。取相位向量沿各投影方向即可达到，正负号可给相反极值。验证包记录12 h为0.0104303/0.1587073，24 h为0.0163469/0.0316912；QR极值扰动记录与之相差不超过\(1.98\times10^{-15}\)，与文稿舍入一致。  
   这些结果针对**参考拟合算子、一次一个频率、每期相同规定幅度**；既不估计环境幅度，也不证明扰动在观测中消失。建议将“coverage suppresses a coherent daily disturbance”替换为：
   *“The sampled phase evolution reduces the worst-case bias induced in this estimator by a prescribed coherent sinusoid.”*  
   Fig.4及Methods保留“参考模型无自由日项”的限定；不能把该界用作加入日项后的误差，也不能用于任意非平稳波形。

3. **【待核实：物理证据】数值重建不能关闭权重、校准及因果归因问题。**  
   来源：验证包`physical`明确共享固体潮CSV、加载输入和天文库，未独立验证海洋卷积与钟位置；`raw`也保留频率参考、修正值及节点假设。R3噪声系数是在扣单位模板后估计、在删除中固定的，ED10已披露其不确定度未传播。这不自动使估计有错，但0.9866±0.1231只能是该固定权重模型的工作误差，不能据“接近1”认证物理或择优。建议保留一句：
   *“Agreement between reductions checks implementation and processing sensitivity on overlapping observations; it does not independently calibrate the physical inputs or the estimated noise weights.”*  
   需要实验校准记录和物理输入溯源才能进一步解决，不能靠增加复算精度关闭。

**必须保留的优点：**

- ED10四行数据与误差绑定正确：现路线0.9726，SE为0.1183/0.1205/0.0947；R3八期0.9866，SE为0.1231/0.1116/0.1314，引用误差仍按各自规则。六期R3加权0.9899与等权0.9538也是同一路线内的受控比较，没有冒充全部处理差异的分解。
- 现路线的六期wild、日F区域及模拟覆盖没有移植给R3；R3九个拟合的复现也未被当成独立实验。不得将R3的LS相关矩阵与最大边际SE拼成未经定义的联合区域。
- 强弱分量分开、M2固定相位尺度与二维相位检验分开；N2未分辨、逐期日项M2联合零点P=0.125均保留。主文没有把单位点不拒绝当成理论为真的概率。
- 重叠样本不合并、测试期nuisance本地重估、B2仅作子集关联，这些边界直接决定结论，应继续保留。

本轮结论是作者审查建议，不构成科学批准或图像验收。