# Exploring the Limits of Weakly Supervised Pretraining #
----
## 요약 ## 
- 원래 비전 task에서 Imagenet Pretrained 를 많이들 쓰지 않나. classification은 물론이고 detection, segmentation, pose estimation 등등등.
- 인스타그램에서 태그로 Weakly-Supervised Annotated 된 이미지 갖고 Pretraining한 다음 transfer learning, fine-tuning을 했더니 imagenet pretrained보다 잘됐다.
- 인스타그램 데이터셋의 크기는 35억 장
- 미니배치의 크기는 8천 장(.......)


## 엔지니어링 ##
1. 비슷한 단어 합치기 (WordNet synset 이라는 것을 사용)
    - 예) Brownbear 와 ursusarctos 가 합쳐짐
2. 중복된 이미지 제거(Training set과 Validation set에서의 중복된/비슷한 이미지)
    - ResNet50 모델을 사용하고 R-MAC Feature를 사용했고 k=21 인 KNN을 test set에 적용
