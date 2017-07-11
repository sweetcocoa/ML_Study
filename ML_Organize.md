### ML_ORGANIZE

# Activation Function 비교
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
