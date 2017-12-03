# cs231n Lecture 6 #
> Training Neural Networks 1

## 1. One time setup ##

### 1. Activation Function ###

#### 1. Sigmoid ####

**문제점** : 
1. 절댓값이 큰 입력에서의 Gradient를 없애버림(saturated)
- backprop을 생각해보자.
    - local gradient가 gate의 output에 곱해진다.
    - sigmoid는 큰 값에서의 local gradient = 0이다.
2. 0에서 0값을 가지지 않음
- 뉴럴넷에서 sigmoid 뒤의 인풋이 zero-centered가 아닌 값이 된다.
- 이는 gradient decent 때 zig-zag dynamics를 초래한다. 
3. exp 계산은 비싸다. (별로 중요한 팩터는 아님)

#### 2. tanhx ####
1. 위의 2번 문제 해결,
2. 1번 문제는 해결되지 않음 

#### 3. ReLU ####

1. saturated 되지 않음 (x > 0 일때 한정, 음수일 땐 saturated)
2. computationally 효율적
3. 더 빠르게 수렴함
4. 생물학적으로 더 어울리는 뉴런 행동임
- AlexNet부터 씀
5. (문제점) Zero-centered되지 않음
6. (문제점) negative input이 들어오는 경우 never activated
- "Dead ReLU" 처음에 잘 되다가도 죽어버림
-  

#### 4. Leaky ReLU ####
1. No saturate
2. 

#### 5. PReLU ####
f(x) = max(ax, x)
Leaky Relu 대신 사용

#### 6. ELU ####
f(x) = a(exp(x) - 1), x
1. 음수에서 saturated

#### 7. Maxout ####
f(x) = max(w1x + b1, w2x +b2)

### 2. Process data ###

Zero centering 

Normalize data 

보통 이미지 데이터에 대해 zero centering은 하지만 data normalize 는 하지 않는 편이다. 

이미 이미지는 각 위치에 상대적으로 잘 비교가능한 상태로 distributed 되어있기 때문(?)

PCA나 whitening은 이미지에 대해 잘 안한다.

이미 이미지는 다른 방법으로 차원 축소를 하기 때문 (e. CNN 자체가 차원 축소임)

### 3. Init Weight ###

모두 0으로 초기화하면 : 전부 죽는건 아닌데 모든 neuron이 같은 일을 한다. 같은 업데이트, 같은 연산을 하게 되어 의미가 없음

아 근데 그게 아님 input에 따라 다른 backprop이 되지 않나. 이건 잘 모르겠다.

그래서 다른 방법 ex : small random numbers, 그냥 아무 다른걸로 초기화하기

이건 작은 network에 나름 쓸만하지만 좀 깊어지면 안된다.

- std가 0으로 빠르게 수렴해감 

- xavier 만세


### Batch normalization ###

### 학습 과정 보살피기(?) ###

