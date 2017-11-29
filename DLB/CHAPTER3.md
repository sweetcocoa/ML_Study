# CHAP3. Probability and Information Theory #

확률 이론은 
1. AI 시스템이 디자인 될 방향성을 제시 (어떻게 reason할 것인가, 그래서 우리가 알고리즘을 어떻게 디자인할 것인가)
2. 제시된 AI 시스템의 행동을 이론적으로 분석하기 위해 사용

정보 이론은
1. Probability Distribution의 Uncertainty를 계량할 수 있게 한다.


## 3.1 Why Probability ##

** Uncertainty가 발생하는 원인 **

1. 시스템 그 자체가 통계적인 경우 
- 양자역학
- 이론적으로 완전히 랜덤한 카드 게임 등
2. 관측이 불완전한 경우(우리가 시스템의 모든 변수를 관측할 수 없음)
- 몬티 홀 문제
    - 참여자의 입장에서 본인이 선택한 문 뒤의 것은 완전히 결정적(Deterministic)이지만 실제로 관측할 수 있는 것은 아니므로 그 결과는 통계적임.
3. 모델링이 불완전한 경우

** Probability의 종류 **
1. Frequentist probabilty(확률빈도)
> 주사위를 하나 던져 1이 나올 확률은?
- Repeatable한 사건에 대해, 무한히 반복했을 때 수렴하는 빈도값
- 전통적인 확률
2. Bayesian Probability(베이지언 확률)
> 의사가 어떤 환자를 진단했다. 어떤 병이 있을 확률은?
- 이것은 사건을 무한히 반복해서 수렴하는 값을 알 수 없다.
- 이런 경우 확률을 **믿음의 정도**로 보는 것을 베이지언 확률이라 한다.

## 3.2 Random variables ##

## 3.3 Probability Distributions ##

**Probability distribution**은 어떤 random variable의 값들이 어떻게 결정될 수 있는지를 나타낸다.

### 3.3.1 Discrete Variables, Probability Mass Function ###

일반적으로 PMF는 P로 나타낸다.

### 3.3.2 Continuous Variables an probability density function ###

일반적으로 PDF는 p로 나타낸다

1. p(x) >= 0, for all x in *x*. 
    - p(x) <= 1일 필요는 없다.
2. integral p(x) dx = 1
3. p의 정의역은 x의 possible state set이어야 한다.

- continuous random variable의 예: 
    - uniform distribution

## 3.4 Marginal Probability ##

어떤 부분집합 안에서의 확률분포

> P(*x*=x) = sigma(for all y) P(*x*=x, *y*=y), for discrete random variable
>
> p(x) = integral p(x,y)dy, for continuous random variable


## 3.5 Conditional Probability ##

다른 사건이 발생했다는 전제하의 확률을 구하고 싶을 때
> P(*y*=y | *x*=x) = P(*y*=y, *x*=x) / P(*x*=x)

* 조건부확률은 P(*x*=x) > 0 인 경우에만 계산 가능.

## 3.6 The Chain Rule of Conditional Probabilities ##

모든 Joint probability distribution은 1개 variable에 대한 conditional distribution으로 decompose할 수 있다.
> P(x1, x2, x3 ... , xn) = P(x1) PI(i=2, n) ( P(xi | x1, x2 ... , xi-1))

Chain rule, 혹은 Product Rule이라고도 한다.

## 3.7 Independence and Conditional Independence ##

확률변수 x,y가 독립이라는 것은 그것들의 확률 분포가 각각의 확률분포 두 개의 곱으로 나타내질 때를 말한다.
> p(x=x, y=y) = p(x=x)p(y=y) for all x, y

확률변수 x,y가 조건부 독립이라는 것은 어떤 확률변수 z에 대해 다음이 성립하는 것이다.
> p(x=x, y=y | z=z) = p(x=x|z=z)p(y=y|z=z) for all x, y, z

## 3.8 Expectation, Variance and Covariance ##

**Covariance** 는 두 개의 값이 얼마나 선형적으로 연관되어있는지를 지시한다.
> Cov(f(x), f(y)) = E( (f(x) - E(f(x)))(g(y) - E(g(y))) )

- |Cov| 값이 크다는 것은 두 변수가 모두 크게 변하며, 각각의 평균에서 멀리 떨어져있음을 뜻한다.
- cov > 0이라면 한 쪽이 큰 값을 가지면 다른 쪽도 큰 값을 가진다
- cov < 0 이라면 한 쪽이 큰 값을 가지면 다른 쪽은 작은 값을 가진다.

**Correlation**은 각 variable을 normalize한 다음의 covariance다.
> Corr(f(x), f(y)) = Cov(f(x),f(y)) / (std(x)*std(y))


## 3.9 Common Probability Distributions ##

### 3.9.2 Multinoulli Distribution ###
여러 개 state로 분화할 수 있는 분포, k개의 서로 다른 state로 나뉘며 k-1차원 벡터 p에 의해 parameterized된다.
각각의 state에서 갖는 값이 1이 아니므로(베르누이 분포와 달리) E, V 값을 구할 일이 거의 없다.

### 3.9.3 Gaussian Distribution ###

정규분포는 변수의 분포에 대한 사전지식이 없을 때 가정하기 좋다.
1. 실제로 많이 따르는 분포이며,
2. 같은 분산을 갖는 확률분포들 중에서 가장 큰 uncertainty를 갖는다.(?)

### 3.9.4 Exponential and Laplace Distributions ###

- Exponential Distributions

> p(x;λ) = λexp(-λx) for all x>=0

![Exponential Distributions](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Exponential_pdf.svg/360px-Exponential_pdf.svg.png)

- Laplace Distributions

> Laplace(x; mu, b) = (1/(2b))exp(-|x-mu|/b)

![Laplace Distributions](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Laplace_pdf_mod.svg/800px-Laplace_pdf_mod.svg.png)

### 3.9.5 Dirac Distribution, Empirical Distribution ###

Empirical Distribution은 여러 개의 dirac distribution 합친 것

### 3.9.6 Mixtures of Distributions ###

1. 어떤 distribution에서 sample이 선택되는지 multinoulli distribution으로 결정한 다음 고른다.
> P(x) = sigma(P(c=i)P(x|c=i))
>
> P(c):multinoulli distribution over component identities

#### Gaussian Mixture Model ####
p(x | c=i) 가 가우시안인 것. 각각의 component는 별개의 mu, covariance를 갖는다. 

????


## 3.10 Useful Properties of Common Functions ##

## 3.11 Bayes' Rule ##

> P(x|y) = P(x)P(y|x)/P(y)

- Recall: Joint distribution
    - P(X=x, Y=y) = P(X=x|Y=y)*P(Y=y) = P(Y=y|X=x)P(X=x)
    - 이걸 다시 쓰면 P(X=x|Y=y)*P(Y=y)/P(X=x) = P(Y=y|X=x)
    - Bayes's Rule이네
    

    
## 3.12 Technical Details of Continuous Variables ##

### Measure Theory ###
- Measure Zero
> 그 차지하는 것이 엄청 작은 점. 그 영향을 무시할 수 있을 정도로
>
> 이를테면 실수 안에서의 유리수, 정수 등

- Almost Everywhere
> Measure Zero를 제외한 곳.
>
> 어떤 feature이 Almost Everywhere에서 성립한다면 Measure Zero를 제외한 곳에서 성립한다는 뜻으로 보면 될 듯하다.

## 3.13 Information Theory ##

- Intuition
> 1. 잘 안일어나는 일이 일어나면 굉장히 informative한 일이다
> 2. 반드시 일어나는 일이 일어나는 것은 의미없는(no information) 일이다.
> 3. 독립적인 사건은 가산적인 사건이다. 이를테면 동전을 두 번 던져 앞면이 두 번 나온 것은 한 번 던져 한 번 나온것의 두 배의 정보를 갖는다.

- self-information : X=x일 때의 정보량    
    - 1 nats 는 확률 1/e 인 사건의 정보량
    - 밑이 2인 log를 사용하면 단위를 nats가 아닌 bits(혹은 shannon)를 쓴다.
    > I(x) = -log(P(x))   (nats)
    
- 


### KL Divergence ###
- 서로 다른 확률 분포가 얼마나 다른가?  