from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

# 動作方向（上、下、左、右）
ACTIONS = {'↑': (-1, 0), '↓': (1, 0), '←': (0, -1), '→': (0, 1)}
ACTION_LIST = ['↑', '↓', '←', '→']

# Policy Iteration 參數
GAMMA = 0.9  # 折扣因子
THETA = 1e-4  # 收斂條件

def policy_iteration(n, start, end, obstacles):
    """執行 Policy Iteration 來計算最優策略"""
    value_matrix = np.zeros((n, n))  # 初始化 V(s)
    policy_matrix = np.random.choice(ACTION_LIST, size=(n, n))  # 隨機初始化 Policy

    # 設定終點的獎勵
    rewards = np.full((n, n), -0.5)  # 普通移動的 reward = -0.5
    rewards[end] = 20  # 碰到終點 reward = 20
    for obs in obstacles:
        rewards[obs] = -1  # 碰到障礙物 reward = -1

    # Policy Iteration
    stable = False
    while not stable:
        # Step 1: Policy Evaluation
        while True:
            delta = 0
            new_value_matrix = np.copy(value_matrix)
            for i in range(n):
                for j in range(n):
                    if (i, j) == end or (i, j) in obstacles:
                        continue  # 終點與障礙物不更新
                    action = policy_matrix[i, j]
                    di, dj = ACTIONS[action]
                    ni, nj = max(0, min(n-1, i+di)), max(0, min(n-1, j+dj))
                    new_value_matrix[i, j] = rewards[i, j] + GAMMA * value_matrix[ni, nj]
                    delta = max(delta, abs(new_value_matrix[i, j] - value_matrix[i, j]))
            value_matrix = new_value_matrix
            if delta < THETA:
                break

        # Step 2: Policy Improvement
        stable = True
        for i in range(n):
            for j in range(n):
                if (i, j) == end or (i, j) in obstacles:
                    continue  # 終點與障礙物不更新
                best_action = None
                best_value = float('-inf')
                for action in ACTION_LIST:
                    di, dj = ACTIONS[action]
                    ni, nj = max(0, min(n-1, i+di)), max(0, min(n-1, j+dj))
                    value = rewards[i, j] + GAMMA * value_matrix[ni, nj]
                    if value > best_value:
                        best_value = value
                        best_action = action
                if policy_matrix[i, j] != best_action:
                    policy_matrix[i, j] = best_action
                    stable = False

    return value_matrix.tolist(), policy_matrix.tolist()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('gridworld.html')

@app.route('/compute', methods=['POST'])
def compute():
    data = request.json
    n = data['n']
    start = tuple(data['start'])
    end = tuple(data['end'])
    obstacles = [tuple(x) for x in data['obstacles']]

    value_matrix, policy_matrix = policy_iteration(n, start, end, obstacles)
    
    return jsonify({'value_matrix': value_matrix, 'policy_matrix': policy_matrix})

if __name__ == '__main__':
    app.run(debug=True)
