# DeepFM: A Factorization-Machine based Neural Network for CTR Prediction #

**CTR**(Click-Through Rate, 클릭률) : 유저에게 추천된 아이템을 유저가 클릭할 확률. 즉 RecSys의 결과물을 클릭할 확률이다.

**Order of Interaction** : 유저가 클릭을 하도록 하는 변인의 수

    예를 들어, 음식 배달 앱의 다운로드는 (앱 카테고리 선택) - (타임스탬프, 즉 식사시간인지?) 두 개의 변인에 영향을 받는다. 
    이 경우 음식 배달 앱 다운로드 수는 order-2 interaction이다. 
    또 다른 예로, 슈팅 게임이나 RPG 게임의 다운로드는 (앱 카테고리 선택) - (유저 성별) - (유저 나이) 세 가지 변인에 영향을 받는다.
    이 경우의 다운로드 수는 order-3 interaction이다.

위의 예에서 제시한 feature은 전문가에 의해 디자인되는 것이다. 그렇지만 실제 많은 데이터들의 상관관계를 찾는 것이 이만큼 쉬운 것은 아니다.

(기저귀와 맥주의 상관관계는 데이터에 의해 찾아짐)

일반적으로 low-ordered(1, 2 정도) feature만 사용하는데, 그마저도 전문가가 직접 고르는 수준에서 크게 벗어나지 않는다.

1-2 ordered feature를 찾아내는 Linear model이 존재하며, 이론상 higher ordered feature도 찾아낼 수 있으나 모델의 complexity가 높아 practically 어렵다.

Neural Network의 도입으로 high-ordered feature를 잡기는 한다. 근데 wide(low) feature은 잘 못잡나봄

CNN, RNN을 CTR Prediction에 사용한 Liu et al., 2015가 있다.

그러나 CNN은 벡터상으로 가까운 차원에 있는 feature간의 interaction을 찾는 경향이 있었다.


## DeepFM 구조 ##

FM (Factorize Machine) + DNN 두 가지 부분으로 나누어져 있다.

x_raw = 유저-아이템 pair 여러 개
- user-categorical data
- user-scalar data

categorical data는 onehot vector로, scalar data는 그 값을 그대로 사용하거나 이산화하여 onehot vector로 사용

x = (x_field1, x_field2 ...)

각각의 x_field는 x_raw의 한 개의 데이터였다.
- x_field_j = x_raw_j
 
x는 d차원 벡터로, 일반적으로 굉장히 sparse한 vector가 된다.

CTR 문제의 목표는 y_hat = sigmoid(y_FM+ y_DNN)를 구현하는 것이다.


DeepFM은 input x를 dense embedding으로 바꿔준 후 그 벡터를 FM부, DNN부에 같이 사용한다.
 
### Dense Embedding ###

이게 좀 신기한데, x (E R^d) 는 카테고리 데이터(onehot), 스칼라 데이터를 모두 포함하고 있는 벡터고, 필드별로 embedding layer의 한 개 원소로 embedding한다.

V는 한 개 필드를 embed layer의 한 개 층으로 대응시키기 위한 latent vectors이다.

Vi는 한 개 필드의 한 개 값(scalar)을 embedding layer로 대응시키는 latent vector이다.


### FM 부분 ###

- 이것은 Factorization machine로, 1-order feature과 2-order feature를 modeling한다.

- dataset이 sparse할 때 featrue interaction을 더 잘 잡는다 