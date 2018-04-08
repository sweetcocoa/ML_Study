# A Hierarchical Latent Vector Model for Learning Long-Term Structure in Music
----

## 1. Abstract 
- VAE(Variational AutoEncoder)는 의미적으로 말이 되는 latent represantation을 만들어내는데 효과적인 모델인데, 여태까지는 시계열 데이터에의 적용에는 퍽 제한적이었습니다. 지금까지의 Recurrent VAE 모델들은 특히 긴 데이터를 모델링하기 어려웠고요. 
- 그래서 이 논문에서는 계층적 Decoder를 사용해서 이러한 이슈를 해결하는 것을 제안합니다. 일단 첫째로 입력의 부분열(Subsequence)에 대한 embedding을 낸 다음 이러한 embedded output으로부터 각각의 부분열을 reconstruct하는 것입니다. 
- 이것으로 모델이 조금 더 latent space에서의 데이터를 사용하도록 하고, 또한 **"Posterior Collapse"** 현상 - *Recurrent VAE에서, RNN이 그 Initial state만을 사용해서 뒤의 수열을 생성하는 데 문제가 없다고 판단해서 latent space의 정보를 사용하지 않는 현상* - 을 완화합니다.
- 이 구조를 사용해서, 음악 notes를 모델링하고 sampling, reconsruction, interpolation(음악을 의미적으로 말이 되게 섞는 일)에서 어마어마하게 더 나은 성능을 보였습니다. 이러한 결과는 모두 MusicVAE Online에서 확인할 수 있습니다.

## 2. Background
- 기본적으로 이 모델은 Autoencoder입니다. 다시 말해 모델의 목표는 Input을 그대로 Reconstruct하는 것이죠. 그렇지만 우리는 Latent space로부터 뭔가 의미 있는 Sample을 뽑고싶었어요. 그래서 
VAE를 사용하기로 했습니다. 

### **2.1. VAE (Variational Autoencoder)**

**VAE, beta-VAE**


- beta-VAE는 ELBO(Evidence lower bound)의 KL Divergence 항에 0<beta<1 인 beta를 곱합니다.
- ELBO는 E(logp(x|z)) - beta*KLD(q(z|x) || p(z)) <= logp(x)로 정의합니다.

- 여기서 첫째 항인 E(logp(x|z))는 latent space로부터 출력된 sample이고, 이 항이 클수록 더 Realistic한 sample이 됩니다.

- 두 번째 항인 beta*KLD 항은 는 posterior이고, z의 representation이 얼마나 compact한지에 따라 다릅니다. z의 representation이 compact 하다면 posterior은 0에 가까워지지만 반대로 realistic함(첫째항) 이 감소합니다. 그래서 첫째와 둘째 항 사이에는 Trade-off가 있습니다.

- ELBO의 KLD 항의 의미
1. p(z), 즉 latent space의 분포가 있습니다.
2. 우리는 q(z|x)로 sample로부터의 z 분포를 근사합니다.
3. 이렇게 뽑은 z의 분포가 p(z)와 비슷해야 KLD 항이 작아집니다.
> 그런데 이러기 위해서는 q에서 샘플에서 뽑아낼 정보량이 많아야하고, 그러면 p(x|z)의
Realistic함이 떨어집니다. 

### 2.1.2 Latent Space Manipulation

넓게 봤을때 Autoencoder의 목표는 데이터의 compact한 representation을 배우는 것입니다. 
창작 목적으로 봤을 때, 우리는 Latent space에 또 다른 특성을 기대하는데 그것들은 아래와 같습니다.

1. 실제 데이터 x에 대응되는 latent space에서의 점 z에 대해, z와 가까운 z' 대응되는 실제 데이터 x' 역시 x와 의미적으로 가까워야 합니다.
2. 이는 latent space - sample 간의 mapping이 smooth해야 하고, 어떠한 `hole`이 존재해서는 안 된다는 뜻입니다. `hole`이란 NSynth 등의 Autoencoder 기반의 모델에서 나타난 현상인데, 어떤 latent space 영역에서 대응되는 실제 데이터의 realistic이 크게 떨어지는 영역을 의미합니다.
3. 또한 이러한 latent space가 의미적으로 엮여 있지(entangle) 않아야 합니다.

위와 같은 성질이 잘 만족하는 지를 알아보는 현실적인 방법은 latent space에서의 interpolation이 input space에서의 의미적인 interpolation인지를 확인하는 것입니다.
예를 들면 x1->z1, x2->z2인 쌍에 대해

`ca = alpha*z1 + (1-alpha)*z2`

인 ca가 어떤 realistic한 sample에 대응되어야 합니다.

> 참고로, VAE에서의 latent space에 대한 사전분포는 spherical Gaussian인데요. 고차원 공간에서 prior에서 sample한다는 것은 실제로 어떤 unit 단위 초원(unit hypersphere)의 uniform distribution에서의 sample과 거의 같습니다. 그래서 우리는 위 식 대신 spherical interpolation을 latent space에서 적용했습니다. 

또다른 방법으로는 우리의 모델이 어떠한 의미벡터(attribute vector)를 생성하는지를 조사하는 것입니다. latent space에서 attribute A를 빼고 attribute B를 더하면, 실제 데이터의 샘플에서도 attribute A 대신 B가 들어간 샘플이 나와야겠죠.

이를 위해서는 어떤 Attribute A를 갖는 샘플의 Average letent vector를 계산하는데 보통 attritubte는 쌍으로 훈련됩니다. 예를 들어 얼굴 이미지라면 안경이 있는 / 없는 으로요.



### ** TODO **

`Spherical Interpolation을 어떻게 적용할 까?`








