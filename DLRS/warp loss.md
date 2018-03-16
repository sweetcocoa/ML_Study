# Weighted Approximate-Rank Pairwise loss : [Source](https://medium.com/@gabrieltseng/intro-to-warp-loss-automatic-differentiation-and-pytorch-b6aa5083187a)

## 역사(?)
- 첫 소개 : [Scaling Up To Large Vocabulary Image Annotation](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37180.pdf)
- 처음에는 RecSys에서 사용된게 아니라 Image annotation임.
- 아주 큰 possible labels에서 correct label을 assign 하는 task에 사용

## 어떻게 동작하나?
- 예) 어떤 고객에게 5개의 사탕 중 하나를 추천하는 RecSys를 생각하자. 5가지 사탕에 대한 Label, 그에 대응하는 확률 값이 5차원 벡터로 나온다.
- Output Vector : 0.35 0.63 0.59 0.76 0.17
- Target Vector : 0.00 0.00 1.00 0.00 0.00
    - Note) 편의상 1개의 사탕을 산다고 했지만 실제로는 여러 개의 사탕을 살 때도 Warp Loss를 사용할 수 있다.

1. 실제로 고객이 산 것은 3번째 벡터에 해당한다. 이것의 Output value = 0.59 = x3_correct 라 하자.
2. 다른 라벨을 샘플링한다. 5번째 벡터를 샘플링했다고 하자.
    - x5_incorrect < x3_correct 이고, 이 부분은 우리 모델이 정확하게 예측한 것이다.
    - 맞게 했으면, 다른 샘플로 넘어간다. (모델이 틀릴때까지)
3. 다른 라벨을 샘플링한다. 2번째 벡터를 샘플링했다고 하자.
    - x2_incorrect > x3_correct 이므로 우리 모델은 틀렸다.(실제로 3번째 사탕을 샀지만, 2번째 사탕을 살 확률이 더 높다고 예측한 것)
    - 이 두 개의 example을 WARP LOSS에 사용할 것이다. WARP LOSS가 두 값 사이의 차이라면
    
    
    Loss = x2_incorrect - x3_correct
    
    
4. 이 쌍에 더해, 우리 모델이 일반적으로 얼마나 잘 예측했는지를 보고싶다. 무슨 말이냐 하면, 그래도 3번째 사탕이 다른 사탕들보다 더 높은 확률로서 예측되었는가? 아님 완전 틀렸는가? 같은 것이다.
    - 모든 example을 다 보는 것 대신(효율을 위해서임, 다 봐도 됨) 다음과 같은 식을 위에서 계산한 loss에 곱한다.


    ln((X-1)/N)
    
    
5. X : Label의 수, N : 모델이 틀렸다는 것을 알아낼 때까지 찾은 샘플 수
    - 몇개 안 봐도 나오면 모델이 많이 틀렸을 가능성이 높고, 많이 봐야 나오면 모델이 잘 맞춘거일 가능성이 높다.

     