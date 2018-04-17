
# Improved Variational Inference with Inverse Autoregressive Flow #



## 중심 아이디어 : Gaussian Autoregressive Function
- Gaussian autoregressive 함수 : 보통 densifty estimation에 쓰이는. 이전 Variable에 Condition된 mean, std를 뿜어낸다.
- 이러한 Autoregressive한 모델에는 RNN, PixelCNN, WaveNet 등이 있다.



## Normalizing Flow ## 
- `Rezende and Mohamed, 2015`
- Flexible inference network를 build하는 일반적인 방법
- 어떤 Computationally Cheap, Simple Distribution에 Invertible한 Parameterized Transform을 연속적으로 적용해서 Zt가 더 flexible한 분포를 가질 수 있도록 하는 아이디어.

` Z0 ~ q(Z0|x), Zt = ft(zt-1, x) where t = 1...T`

- 각각의 transform(ft)의 Jacobian이 계산가능하다면, 우리는 마지막 iterate의 pdf를 계산할 수 있다.
    - 그런데 이러한 Calculatable, Invertible한 Jacobian을 갖는 transform은 몇 가지 없다.
    - 이러한 transform은 `f[t](z[t-1]) = z[t-1] + uh(wTz[t-1] + b)`, h는 비선형 함수를 뜻한다.
    - 어 이거 어디서 본 거잖아? uh(*) 부분은 single bottleneck을 갖는 MLP로 해석할 수 있다.
    - 이렇게 줄줄이 잇는 transform의 연결을 고차원의 의존성을 해석하는 데에 쓸 수 있다.
    - 걍 적용가능한 선에서는 간단히 말해 Gaussian 분포에다 MLP를 줄줄이 잇는 거인 듯.


- 이러한 Normalizing flow에서 Inverse transformation은 굉장히 흥미롭다.
    - 원래 이런 Normalizing Flow에서의 각 Variational inference는 사후확률로부터 샘플링되는데, 이는 병렬적으로 계산되지 않고 줄줄이 계산되어야 한다는 것을 말한다. 
    - `sigma[i] > 0 for all i` 이라면 원래 아래와 같은 식을
        
        `y[i] = mu[i](y[1:i-1]) + eps[i]*std[i](y[1:i-1])`
        
        다음과 같이 바꿀 수 있다. (덧셈, 나눗셈은 elementwise)
        
        `eps = (y - mu(y)) / std(y)`
        
    - 또 다른 특별한 성질은, 원래 autoregressive한 structure로 인해 그 Jacobian이 Lower Triangular Structure인데, 
    따라서 이의 determinant는 그 대각선 원소인 std[i]의 곱으로 나타낼 수 있다. 다시 말해
    
        `logdet|d(eps)/d(y)| = -sigma log(std[i](y))` 
        
        이고, 병렬 계산이 가능하게 된다.(?)
        
## Inverse Autoregressive Flow (IAF) ##


     