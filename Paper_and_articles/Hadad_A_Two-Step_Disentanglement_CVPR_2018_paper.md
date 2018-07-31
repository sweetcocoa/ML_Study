# A Two-Step Disentanglement Method # 
---
## 요약 ##
1. Disentanglement 하고싶은 속성에 대한 Classifier 훈련
2. Classifier의 중간에서 Embedding 뽑아서 Encoder1로 사용
3. 새로운 Encoder2를 훈련시키는데 목적은
- Encoder1 + Encoder2 -> Decoder -> Autoencoder 구현
- Encoder2 -> Adversarial Classifier

4. Adversarial Classifier의 목적은 Encoder2에서 나오는 Embedding Vector에 Class에 관한 정보가 없도록 하는 것

```
Image -> Encoder1 --- Decoder
      -> Encoder2 --J ------ Adv.Classifier

```
