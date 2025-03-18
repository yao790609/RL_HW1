# GridWorld Web Application (Flask + jQuery)

## 📝 Project Overview
This project is a **web-based GridWorld simulation** for **Deep Reinforcement Learning (DRL)**.  
It is built using **Flask** and **jQuery**, allowing users to configure a dynamic `n × n` grid for policy iteration and value function visualization.

Users can interact with the grid to **set a start point, goal, and obstacles**, and the system provides visual feedback.

# Prompt
## Project Overview
- I am developing the classic **GridWorld** problem in **deep reinforcement learning**, using **Flask** to build the web application.
- Users can input **n (range: 3–10)** to define the grid size and generate an **n×n grid** dynamically.

## Basic Specifications
1. **File Name**: `app.html`
2. **Layout**:
   - A **form at the top** to allow users to input `n`.
   - The **n×n grid displayed in the center** of the page.
3. **Grid Styling**:
   - Each **small grid cell has a size of 30px × 30px**.
   - Each **grid cell has a 1px border**.
   - The **number label inside each grid cell is centered**.
     
## Advanced Features (New Additions)
1. **Enhancing GridWorld Display Using JQuery**:
   - The **start cell** is marked with a **green background**.
   - The **goal cell** is marked with a **red background**.
2. **Obstacle Configuration**:
   - **n-2 obstacle cells** can be set **by clicking on grid cells**.
   - **Obstacle cells** are marked with a **gray background** and are impassable.
3. **Start & Goal Selection**:
   - Users can **click on grid cells** to define the **start and goal positions**.
4. **Displaying Operation Steps on the Frontend**:
   - Instead of recording user actions, it **guides the user on what steps to take**.
   - 
## Operation Step Display Adjustments
1. **Numbering steps as "Step 1 – Step 4"**.
2. **Color-coded key terms**:
   - **Start**: Green background
   - **Goal**: Red background
   - **n-2 (Obstacles)**: Gray background
   - **Complete**: Blue background
3. **Resizing the operation steps box**:
   - **Adjust the size to match the lower grid cells**, making it more compact.
   - **Center-align the text inside the step instructions**.
4. **Width Adjustment**:
   - Ensure **"Step 1" can fit in a single line**.
5. **Center-align the input field for `n`** for better aesthetics.

## 🎯 GridWorld Reinforcement Learning  
This project supports **Value Iteration** & **Policy Iteration** with:  

### 📊 Visualization  
- **Value Function (`Value Matrix`)**  
- **Optimal Policy (`Policy Matrix`)**  

### 🎯 Rewards  
- **Goal Cell:** `+20`  
- **Obstacle Cells:** `-1`  

These matrices help analyze **reinforcement learning strategies**.  
---
## 💡 Future Improvements  
- 🚀 Implement **Deep Q-Learning (DQN)** for optimal policy learning.  
- 🎨 Enhance **grid customization** (e.g., different obstacle types).  
- ⏳ Add **real-time updates** for value iteration.  

