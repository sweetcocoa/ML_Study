# Music Signal Processing Using Vector Product Neural Network #

## 1. Other Approches in the past ##

MIR (장르 분류, Music Segmentation, Onset Detection, Chord Recognition, Vocal detection 등) 기존의 다른 알고리즘들은 CNN, RNN을 쓴다. 오디오 분류 문제와 같은 것( 단위 Time-Frequency에서의 Spectogram 계산을 필요로 하는)들은 특히 DNN에 의존하는데, 그런 문제들은 입력과 출력이 같은 차원의 행렬을 사용한다. 그래서 신경망은 spatial resolution을 줄일 수 있는 operation을 수행할 수 없다.

그런 문제를 해결하기 위한 기존의 DNN 모델들은 t-f 각 유닛을 실수화하고 신경망의 입력으로 썼다. 우리는 이 논문에서 어떠한 방법을 써서 t-f유닛의 정보를 늘릴 수 있는 더 나은 방법이 있는지를 찾아 보았다.

널리 사용되는 t-f유닛의 정보를 늘리는 방법은 temporal context 정보를 추가하는 것이다. 예를 들어, 현재 프레임에 더해 이전-이후의 k 프레임을 실수행렬로 사용하여 신경망에 입력하는 것이다. 이러한 문제에서는 (2k+1)차원의 신경망이 필요하다.

우리는 일단 이것을 Vector Product neural network(VPNN)을 통해 구현했다.

## 2. Introduce to Vector Product Neural Network(VPNN) ##

이 신경망의 I/O, Weight, Bias는 모두 Vector로 이루어져있다. 
l번째 레이어에서 activation function을 거치기 전의 output은 아래와 같다

	Zi(l) = sigma[j = 1 to J](Wij(l) x aj(l-1)) + bi(l)

x는 벡터곱, Wij(l)은 i,j 사이의 weight neurons, aj(l-1)은 이전 층에서 들어온 signal vector이다.

이를 GPU연산에 최적화시키기위해 행렬 equivalent 식으로 나타내면 아래와 같다

	P (*) Q = [p2q3 - p3q2, p3q1 - p1q3, p1q2 - p2q1]

p1,2,3은 P를 이루는 행렬이다. (q1, 2, 3도 마찬가지) 이를 정리해서 다시 Activation function까지 고려한 Neural network의 식은

	A(l) = f(W(l) (*) A(l-1) + B(l))

이다. A(0) 은 Input Signal이며, l != 1일 때의 A(l)은 Hidden state가 된다.

## 3. 차원 변환과 목적 함수 ##

### 3.1 Context-Windowed Transformation ###

여기서는 각 t-f유닛의 정보를 늘리기 위해 이전 - 현재 - 미래 프레임을 각 t-f유닛에 3차원 벡터로 삼는다. 일반적인 NN에서는 이것이 3차원 벡터가 아니라 3개 행렬이 된다. VPNN에서는 이것이 3차원 매트릭스가 되고, 우리는 이것을 ** Context-Window Vector Product Neural Network (WVPNN) ** 이라 부른다.

첫번째 차원은 이전 프레임, 두번째 차원은 현재 프레임, 세번째 차원은 후속 프레임이 된다. VPNN에 3차원 매트릭스를 입력하면 우리는 3차원 출력을 얻고, 여기서 두 번째 차원이 예측 결과가 된다.

### 3.2 Spectral Color Transformation ###

y

