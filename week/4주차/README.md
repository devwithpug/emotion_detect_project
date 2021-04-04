# 프로젝트 4주차

(2021.04.04 13:00 ~ 17:00)

***

# 학습 내용

- kaggle에서 face emotion 데이터 다운로드
- 불러온 데이터를 커스텀 데이터셋으로 이용

![image](https://user-images.githubusercontent.com/69145799/113499995-8de0a280-9555-11eb-8190-396c2ffe73ec.png)

- Batch Normalization 적용

![image](https://user-images.githubusercontent.com/69145799/113500736-5674f480-955b-11eb-9c7b-93f7709b0745.png)

배치 정규화를 통해 얻는 이점

1. 학습 속도 개선
2. 가중치 초깃값 선택의 의존성이 적어짐
3. over-fitting 위험을 줄일 수 있다
4. Gradient Vanishing/Exploding 문제 해결
5. Local optimum에 빠지는 문제 해결

![image](https://user-images.githubusercontent.com/69145799/113500762-9cca5380-955b-11eb-8527-545657416328.png)

# 문제 인식 / 원인 분석 / 해결

### 오류 1

![image](https://user-images.githubusercontent.com/69145799/113500012-bcf71400-9555-11eb-97d4-8e71e87f35e9.png)

> RuntimeError: The size of tensor a (3) must match the size of tensor b (2) at non-singleton dimension 0

* __원인__: 데이터셋을 불러올 때 `transforms.Normalize((0.5, 0.5))`와 같이 2차원 텐서로 전처리를 함 // 이미지 데이터는 3차원 텐서!!

* __해결__: `transforms.Normalize((0.5, 0.5, 0.5))` 이미지 데이터를 3차원 텐서로 정규화 하여 해결

### 오류 2

> ValueError: Expected input batch_size (128) to match target batch_size (32).

* __원인__: 에폭에서 loss를 계산할 때 모델이 생성한 배치 사이즈와 데이터셋의 배치 사이즈가 일치하지 않음 

* __해결__: 데이터셋 loader 배치사이즈와 학습시에 배치사이즈를 동일하게 한다.

# 결과

### 시도 (1)

- BATCH_SIZE 16
- conv2d layer (3, 16) -> linear layer(512, 7)

![image](https://user-images.githubusercontent.com/69145799/113500091-3c84e300-9556-11eb-80a4-b8009b34b3ec.png)

### 시도 (2)

- BATCH_SIZE 32
- conv2d layer (3, 16) -> linear layer(512, 7)

> 큰 변화 없음 // 오히려 정확도 하락

### 시도 (3)

- Batch Normalizaion 도입

![image](https://user-images.githubusercontent.com/69145799/113501156-5296a180-955e-11eb-916c-994624105b70.png)

> 에폭당 학습률 향상 / 하지만 정확도 상한선을 크게 넘지는 못함

### 시도 (4)

- 신경망 구조 변경: 조금더 deep 하게 쌓아보기

![image](https://user-images.githubusercontent.com/69145799/113502020-5cbb9e80-9564-11eb-9e44-3afde3c5252a.png)

> 정확도 감소..
구조에 최적화가 필요해보임


## 다음 주. . .

- 다른 CNN 신경망들 분석, 차이점이 무엇인지, 개선방향 찾기
- 신경망 모델 개선하여 정확도 향상