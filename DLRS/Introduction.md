# Deep Learning for Recommendation Systems (DLRS) #

Item Embeddings 

Embedding (Latent feature vector)



출처 : [deep learning in recommender systems](https://www.slideshare.net/balazshidasi/deep-learning-in-recommender-systems-recsys-summer-school-2017)


## 구현에 필요한 것들 ##
- A/B 테스트 등 실제로 더 잘 동작하는지의 여부를 알아볼 방법
- 어떤 데이터셋이 주어질 것인지, (어떤 데이터셋을 줄 것인지) 결정
- 알고리즘 혹은 딥러닝 모델 결정


## Top-N Recommendation System ##
> 이걸 구현해야 됨


## 일반적인 RecSys 문제 ##
**주어진 값** : 사람들의 여러 항목에 대한 선호도

**출력값** : 

- 선호도가 주어지지 않은 항목에 대해 선호도를 예측하거나(Matrix Factorization) 
- 선호도가 주어지지 않은 항목에 대해 선호도의 상대적인 순서를 예측(?)


## CTR Prediction ##

> Click-Through Rate Prediction

출처 : [DeepFM: A Factorization-Machine based Neural Network for CTR Prediction](https://arxiv.org/pdf/1703.04247.pdf)

CTR은 RecSys에서 추천된 아이템을 클릭할 확률을 말한다. 

이러한 Click through rate를 예상하는 데에는 유저와의 interaction을 signal로 하여 CTR을 예상하는데,

영향을 미치는 interaction의 수를 order of interaction 이라 한다.

    예를 들어, 음식 배달 앱의 다운로드는 (앱 카테고리 선택) - (타임스탬프, 즉 식사시간인지?) 두 개의 변인에 영향을 받는다. 
    이 경우 음식 배달 앱 다운로드 수는 order-2 interaction이다. 
    또 다른 예로, 슈팅 게임이나 RPG 게임의 다운로드는 (앱 카테고리 선택) - (유저 성별) - (유저 나이) 세 가지 변인에 영향을 받는다.
    이 경우의 다운로드 수는 order-3 interaction이다.

위의 예에서 제시한 feature은 전문가에 의해 디자인되는 것이다. 그렇지만 실제 많은 데이터들의 order은 이만큼 쉬운 것은 아니다.

(기저귀와 맥주의 상관관계는 데이터에 의해 찾아짐)

