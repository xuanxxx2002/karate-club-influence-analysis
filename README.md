# karate-club-influence-analysis

使用 NetworkX 對經典的 **Karate Club** 社交網路進行中心性分析，識別網路中的關鍵影響者。

## 分析內容

| 指標 | 說明 |
|---|---|
| PageRank | 衡量節點的整體影響力（參考 Google 搜尋排名演算法）|
| Betweenness Centrality | 衡量節點作為橋樑的重要程度 |
| Degree Centrality | 衡量節點的直接連結數量 |
| Closeness Centrality | 衡量節點與其他節點的平均距離 |

## 輸出

| 檔案 | 內容 |
|---|---|
| `centrality_results.csv` | 所有 34 位成員的四項指標數值 |
| `centrality_chart.png` | 網路圖（左）＋ Top-10 成員指標長條圖（右）|

## 快速開始

**安裝依賴**

```bash
python -m pip install networkx matplotlib pandas scipy
```

**執行**

```bash
python karate_club_influence_analysis.py
```

![image](https://github.com/xuanxxx2002/karate-club-influence-analysis/blob/main/centrality_chart.png)

## 資料集

[Zachary's Karate Club](https://en.wikipedia.org/wiki/Zachary%27s_karate_club)（1977）— 34 個節點、78 條邊，是社會網路分析領域的經典基準資料集。
