### ML_ORGANIZE ###

# Activation Function 비교 #
- Sigmoid(Logistic Function)

    - 'S' 모양으로 휘어진 함수,
    - ![Sigmoid](https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Logistic-curve.svg/320px-Logistic-curve.svg.png)
    - f(x) = 1 / 1 + e^-x


        = 1 / 2 + (1/2)*tanh(x/2)


- ReLU(Rectified Linear Unit)

    - ( x>0 )? x : 0 인 함수
    - ReLU는 Deep한 Neural Net에서 Gradient Vanishing을 방지하는 기능이 있다
    - 그러나 정보의 절반이 손실되므로 느리고 비효율적이다.
    - 변형 형태로 Leaky ReLU(음수에 대해 1/10으로 값을 감소) 등이 쓰임.


- Softplus

    - Softplus는 log(exp(x)+1)을 계산하는 Function이다.
    - ReLU와 비교하면 아래와 같다
    - ![ReLU vs Softplus, 출처 : https://en.wikipedia.org/wiki/Rectifier_(neural_networks)](https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Rectifier_and_softplus_functions.svg/495px-Rectifier_and_softplus_functions.svg.png)
    - ReLU와 비교해서 계산이 복잡하고 느리다.


# weight Initialize 방법 #
- Xavier/He initialization
    - 적당한 값으로, (너무 크지도, 작지도 않게) 초기화하는 방법.
    - fan_in, fan_out 두 가지 수만으로 한다
    - ## Xavier Init ##
    > W = np.random.randn(fan_in, fan_out) / np.sqrt(fan_in)


    - ## He Init ##
	> W = np.random.randn(fan_in, fan_out) / np.sqrt(fan_in/2)
	

# Batch Normalization #
- Reference : (https://shuuki4.wordpress.com/2016/01/13/batch-normalization-%EC%84%A4%EB%AA%85-%EB%B0%8F-%EA%B5%AC%ED%98%84/)

- Gradient vanishing/exploding 문제가 일어나지 않도록 하는 기법
- Activation function에 집어넣기 전에 Normalize를 한다.
- 단순히 avg(0), std(1)의 Normalize를 하면 activation function의 Non-linearity를 해칠 수 있으므로 신중하게 해야한다. 

- Whitening이라는 기법이 있다. 이는 input feature를 uncorrelated하게 만들어주고 각 variance를 1로 만든다.
	- 근데 이는 매우 계산량이 많다(Cov(M)과 Inv(M)의 계산이 필요함)
	- 심지어 일부 parameter의 영향이 무시되기도 한다.

- 다음과 같은 방법으로 이러한 Whitening의 단점을 보완한다.

> 1. 각각의 feature들이 이미 uncorrelated되어있다고 가정, feature각각에 대해서 scalar형태로 normalize한다.
> 2. normalize된 값에 scale factor (gamma)와 shift factor(beta)를 더해주고, 이 변수들을 back-prop 과정에서 같이 train시킨다.(Activation function의 non-linearity 보존)
> 3. Training data 전체에 대해 mean과 Variance를 구하는 것이 아니라, mini-batch 단위로 접근하여 계산한다. 즉 train할 대, mini-batch 안에서의 mean, variance를 구하고 이 것을 이용해 normalize한다.
