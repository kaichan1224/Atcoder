"""
def scoring(state):
    return stateのスコア

states = [[初期スコア, 初期状態]] # 基本的には初期状態は空の配列になると思います
for idx in range(解の長さ):
    next_states = []
    for _, state in states:
        for num in 考えうる手:
            next_state = copy(state)
            next_state.append(num)
            # next_statesにスコアと次の状態を入れておく
            next_states.append([scoring(next_state), next_state])
    next_states.sort() # スコアが良い順にソートする
    states = [] # statesを初期化
    for next_state_idx in range(min(ビーム幅, len(next_states)):
        score, next_state = next_states[next_state_idx]
        states.append([score, next_state])
"""