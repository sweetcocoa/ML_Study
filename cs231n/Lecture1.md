# ** cs231n Lecture 1 ** #

Computer Vision은 Visual data에 관한 것

2015년 Cisco는 2017년 대략 인터넷 전체 트래픽의 80%가 비디오일 것이라 예상했다.

Visual data는 컴퓨터 알고리즘으로 이해하기 어려움.

Youtube에는 초당 5시간의 동영상이 업로드되고 있다.

컴퓨터 비전은 진짜 다학제간 분야인데, 다음과 같은 분야에 걸쳐있다
  - Biology
    - Neuroscience, Optics,
  - Psychology
    - Cognitive sciences
  - Computer Science
    - Graphics, Algorithms,
    - Systems, Architecture,
  - Mathematics
    - Information retrieval. Machine learning
  - Engineering
    - Robotics, NLP ...

  cs231n은 CNN을 활용한 Visual data 처리에 중점을 둘 것.


## History of computer vision ##

### History of biological vision ###

5.4억년 전, 천만년 정도의 짧은 기간에 수많은 종이 발생하였다. (**Evolution's Big Bang**)

원인 : 어떤 종이 눈을 만들어냈음
- 먹이를 잘 찾고
- 포식자에게서 잘 도망침

인간 : 대뇌 피질의 50%정도가 시각 정보를 처리할 정도로 가장 비중이 큰 감각 기관이 됨.

### history of mechanical vision ###

핀홀 카메라 이론 : 빛을 모아 망막에 상을 맺는 눈의 구조


Hubel and Wiesel에 의해 수행된, 고양이 눈 연구 (시각 정보가 어떻게 처리 되는지를 연구한, 고양이 피질에 전극을 꽂아 연구)

Cat brain의 일차 시각 피질(Primary Visual Cortex)에는 여러 가지의

### Computer vision's history ###

** Object를 표현하기 위한 여러 가지 방법 시도 **
- 모든 Complex Object는 간단한 기본 도형과 그 위치 등을 나타내는 Configuration으로 나타낼 수 있음

** Object Recognition **

- 이미지를 인식은 어렵고, 그 전에 이미지를 분리(Segmentation)한다.
 - 1997, Shi & Malik. Normalized cut
   - Pixels를 모아 Image segmentation.
 - Face detection
   - Face detection는 Vision의 중요한 일 중 하나임
   - 1999, 2000 SVM, Boosting, Graphical Models, 등 CV 이론 발달로 머신러닝 기술의 발달 시발점
   - Adaboost Algorithm의 등 장 : 실시간 Face detection을 가능하게 함 : Vision 기술의 현실 application 사례

- Feature based Object Recognition
  - "SIFT", Object recognition, David Lowe, 1999
    - 물체의 특정한 특성은 이미지에서 Invariant하지 않은가?
 - Spatial Pyramid Matching,
   - 그림의 일부를 잘 쪼개면 이게 무슨 그림인지 알 수 있지 않을까?
   - 어떻게 쪼개냐?
   - 이미지에는 우리가 이 scene이 어떤 그림인지 알 수있는 Clue가 존재한다.
   - SVM을 그 위에 얹어 어떤 이미진지 판별한다.
 - Human body Recognition
   - Histogram of Gradients, Dalal & Triggs, 2005
   - Deformable Part Model, McAllester & Ramanan, 2009

** 시대의 변화 **

60, 70, 80년대를 지나 2000년대로 오며 Vision 분야에서 크게 바뀐 것
- 인터넷, 디지털 카메라의 발달로 이미지의 퀄리티가 크게 올라감
   - 2000년 초, Pascal이라는 Object recognition의 Benchmark dataset이 도입됨
   - 20개 Object class로 구성됨, category당 수천~수만개의 데이터셋이 존재

   - ** IMAGENET **
     - 더 어려운 데이터셋, 더 많은 object in the world 사용. 이 세상 대부분의 사물을 사용하겠다
     - Visual Recognition Challenge
     - Graphical model, SVM, AdaBoost 등의 머신러닝 알고리즘은 오버피팅되기 매우 쉽다. 이미지는 적은 데이터셋이라서 (그 이미지의 차원에 비해)특히 더더욱.
     - 1500만개 이미지,  22000개 이미지 클래스.
     - 2009년부터 IMAGENET Challenge 시작
     - 2015년 Error rate가 인간의 그것보다 낮아짐
     - 2012년 그 전해보다 10%가량 error rate가 떨어짐. 그것이 CNN의 도입

### ** cs231n의 포커스 ** ###

이미지 분류, Visual recognition의 가장 큰 중요한 문제.
   - Object detectgion, Object detection도 Classificaion에서 사용하는 도구들을 사용하여 다룰 계획임
   - Image captioning..


   CNN이 유명해진건 Imagenet 2012년의 Alexnet이지만, 그 이전에 1998년 LeCun이 BellLab에서 CNN을 사용해서 Digit을 구분해내는 작업을 사용함.

   그때보다 엄청 컴퓨터가 빨라져서 (1000배 이상) 더 큰 모델과 계산을 알고리즘에 도입할 수 있게 되었다.

   Data도 많아짐 (Labeled pixel의 증가)
