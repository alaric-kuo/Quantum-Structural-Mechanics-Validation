# 以球面滑動隔震實驗資料驗證量子結構力學

**作者：郭瀚嶸**
**日期：2026.05.10**

## 摘要
本文以《An Experimental Study of a Spherical Sliding Isolation System Subjected to Pulse-Like Ground Motions》公開之球面滑動隔震系統實驗資料為基礎，嘗試以量子結構力學 (Quantum Structural Mechanics, QSM) 的觀點，重新閱讀地震波對隔震位移的作用機制。原研究已指出：對隔震系統而言，只依賴加速度或平均反應譜加速度，無法充分解釋實際隔震位移；速度脈衝、脈衝週期與隔震系統有效週期，必須一併納入討論。

本文沿著原研究的實證結論往前推進。第一層檢查顯示，輸入加速度峰值與隔震位移峰值的相關性很弱；第二層檢查顯示，速度峰值與隔震位移的關係明顯提高。接著，本文將加速度與速度合成為輸入端量子結構力學能勢流 (Input-Side QSM Power Flow)，即 $P_{\mathrm{in}}(t)=a(t)v(t)$ ，並進一步觀察一秒能勢波包 (1s Power Packet)、介面能勢／做功交換 (Interface Power / Work Exchange)、累積介面做功 (Accumulated Interface Work)，以及量子結構力學能勢頻率群 (QSM Power Frequency Group) 與有效隔震頻率群 (Effective Isolation Frequency Group) 的接觸關係。

分析結果顯示，真正接近隔震位移反應的，不是輸入端單一加速度峰值或單一速度峰值，而是能勢進入隔震介面後形成的介面能勢／做功交換。跨案例群組 Group1–4 的總結圖顯示，量測介面做功波包 (Measured Interface Power/Work Packet) 與量測隔震位移峰值 (measured upper-lower isolation displacement peak) 呈現最清楚的關係。另一方面，頻率群圖譜也顯示，隔震反應不能只用一個有效頻率或有效週期概括； $f_{\mathrm{eff}}$ 是入口尺度，背後仍存在 QSM Power Frequency Group、Interface Frequency Group 與 Displacement Response Frequency 案例群組的轉換關係。尤其在單筆診斷圖 (Diagnosis Figure) 的頻率群收斂比較中，高位移案例常可看到位移反應頻率貼近 $f_{\mathrm{eff}}$ 及其整齊倍頻序列。這表示有效頻率不是單一控制值，而是一組可被能勢接觸、轉換與顯化的入口頻率族。

本文的核心結論是：地震波對隔震系統而言，可以被視為一個進入結構的能勢場。當此能勢場無法被隔震系統順利轉化為穩定通道時，它會在介面形成做功交換，並顯化為可觀測的隔震位移。這是本文對原實驗資料的 QSM 解讀，也是量子結構力學第一次以真實實驗資料建立機制性驗證的嘗試。

---

## 名詞說明
**量子結構力學 (Quantum Structural Mechanics, QSM)**
本文使用的結構分析觀點。它把結構視為能勢進入、傳遞、交換、耗散與顯化的系統，而不只是一個承受外力並產生位移的剛度系統。

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
指本文針對單一地震資料所繪製的十子圖診斷圖。它同時呈現加速度、速度、QSM Power Flow、Power Packet、Interface Power / Work Exchange、Isolation Displacement 與 Frequency-Group Closure。本文後續提到 J 圖時，指的就是 Diagnosis Figure 中用來比較 QSM Power Frequency Group、Interface Frequency Group 與 Displacement Response Frequency 案例群組的最後一個子圖。

**頻率群收斂比較 (Frequency-Group Closure)**
指單筆診斷圖中用來比較 QSM Power Frequency Group、Interface Frequency Group 與 Displacement Response Frequency 案例群組的圖面。它的重點不是只看三種頻率是否相近，而是看位移反應是否形成接近 $f_{\mathrm{eff}}$ 及其倍頻的整齊序列。若高位移案例中出現這種序列，代表隔震系統並非只從單一有效頻率接收能勢，而是透過一組有效頻率入口被推動。

**時間差 (Lag)**
指兩個事件峰值之間的時間距離，例如 QSM Power Packet peak 與隔震位移峰值之間的時間差。本文用它判斷能勢事件與位移事件是否在時間上接近。

**瞬時能勢峰值 (QSM Power Shock)**
指 QSM Power Flow 歷時中較尖銳的瞬間能勢峰值。它可提示地震輸入中短時間的強烈能勢衝擊，但本文不把它視為唯一判斷依據。

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

[建議置入 Figure 1：跨案例群組 Group1–4 的總體相關性與 QSM 視角轉換]

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

[建議置入 Figure 2：跨案例群組 Group1–4 的 QSM Power 頻率群接觸圖譜 (Frequency-Group Contact Map)]

跨案例群組的 Figure 2 用來回答第二個問題：當輸入地震被轉成 QSM Power Flow 後，它在頻率域中如何展開。這張圖應被視為頻率群接觸圖譜 (Frequency-Group Contact Map)。每一筆地震資料都有一組 QSM Power 頻率峰值；同一筆資料在圖上會形成同一條位移水準附近的多個點。這些點與 $0.5f_{\mathrm{eff}}$ 、 $f_{\mathrm{eff}}$ 、 $2f_{\mathrm{eff}}$ 、 $3f_{\mathrm{eff}}$ 、 $4f_{\mathrm{eff}}$ 的相對關係，提供了能勢如何接觸隔震系統入口頻率族的線索。更重要的是，單筆 J 圖進一步顯示：許多高位移案例的 Displacement Response Frequency 不是任意散落，而是貼近系統有效頻率及其倍頻序列。這使本文可以把 $f_{\mathrm{eff}}$ 從單一設計參數，重新理解為一組能勢入口的基準尺度。

各案例群組的分析保留分組差異，不把所有地震資料混成同一種行為。短週期脈衝、中週期脈衝、非脈衝與頻譜匹配資料，雖然都可被放在同一套 QSM 讀法中，但它們的能勢進入方式、介面轉換方式與位移顯化方式並不相同。因此，本文在各組分析中同時閱讀兩種圖：一種是分組相關性圖，用來看該組的加速度、速度、能勢、做功與位移關係；另一種是分組頻率群接觸圖譜 (Frequency-Group Contact Map)，用來看該組的能勢頻率如何接觸有效隔震頻率族。單筆診斷圖 (Diagnosis Figure) 則用來回到時間序列本身，檢查事件是否真的在波形中成立。其中 J 圖是本文判讀頻率顯化的核心圖面：圓點代表 QSM Power Frequency Group，方形代表 Interface Frequency Group，三角形代表 Displacement Response Frequency Group。當位移頻率在高位移案例中呈現接近 $f_{\mathrm{eff}}$ 、 $2f_{\mathrm{eff}}$ 、 $3f_{\mathrm{eff}}$ 或其低階分量的整齊序列時，代表位移不是隨機振盪，而是隔震系統有效頻率族被能勢場推動後的顯化結果。

---

# 三、跨案例群組 Group1–4 的總體證據：從輸入指標到介面做功

跨案例群組 Group1–4 的 Figure 1 給出第一個很直接的結果：輸入加速度峰值 (Input Acceleration Peak) 與量測隔震位移峰值 (measured IsoDisp peak) 的相關性很弱。

- 輸入加速度峰值 (Input Acceleration Peak)：Pearson $r \approx 0.051$ - Spearman $\rho \approx 0.019$ 這代表在這批實驗資料中，單純看加速度峰值，幾乎無法判斷隔震層最後會被推到多大位移。這與原論文的問題意識一致：對隔震系統而言，平均反應譜加速度或加速度峰值不應被視為唯一充分指標。

當分析轉向 Input Velocity Peak，資料秩序明顯提高：

- 輸入速度峰值 (Input Velocity Peak)：Pearson $r \approx 0.547$ - Spearman $\rho \approx 0.586$ 這表示隔震位移與地震波是否具有推動滑移的速度成分有關。這也呼應原論文對 velocity pulse 與 pulse period 的重視。隔震層不是一般固定構件，它的反應核心是相對位移；能否把隔震層推開，速度脈衝自然比瞬時加速度峰值更接近問題核心。

但 QSM 的重點不只是在 加速度與速度 之間選一個比較好的指標。真正的轉換，是將兩者合成：


$$
P_{\mathrm{in}}(t)=a(t)v(t)
$$


在本文中，這個量被視為輸入端 QSM Power Flow 代理量。它把加速度的變化能力與速度的傳遞方向合起來，使地震輸入不再只是「多大」的問題，而是「是否形成能勢流」的問題。

跨案例群組的結果顯示：

- 輸入端 QSM Power peak：Pearson $r \approx 0.424$ ，Spearman $\rho \approx 0.466$ - 輸入端 QSM 1s Power Packet：Pearson $r \approx 0.461$ ，Spearman $\rho \approx 0.448$ 這些數值本身不是最強，但它們完成了一個關鍵轉向：地震輸入從運動量測變成能勢事件。真正最強的結果出現在介面層：

- 量測介面做功波包 (Measured Interface Power/Work Packet)：Pearson $r \approx 0.729$ ，Spearman $\rho \approx 0.810$ - 量測累積介面做功 (measured Accumulated Interface Work)：Pearson $r \approx 0.595$ ，Spearman $\rho \approx 0.698$ 這是整篇文章最重要的總體證據。它顯示隔震位移不是只由輸入端 加速度或速度 決定，而是當輸入能勢進入隔震介面，形成實際 Power / Work Exchange 後，才與位移峰值呈現更清楚的關係。

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

在 Group1 Figure 1 中，Input Acceleration Peak 與 隔震位移峰值 (IsoDisp peak) 的關係很弱，甚至呈現負相關：


$$
r \approx -0.217,\quad \rho \approx -0.127
$$


進入 Input Velocity Peak 後，關係變得非常清楚：


$$
r \approx 0.854,\quad \rho \approx 0.733
$$


這代表 Group1 的位移不是由加速度峰值決定，而更接近速度脈衝的推動效果。接著看 QSM Power：

- 輸入端 QSM Power peak： $r \approx 0.757,\ \rho \approx 0.794$ - 輸入端 QSM 1s Power Packet： $r \approx 0.840,\ \rho \approx 0.624$ - 量測介面做功波包 (Measured Interface Power/Work Packet)： $r \approx 0.901,\ \rho \approx 0.964$ - Accumulated Interface Work： $r \approx 0.782,\ \rho \approx 0.782$ Group1 的最大價值在於：它不只相關性漂亮，時間上也非常有力。許多案例中，QSM Power Packet peak 與 displacement peak 非常接近。這表示位移峰值不是整段地震能量慢慢平均累積出來，而是在關鍵短時間窗內，由能勢波包進入介面後快速推動形成。

[建議置入 Group1 Figure 1：短週期脈衝組之 加速度／速度、QSM Power、Interface Work 與 IsoDisp 關係]

[建議置入 Group1 Figure 2：短週期脈衝組之 QSM Power 頻率群接觸圖譜 (Frequency-Group Contact Map)]

Group1 Figure 2 是理解短週期脈衝組的重要圖。它顯示，Group1 的高位移案例並不是只集中在單一頻率點，而是在有效隔震頻率族附近與其倍頻帶上形成多點接觸。上半圖保留完整 QSM Power Frequency Group，可以看到同一筆資料在固定 IsoDisp 水準上展開成多個頻率點；下半圖則放大靠近 $0.5f_{\mathrm{eff}}$ 、 $f_{\mathrm{eff}}$ 、 $2f_{\mathrm{eff}}$ 、 $3f_{\mathrm{eff}}$ 、 $4f_{\mathrm{eff}}$ 的區域。這張圖的重點不是宣稱某一個倍頻單獨控制位移，而是顯示短週期脈衝會把能勢推入一組頻率入口，最後再由隔震系統轉化為較低頻的位移反應。

從圖中可見，RSN1013 與 RSN4847 形成 Group1 的高位移橫排，且它們的 QSM Power 頻率點同時接觸接近 $2f_{\mathrm{eff}}$ 、 $3f_{\mathrm{eff}}$ 、 $4f_{\mathrm{eff}}$ 的區域。這說明短週期脈衝雖然在時間上是一個短促事件，但在能勢頻率上並不單薄；它會以一組頻率群進入系統。中低位移案例如 RSN148、RSN4102、RSN4100 則同樣有頻率群接觸，但其位移水準較低，表示頻率接觸本身不是充分條件，仍必須與 Power Packet 強度、介面做功交換與時間同步性一起閱讀。

因此，Group1 Figure 2 應放在 Group1 Figure 1 之後閱讀。Figure 1 證明 Group1 的位移更接近 V、QSM Power Packet 與 Interface Work；Figure 2 則補上頻率層的說明：這些能勢不是只以單一有效頻率進入隔震層，而是透過有效頻率族與倍頻入口形成接觸。這正是 QSM 要強調的地方： $f_{\mathrm{eff}}$ 不是終點，而是能勢進入隔震系統的入口座標。

## Group1 代表案例

### RSN784：時間同步型案例

RSN784 的隔震位移峰值 (IsoDisp peak) 約 73 mm，屬於 Group1 中等位移案例。它的 QSM Power Packet 與 隔震位移峰值 (IsoDisp peak) 幾乎同步，Lag 約為 -0.051 s；Interface Power/Work Packet 與 隔震位移峰值 (IsoDisp peak) 的 Lag 約為 -0.008 s。

這筆資料很適合用來說明：QSM Power Packet 不是事後統計指標，而是與位移峰值發生在同一事件時間窗中的機制訊號。其 QSM Power Frequency Group 包含約 0.5 Hz、1.749 Hz、2.249 Hz、2.749 Hz、3.873 Hz 等成分；Interface Power 也出現約 0.25 Hz、1.749 Hz、2.749 Hz、3.873 Hz；隔震位移反應 (IsoDisp response) 則顯化為約 0.25 Hz、0.625 Hz 的低頻反應。

RSN784 顯示，Input-Side Power Frequency Group 進入介面後，不一定以原頻率一比一出現在位移中，而可能被隔震系統轉化為更低頻、更長週期的位移顯化。

### RSN1013：高位移、高 Power、高介面交換案例

RSN1013 是 Group1 高反應代表。其 隔震位移峰值 (IsoDisp peak) 約 150 mm，輸入端 QSM Power Shock 約 1.36 W/kg，1s QSM Power Packet 約 0.372 J/kg，Interface Power/Work Packet 約 5.50 kJ。

這筆資料在 velocity、QSM Power peak、QSM Power Packet 與 Interface Work 圖中都落在高反應區。它的診斷圖顯示，位移反應不是單純振盪後快速回零，而是被推向明顯滑移狀態。這正好支撐 QSM 的核心說法：當結構無法把輸入能勢整理成穩定通道，能勢會在介面推動位移。

RSN1013 的 QSM Power Frequency Group 包含 0.666、1.110、1.554、1.998、2.442、3.109、4.219、7.105 Hz；Interface Frequency Group 包含 0.666、1.554、2.442 Hz；隔震位移反應 (IsoDisp response) 則落在 0.137、0.274、0.411、0.548、0.685、0.822、0.959 Hz 等低頻群。這代表高頻與中頻的 Power Flow 經介面轉換後，最終以低頻位移群顯化。從 J 圖看，RSN1013 的位移頻率不是雜亂散點，而是以接近系統有效頻率相關尺度的整齊低頻序列出現。這是高位移案例最關鍵的證據之一：能勢不是只從單一頻率入口進入，而是沿著有效頻率族被系統接收，最後顯化為位移。

### RSN4102：低位移但時間同步乾淨的對照案例

RSN4102 的隔震位移峰值 (IsoDisp peak) 約 44.6 mm，是低位移案例。它的 QSM Power Shock 約 0.589 W/kg，1s Power Packet 約 0.204 J/kg，Interface Power/Work Packet 約 1.71 kJ。

這筆資料最漂亮的地方是時間同步。QSM Power Packet 與 隔震位移峰值 (IsoDisp peak) 的 Lag 約 -0.031 s，Interface Power/Work Packet 與 隔震位移峰值 (IsoDisp peak) 的 Lag 約 0.012 s。也就是說，雖然它沒有形成高位移，但 Power Packet、Interface Exchange 與位移峰值仍然幾乎同時發生。

RSN4102 的價值在於，它證明 QSM Power Packet 的時間位置是有效的；差別在於 packet 與 Interface Exchange 的強度不足，因此位移沒有被推高。它與 RSN1013 形成對照：一個是高 Power、高介面交換、高位移；另一個是低 Power、低介面交換、低位移。兩者共同支持同一條機制鏈。

## Group1 小結

Group1 顯示，在短週期脈衝輸入下，加速度不是主要解釋軸，速度是更好的入口，而 QSM Power Packet 與 Interface Power / Work Exchange 才真正接近位移事件。它最重要的證據是時間：QSM peak 與 displacement peak 常常非常接近。這說明隔震位移是能勢波包進入介面後的瞬時顯化事件。

---

# 五、Group2：中週期脈衝案例中的能勢波包與大位移放大

Group2 是中週期脈衝組，也是最適合展示「速度脈衝 → Power Packet → Interface Exchange → 大位移」的組別。原論文指出 medium $T_p$ 的脈衝型地震會造成較大的隔震位移。QSM 的分析可以補上更具機制性的說明：中週期速度脈衝更容易把輸入能勢整理成有效 Power Packet，並在介面形成強烈做功交換。

Group2 Figure 1 中，Input Acceleration Peak 幾乎沒有解釋力：


$$
r \approx 0.059,\quad \rho \approx -0.200
$$


Input Velocity Peak 明顯提高：


$$
r \approx 0.777,\quad \rho \approx 0.806
$$


輸入端 QSM Power peak 只有中等關係：


$$
r \approx 0.468,\quad \rho \approx 0.406
$$


但輸入端 QSM 1s Power Packet 明顯更好：


$$
r \approx 0.704,\quad \rho \approx 0.770
$$


這表示 Group2 的重點不在瞬間 shock，而在一段可持續的能勢波包。最強證據仍然出現在介面：


$$
\text{Interface Power/Work Packet:}\quad r \approx 0.889,\quad \rho \approx 0.794
$$


相較之下，Accumulated Interface Work 為：


$$
r \approx 0.539,\quad \rho \approx 0.527
$$


這個差異很關鍵。它表示 Group2 的大位移不是由總能量累積單獨決定，而是由有效時間窗內的 Interface Power/Work Packet 決定。也就是說，能勢是否集中進入隔震介面，比最後總共累積多少更接近位移峰值的形成。

[建議置入 Group2 Figure 1：中週期脈衝組之 加速度／速度、QSM Power、Interface Work 與 IsoDisp 關係]

[建議置入 Group2 Figure 2：中週期脈衝組之 QSM Power 頻率群接觸圖譜 (Frequency-Group Contact Map)]

Group2 Figure 2 顯示中週期脈衝組的核心特徵：位移水準整體明顯高於 Group1，且許多高位移資料在 $2f_{\mathrm{eff}}$ 、 $3f_{\mathrm{eff}}$ 、 $4f_{\mathrm{eff}}$ 附近仍保有 QSM Power Frequency 案例群組的接觸。這與 Group1 不同。Group1 更像短時間能勢事件；Group2 則呈現較長週期速度脈衝把能勢持續推入隔震系統，形成更大的介面做功與更大的位移顯化。

圖中 RSN170 是最醒目的高位移案例。它在多個 QSM Power 頻率峰值 上維持高 IsoDisp 水準，代表大位移不是由單一頻率點造成，而是由一組能勢頻率共同參與。RSN1165、RSN802、RSN983 等案例也落在中高位移層，顯示中週期脈衝的危險性不只是速度峰值高，而是它的能勢頻率群較容易與隔震系統入口頻率族形成有效接觸。

相對地，RSN3317、RSN8130、RSN1085 等低位移案例也能看到頻率點，但其橫排位移水準明顯較低。這表示 Group2 的判讀不能停在「有沒有接觸 $f_{\mathrm{eff}}$ 或倍頻」，而要同時看接觸之後是否形成足夠強的 Power Packet 與 Interface Work packet。換句話說，Group2 Figure 2 的功能，是把「中週期脈衝造成大位移」從單純週期描述，推進到「能勢頻率群如何進入隔震介面」的描述。

## Group2 代表案例

### RSN170：高位移代表，Power Packet 與 Interface Exchange 都很強

RSN170 是 Group2 的高反應代表：

- 隔震位移峰值 (IsoDisp peak)：約 588.7 mm
- 輸入加速度峰值 (Input Acceleration Peak)：約 0.260 g
- Input Velocity Peak：約 0.858 m/s
- QSM Power Shock：約 1.508 W/kg
- QSM 1s Power Packet：約 0.612 J/kg
- Interface Power/Work Packet：約 28.51 kJ

它的加速度不是最大，但速度、Power Packet、Interface Exchange 都很強，最後位移非常大。QSM Power Packet peak 與 隔震位移峰值 (IsoDisp peak) 的 Lag 約 -0.809 s，Interface Power/Work Packet 與 隔震位移峰值 (IsoDisp peak) 的 Lag 約 -0.734 s。Power event 發生在位移峰值之前不到一秒，時間機制合理。

RSN170 的 QSM Power Frequency Group 包含 0.500、1.000、1.500、2.250、2.750、3.750、4.375、6.000 Hz；Interface Frequency Group 包含 0.500、1.000、1.499、2.249 Hz；隔震位移反應 (IsoDisp response) 則集中在 0.125、0.250、0.375、0.500 Hz。這顯示 Input-Side Power group 經介面接收後，轉成低頻大位移反應。J 圖中，RSN170 的位移頻率高度集中在與 $f_{\mathrm{eff}}$ 相關的低頻序列上，這使它成為「中週期脈衝如何透過有效頻率族放大位移」的代表案例。

### RSN983：中高位移案例，顯示高 Power Shock 不必然等於最高位移

RSN983 的隔震位移峰值 (IsoDisp peak) 約 374.4 mm。它的輸入端 QSM Power Shock 約 1.685 W/kg，QSM 1s Power Packet 約 0.496 J/kg，Interface Power/Work Packet 約 13.44 kJ。

這筆資料很適合用來提醒讀者：單一 Power Shock 不是全部。RSN983 的 shock 高，但位移沒有超過 RSN170，因為真正要看的是 packet、Interface Exchange 與頻率群如何轉換。其 QSM Power Packet → 隔震位移峰值 (IsoDisp peak) Lag 約 0.930 s，Interface Power/Work Packet → 隔震位移峰值 (IsoDisp peak) Lag 約 0.840 s，顯示 Power event 先發生，位移隨後顯化。

RSN983 的 QSM Power Frequency Group 包含 0.768、1.729、2.305、2.881、3.265、3.649、4.225、5.762 Hz；Interface Frequency Group 包含 0.755、1.699、2.266、2.832、3.210、3.587 Hz；隔震位移反應 (IsoDisp response) 約 0.326 Hz。QSM 與 interface 的頻率群高度接近，但位移最後顯化為低頻反應。這是阻尼隔震系統不能用單一輸入頻率描述的典型例子。

### RSN8130：低位移代表，Power Packet 與 Interface Exchange 量級不足

RSN8130 的隔震位移峰值 (IsoDisp peak) 約 165.0 mm，屬於 Group2 低反應代表：

- Input Velocity Peak：約 0.528 m/s
- QSM Power Shock：約 0.645 W/kg
- QSM 1s Power Packet：約 0.286 J/kg
- Interface Power/Work Packet：約 7.07 kJ

它的 QSM Power Packet → 隔震位移峰值 (IsoDisp peak) Lag 約 -0.699 s，Interface Power/Work Packet → 隔震位移峰值 (IsoDisp peak) Lag 約 -0.641 s。時間上仍然接近，但能勢量級明顯小於 RSN170 與 RSN983，所以位移被限制在較低層級。

RSN8130 的 QSM Power Frequency Group 包含 0.625、1.374、1.874、2.374、2.874、3.248、3.873、6.247 Hz；Interface Frequency Group 包含 0.625、1.374、1.874、2.374 Hz；隔震位移反應 (IsoDisp response) 包含 0.250、1.000 Hz。它也有頻率群接觸，但因為 Power Packet 與 Interface Exchange 不夠強，沒有形成 Group2 的高位移。

## Group2 小結

Group2 是 QSM Power Flow 最清楚的中週期脈衝證據。它說明中週期速度脈衝不是只讓速度峰值變大，而是更容易形成能夠推動隔震層的 Power Packet。當這個 packet 進入介面，並形成強 Interface Power / Work Exchange，隔震層就會被推到大位移。

---

# 六、Group3：非脈衝案例中的分散能勢場與低頻位移顯化

Group3 是 non-pulse-like group。傳統上，這組容易被視為脈衝組的對照。但 QSM 的分析顯示，Group3 不應只被理解為「沒有脈衝」。它更像是一種分散能勢場：能勢不以清楚單一速度脈衝進入系統，而是透過更長時間、更寬頻率群、更分散的方式進入隔震介面，最後仍可能顯化為大位移。

Group3 Figure 1 中，Input Acceleration Peak 與 隔震位移峰值 (IsoDisp peak) 的關係不高：


$$
r \approx 0.287,\quad \rho \approx 0.370
$$


Input Velocity Peak 明顯提升：


$$
r \approx 0.559,\quad \rho \approx 0.733
$$


QSM Power peak 顯示出有趣的排序性：


$$
r \approx 0.486,\quad \rho \approx 0.794
$$


輸入端 QSM Power Packet：


$$
r \approx 0.387,\quad \rho \approx 0.733
$$


這代表 Group3 的 Power 指標不一定呈現乾淨線性比例，但能分辨位移層級。這與 Group2 很不同。Group2 比較像一段中週期脈衝直接形成強 packet；Group3 則像分散能勢在頻率群與介面中重新組合。

Interface Power/Work Packet：


$$
r \approx 0.586,\quad \rho \approx 0.576
$$


Accumulated Interface Work：


$$
r \approx 0.533,\quad \rho \approx 0.576
$$


這些關係不像 Group2 那麼強，但合理。非脈衝輸入的能勢不集中於單一短時間窗，而是以較分散方式進入系統。因此，Group3 的分析不能只盯著單一 peak 或單一 packet，必須同時看 Input-Side Power、Interface Exchange、Frequency Group 與 displacement response。

[建議置入 Group3 Figure 1：非脈衝組之 加速度／速度、QSM Power、Interface Work 與 IsoDisp 關係]

[建議置入 Group3 Figure 2：非脈衝組之 QSM Power 頻率群接觸圖譜 (Frequency-Group Contact Map)]

Group3 Figure 2 是本文中最容易被低估、也最重要的分組頻率圖。因為 Group3 被原研究歸類為 non-pulse-like，很容易被讀成「沒有明顯脈衝，因此比較不危險」。但這張圖顯示，非脈衝並不代表沒有能勢場；它代表能勢不是以單一清楚速度脈衝進入，而是以更分散、更寬頻、更長時間的方式進入。

圖中 RSN1164FP 與 RSN1233FN 形成非常高的位移水準，並且它們的 QSM Power Frequency Group 不是只貼在 $f_{\mathrm{eff}}$ 附近，而是展開到較寬的頻率範圍。這說明非脈衝地震波可以透過寬頻能勢場與隔震系統作用，最後仍顯化為極大位移。這一點很關鍵：若只用 pulse / non-pulse 的分類，RSN1164FP 可能被看成對照組；但在 QSM 讀法中，它反而是分散能勢場造成大位移的強證據。

Group3 Figure 2 也顯示，多數中低位移案例在 0.5–1.5 Hz 附近有密集接觸，同時也延伸到 2 Hz 以上。這代表非脈衝組的位移不是由一條乾淨的頻率線控制，而是由能勢場在多頻率入口上的分布、介面選擇與低頻位移顯化共同決定。因此，Group3 的分析要比 Group1、Group2 更小心：不能只看 peak，也不能只看一秒 packet，必須把 Frequency Group 與 Interface Exchange 一起看。

這張圖支撐本文一個重要推論：隔震系統面對的不是「某一筆地震有沒有脈衝」這麼簡單，而是該地震波是否形成足以進入系統、穿過介面、最後推動位移的能勢場。

## Group3 代表案例

### RSN1164FP：非脈衝也能形成極大位移

RSN1164FP 是 Group3 最重要的案例之一：

- 隔震位移峰值 (IsoDisp peak)：約 885.3 mm
- Input Acceleration Peak：約 0.416 g
- Input Velocity Peak：約 0.537 m/s
- QSM Power Shock：約 1.339 W/kg
- QSM 1s Power Packet：約 0.327 J/kg
- Interface Power/Work Packet：約 10.053 kJ

它不是 Group2 的中週期脈衝，卻形成極大位移。這證明「非脈衝」不等於低風險。它的輸入端 QSM Power Packet 不是 Group3 最大，但位移極大，代表位移不是只靠輸入端 packet 大小解釋，而與介面轉換、低頻位移顯化密切相關。

RSN1164FP 的 QSM Power Frequency Group 包含 2.749、4.873、3.124、7.247、1.749、0.875、5.748、1.249 Hz；Interface Frequency Group 包含 0.250、0.875、1.249、0.625、2.749、1.749、1.999、2.499 Hz；隔震位移反應 (IsoDisp response) 則集中在 0.125、0.250、0.375、0.500 Hz。這是一個典型的「寬頻輸入 → 介面選擇 → 低頻位移顯化」案例。J 圖特別重要：RSN1164FP 雖然不是脈衝案例，但其位移頻率仍形成接近有效頻率族的低頻序列，顯示非脈衝能勢場也能透過系統入口頻率族被整理成極大位移。

### RSN175FN：高 Power Packet，但不是最大位移

RSN175FN 的隔震位移峰值 (IsoDisp peak) 約 336.6 mm：

- Input Acceleration Peak：約 0.346 g
- Input Velocity Peak：約 0.706 m/s
- QSM Power Shock：約 1.718 W/kg
- QSM 1s Power Packet：約 0.624 J/kg
- Interface Power/Work Packet：約 10.774 kJ

這筆資料的 Power Shock 與 Power Packet 都很高，Interface Power/Work Packet 也不小，但位移遠低於 RSN1164FP。它提醒我們：QSM 不能被簡化成「Power 越大，位移越大」。頻率群是否被介面接收，是否轉化為隔震系統的低頻位移模式，同樣重要。

RSN175FN 的 QSM Power Frequency Group 包含 3.500、2.500、0.875、1.125、1.625、4.375、8.626、6.375 Hz；Interface Frequency Group 包含 0.250、1.499、2.249、1.999 Hz；隔震位移反應 (IsoDisp response) 包含 0.125、0.250、0.375、0.500、0.625 Hz。它是「高 Power、中高位移，但非最大位移」的典型對照。

### RSN878FN：低位移代表，頻率群存在但能勢不足

RSN878FN 的隔震位移峰值 (IsoDisp peak) 約 140.3 mm：

- Input Acceleration Peak：約 0.275 g
- Input Velocity Peak：約 0.370 m/s
- QSM Power Shock：約 0.572 W/kg
- QSM 1s Power Packet：約 0.144 J/kg
- Interface Power/Work Packet：約 4.392 kJ

它也有 QSM Frequency Group，也有 Interface Frequency Group，也有 displacement response，但 Power Packet 與 Interface Exchange 都偏低，所以沒有形成大位移。它的 frequency closure 顯示：QSM Power Frequency Group 包含 0.750、1.249、1.499、2.124、2.624、3.249、1.874、3.623 Hz；Interface Frequency Group 包含 0.750、1.125、1.499、2.124 Hz；隔震位移反應 (IsoDisp response) 包含 0.250、0.750 Hz。

RSN878FN 說明，頻率群接觸是條件，不是保證。能勢量級不足時，即使存在頻率群閉合，也不會自動顯化為高位移。

## Group3 小結

Group3 的意義是把 QSM 從脈衝案例推展到非脈衝能勢場。非脈衝地震波不是沒有能勢，而是能勢以分散場的形式進入系統。當這些分散頻率群經由介面轉換成隔震系統的低頻位移反應時，仍可能形成極大位移。

---

# 七、Group4：頻譜匹配案例中的能勢差異

Group4 是 Spectrally Matched Group。它對本文非常重要，因為它直接碰到工程設計中很核心的問題：如果地震波在反應譜座標上已經被調整得相近，實際隔震位移是否也應該相近？

QSM 的回答是：不一定。反應譜相似，不代表 QSM Power Flow、Interface Work exchange 與 frequency-group contact 相同。

Group4 Figure 1 中，Input Acceleration Peak 與 隔震位移峰值 (IsoDisp peak) 仍然偏弱：


$$
r \approx 0.265,\quad \rho \approx 0.127
$$


Input Velocity Peak 提高到：


$$
r \approx 0.496,\quad \rho \approx 0.479
$$


輸入端 QSM Power peak：


$$
r \approx 0.470,\quad \rho \approx 0.442
$$


輸入端 QSM 1s Power Packet：


$$
r \approx 0.448,\quad \rho \approx 0.418
$$


最關鍵仍然是 Interface Power/Work Packet：


$$
r \approx 0.676,\quad \rho \approx 0.576
$$


它比 acceleration、velocity、輸入端 QSM Power 更接近 隔震位移峰值 (IsoDisp peak)。這說明 Group4 的差異真正開始在介面層被放大：輸入端看起來已經被頻譜匹配整理過，但到了隔震介面，Power / Work Exchange 仍顯示不同的能勢交換強度。

[建議置入 Group4 Figure 1：頻譜匹配組之 加速度／速度、QSM Power、Interface Work 與 IsoDisp 關係]

[建議置入 Group4 Figure 2：頻譜匹配組之 QSM Power 頻率群接觸圖譜 (Frequency-Group Contact Map)]

Group4 Figure 2 是本文對 頻譜匹配 最直接的補充證據。這組資料在反應譜上經過匹配，照理說傳統讀法會期待它們具有較接近的反應需求；但頻率群接觸圖譜 (Frequency-Group Contact Map) 顯示，即使反應譜被整理過，QSM Power Frequency Group 仍然保有明顯差異。

圖中 RSN802M 形成最高位移橫排，RSN803M 與 RSN1085M 也位於高位移層，而 RSN8130M 等案例位移較低。這些差異不是 Figure 1 中 Input Acceleration Peak 可以單獨解釋的，也不是 頻譜匹配 之後自然消失的。Group4 Figure 2 顯示，頻譜匹配資料 在 $f_{\mathrm{eff}}$ 及其倍頻附近仍有不同的接觸密度與能勢分布；某些資料能把 QSM Power Frequency Group 有效帶入隔震系統，某些資料則不能。

這張圖的意義，不是說 頻譜匹配 沒有價值，而是說它控制的是反應譜外觀，不保證控制能勢路徑。對隔震系統而言，真正要進一步確認的是：匹配後的地震波是否仍在時間窗內形成 Power Packet，是否在介面形成做功交換，是否在頻率群上接觸有效隔震頻率族，最後是否轉成低頻位移顯化。

因此，Group4 Figure 2 應被視為本文對工程設計語言的提醒：反應譜相似，不等於能勢相似；頻率群相似，也不必然等於介面做功相似。隔震位移要回到能勢通過介面的實際路徑來判讀。

## Group4 代表案例

### RSN802M：高位移頻譜匹配案例

RSN802M 是 Group4 的高位移代表。它的位移反應高，且在 Group4 頻率圖譜 中形成明顯高位移橫排。這表示即使經過頻譜匹配，某些地震波仍可在 QSM Power Frequency Group 與 Interface Exchange 層面形成強作用。

從診斷圖看，RSN802M 的 input signal 經過 $a(t)v(t)$ 轉換後，Power Packet 在主反應時間窗內形成，Interface Work 隨後明顯累積，位移反應則在後續低頻模式中顯化。這很適合用來說明：譜匹配後的輸入仍保留時間結構與頻率群差異，這些差異會在介面層重新放大。J 圖也顯示，即使經過 頻譜匹配，高位移案例的 Displacement Response Frequency 仍會回到系統有效頻率族附近，形成可辨識的整齊序列；這正是 頻譜匹配 無法完全取代能勢頻率群判讀的原因。

### RSN170M：頻譜匹配後仍保留中高位移機制

RSN170M 是 Group4 中與原始中週期脈衝脈絡相連的重要案例。它的診斷圖顯示，Input-Side Power Flow 與 Interface Exchange 仍有清楚時間窗；位移反應不是只由設計譜相似性決定，而是與介面實際吃進多少 Power/Work 有關。

這筆資料可以拿來對照 Group2 的 RSN170：自然中週期脈衝與 頻譜匹配後地震波，在傳統譜座標上可能被拉近，但在 QSM QSM Power Flow 的時間波包、頻率群與 Interface Exchange 上仍然不同。

### RSN8130M：低位移 頻譜匹配案例

RSN8130M 是 Group4 低位移代表。它顯示即使在 頻譜匹配組 中，也有能勢沒有被強烈轉成大位移的案例。這類資料對文章很重要，因為它避免把 Group4 寫成「譜匹配都失效」。更準確的說法是：頻譜匹配 能控制一部分反應譜外觀，但它不能保證每一筆輸入在 QSM Power Flow 與 Interface Exchange 上等價。

## Group4 小結

Group4 的核心貢獻，是指出 頻譜匹配 的盲點：它對齊的是反應譜，不一定對齊能勢通道。它控制的是輸入在設計譜上的外觀，但結構真正承受的是時間波包、速度推動、Power Flow、介面做功與頻率群接觸。這也是為什麼 頻譜匹配組 仍然會呈現明顯位移差異。

---

# 八、結論：地震波作為能勢場，隔震位移作為介面顯化

本文以球面滑動隔震系統的真實實驗資料，對量子結構力學進行第一次實證性驗證。這項工作並不是為了取代原研究，而是承接原研究最重要的發現：只看加速度或平均反應譜加速度，無法充分解釋隔震位移。

本文的第一個結論，是原研究的資料確實支持「只看加速度不夠」這件事。跨案例群組 Group1–4 的總結圖顯示，輸入加速度峰值 (Input Acceleration Peak) 與量測隔震位移峰值 (measured IsoDisp peak) 的相關性極低。當分析轉向 Input Velocity Peak，關係明顯提高。這說明隔震位移與速度脈衝、推動能力與時間持續性有關。

第二個結論，是 QSM 的視角轉換具有資料合理性。將 $a(t)$ 與 $v(t)$ 合成為 $P_{\mathrm{in}}(t)=a(t)v(t)$ 後，地震輸入不再只是加速度或速度序列，而成為一個隨時間進入結構的能勢流。當這個能勢流被整理為 Power Packet，並進一步進入隔震介面形成 $F_{\mathrm{interface}}(t)v_{\mathrm{rel}}(t)$ 的 Power / Work Exchange 時，它與位移反應的關係變得最清楚。

第三個結論，是隔震位移背後的頻率不應只被壓縮成單一有效頻率。 $f_{\mathrm{eff}}$ 很重要，但它是入口尺度，不是完整答案。實際反應包含 QSM Power Frequency Group、Interface Frequency Group 與 Displacement Response Frequency 案例群組的連續轉換。各組 Figure 2 的意義正在這裡：Group1 顯示短週期脈衝如何以時間事件方式接觸有效頻率族；Group2 顯示中週期脈衝如何透過較強能勢波包與倍頻入口形成大位移；Group3 顯示非脈衝地震波仍可能以分散寬頻能勢場造成大位移；Group4 顯示頻譜匹配不等於能勢匹配。

更關鍵的是單筆診斷圖中的頻率群收斂比較。許多高位移案例的位移反應頻率並不是無規則散布，而是靠近原本系統有效頻率及其倍頻所形成的整齊序列。這是本文最重要的驗證證據之一。它說明隔震系統的有效頻率不應被理解為單一數字，而是一個能勢入口族；地震波的 QSM Power Frequency Group 進入系統後，會經由介面選擇與轉換，最後在 Displacement Response Frequency Group 中顯化。換言之，J 圖所呈現的不是單一頻率命中，而是一組能勢入口被連續接觸後，位移在系統有效頻率族中顯化的結果。

因此，本文對 QSM 的核心論述可以收束為一句話：

> 地震波對結構物而言，是一個進入系統的能勢場；當結構無法把這個能勢場轉化為穩定通道時，能勢會在介面形成做功交換，並顯化為隔震位移。

這句話也是本文對原實驗資料的主要貢獻。原研究已經指出，只看加速度不夠；本文進一步說明，問題不只在於少看了速度，也在於傳統觀察方式還沒有完整描述能勢如何進入系統、穿過介面、接觸頻率群，並最後成為位移。QSM Power Flow 提供的不是單一新指標，而是一條新的資料閱讀路徑：從 輸入運動 (Input Motion)，走向 Power Packet，再走向 Interface Exchange，最後走向 頻率群顯化 (Frequency-Group Manifestation)。

對工程應用而言，這代表未來隔震系統評估不應只問「輸入地震有多大」，也要問「地震能勢如何進入系統」。如果一套隔震系統能把輸入能勢導成通道、分流、耗散，它就有機會降低位移顯化；如果不能，能勢便可能集中在介面，推動隔震層產生大位移。

這就是本文用真實實驗資料為量子結構力學建立的第一個實證基礎。
