import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# 載入 Karate Club 圖形
G = nx.karate_club_graph()

# 計算各項指標
pr        = nx.pagerank(G)
betw      = nx.betweenness_centrality(G)
deg       = nx.degree_centrality(G)
closeness = nx.closeness_centrality(G)

# 整理成 DataFrame 並輸出 CSV
df = pd.DataFrame({
    "pagerank":    pr,
    "betweenness": betw,
    "degree":      deg,
    "closeness":   closeness,
}).sort_values("pagerank", ascending=False)

df.index.name = "member"
df.to_csv("centrality_results.csv")
print(df.to_string())

influencer = df["pagerank"].idxmax()
print(f"\n影響者: Member {influencer}  PageRank: {df.loc[influencer, 'pagerank']:.4f}")

# 視覺化
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 左圖：依 PageRank 著色的網路圖
pos        = nx.spring_layout(G, seed=42)
node_sizes = [pr[n] * 5000 for n in G.nodes()]
node_color = [pr[n] for n in G.nodes()]

nx.draw_networkx(
    G, pos, ax=axes[0],
    node_size=node_sizes,
    node_color=node_color,
    cmap=plt.cm.YlOrRd,
    with_labels=True,
    font_size=8,
    edge_color="#cccccc",
)
axes[0].set_title("Karate Club — node size/color = PageRank")
axes[0].axis("off")

# 右圖：Top-10 成員四項指標長條圖
top10 = df.head(10)
top10.plot(kind="bar", ax=axes[1], colormap="tab10")
axes[1].set_title("Top-10 Members — Centrality Metrics")
axes[1].set_xlabel("Member")
axes[1].set_ylabel("Score")
axes[1].legend(loc="upper right", fontsize=8)
axes[1].tick_params(axis="x", rotation=0)

plt.tight_layout()
plt.savefig("centrality_chart.png", dpi=150)
plt.show()
print("\n已儲存 centrality_results.csv 與 centrality_chart.png")
