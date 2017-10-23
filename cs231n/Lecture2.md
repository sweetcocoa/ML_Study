# **cs231n Lecture 2** #
---
## Image Classification :: Core task in Computer vision ##

고양이 그림을 보고 여러 가지 Label 중 고양이를 고르는 일은
사람한테는 쉽지만, 컴퓨터에게는 어려운 일이다.

### 왜 어려운가요? ###

1. Semantic Gap

> 컴퓨터에서 인식하는 고양이 : RGB 픽셀들의 값들
> 
> 컴퓨터에서 인식하는 고양이 라벨 : 그냥 라벨

- 이 둘 사이의 의미적 차이를 Semantic Gap이라고 함


2. Viewpoint variation

> 고양이를 다른 시점에서 본다면 픽셀 값들은 완전 구분도 못할만큼 달라진다

3. Illumination

> 조명

4. Deformation

> 식빵고양이도 고양이로 볼 수 있을까

5. Occlusion

> 일부만 드러난 고양이도 고양이로 볼 수 있을가
>
> 풀숲에 가려진 고양이라든가

6. Background Clutter

7. Intraclass variation

> 같은 고양이라도 여러 모양이 있음 (종간 차이?)

8. 기타 등등..

### 옛날엔 어떻게 했나 ###

1. Edge를 찾아서.. Rule-Base로
> 잘 안됨
>
> 다른 물체를 인식할 때 사용할 수 있는 알고리즘이 아님

그러니까 이제 Data-driven을 쓰자

### K-Nearest Neighbors ###

> 이미지를 어떻게 비교하지

새로운 이미지가 들어오면 기존에 학습한 데이터 중에서 가까운 것 K개를 구해서 제일 많은것의 라벨을 붙인다.

특징 : Training time이 없음(거의)

대신 구분이 오래 걸림(제일 가까운 점을 찾아야 함)

가깝다는건
- 유클리드 거리를 쓸 수도 있고 
- 맨하탄 거리를 쓸 수도 있는데,

후자는 전자와 달리 설정된 좌표에 따라 다른 결과를 냄 ()

### Hyperparameters ###

- K
- 어떤 distance를 사용할 것인지?

    - L1 을 사용하는게 적합한 경우는 각 좌표의 방향이 의미를 가질 때. 
        > (이미지는 회전해도 그게 그건데, 예를 들어 x축은 봉급, y축은 고용률 같은 의미를 갖는 축일 경우)

    - 어쨌든 둘다 써보고 더 나은걸 고르는게 낫다.

- 어떻게 Hyperparameter를 결정할 것인가?

1. 데이터셋 전체에 대해 잘 맞는 것을 사용
- 안좋음. K=1이 모든 경우에 대해 제일 잘 맞는 것이 된다.
2. 데이터셋을 Train set, Test set으로 나눠서 Test set에서 좋은 결과를 내는 것을 사용
- 안좋음. 왜냐 하면 Test set에 가장 잘 맞는 모델을 찾게 된다. 
- Unseen data에 어떤 결과를 내는 지에 대한 insight가 없음.
3. 데이터셋을 Train set, Validation set, Test set 으로 나눈다.
- Better ! 
- train set에서 훈련하고, Validation set에서 좋은 성능을 내는 것을 구한 뒤 Test set에서의 성능을 측정
4. Cross-validation
- Deep Learning에서는 잘 쓰이지 않지만 Small dataset에 좋음
- 여러 종류의 validation set을 쓰고, 각각의 결과를 평균낸다.
- 딥러닝에서는 한 번의 계산이 오래 걸려서 잘 안 쓴다.

### Linear Classification ###

- 딥러닝, CNN 에 중요
- Neural network는 여러가지 블록을 연결하는 작업
- Linear classifier가 기본적인 블록 중 하나임

image -> f(x, W) -> label scored

- k-nearest보다 좋은 점 : test할 때 training set이 더이상 필요없음. 필요한 것은 f,W


 
