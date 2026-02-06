# 🎮 Player Behavior Segmentation (Unsupervised Machine Learning)

This project applies **unsupervised machine learning** techniques to analyze gameplay telemetry and automatically discover **distinct player behavior archetypes** without using predefined labels.

The goal is not to predict difficulty or outcomes, but to answer a more fundamental analytics question:

> **“What types of players naturally exist in the game?”**

This problem is central to real-world **game analytics, player modeling, and personalization systems** used by modern game studios.

---

## 🧠 Project Objectives

- Segment players based purely on gameplay behavior
- Discover latent player archetypes using clustering
- Interpret clusters using human + ML reasoning
- Validate findings using multiple unsupervised techniques
- Translate ML insights into **game design and business decisions**

---

## 🧩 Dataset Overview

- **Type:** Synthetic but behavior-driven gameplay telemetry  
- **Size:** 1,200 players  
- **Labels:** None (true unsupervised learning)  

### Features Used
- `avg_session_time`
- `sessions_per_week`
- `levels_completed`
- `time_to_complete_level`
- `death_rate`
- `retry_rate`
- `accuracy`
- `exploration_score`
- `aggression_score`
- `completion_rate`

The dataset was carefully designed to reflect **realistic human gameplay behavior**, including overlap, noise, and hybrid play styles.

---

## 🛠️ Techniques Used

### Core Methods
- **KMeans Clustering** (baseline segmentation)
- **DBSCAN** (density-based clustering & outlier detection)
- **Hierarchical Clustering** (relationship analysis via dendrogram)

### Supporting Techniques
- **StandardScaler** (feature scaling)
- **PCA (Principal Component Analysis)** for visualization
- **Silhouette Score** for cluster quality evaluation

---

## 📊 Results & Insights

### Clustering Summary

- Final KMeans model used **k = 6**
- Achieved **silhouette score ≈ 0.42**, which is strong for complex human behavior data
- PCA visualization showed clear but realistic separation with overlap
- Results were validated using DBSCAN and Hierarchical clustering

---

### Identified Player Archetypes

#### 1. Hardcore / Try-Hard Players
Highly skilled and highly committed players. They play frequently for long sessions, complete levels quickly, maintain very high accuracy, and exhibit near-perfect completion rates. These players focus on mastery and performance optimization rather than exploration.

#### 2. Explorers
Curiosity-driven players who prioritize immersion and discovery. They show very high exploration scores, slower level completion times, medium skill levels, and strong engagement with optional content and side objectives.

#### 3. Casual Players
Low-commitment players with short play sessions and fewer sessions per week. They complete fewer levels, retry less often, and represent the mainstream audience segment with moderate skill and engagement.

#### 4. Risk-Takers
Aggressive, excitement-driven players who prioritize combat and high-risk actions. They exhibit high aggression scores, high death rates, moderate accuracy, and lower overall completion rates. Hierarchical clustering showed this group to be behaviorally distinct.

#### 5. Persistent Learners
Players who struggle initially but demonstrate strong perseverance. They have long sessions, high retry rates, moderate accuracy, and improving completion rates over time, indicating high long-term retention potential.

#### 6. Speedrunners
Efficiency-focused players who complete levels extremely quickly with high accuracy and minimal exploration. They replay content frequently and are closely related to hardcore players, as confirmed by hierarchical clustering.

---

### Cross-Algorithm Validation

- **PCA** explained ~64% of total variance and visually confirmed cluster structure
- **DBSCAN** identified dense core player groups while labeling many hybrid players as noise, highlighting transitional behaviors
- **Hierarchical clustering** revealed meaningful relationships between archetypes, with closely related groups merging early and behaviorally distinct groups merging late

The agreement across multiple unsupervised methods confirms that the discovered archetypes represent **genuine behavioral patterns**, not artifacts of a single algorithm.

---

## 🎮 Business & Game Design Implications

### Hardcore / Try-Hard Players
- Enable ranked modes, leaderboards, and mastery challenges  
- Provide skill-based rewards and performance analytics  

### Explorers
- Expand optional content, hidden areas, and lore  
- Reward curiosity through achievements and narrative depth  

### Casual Players
- Simplify onboarding and tutorials  
- Offer flexible difficulty and short-session gameplay  

### Risk-Takers
- Design high-risk, high-reward combat encounters  
- Add dynamic and chaotic gameplay events  

### Persistent Learners
- Implement adaptive difficulty and progression hints  
- Reward persistence rather than raw skill  

### Speedrunners
- Support time trials, ghost replays, and speedrun leaderboards  
- Encourage replayability and community-driven challenges  

---

## 🧠 Key Takeaways

- Player behavior exists on a **spectrum**, not in rigid categories  
- Unsupervised learning can reveal meaningful player archetypes without labels  
- Combining multiple clustering techniques leads to more robust insights  
- Behavioral segmentation can directly inform game design, retention, and monetization strategies  

---

## 📂 Project Structure

```
player-behavior-segmentation/
│
├── data/
│   ├── raw/
│   │   └── players.csv
│   └── processed/
│       └── .gitkeep
│
├── notebooks/
│   ├── 01_data_generation.ipynb
│   ├── 02_eda.ipynb
│   └── 03_clustering.ipynb
│
├── src/
│   └── data_generator.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 🚀 Future Improvements

- Apply sequence-based modeling (HMMs / RNNs) for temporal behavior
- Integrate real gameplay telemetry
- Deploy clustering results in a live personalization system
- Add automated reporting dashboards

---

## 📌 Final Note

This project emphasizes **interpretation, reasoning, and validation** over raw metrics.  
It demonstrates how unsupervised ML can be used to understand **human behavior**, not just optimize models.

---


