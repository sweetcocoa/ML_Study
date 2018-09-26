# Convolutional_GAN_With_Binary_Neurons_For_Polyphonic_Music_Generation #

## Input & Output Domain ##
- 각 Track에 따라 Piano Roll

## 아이디어 ##
- 일반적으로 GAN을 훈련시킬 때 Geneartor가 생성한 Fake Sample과 Real Data를 구분하는데,
- Music Sequence의 경우 Generator에서 나온 Fake Sample은 Real-Valued이고, Real은 Binary Value를 갖는다.
- 이 경우, Discriminator의 Decision Boundary를 형성할 때 이게 Binary Value인지 아닌지를 기준으로 삼을 가능성이 있다
- Fake Sample의 경우에도 Binary Value로 된 Sample을 전달해줄 수 있으면 Discriminator가 어떤 음악적인 특성을 바탕으로 Decision Boundary를 형성하는 데에 도움이 될 것

## Binary Neuron ##
- Bernoulli Sample
    - GAN의 output에 softmax를 하지 않고 각 음계에 따른 확률값을 갖는 베르누이 샘플링
- Hard Thresholding
    - Threshold값을 넘는 값을 모두 1, 아니면 0

## 이게 안 됐던 이유? ##
- 미분이 안되기 때문(혹은 Computationally Expensive)
- Gradient의 Backward가 일어나지 않는다.

## How to Train? ##
1. 일반적인 GAN 훈련 과정으로 1차적 훈련
2. Binary Neuron을 넣고 Fine-Tune

## 안 된다며? ##
- Binary Neuron을 Identity Layer로 취급(Hinton's Idea)
- Identity 말고 그 값에서의 Sigmoid Gradient로 취급(Adjusted ST)