---
layout: post
title: Dance Dance Convolution 논문 읽는 중
---

## DDC 논문 리뷰 ##
-----
# **1. 개괄** #
DDR 게임과 같이, 음악과 그에 맞춘 Chart 를 생성한다. 주어지는 음악은 Raw audio이다.

이와 같은 일을 위해 두 가지 소작업을 나눈다.

	1. 언제 Step을 배치할 것인지, 
	2. 어떤 Step을 선택할 것인지.
			
언제 Step을 배치할 것인지를 결정하기 위해서 저수준의 Audio feature인 Spectogram을 Recurrent CNN에 입력하여 Step을 예측한다.

어떤 Step을 선택할 것인지를 결정하기 위해서, Conditional LSTM Generative Model을 써서 n-gram법이나 fixed window 법에 비해 상당히 우수한 결과를 냈다. 
			

# **2. 도입** #
Dance Pad는 상, 하, 좌, 우 4가지 방향을 갖고, 각각의 방향에 대해 4가지 상태를 갖는다 : ON, OFF, Hold, Release.

각각의 방향은 독립적인 상태를 가지므로 전체 상태는 매순간 256개의 Step combination을 갖는다.

Choreograph(안무 작성)을 학습하는 것은 MIR에도 도움이 되는데 특히 소작업 1번인 Step의 배치는 MIR에서 잘 연구된 *Onset Detection* 문제이다.

Onset Detection은 음악적으로 중요한 이벤트를 모두 인식하는 것이다. 이를 테면 멜로디 음정, 드럼 치는 소리 등이다. 
			
비록 우리 데이터의 모든 Onset이 DDR Step에 매칭되지는 않지만, 모든 DDR Step은 Onset에 매칭된다.
				
Step을 만드는 것에 더해, DDR Pack은 각 노래의 Metronome click을 인식하고 있다. 박자가 변하는 음악에서 모든 박자가 변하는 정확한 지점에는 Step이 표현된다. 이러한 Click data는 우리의 *beat tracking*과 *tempo detection* 에 긍정적 영향을 준다.

불행히도, 노래를 사용한 MIR 연구의 데이터셋은 저작권 문제가 있어 제대로 배포되기가 어렵다. 연구를 하려면 연구자가 직접 메타데이터(주석)를 모아야한다. DDR Chart는 MIR 연구에 주석이 달린 풍부한 데이터를 제공한다. Stepmania Online에서는 350Gb 이상의 팩을 100,000 곡이 넘는 메타데이터와 함께 배포하고, 우리는 이 데이터셋을 높은 품질과 일관성이 있는 것으로 간주한다.

## **3. 관련 연구** ##

	소작업 1은 MIR의 onset detection과 매우 비슷하다. 
	소작업 2는 자연언어처리의 통계적 언어 모델링과 비슷하다.

안무 작성을 학습하는 것은 각각의 음악 조각에 대해 이벤트의 *timing* 과 *type*을 결정하는 일이다. 이와 비슷한 작업에는 음성 인식, 악보 작성 등이 있다. RNN은 음성 인식에 널리 사용되어왔으며 최근에는 Convolutional and Recurrent Neural network가 가장 좋다.   

## **4. 방법** ##
작업 파이프라인은 아래와 같다


	(1) 오디오 특성 표현을 추출한다.
	(2) 그것을 Step 배치 알고리즘에 대입한다. 그것은 각 프레임에 Step이 배치될 확률을 계산한다.
	(3) 그 확률 순열에 피크-피킹 프로세스를 사용해서 어떤 정확한 timestamp에 Step이 배치될 것인지를 결정한다.
	(4) 주어진 timestamp의 수열에, Step 선택 알고리즘을 적용하여 각 시간에 어떤 스텝이 배치될 것인지를 결정한다.


## **5. 오디오** ##

음악 데이터에 다중 크기 윈도우를 갖는 STFT(Short Time Fourier Transform)를 수행했다. 23ms, 46ms, 93ms window size를 갖고 10ms의 stride를 가진다.

짧은 윈도우 크기의 STFT에서는 저차원의 특성 - 이를 테면 pitch(높낮이), timbre(음색) 등 - 의 특성이 잘 보존되며, 큰 윈도우 크기에서는 Melody나 rhythm 등의 배경적 특성이 보존된다. 여튼 이렇게 해서 3 채널을 갖는 2차원 스펙토그램이 생성된다.

STFT의 차원을 줄이기 위해 Spectrum의 크기에 Mel-scale 필터를 적용해서 80개의 주파수 대역으로 나누었다. 이는 로그 단위에서 인간 인지와 가장 유사한 표현을 나타낸다.

마지막으로, 각 프레임에 7개의 과거와 미래 프레임을 붙였다. ( 1프레임 : 1 Stride )

고정된 폭 연산을 위해, 최종적인 오디오 표현은 15 x 80 x 3 크기의 텐서가 되었다. ( 15 : 프레임, 80 : Spectrum 강도, 3 : 채널 ) 
이것은 150ms의 오디오 배경에 80주파수 대역, 그리고 3가지 서로 다른 윈도우 크기를 뜻한다.
더 좋은 학습 성능을 위해, 우리는 80개의 주파수 밴드를 표준정규화하였다. 이러한 특성 추출은 ESSENTIA library를 이용하였다.
