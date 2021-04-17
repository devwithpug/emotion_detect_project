# 프로젝트 6주차

(2021.04.17 19:00 ~ 23:00)

***

# 학습 내용

1. optimizer

* SGD, ADAM

2. 스케쥴러

* StepLR

* OneCycleLR

# 오류 발생 / 원인 분석 / 해결

### 오류 1

> 함께 모델에 대한 학습을 진행하면서 두 사람의 딥러닝 모델이 정확히 같음에도 불구하고 한쪽의 정확도가 모든 에폭에서 24.71% 로 고정되는 문제가 있었다.

__발생 경우__
1. 배치 사이즈가 너무 낮은 경우
2. lerning rate 값이 너무 높은 경우

* __원인__: 확실한 원인은 찾지 못했지만 오차를 계산함에 있어서 문제가 생긴걸로 추측

* __해결__: 배치 사이즈와 lr 값을 알맞게 설정하여 해결

# 진행 결과

### 시도 (1)

* SGD -> ADAM

```python
"""
BEFORE
"""
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

"""
AFTER
"""
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

### 결과 (1)

* 기존 optimizer의 경우(SGD)

![image](https://user-images.githubusercontent.com/69145799/115114133-a1195680-9fc8-11eb-8d48-f36425e66da3.png)

![image](https://user-images.githubusercontent.com/69145799/115114145-ad051880-9fc8-11eb-8813-b1f4445758b0.png)

* ADAM으로 변경 후

![image](https://user-images.githubusercontent.com/69145799/115114882-80530000-9fcc-11eb-9e63-5fe0dfdd895d.png)

![image](https://user-images.githubusercontent.com/69145799/115114898-9cef3800-9fcc-11eb-9537-38c72bbe31d8.png)

>__결과 : 정확도 향상(50% -> 52%)__

### 시도 (2)

* scheduler 변경 (lr_scheduler.StepLR -> lr_scheduler.OneCycleLR)

```python
"""
BEFORE
"""
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.1)

"""
AFTER
"""
MAX_LR = 0.008
optimizer = optim.Adam(model.parameters(), lr=MAX_LR)
scheduler = optim.lr_scheduler.OneCycleLR(optimizer, MAX_LR, epochs=EPOCHS, steps_per_epoch=len(train_loader))
```

### 결과 (2)

```
[1] Test Loss: 1.6440, Accuracy: 38.95%
[2] Test Loss: 1.5556, Accuracy: 41.53%
[3] Test Loss: 1.4788, Accuracy: 44.93%
[4] Test Loss: 1.4237, Accuracy: 46.91%
[5] Test Loss: 1.4030, Accuracy: 47.62%
[6] Test Loss: 1.3710, Accuracy: 50.64%
[7] Test Loss: 1.3397, Accuracy: 51.39%
[8] Test Loss: 1.2935, Accuracy: 51.56%
[9] Test Loss: 1.2963, Accuracy: 52.62%
[10] Test Loss: 1.3025, Accuracy: 53.05%
[11] Test Loss: 1.2662, Accuracy: 54.46%
[12] Test Loss: 1.2526, Accuracy: 54.44%
[13] Test Loss: 1.2243, Accuracy: 55.32%
[14] Test Loss: 1.2146, Accuracy: 55.78%
[15] Test Loss: 1.2080, Accuracy: 56.02%
[16] Test Loss: 1.2011, Accuracy: 56.83%
[17] Test Loss: 1.2076, Accuracy: 57.34%
[18] Test Loss: 1.1650, Accuracy: 57.94%
[19] Test Loss: 1.1882, Accuracy: 57.09%
[20] Test Loss: 1.1562, Accuracy: 58.02%
[21] Test Loss: 1.1579, Accuracy: 57.82%
[22] Test Loss: 1.1505, Accuracy: 58.82%
[23] Test Loss: 1.1444, Accuracy: 58.50%
[24] Test Loss: 1.1381, Accuracy: 58.75%
[25] Test Loss: 1.1456, Accuracy: 59.63%
[26] Test Loss: 1.1232, Accuracy: 59.11%
[27] Test Loss: 1.1251, Accuracy: 58.94%
[28] Test Loss: 1.1010, Accuracy: 59.18%
[29] Test Loss: 1.1097, Accuracy: 59.19%
[30] Test Loss: 1.1097, Accuracy: 59.72%
[31] Test Loss: 1.1130, Accuracy: 60.02%
[32] Test Loss: 1.0979, Accuracy: 59.10%
[33] Test Loss: 1.1056, Accuracy: 59.74%
[34] Test Loss: 1.0805, Accuracy: 60.38%
[35] Test Loss: 1.0845, Accuracy: 59.61%
[36] Test Loss: 1.0773, Accuracy: 60.76%
[37] Test Loss: 1.0821, Accuracy: 59.60%
[38] Test Loss: 1.0984, Accuracy: 59.22%
[39] Test Loss: 1.0697, Accuracy: 60.30%
[40] Test Loss: 1.0822, Accuracy: 60.30%
[41] Test Loss: 1.0904, Accuracy: 60.30%
[42] Test Loss: 1.0691, Accuracy: 60.74%
[43] Test Loss: 1.0639, Accuracy: 60.45%
[44] Test Loss: 1.0702, Accuracy: 60.50%
[45] Test Loss: 1.0695, Accuracy: 60.50%
[46] Test Loss: 1.0643, Accuracy: 60.64%
[47] Test Loss: 1.0658, Accuracy: 60.66%
[48] Test Loss: 1.0693, Accuracy: 60.14%
[49] Test Loss: 1.0635, Accuracy: 60.74%
[50] Test Loss: 1.0632, Accuracy: 60.95%
```

![image](https://user-images.githubusercontent.com/69145799/115114192-e8074c00-9fc8-11eb-8b86-3585470ceeb9.png)

>__정확도 60% 달성!__

## 다음 주

- 학습된 모델 저장, 직접 테스트
- API 설계 방안 토론