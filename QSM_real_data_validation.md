# 以球面滑動隔震實驗資料驗證量子結構力學

**作者：郭瀚嶸**
**日期：2026.05.10**

## 摘要
本文以《An Experimental Study of a Spherical Sliding Isolation System Subjected to Pulse-Like Ground Motions》公開之球面滑動隔震系統實驗資料為基礎，嘗試以量子結構力學 (Quantum Structural Mechanics, QSM) 的觀點，重新閱讀地震波對隔震位移的作用機制。原研究已指出：對隔震系統而言，只依賴加速度或平均反應譜加速度，無法充分解釋實際隔震位移；速度脈衝、脈衝週期與隔震系統有效週期，必須一併納入討論。

本文沿著原研究的實證結論往前推進。第一層檢查顯示，輸入加速度峰值與隔震位移峰值的相關性很弱；第二層檢查顯示，速度峰值與隔震位移的關係明顯提高。接著，本文將加速度與速度合成為輸入端量子結構力學能勢流 (Input-Side QSM Power Flow)，即 $P_{\mathrm{in}}(t)=a(t)v(t)$ ，並進一步觀察一秒能勢波包 (1s Power Packet)、介面能勢／做功交換 (Interface Power / Work Exchange)、累積介面做功 (Accumulated Interface Work)，以及量子結構力學能勢頻率群 (QSM Power Frequency Group) 與有效隔震頻率群 (Effective Isolation Frequency Group) 的接觸關係。

分析結果顯示，真正接近隔震位移反應的，不是輸入端單一加速度峰值或單一速度峰值，而是能勢進入隔震介面後形成的介面能勢／做功交換。跨案例群組 Group1–4 的總結圖顯示，量測介面做功波包 (Measured Interface Power/Work Packet) 與量測隔震位移峰值 (Measured Upper-Lower Isolation Displacement Peak) 呈現最清楚的關係。另一方面，頻率群圖譜也顯示，隔震反應不能只用一個有效頻率或有效週期概括； $f_{\mathrm{eff}}$ 是入口尺度，背後仍存在 QSM Power Frequency Group、Interface Frequency Group 與 Displacement Response Frequency Group的轉換關係。尤其在單筆診斷圖 (Diagnosis Figure) 的頻率群收斂比較中，高位移案例常可看到位移反應頻率貼近 $f_{\mathrm{eff}}$ 及其整齊倍頻序列。這表示有效頻率不是單一控制值，而是一組可被能勢接觸、轉換與顯化的入口頻率族。

本文的核心結論是：地震波對隔震系統而言，可以被視為一個進入結構的能勢場。當此能勢場無法被隔震系統順利轉化為穩定通道時，它會在介面形成做功交換，並顯化為可觀測的隔震位移。這是本文對原實驗資料的 QSM 解讀，也是量子結構力學第一次以真實實驗資料建立機制性驗證的嘗試。

---

## 名詞說明
**量子結構力學 (Quantum Structural Mechanics, QSM)**
本文使用的結構分析觀點。它把地震波視為量子力學的波函數，並將結構視為能勢進入、傳遞、交換、耗散與顯化的系統，而不只是一個承受外力並產生位移的剛度系統。

**隔震位移 (Isolation Displacement, IsoDisp)**
本文指上部結構與下部基礎之間的相對位移，亦即隔震層實際承受與顯化出來的位移反應。本文主要比較量測隔震位移峰值 (Measured Upper-Lower Isolation displacement peak)。

**輸入加速度峰值 (Input Acceleration Peak)**
指地震輸入端加速度歷時中的峰值。它是傳統地震工程常用的輸入強度描述之一，但本文分析顯示，單看此一數值不足以解釋隔震位移。

**輸入速度峰值 (Input Velocity Peak)**
指地震輸入端速度歷時中的峰值。對隔震系統而言，速度峰值比加速度峰值更接近位移需求，因為隔震位移與地震波能否持續推動隔震層滑移有關。

**量子結構力學能勢流 (QSM Power Flow)**
本文使用 $P_{\mathrm{in}}(t)=a(t)v(t)$ 作為輸入端單位質量能勢流的代理量。它不是傳統總功率，而是把加速度代表的運動改變能力，以及速度代表的推動與傳遞方向，合成為一個能勢流動指標。

**輸入端量子結構力學能勢流 (Input-Side QSM Power Flow)**
指由地震輸入端的 $a(t)$ 與 $v(t)$ 所形成的 QSM Power Flow。它描述地震波進入隔震系統之前，輸入端已經形成的能勢流動狀態。

**輸入端量子結構力學能勢峰值 (Input-Side QSM Power Peak)**
指 Input-Side QSM Power Flow 歷時中的峰值，用來觀察地震輸入是否在某一瞬間形成明顯能勢衝擊。

**能勢波包 (Power Packet)**
指某一短時間窗內集中的 QSM Power Flow。本文特別使用一秒時間窗觀察能勢是否集中形成可推動隔震層的事件；後文的 1s Power Packet 即指一秒能勢波包。

**介面能勢／做功交換 (Interface Power / Work Exchange)**
指隔震介面上的 $F_{\mathrm{interface}}(t)v_{\mathrm{rel}}(t)$ 與其時間積分量。這是輸入能勢真正進入隔震介面後的交換與做功。後文若使用 Interface Power、Interface Work 或 Interface Power/Work Packet，皆指此一介面層級的能勢與做功反應。

**量測介面做功波包 (Measured Interface Power/Work Packet)**
指由實測介面資料得到的短時間介面能勢／做功交換量。本文的跨案例群組總結顯示，這個量與量測隔震位移峰值呈現最清楚的關係。

**累積介面做功 (Accumulated Interface Work)**
指介面能勢／做功交換隨時間累積後的總量。它可反映介面整體做功，但本文結果顯示，在部分案例群組中，短時間介面做功波包比累積做功更接近位移峰值。

**有效隔震週期 (Effective Isolation Period, $T_{\mathrm{eff}}$ )**
指隔震系統在等效描述下的主要週期尺度。原研究已將其視為理解隔震反應的重要參數，本文進一步將其轉換為有效隔震頻率。

**有效隔震頻率 (Effective Isolation Frequency, $f_{\mathrm{eff}}$ )**
由有效隔震週期 $T_{\mathrm{eff}}$ 對應而來的頻率尺度，本文使用 $f_{\mathrm{eff}}=1/T_{\mathrm{eff}}$ 表示。

**有效隔震頻率群 (Effective Isolation Frequency Group)**
由 $f_{\mathrm{eff}}$ 延伸而來的頻率族，包括 $0.5f_{\mathrm{eff}}$ 、 $f_{\mathrm{eff}}$ 、 $2f_{\mathrm{eff}}$ 、 $3f_{\mathrm{eff}}$ 、 $4f_{\mathrm{eff}}$ 等。本文將其視為隔震系統的入口頻率族，而非唯一控制頻率。

**量子結構力學能勢頻率群 (QSM Power Frequency Group)**
指輸入端 QSM Power Flow 經頻率分析後得到的一組主要頻率。它用來觀察地震波的能勢不是以單一頻率進入系統，而是以一組頻率成分接觸隔震系統。

**介面頻率群 (Interface Frequency Group)**
指 Interface Power / Work Exchange 經頻率分析後得到的一組主要頻率。它用來觀察輸入端能勢進入隔震介面後，哪些頻率成分被保留、轉換或放大。

**位移反應頻率群 (Displacement Response Frequency Group)**
指隔震位移反應 $u_{\mathrm{iso}}(t)$ 的主要頻率群。本文特別關注高位移案例中，位移反應頻率是否貼近 $f_{\mathrm{eff}}$ 及其倍頻序列。

**案例群組 (Case Group)**
指本文依原研究資料分類所使用的 Group1–4。本文將 Group1–4 稱為案例群組；只有 Frequency Group 才翻譯為頻率群。

**頻率群接觸圖譜 (Frequency-Group Contact Map)**
指本文總結圖與各案例群組 Figure 2 所呈現的頻率群關係圖。它用來觀察 QSM Power Frequency Group 如何接觸 Effective Isolation Frequency Group，而不是將頻率關係壓縮成單一分數。

**單筆診斷圖 (Diagnosis Figure)**
指本文針對單一地震資料所繪製的十子圖診斷圖。它同時呈現加速度、速度、QSM Power Flow、Power Packet、Interface Power / Work Exchange、Isolation Displacement 與 Frequency-Group Closure。本文後續提到 J 圖時，指的就是 Diagnosis Figure 中用來比較 QSM Power Frequency Group、Interface Frequency Group 與 Displacement Response Frequency Group的最後一個子圖。

**頻率群收斂比較 (Frequency-Group Closure)**
指單筆診斷圖中用來比較 QSM Power Frequency Group、Interface Frequency Group 與 Displacement Response Frequency Group的圖面。它的重點不是只看三種頻率是否相近，而是看位移反應是否形成接近 $f_{\mathrm{eff}}$ 及其倍頻的整齊序列。若高位移案例中出現這種序列，代表隔震系統並非只從單一有效頻率接收能勢，而是透過一組有效頻率入口被推動。

**時間差 (Lag)**
指兩個事件峰值之間的時間距離，例如 QSM Power Packet peak 與隔震位移峰值之間的時間差。本文用它判斷能勢事件與位移事件是否在時間上接近。

**瞬時能勢峰值 (QSM Power Shock)**
指 QSM Power Flow 歷時中較尖銳的瞬間能勢峰值。它可提示地震輸入中短時間的強烈能勢衝擊，但本文不把它視為唯一判斷依據。

**輸入運動 (Input Motion)**
指地震波輸入端的加速度、速度與由此形成的能勢歷時。本文在結論中用它概括地震輸入的運動資料層。

**頻率群顯化 (Frequency-Group Manifestation)**
指能勢經由輸入端與介面轉換後，在位移反應頻率群中呈現可辨識序列的現象。

**圖面英文標籤使用說明 (Figure Label Convention)**
本文正文以中文說明為主，但由於輸出圖面採用英文標籤，部分術語在完成名詞定義後，後文會保留英文名稱。例如 QSM Power Flow、Power Packet、Interface Power / Work Exchange、QSM Power Frequency Group、Interface Frequency Group 與 Displacement Response Frequency Group。這樣安排是為了讓正文、圖面與未來英文論文版本可以互相對應。

---

# 一、研究起點：沿著原論文的結論繼續往前走

原研究最重要的貢獻，是用實驗資料指出一件對隔震設計很關鍵的事：只看加速度或平均反應譜加速度，無法充分描述隔震位移需求。

這個結論很重要，也值得尊重。因為在一般結構設計與地震工程中，加速度與反應譜一直是主要語言。它們可以提供設計尺度，也能讓不同地震波在同一個工程座標中比較。但是，當研究對象變成球面滑動隔震系統，問題就變得更細。隔震系統的核心反應是相對位移，而位移不是瞬間加速度峰值的直接結果。地震波若要把隔震層推開，必須透過速度脈衝、時間持續性、介面摩擦與系統有效週期共同作用。

因此，本文的立場很清楚：這不是要否定原論文，而是沿著原論文已經打開的門繼續走。原論文已經證明「只看加速度不夠」。本文接著問：如果只看加速度不夠，那麼能不能找到一條更接近位移生成機制的資料閱讀路徑？

這條路徑在本文中分成五步：

1. 從輸入加速度峰值 (Input Acceleration Peak) 檢查開始，確認加速度對隔震位移的解釋力不足。
2. 轉向輸入速度峰值 (Input Velocity Peak)，確認速度比加速度更接近隔震位移需求。
3. 將 $a(t)$ 與 $v(t)$ 合成為 $P_{\mathrm{in}}(t)=a(t)v(t)$ ，把地震輸入轉換成 QSM Power Flow。
4. 觀察能勢波包 (Power Packet) 是否進入隔震介面，形成 $F_{\mathrm{interface}}(t)v_{\mathrm{rel}}(t)$ 與介面做功。
5. 將 QSM Power Flow 展開為頻率群，觀察其與有效隔震頻率族之間的接觸、轉換與位移顯化。

這五步合起來，就是本文的 QSM Power viewpoint transformation。

---

# 二、圖像與資料閱讀架構：從總體關係進入單筆機制

本文的圖像分析分為三個層次。第一層是跨案例群組 Group1–4 的總體關係，用來觀察加速度、速度、QSM Power Flow、介面做功與隔震位移之間的整體趨勢。第二層是各案例群組的分組關係，用來保留短週期脈衝、中週期脈衝、非脈衝與頻譜匹配資料之間的差異。第三層是單筆資料的診斷圖，用來檢查時間波形、能勢波包、頻率群、介面做功與位移峰值是否能形成一條可追蹤的機制鏈。

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Fig01_core_power_viewpoint_transformation.png)

跨案例群組的 Figure 1 用來回答第一個問題：若以量測隔震位移峰值 (Measured Upper-Lower Isolation displacement peak) 作為反應量，輸入加速度峰值 (Input Acceleration Peak)、輸入速度峰值 (Input Velocity Peak)、輸入端量子結構力學能勢峰值 (Input-Side QSM Power Peak)、輸入端一秒能勢波包 (Input-Side 1s QSM Power Packet)、量測介面做功波包 (Measured Interface Power/Work Packet)，以及累積介面做功 (Accumulated Interface Work) 分別能提供多少解釋力。這張圖的目的不是把所有現象壓成單一分數，而是呈現資料如何從加速度／速度指標，逐步轉向能勢／做功指標。

其閱讀順序如下：

```text
輸入加速度峰值 (Input Acceleration Peak)
→ 輸入速度峰值 (Input Velocity Peak)
→ 輸入端量子結構力學能勢峰值 (Input-Side QSM Power Peak)
→ 輸入端一秒能勢波包 (Input-Side 1s QSM Power Packet)
→ 量測介面做功波包 (Measured Interface Power/Work Packet)
→ 累積介面做功 (Accumulated Interface Work)
→ 隔震位移 (Isolation Displacement)
```
![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Fig02_qsm_power_frequency_group_contact_combined.png)

跨案例群組的 Figure 2 用來回答第二個問題：當輸入地震被轉成 QSM Power Flow 後，它在頻率域中如何展開。這張圖應被視為頻率群接觸圖譜 (Frequency-Group Contact Map)。每一筆地震資料都有一組 QSM Power 頻率峰值；同一筆資料在圖上會形成同一條位移水準附近的多個點。這些點與 $0.5f_{\mathrm{eff}}$ 、 $f_{\mathrm{eff}}$ 、 $2f_{\mathrm{eff}}$ 、 $3f_{\mathrm{eff}}$ 、 $4f_{\mathrm{eff}}$ 的相對關係，提供了能勢如何接觸隔震系統入口頻率族的線索。更重要的是，單筆 J 圖進一步顯示：許多高位移案例的 Displacement Response Frequency 不是任意散落，而是貼近系統有效頻率及其倍頻序列。這使本文可以把 $f_{\mathrm{eff}}$ 從單一設計參數，重新理解為一組能勢入口的基準尺度。

各案例群組的分析保留分組差異，不把所有地震資料混成同一種行為。短週期脈衝、中週期脈衝、非脈衝與頻譜匹配資料，雖然都可被放在同一套 QSM 讀法中，但它們的能勢進入方式、介面轉換方式與位移顯化方式並不相同。因此，本文在各組分析中同時閱讀兩種圖：一種是分組相關性圖，用來看該組的加速度、速度、能勢、做功與位移關係；另一種是分組頻率群接觸圖譜 (Frequency-Group Contact Map)，用來看該組的能勢頻率如何接觸有效隔震頻率族。單筆診斷圖 (Diagnosis Figure) 則用來回到時間序列本身，檢查事件是否真的在波形中成立。其中 J 圖是本文判讀頻率顯化的核心圖面：圓點代表 QSM Power Frequency Group，方形代表 Interface Frequency Group，三角形代表 Displacement Response Frequency Group。當位移頻率在高位移案例中呈現接近 $f_{\mathrm{eff}}$ 、 $2f_{\mathrm{eff}}$ 、 $3f_{\mathrm{eff}}$ 或其低階分量的整齊序列時，代表位移不是隨機振盪，而是隔震系統有效頻率族被能勢場推動後的顯化結果。

---

# 三、跨案例群組 Group1–4 的總體證據：從輸入指標到介面做功

跨案例群組 Group1–4 的 Figure 1 給出第一個很直接的結果：輸入加速度峰值 (Input Acceleration Peak) 與量測隔震位移峰值 (Measured IsoDisp Peak) 的相關性很弱。

- 輸入加速度峰值 (Input Acceleration Peak)：Pearson r ≈ 0.051，Spearman ρ ≈ 0.019

這代表在這批實驗資料中，單純看加速度峰值，幾乎無法判斷隔震層最後會被推到多大位移。這與原論文的問題意識一致：對隔震系統而言，平均反應譜加速度或加速度峰值不應被視為唯一充分指標。

當分析轉向 Input Velocity Peak 後，資料秩序明顯提高：

- 輸入速度峰值 (Input Velocity Peak)：Pearson r ≈ 0.547，Spearman ρ ≈ 0.586

這表示隔震位移與地震波是否具有推動滑移的速度成分有關。這也呼應原論文對 velocity pulse 與 pulse period 的重視。隔震層不是一般固定構件，它的反應核心是相對位移；能否把隔震層推開，速度脈衝自然比瞬時加速度峰值更接近問題核心。

但 QSM 的重點不只是在加速度與速度之間選一個比較好的指標。真正的轉換，是將兩者合成：


$$
P_{\mathrm{in}}(t)=a(t)v(t)
$$


在本文中，這個量被視為輸入端 QSM Power Flow 代理量。它把加速度的變化能力與速度的傳遞方向合起來，使地震輸入不再只是「多大」的問題，而是「是否形成能勢流」的問題。

跨案例群組的結果顯示：

- 輸入端 QSM Power peak：Pearson r ≈ 0.424，Spearman ρ ≈ 0.466
- 輸入端一秒能勢波包 (Input-Side 1s QSM Power Packet)：Pearson r ≈ 0.461，Spearman ρ ≈ 0.448

這些數值本身不是最強，但它們完成了一個關鍵轉向：地震輸入從運動量測變成能勢事件。真正最強的結果出現在介面層：

- 量測介面做功波包 (Measured Interface Power/Work Packet)：Pearson r ≈ 0.729，Spearman ρ ≈ 0.810
- 累積介面做功 (Accumulated Interface Work)：Pearson r ≈ 0.595，Spearman ρ ≈ 0.698

這是整篇文章最重要的總體證據。它顯示隔震位移不是只由輸入端加速度或速度決定，而是當輸入能勢進入隔震介面，形成實際 Interface Power / Work Exchange 後，才與位移峰值呈現更清楚的關係。

換句話說，輸入地震波必須經過三層轉換：


$$
a(t),v(t)
\rightarrow P_{\mathrm{in}}(t)=a(t)v(t)
\rightarrow F_{\mathrm{interface}}(t)v_{\mathrm{rel}}(t)
\rightarrow u_{\mathrm{iso}}(t)
$$


這就是本文對原實驗資料的第一個 QSM 結論：隔震位移是能勢通過介面後的顯化，而非輸入加速度的直接映射。

---

# 四、Group1：短週期脈衝案例中的時間同步與位移顯化

Group1 是短週期脈衝案例。它不是位移最大的一組，但非常適合用來建立 QSM 的時間事件觀點。

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group1/Group1_Fig01_core_power_viewpoint_transformation.png)

在 Group1 Figure 1 中，Input Acceleration Peak 與 隔震位移峰值 (IsoDisp peak) 的關係很弱，甚至呈現負相關：


Pearson r ≈ -0.217，Spearman ρ ≈ -0.127。

進入 Input Velocity Peak 後，關係變得非常清楚：


Pearson r ≈ 0.854，Spearman ρ ≈ 0.733。

這代表 Group1 的位移不是由加速度峰值決定，而更接近速度脈衝的推動效果。接著看 QSM Power：

- 輸入端 QSM Power peak：Pearson r ≈ 0.757，Spearman ρ ≈ 0.794
- 輸入端一秒能勢波包 (Input-Side 1s QSM Power Packet)：Pearson r ≈ 0.840，Spearman ρ ≈ 0.624
- 量測介面做功波包 (Measured Interface Power/Work Packet)：Pearson r ≈ 0.901，Spearman ρ ≈ 0.964
- 累積介面做功 (Accumulated Interface Work)：Pearson r ≈ 0.782，Spearman ρ ≈ 0.782

Group1 的最大價值在於：它不只相關性漂亮，時間上也非常有力。許多案例中，QSM Power Packet peak 與 displacement peak 非常接近。這表示位移峰值不是整段地震能量慢慢平均累積出來，而是在關鍵短時間窗內，由能勢波包進入介面後快速推動形成。

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group1/Group1_Fig02_qsm_power_frequency_group_contact_combined.png)

Group1 Figure 2 是理解短週期脈衝組的重要圖。它顯示，Group1 的高位移案例並不是只集中在單一頻率點，而是在有效隔震頻率族附近與其倍頻帶上形成多點接觸。上半圖保留完整 QSM Power Frequency Group，可以看到同一筆資料在固定 IsoDisp 水準上展開成多個頻率點；下半圖則放大靠近 $0.5f_{\mathrm{eff}}$ 、 $f_{\mathrm{eff}}$ 、 $2f_{\mathrm{eff}}$ 、 $3f_{\mathrm{eff}}$ 、 $4f_{\mathrm{eff}}$ 的區域。這張圖的重點不是宣稱某一個倍頻單獨控制位移，而是顯示短週期脈衝會把能勢推入一組頻率入口，最後再由隔震系統轉化為較低頻的位移反應。

從圖中可見，RSN1013 與 RSN4847 形成 Group1 的高位移橫排，且它們的 QSM Power 頻率點同時接觸接近 $2f_{\mathrm{eff}}$ 、 $3f_{\mathrm{eff}}$ 、 $4f_{\mathrm{eff}}$ 的區域。這說明短週期脈衝雖然在時間上是一個短促事件，但在能勢頻率上並不單薄；它會以一組頻率群進入系統。中低位移案例如 RSN148、RSN4102、RSN4100 則同樣有頻率群接觸，但其位移水準較低，表示頻率接觸本身不是充分條件，仍必須與 Power Packet 強度、介面做功交換與時間同步性一起閱讀。

因此，Group1 Figure 2 應放在 Group1 Figure 1 之後閱讀。Figure 1 證明 Group1 的位移更接近 V、QSM Power Packet 與 Interface Work；Figure 2 則補上頻率層的說明：這些能勢不是只以單一有效頻率進入隔震層，而是透過有效頻率族與倍頻入口形成接觸。這正是 QSM 要強調的地方： $f_{\mathrm{eff}}$ 不是終點，而是能勢進入隔震系統的入口座標。

## Group1 代表案例

### RSN784：低位移案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group1/RSN784_1_0_21_V25_core_diagnosis.png)

RSN784 的量測隔震位移峰值為 73.06 mm，峰值時間約為 11.95 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.271 g
- 輸入速度峰值 (Input Velocity Peak)：0.38 m/s
- 瞬時能勢峰值 (QSM Power Shock)：0.561 W/kg
- 一秒能勢波包 (1s Power Packet)：0.217 J/kg；與位移峰值時間差 (Lag)：-0.051 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：3.708 kJ；與位移峰值時間差 (Lag)：-0.008 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：1.749;2.249;2.749;3.873;4.998;0.500;4.498;5.873 Hz
- Interface Frequency Group：0.250;1.749;2.749;3.873 Hz
- Displacement Response Frequency Group：0.250;0.625 Hz

這筆資料屬於低位移反應。它的價值在於提供低反應對照，說明頻率群接觸本身不是充分條件；能勢量級、介面做功交換與位移頻率顯化必須一起成立，才會形成大位移。

### RSN1013：中等位移案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group1/RSN1013_1_0_21_V25_core_diagnosis.png)

RSN1013 的量測隔震位移峰值為 150.2 mm，峰值時間約為 3.297 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.343 g
- 輸入速度峰值 (Input Velocity Peak)：0.6 m/s
- 瞬時能勢峰值 (QSM Power Shock)：1.361 W/kg
- 一秒能勢波包 (1s Power Packet)：0.372 J/kg；與位移峰值時間差 (Lag)：2.797 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：5.504 kJ；與位移峰值時間差 (Lag)：2.797 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：3.109;1.110;2.442;0.666;1.998;1.554;7.105;4.219 Hz
- Interface Frequency Group：0.666;1.554;2.442 Hz
- Displacement Response Frequency Group：0.137;0.274;0.411;0.548;0.685;0.822;0.959 Hz

這筆資料屬於中等位移反應。它的價值在於提供對照：即使存在 QSM Power Frequency Group 與 Interface Frequency Group，若介面做功波包或位移接收條件不足，位移仍不會被推到最高層級。

### RSN4102：低位移案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group1/RSN4102_1_0_21_V25_core_diagnosis.png)

RSN4102 的量測隔震位移峰值為 44.58 mm，峰值時間約為 0.836 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.461 g
- 輸入速度峰值 (Input Velocity Peak)：0.393 m/s
- 瞬時能勢峰值 (QSM Power Shock)：0.589 W/kg
- 一秒能勢波包 (1s Power Packet)：0.204 J/kg；與位移峰值時間差 (Lag)：-0.031 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：1.708 kJ；與位移峰值時間差 (Lag)：0.012 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：1.026;1.437;2.258;2.669;0.616;6.159;3.079;4.311 Hz
- Interface Frequency Group：2.280;1.866 Hz
- Displacement Response Frequency Group：1.033;0.620 Hz

這筆資料屬於低位移反應。它的價值在於提供低反應對照，說明頻率群接觸本身不是充分條件；能勢量級、介面做功交換與位移頻率顯化必須一起成立，才會形成大位移。

## Group1 小結

Group1 顯示，在短週期脈衝輸入下，加速度不是主要解釋軸，速度是更好的入口，而 QSM Power Packet 與 Interface Power / Work Exchange 才真正接近位移事件。它最重要的證據是時間：QSM peak 與 displacement peak 常常非常接近。這說明隔震位移是能勢波包進入介面後的瞬時顯化事件。

---

# 五、Group2：中週期脈衝案例中的能勢波包與大位移放大

Group2 是中週期脈衝組，也是最適合展示「速度脈衝 → Power Packet → Interface Exchange → 大位移」的組別。原論文指出 medium $T_p$ 的脈衝型地震會造成較大的隔震位移。QSM 的分析可以補上更具機制性的說明：中週期速度脈衝更容易把輸入能勢整理成有效 Power Packet，並在介面形成強烈做功交換。

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group2/Group2_Fig01_core_power_viewpoint_transformation.png)

Group2 Figure 1 中，Input Acceleration Peak 幾乎沒有解釋力：


Pearson r ≈ 0.059，Spearman ρ ≈ -0.200。

Input Velocity Peak 明顯提高：


Pearson r ≈ 0.777，Spearman ρ ≈ 0.806。

輸入端 QSM Power peak 只有中等關係：


Pearson r ≈ 0.468，Spearman ρ ≈ 0.406。

但輸入端 QSM 1s Power Packet 明顯更好：


Pearson r ≈ 0.704，Spearman ρ ≈ 0.770。

這表示 Group2 的重點不在瞬間 shock，而在一段可持續的能勢波包。最強證據仍然出現在介面：


Interface Power/Work Packet：Pearson r ≈ 0.889，Spearman ρ ≈ 0.794。


相較之下，Accumulated Interface Work 為：


Pearson r ≈ 0.539，Spearman ρ ≈ 0.527。

這個差異很關鍵。它表示 Group2 的大位移不是由總能量累積單獨決定，而是由有效時間窗內的 Interface Power/Work Packet 決定。也就是說，能勢是否集中進入隔震介面，比最後總共累積多少更接近位移峰值的形成。

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group2/Group2_Fig02_qsm_power_frequency_group_contact_combined.png)

Group2 Figure 2 顯示中週期脈衝組的核心特徵：位移水準整體明顯高於 Group1，且許多高位移資料在 $2f_{\mathrm{eff}}$ 、 $3f_{\mathrm{eff}}$ 、 $4f_{\mathrm{eff}}$ 附近仍保有 QSM Power Frequency Group的接觸。這與 Group1 不同。Group1 更像短時間能勢事件；Group2 則呈現較長週期速度脈衝把能勢持續推入隔震系統，形成更大的介面做功與更大的位移顯化。

圖中 RSN170 是最醒目的高位移案例。它在多個 QSM Power 頻率峰值 上維持高 IsoDisp 水準，代表大位移不是由單一頻率點造成，而是由一組能勢頻率共同參與。RSN1165、RSN802、RSN983 等案例也落在中高位移層，顯示中週期脈衝的危險性不只是速度峰值高，而是它的能勢頻率群較容易與隔震系統入口頻率族形成有效接觸。

相對地，RSN3317、RSN8130、RSN1085 等低位移案例也能看到頻率點，但其橫排位移水準明顯較低。這表示 Group2 的判讀不能停在「有沒有接觸 $f_{\mathrm{eff}}$ 或倍頻」，而要同時看接觸之後是否形成足夠強的 Power Packet 與 Interface Work packet。換句話說，Group2 Figure 2 的功能，是把「中週期脈衝造成大位移」從單純週期描述，推進到「能勢頻率群如何進入隔震介面」的描述。

## Group2 代表案例

### RSN170：高位移案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group2/RSN170_1_0_31_V25_core_diagnosis.png)

RSN170 的量測隔震位移峰值為 588.7 mm，峰值時間約為 4 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.26 g
- 輸入速度峰值 (Input Velocity Peak)：0.858 m/s
- 瞬時能勢峰值 (QSM Power Shock)：1.508 W/kg
- 一秒能勢波包 (1s Power Packet)：0.612 J/kg；與位移峰值時間差 (Lag)：-0.809 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：28.51 kJ；與位移峰值時間差 (Lag)：-0.734 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：0.500;1.500;2.250;1.000;2.750;3.750;4.375;6.000 Hz
- Interface Frequency Group：0.500;1.499;1.000;2.249 Hz
- Displacement Response Frequency Group：0.125;0.250;0.375;0.500 Hz

這筆資料的關鍵在於，它同時呈現較大的位移反應與明顯的介面做功交換。從 J 圖閱讀時，Displacement Response Frequency Group 不是任意散落，而是集中在低頻序列，並與有效隔震頻率族形成可讀的關係。因此，RSN170 適合作為「能勢進入介面後顯化為大位移」的代表案例。

### RSN983：中高位移案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group2/RSN983_1_0_22_V25_core_diagnosis.png)

RSN983 的量測隔震位移峰值為 374.4 mm，峰值時間約為 2.133 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.342 g
- 輸入速度峰值 (Input Velocity Peak)：0.688 m/s
- 瞬時能勢峰值 (QSM Power Shock)：1.685 W/kg
- 一秒能勢波包 (1s Power Packet)：0.496 J/kg；與位移峰值時間差 (Lag)：0.93 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：13.44 kJ；與位移峰值時間差 (Lag)：0.84 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：3.265;0.768;2.881;2.305;1.729;3.649;5.762;4.225 Hz
- Interface Frequency Group：0.755;1.699;3.210;2.266;2.832;3.587 Hz
- Displacement Response Frequency Group：0.326 Hz

這筆資料顯示，中高位移不一定只由單一瞬時峰值決定，而要同時看 Power Packet、Measured Interface Power/Work Packet 與頻率群轉換。它適合作為中間層案例，用來說明能勢強度、介面交換與位移顯化之間不是單一線性關係。

### RSN8130：中等位移案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group2/RSN8130_1_0_21_V25_core_diagnosis.png)

RSN8130 的量測隔震位移峰值為 165.0 mm，峰值時間約為 4.938 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.242 g
- 輸入速度峰值 (Input Velocity Peak)：0.528 m/s
- 瞬時能勢峰值 (QSM Power Shock)：0.645 W/kg
- 一秒能勢波包 (1s Power Packet)：0.286 J/kg；與位移峰值時間差 (Lag)：-0.699 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：7.074 kJ；與位移峰值時間差 (Lag)：-0.641 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：1.374;0.625;1.874;2.374;3.248;2.874;3.873;6.247 Hz
- Interface Frequency Group：0.625;1.374;1.874;2.374 Hz
- Displacement Response Frequency Group：0.250;1.000 Hz

這筆資料屬於中等位移反應。它的價值在於提供對照：即使存在 QSM Power Frequency Group 與 Interface Frequency Group，若介面做功波包或位移接收條件不足，位移仍不會被推到最高層級。

## Group2 小結

Group2 是 QSM Power Flow 最清楚的中週期脈衝證據。它說明中週期速度脈衝不是只讓速度峰值變大，而是更容易形成能夠推動隔震層的 Power Packet。當這個 packet 進入介面，並形成強 Interface Power / Work Exchange，隔震層就會被推到大位移。

---

# 六、Group3：非脈衝案例中的分散能勢場與低頻位移顯化

Group3 是 non-pulse-like group。傳統上，這組容易被視為脈衝組的對照。但 QSM 的分析顯示，Group3 不應只被理解為「沒有脈衝」。它更像是一種分散能勢場：能勢不以清楚單一速度脈衝進入系統，而是透過更長時間、更寬頻率群、更分散的方式進入隔震介面，最後仍可能顯化為大位移。

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group3/Group3_Fig01_core_power_viewpoint_transformation.png)

Group3 Figure 1 中，Input Acceleration Peak 與 隔震位移峰值 (IsoDisp peak) 的關係不高：


Pearson r ≈ 0.287，Spearman ρ ≈ 0.370。

Input Velocity Peak 明顯提升：


Pearson r ≈ 0.559，Spearman ρ ≈ 0.733。

QSM Power peak 顯示出有趣的排序性：


Pearson r ≈ 0.486，Spearman ρ ≈ 0.794。

輸入端 QSM Power Packet：


Pearson r ≈ 0.387，Spearman ρ ≈ 0.733。

這代表 Group3 的 Power 指標不一定呈現乾淨線性比例，但能分辨位移層級。這與 Group2 很不同。Group2 比較像一段中週期脈衝直接形成強 packet；Group3 則像分散能勢在頻率群與介面中重新組合。

Interface Power/Work Packet：


Pearson r ≈ 0.586，Spearman ρ ≈ 0.576。

Accumulated Interface Work：


Pearson r ≈ 0.533，Spearman ρ ≈ 0.576。

這些關係不像 Group2 那麼強，但合理。非脈衝輸入的能勢不集中於單一短時間窗，而是以較分散方式進入系統。因此，Group3 的分析不能只盯著單一 peak 或單一 packet，必須同時看 Input-Side Power、Interface Exchange、Frequency Group 與 displacement response。

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group3/Group3_Fig02_qsm_power_frequency_group_contact_combined.png)

Group3 Figure 2 是本文中最容易被低估、也最重要的分組頻率圖。因為 Group3 被原研究歸類為 non-pulse-like，很容易被讀成「沒有明顯脈衝，因此比較不危險」。但這張圖顯示，非脈衝並不代表沒有能勢場；它代表能勢不是以單一清楚速度脈衝進入，而是以更分散、更寬頻、更長時間的方式進入。

圖中 RSN1164FP 與 RSN1233FN 形成非常高的位移水準，並且它們的 QSM Power Frequency Group 不是只貼在 $f_{\mathrm{eff}}$ 附近，而是展開到較寬的頻率範圍。這說明非脈衝地震波可以透過寬頻能勢場與隔震系統作用，最後仍顯化為極大位移。這一點很關鍵：若只用 pulse / non-pulse 的分類，RSN1164FP 可能被看成對照組；但在 QSM 讀法中，它反而是分散能勢場造成大位移的強證據。

Group3 Figure 2 也顯示，多數中低位移案例在 0.5–1.5 Hz 附近有密集接觸，同時也延伸到 2 Hz 以上。這代表非脈衝組的位移不是由一條乾淨的頻率線控制，而是由能勢場在多頻率入口上的分布、介面選擇與低頻位移顯化共同決定。因此，Group3 的分析要比 Group1、Group2 更小心：不能只看 peak，也不能只看一秒 packet，必須把 Frequency Group 與 Interface Exchange 一起看。

這張圖支撐本文一個重要推論：隔震系統面對的不是「某一筆地震有沒有脈衝」這麼簡單，而是該地震波是否形成足以進入系統、穿過介面、最後推動位移的能勢場。

## Group3 代表案例

### RSN175FN：中高位移案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group3/RSN175FN_1_0_31_V25_core_diagnosis.png)

RSN175FN 的量測隔震位移峰值為 336.6 mm，峰值時間約為 7.113 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.346 g
- 輸入速度峰值 (Input Velocity Peak)：0.706 m/s
- 瞬時能勢峰值 (QSM Power Shock)：1.718 W/kg
- 一秒能勢波包 (1s Power Packet)：0.624 J/kg；與位移峰值時間差 (Lag)：0.934 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：10.77 kJ；與位移峰值時間差 (Lag)：-5.934 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：3.500;2.500;0.875;1.125;1.625;4.375;8.626;6.375 Hz
- Interface Frequency Group：0.250;1.499;2.249;1.999 Hz
- Displacement Response Frequency Group：0.125;0.250;0.375;0.500;0.625 Hz

這筆資料顯示，中高位移不一定只由單一瞬時峰值決定，而要同時看 Power Packet、Measured Interface Power/Work Packet 與頻率群轉換。它適合作為中間層案例，用來說明能勢強度、介面交換與位移顯化之間不是單一線性關係。

### RSN878FN：中等位移案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group3/RSN878FN_1_0_31_V25_core_diagnosis.png)

RSN878FN 的量測隔震位移峰值為 140.3 mm，峰值時間約為 40.91 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.275 g
- 輸入速度峰值 (Input Velocity Peak)：0.37 m/s
- 瞬時能勢峰值 (QSM Power Shock)：0.572 W/kg
- 一秒能勢波包 (1s Power Packet)：0.144 J/kg；與位移峰值時間差 (Lag)：2.246 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：4.392 kJ；與位移峰值時間差 (Lag)：0.945 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：0.750;1.249;1.499;2.124;2.624;3.249;1.874;3.623 Hz
- Interface Frequency Group：0.750;1.125;1.499;2.124 Hz
- Displacement Response Frequency Group：0.250;0.750 Hz

這筆資料屬於中等位移反應。它的價值在於提供對照：即使存在 QSM Power Frequency Group 與 Interface Frequency Group，若介面做功波包或位移接收條件不足，位移仍不會被推到最高層級。

### RSN1164FP：高位移案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group3/RSN1164FP_1_0_31_V25_core_diagnosis.png)

RSN1164FP 的量測隔震位移峰值為 885.3 mm，峰值時間約為 59.37 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.416 g
- 輸入速度峰值 (Input Velocity Peak)：0.537 m/s
- 瞬時能勢峰值 (QSM Power Shock)：1.339 W/kg
- 一秒能勢波包 (1s Power Packet)：0.327 J/kg；與位移峰值時間差 (Lag)：3.715 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：10.05 kJ；與位移峰值時間差 (Lag)：5.203 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：2.749;4.873;3.124;7.247;1.749;0.875;5.748;1.249 Hz
- Interface Frequency Group：0.250;0.875;1.249;0.625;2.749;1.749;1.999;2.499 Hz
- Displacement Response Frequency Group：0.125;0.250;0.375;0.500 Hz

這筆資料的關鍵在於，它同時呈現較大的位移反應與明顯的介面做功交換。從 J 圖閱讀時，Displacement Response Frequency Group 不是任意散落，而是集中在低頻序列，並與有效隔震頻率族形成可讀的關係。因此，RSN1164FP 適合作為「能勢進入介面後顯化為大位移」的代表案例。

## Group3 小結

Group3 的意義是把 QSM 從脈衝案例推展到非脈衝能勢場。非脈衝地震波不是沒有能勢，而是能勢以分散場的形式進入系統。當這些分散頻率群經由介面轉換成隔震系統的低頻位移反應時，仍可能形成極大位移。

---

# 七、Group4：頻譜匹配案例中的能勢差異

Group4 是 Spectrally Matched Group。它對本文非常重要，因為它直接碰到工程設計中很核心的問題：如果地震波在反應譜座標上已經被調整得相近，實際隔震位移是否也應該相近？

QSM 的回答是：不一定。反應譜相似，不代表 QSM Power Flow、Interface Work exchange 與 frequency-group contact 相同。

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group4/Group4_Fig01_core_power_viewpoint_transformation.png)

Group4 Figure 1 中，Input Acceleration Peak 與 隔震位移峰值 (IsoDisp peak) 仍然偏弱：


Pearson r ≈ 0.265，Spearman ρ ≈ 0.127。

Input Velocity Peak 提高到：


Pearson r ≈ 0.496，Spearman ρ ≈ 0.479。

輸入端 QSM Power peak：


Pearson r ≈ 0.470，Spearman ρ ≈ 0.442。

輸入端 QSM 1s Power Packet：


Pearson r ≈ 0.448，Spearman ρ ≈ 0.418。

最關鍵仍然是 Interface Power/Work Packet：


Pearson r ≈ 0.676，Spearman ρ ≈ 0.576。

它比 acceleration、velocity、輸入端 QSM Power 更接近 隔震位移峰值 (IsoDisp peak)。這說明 Group4 的差異真正開始在介面層被放大：輸入端看起來已經被頻譜匹配整理過，但到了隔震介面，Interface Power / Work Exchange 仍顯示不同的能勢交換強度。

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group4/Group4_Fig02_qsm_power_frequency_group_contact_combined.png)

Group4 Figure 2 是本文對 頻譜匹配 最直接的補充證據。這組資料在反應譜上經過匹配，照理說傳統讀法會期待它們具有較接近的反應需求；但頻率群接觸圖譜 (Frequency-Group Contact Map) 顯示，即使反應譜被整理過，QSM Power Frequency Group 仍然保有明顯差異。

圖中 RSN802M 形成最高位移橫排，RSN803M 與 RSN1085M 也位於高位移層，而 RSN8130M 等案例位移較低。這些差異不是 Figure 1 中 Input Acceleration Peak 可以單獨解釋的，也不是 頻譜匹配 之後自然消失的。Group4 Figure 2 顯示，頻譜匹配資料 在 $f_{\mathrm{eff}}$ 及其倍頻附近仍有不同的接觸密度與能勢分布；某些資料能把 QSM Power Frequency Group 有效帶入隔震系統，某些資料則不能。

這張圖的意義，不是說 頻譜匹配 沒有價值，而是說它控制的是反應譜外觀，不保證控制能勢路徑。對隔震系統而言，真正要進一步確認的是：匹配後的地震波是否仍在時間窗內形成 Power Packet，是否在介面形成做功交換，是否在頻率群上接觸有效隔震頻率族，最後是否轉成低頻位移顯化。

因此，Group4 Figure 2 應被視為本文對工程設計語言的提醒：反應譜相似，不等於能勢相似；頻率群相似，也不必然等於介面做功相似。隔震位移要回到能勢通過介面的實際路徑來判讀。

## Group4 代表案例

### RSN170M：中高位移頻譜匹配案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group4/RSN170M_1_0_31_V25_core_diagnosis.png)

RSN170M 的量測隔震位移峰值為 397.9 mm，峰值時間約為 61.37 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.209 g
- 輸入速度峰值 (Input Velocity Peak)：0.53 m/s
- 瞬時能勢峰值 (QSM Power Shock)：0.75 W/kg
- 一秒能勢波包 (1s Power Packet)：0.275 J/kg；與位移峰值時間差 (Lag)：8.645 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：12.85 kJ；與位移峰值時間差 (Lag)：1.785 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：1.624;0.500;2.874;1.249;2.374;2.124;3.249;3.623 Hz
- Interface Frequency Group：0.375;1.499 Hz
- Displacement Response Frequency Group：0.125;0.250;0.375 Hz

這筆資料顯示，中高位移不一定只由單一瞬時峰值決定，而要同時看 Power Packet、Measured Interface Power/Work Packet 與頻率群轉換。它適合作為中間層案例，用來說明能勢強度、介面交換與位移顯化之間不是單一線性關係。

### RSN802M：高位移頻譜匹配案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group4/RSN802M_1_0_31_V25_core_diagnosis.png)

RSN802M 的量測隔震位移峰值為 659.7 mm，峰值時間約為 25.85 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.39 g
- 輸入速度峰值 (Input Velocity Peak)：0.661 m/s
- 瞬時能勢峰值 (QSM Power Shock)：1.28 W/kg
- 一秒能勢波包 (1s Power Packet)：0.503 J/kg；與位移峰值時間差 (Lag)：19.48 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：22.15 kJ；與位移峰值時間差 (Lag)：-1.176 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：2.500;1.125;3.250;1.625;0.625;4.750;3.750;6.375 Hz
- Interface Frequency Group：0.250;0.750 Hz
- Displacement Response Frequency Group：0.125;0.250 Hz

這筆資料的關鍵在於，它同時呈現較大的位移反應與明顯的介面做功交換。從 J 圖閱讀時，Displacement Response Frequency Group 不是任意散落，而是集中在低頻序列，並與有效隔震頻率族形成可讀的關係。因此，RSN802M 適合作為「能勢進入介面後顯化為大位移」的代表案例。

### RSN8130M：中等位移頻譜匹配案例

![image](https://github.com/alaric-kuo/Quantum-Structural-Mechanics-Validation/blob/main/data/Group4/RSN8130M_1_0_31_V25_core_diagnosis.png)

RSN8130M 的量測隔震位移峰值為 118.4 mm，峰值時間約為 34.83 s。其主要數值如下：

- 輸入加速度峰值 (Input Acceleration Peak)：0.312 g
- 輸入速度峰值 (Input Velocity Peak)：0.323 m/s
- 瞬時能勢峰值 (QSM Power Shock)：0.452 W/kg
- 一秒能勢波包 (1s Power Packet)：0.164 J/kg；與位移峰值時間差 (Lag)：19.04 s
- 量測介面做功波包 (Measured Interface Power/Work Packet)：3.593 kJ；與位移峰值時間差 (Lag)：-0.613 s

其頻率群收斂比較如下：

- QSM Power Frequency Group：1.999;2.749;3.499;1.499;0.750;6.747;7.497;4.248 Hz
- Interface Frequency Group：0.750;1.249 Hz
- Displacement Response Frequency Group：0.375 Hz

這筆資料屬於中等位移反應。它的價值在於提供對照：即使存在 QSM Power Frequency Group 與 Interface Frequency Group，若介面做功波包或位移接收條件不足，位移仍不會被推到最高層級。

## Group4 小結

Group4 的核心貢獻，是指出 頻譜匹配 的盲點：它對齊的是反應譜，不一定對齊能勢通道。它控制的是輸入在設計譜上的外觀，但結構真正承受的是時間波包、速度推動、Power Flow、介面做功與頻率群接觸。這也是為什麼 頻譜匹配組 仍然會呈現明顯位移差異。

---

# 八、結論：地震波作為能勢場，隔震位移作為介面顯化

本文以球面滑動隔震系統的真實實驗資料，對量子結構力學進行第一次實證性驗證。這項工作並不是為了取代原研究，而是承接原研究最重要的發現：只看加速度或平均反應譜加速度，無法充分解釋隔震位移。

本文的第一個結論，是原研究的資料確實支持「只看加速度不夠」這件事。跨案例群組 Group1–4 的總結圖顯示，輸入加速度峰值 (Input Acceleration Peak) 與量測隔震位移峰值 (Measured IsoDisp Peak) 的相關性極低。當分析轉向 Input Velocity Peak，關係明顯提高。這說明隔震位移與速度脈衝、推動能力與時間持續性有關。

第二個結論，是 QSM 的視角轉換具有資料合理性。將 $a(t)$ 與 $v(t)$ 合成為 $P_{\mathrm{in}}(t)=a(t)v(t)$ 後，地震輸入不再只是加速度或速度序列，而成為一個隨時間進入結構的能勢流。當這個能勢流被整理為 Power Packet，並進一步進入隔震介面形成 $F_{\mathrm{interface}}(t)v_{\mathrm{rel}}(t)$ 的 Interface Power / Work Exchange 時，它與位移反應的關係變得最清楚。

第三個結論，是隔震位移背後的頻率不應只被壓縮成單一有效頻率。 $f_{\mathrm{eff}}$ 很重要，但它是入口尺度，不是完整答案。實際反應包含 QSM Power Frequency Group、Interface Frequency Group 與 Displacement Response Frequency Group的連續轉換。各組 Figure 2 的意義正在這裡：Group1 顯示短週期脈衝如何以時間事件方式接觸有效頻率族；Group2 顯示中週期脈衝如何透過較強能勢波包與倍頻入口形成大位移；Group3 顯示非脈衝地震波仍可能以分散寬頻能勢場造成大位移；Group4 顯示頻譜匹配不等於能勢匹配。

更關鍵的是單筆診斷圖中的頻率群收斂比較。許多高位移案例的位移反應頻率並不是無規則散布，而是靠近原本系統有效頻率及其倍頻所形成的整齊序列。這是本文最重要的驗證證據之一。它說明隔震系統的有效頻率不應被理解為單一數字，而是一個能勢入口族；地震波的 QSM Power Frequency Group 進入系統後，會經由介面選擇與轉換，最後在 Displacement Response Frequency Group 中顯化。換言之，J 圖所呈現的不是單一頻率命中，而是一組能勢入口被連續接觸後，位移在系統有效頻率族中顯化的結果。

因此，本文對 QSM 的核心論述可以收束為一句話：

> 地震波對結構物而言，是一個進入系統的能勢場；當結構無法在這個能勢場轉化為穩定通道時，能勢會在介面形成做功交換，並顯化為隔震位移。

這句話也是本文對原實驗資料的主要貢獻。原研究已經指出，只看加速度不夠；本文進一步說明，問題不只在於少看了速度，也在於傳統觀察方式還沒有完整描述能勢如何進入系統、穿過介面、接觸頻率群，並最後成為位移。QSM Power Flow 提供的不是單一新指標，而是一條新的資料閱讀路徑：從 輸入運動 (Input Motion)，走向 Power Packet，再走向 Interface Exchange，最後走向 頻率群顯化 (Frequency-Group Manifestation)。

對工程應用而言，這代表未來隔震系統評估不應只問「輸入地震有多大」，也要問「地震能勢如何進入系統」。如果一套隔震系統能把輸入能勢導成通道、分流、耗散，它就有機會降低位移顯化；如果不能，能勢便可能集中在介面，推動隔震層產生大位移。

這就是本文用真實實驗資料為量子結構力學建立的第一個實證基礎。
