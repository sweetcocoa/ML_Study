### 개요

- 추천 알고리즘의 종류에는 크게
1. user-based filtering : 비슷한 사용자가 좋아하는 상품 추천
1. content-based filtering :  비슷한 내용의 다른 상품 추천
2. item-based filtering :  비슷한 다른 상품 추천
3. stereo-type recommend : 편견 기반 (예: 남자는 자동차를 좋아할 것, 여자는 화장품을 좋아할 것)
4. most-popular recommend : 인기순 (예 : 뉴스기사는 가장 조회수가 높은 기사를 사람들이 좋아함)

- 그리고 이러한 알고리즘 중 3,4 는 RecSys 계에서 관심을 받지 못하고 있다.


### Sowispot 은 Article 라이브러리이다. 여기서 저 중에 어떤게 잘 될까
(기준 : CTR)
- CB > item > stereo > Baseline(random) > most-popular
