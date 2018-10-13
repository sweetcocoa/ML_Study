# Relativistic_Discriminator_Key_Element_Missing_From_Standard_GAN #

## 아이디어 ##
- Standard GAN에서, Generator의 목적은 Fake Data를 Realistic하게 보이는 것이다.
- 근데 Real Data를 Discriminator가 Fake로 믿도록 하는 것이 중요함
    - 우리가 사용할 Mini-Batch 에는 Real과 Fake가 반반씩 들어있는데,
    Discriminator가 mini-batch 안의 Real을 Fake로 믿도록 하면 더 좋을 것
    - Standard GAN에는 이러한 내용을 고려하지 않고, E(D(G(z))) 를 1로 보내는 것만 생각하기 때문.

## 논의 1 : 정말 SGAN은 Jensen-Shannon Divergence를 줄이고 있는건가? ##
- 그렇다고 믿었건만
- ![이미지](https://ajolicoeur.files.wordpress.com/2018/06/figure1-1.png?w=1312)
- 실제로 하는건 좀 다르다. -> Generator를 1로 보낼 뿐..
- 제일 좋은건 우측, Discriminator가 Real을 Fake로 믿게 만드는 것 역시도 중요하다

## 논의 2 : IPM-based GAN ##
### 잠깐! IPM이 뭔데 (모름) ###
---
- **I**ntegral **P**robability **M**etrics
- 걍 쉽게 말하면 WGAN, WGAN-GP 계열에서 좀 다른 Loss 쓰나봄(근데 내가 WGAN을 몰라서 더 적을게 없다)

## Loss 식 ##
### RGANs Non-Saturating Loss ###
- L_D = E(Xr, Xf ~ P, Q) [ f1(C(Xr) - C(Xf)) ]
- L_G = E(Xr, Xf ~ P, Q) [ f1(C(Xf) - C(Xr)) ]

- C(.) : Discriminator 의 logit
-