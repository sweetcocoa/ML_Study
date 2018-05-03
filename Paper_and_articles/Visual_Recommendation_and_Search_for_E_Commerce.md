# Visual_Recommendation_and_Search_for_E_Commerce #
---
`요약 : 옷 쇼핑몰 사이트에서 옷 사진을 기반으로 비슷한 이미지를 찾는 방법`
## 키워드 ##
1. 도메인이 카탈로그 사진인 곳에서 비슷한 이미지 찾기 
    - (사람이 비슷한 상품을 입은 사진에서 사람이 안 입은 카탈로그 이미지 연결)
2. 도메인이 자연 이미지(Wild image)인 곳에서 찍은 사진을 바탕으로 비슷한 상품 찾기
3. Triplet loss
4. Siamese Network

## 생각나는 것 ##
1. 사람들이 비슷하다고 생각하는 셔츠
    - 색이 비슷한 셔츠 (초록 티셔츠 ~ 연두 티셔츠)
    - 무늬가 비슷한 셔츠 (줄 두개 체크무늬 ~ 줄 세개 체크무늬) 
        - Detail-based similarity
    - 무늬의 내용이 비슷한 셔츠 (귀신 그려진 셔츠 ~ 해골 그려진 셔츠)    
        - Concept-based similarity
    - `이런 것들을 각각 추상화하는 방법 필요`
    
2. 여기서 사용한 기본 모델 : VisNet : Deep ranking paradigm을 채택해서 triplet loss를 사용해 훈련한 모델
    - 3개의 vgg-16 network 을 병렬로 연결하여 사용.

3. Triplet loss
    - `loss = max(0, g + D(q, p) - D(q, n))` (Hinge loss)
    - Query, Positive, Negative
    - 훈련할 때 Query, Positive, Negative sample을 주고 이걸 작게 한다. 
    - ** Siamese Network가 binary decision을 할 때보다 triplet loss를 쓰면, Image를 Rank 매기는 법을 직접적으로 배울 수 있다. ** 
    - 또한 Relative Similarity에 대한 Label만 있으면 정의할 수 있다.   
4. Image Similarity Model
    - Object Recognition Model에서는 그 카테고리의 짜잘한 디테일을 뭉개버리는 경향이 있다.
    - 근데 이러한 짜잘한 디테일은 Similarity estimation에서 아주 중요하다. 
    
    - Siamese Networks for Image Similarity:
        - 여러 Weight-sharing CNN들로 이루어져있음.
        - 이미지 쌍들을 input으로 받아 image pair이 similar인지 dissimilar인지 밝힘.
        - binary decision(yes/no)를 뿜도록 훈련된 Siamese Network는 이미지의 짜잘한(fine) 비슷함을 놓치기 쉽다.

    -  이미지가 비슷하다는 것은 근본적으로 애매한 문제다
        - 사람한테 줘도 이 사람 저 사람 많이 다를 것이다.
        - 여럿한테 주고 평균 낼 수도 있지만 근원적인 해결책은 못 된다.

5. CNN을 AlexNet으로 쓰다가 VGG로 바꿨더니 더 좋아졌는데, (커널 크기가 더 작음) 이게 Image Similarity에 중요한 fine detail을 더 잘잡기 때문인 걸로 추측된다. 